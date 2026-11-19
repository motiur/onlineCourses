#!/usr/bin/env python3
"""Render a course document from Markdown to PDF.

    python3 tools/build_course_pdf.py Course_3_Ten_Years_of_Deep_Learning_Ideas

Reads <folder>/course_document.md and writes <folder>/<folder>_course_document.pdf
(US Letter, with the course title in the header and page numbers in the footer).
Inline maths written as $...$ is converted to MathML, which Chromium renders natively.

Needs: pip install mistune latex2mathml, and Node.js with Playwright's Chromium
(require('playwright') must work).
"""
from __future__ import annotations

import html
import os
import re
import subprocess
import sys
import tempfile

import mistune
from latex2mathml.converter import convert as latex_to_mathml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MATH = re.compile(r"(?<![\\$\w])\$(?=\S)([^$\n]+?)(?<=\S)\$(?![\w$])")

CSS = """
@page { size: Letter; margin: 0.85in 0.9in 0.8in 0.9in; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Inter", "DejaVu Sans", sans-serif; font-size: 10.5pt; line-height: 1.5;
       color: #1d2330; margin: 0; }
h1 { font-size: 24pt; line-height: 1.15; letter-spacing: -0.02em; margin: 0 0 6pt; color: #10151f; }
.byline { color: #5b6476; font-size: 10pt; margin: 0 0 14pt; }
h2 { font-size: 16.5pt; margin: 22pt 0 6pt; letter-spacing: -0.01em; color: #10151f;
     padding-top: 6pt; border-top: 2px solid #2f54eb; }
h2.session { break-before: page; border-top: 0; padding-top: 0; }
h3 { font-size: 12pt; margin: 16pt 0 5pt; color: #2443c9; }
p { margin: 0 0 7pt; }
ul, ol { margin: 0 0 8pt; padding-left: 18pt; }
li { margin: 2.5pt 0; }
li > ul, li > ol { margin: 3pt 0 3pt; }
strong { color: #10151f; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; background: #f1f3f9;
       padding: 0.5pt 3pt; border-radius: 3pt; }
pre { background: #f6f8fb; border: 1px solid #e3e6ef; border-radius: 6pt; padding: 8pt 10pt;
      font-size: 8.5pt; line-height: 1.45; white-space: pre-wrap; break-inside: avoid; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 6pt 0 10pt; font-size: 9.5pt; width: 100%; }
th, td { border: 1px solid #d6dae5; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #eef1f8; }
a { color: #2443c9; text-decoration: none; word-break: break-word; }
blockquote { margin: 0 0 8pt; padding: 6pt 10pt; border-left: 3px solid #2f54eb; background: #f3f5fd; }
math { font-size: 1.05em; }
hr { border: 0; border-top: 1px solid #d6dae5; margin: 14pt 0; }
"""

NODE = r"""
const { chromium } = require('playwright');
(async () => {
  const [src, out, title] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  await page.pdf({
    path: out, format: 'Letter', printBackground: true, displayHeaderFooter: true,
    margin: { top: '0.85in', bottom: '0.8in', left: '0.9in', right: '0.9in' },
    headerTemplate: `<div style="font-family:Inter,sans-serif;font-size:8px;color:#7a8396;width:100%;padding:0 0.9in;">${esc(title)}</div>`,
    footerTemplate: `<div style="font-family:Inter,sans-serif;font-size:8px;color:#7a8396;width:100%;padding:0 0.9in;text-align:right;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>`,
  });
  await browser.close();
})();
"""


def render_markdown(text: str) -> str:
    maths: list[str] = []

    def stash(m):
        maths.append(m.group(1))
        return f"\u0000MATH{len(maths) - 1}\u0000"

    # Keep code spans and code blocks away from the maths pass.
    parts = re.split(r"(```.*?```|`[^`\n]+`)", text, flags=re.S)
    text = "".join(p if p.startswith("`") else MATH.sub(stash, p) for p in parts)

    md = mistune.create_markdown(escape=False, plugins=["table", "strikethrough"])
    out = md(text)

    def unstash(m):
        tex = maths[int(m.group(1))]
        try:
            return latex_to_mathml(tex)
        except Exception:
            return f"<code>{html.escape(tex)}</code>"

    out = re.sub("\u0000MATH(\\d+)\u0000", unstash, out)
    # Page break before each session, and links that show their target.
    out = re.sub(r"<h2>(Session \d+:)", r'<h2 class="session">\1', out)
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = sys.argv[1].rstrip("/")
    src_md = os.path.join(ROOT, folder, "course_document.md")
    text = open(src_md, encoding="utf-8").read()
    title_line = text.splitlines()[0].lstrip("# ").strip()
    body = render_markdown(text)
    body = body.replace("<h1>", "<h1>", 1)
    doc = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{html.escape(title_line)}"
           f"</title><style>{CSS}</style></head><body>{body}</body></html>")
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "doc.html")
        script = os.path.join(tmp, "pdf.js")
        open(page, "w", encoding="utf-8").write(doc)
        open(script, "w", encoding="utf-8").write(NODE)
        out = os.path.join(ROOT, folder, f"{os.path.basename(folder)}_course_document.pdf")
        env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True,
                                                         text=True).stdout.strip())
        subprocess.run(["node", script, page, out, title_line], check=True, env=env)
    print(f"Wrote {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the course website.

The site is published from the motiur.github.io repository, in its
onlineCourses/ folder, so it appears at https://motiur.github.io/onlineCourses/.
With both repositories checked out side by side, run from this repository's root:

    pip install nbconvert
    python3 tools/build_site.py --out ../motiur.github.io/onlineCourses

Then commit and push the motiur.github.io repository.

The output folder is self-contained: index.html, courses/, assets/ and a copy of
each course PDF and notebook for downloading. The course folders here (Course_*/)
are the source; nothing in them is changed. The script only replaces a folder it
created itself (marked by a .built-by-build_site file), so it cannot overwrite
other content by mistake.
"""
from __future__ import annotations

import argparse
import glob
import sys
import html
import json
import os
import re
import shutil

import mistune
import nbformat
from nbconvert import HTMLExporter
from pygments.formatters import HtmlFormatter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "motiur/onlineCourses"
BRANCH = "main"
SITE_TITLE = "AI Courses"
TAGLINE = "From first principles to current research"

# ---------------------------------------------------------------------------
# Course metadata (summaries are taken from the course index)
# ---------------------------------------------------------------------------
COURSES = [
    dict(n=1, folder="Course_1_From_Beginner_to_an_AI_Research_Lab",
         title="From Beginner to an AI Research Lab", level="Beginner",
         track="Start here",
         summary="The entry course: how research labs work, the math and code you actually use, ML and deep "
                 "learning from scratch, transformers, reading and reproducing papers, experiments that "
                 "convince, writing, and getting in through applications, cold emails and interviews.",
         topics=["Foundations", "Reproducing papers", "Experiments", "Research writing", "Applications"],
         prereq="None beyond school mathematics and willingness to code."),
    dict(n=2, folder="Course_2_Ten_Years_of_Deep_Learning_Ideas",
         title="Ten Years of Deep Learning Ideas", level="Core",
         track="Foundations · after Course 1",
         summary="The big deep learning ideas of 2016–2026 that the other courses don't teach: residuals, "
                 "normalization and µP, modern optimizers, the generalization puzzles, vision transformers, "
                 "self-supervised and in-context learning, VAEs to GANs, diffusion and flow matching, deep RL,"
                 " neural fields, and robustness and calibration.",
         topics=["Normalization & µP", "Optimizers", "Self-supervised learning", "Diffusion & flow matching", "Deep RL", "Neural fields"],
         prereq="Course 1 (PyTorch training loops and basic deep learning)."),
    dict(n=3, folder="Course_3_Large_Language_Models",
         title="Large Language Models", level="Research",
         track="Build · after Course 2",
         summary="How today's language models are built, trained and evaluated: the modern transformer, "
                 "tokenization across languages, scaling laws, efficient inference, LoRA and QLoRA, DPO, GRPO "
                 "and reasoning, agents, multimodality, diffusion LMs and interpretability.",
         topics=["Transformers", "Scaling laws", "LoRA", "DPO & GRPO", "Agents", "Interpretability"],
         prereq="Python, PyTorch and the basics of neural networks; Course 2 helps."),
    dict(n=4, folder="Course_4_Building_a_Small_Bangla_Language_Model",
         title="Building a Small Bangla Language Model", level="Project",
         track="Build · a project after Course 3",
         summary="Take a 5–30M-parameter Bangla GPT from raw text to a public release: Unicode cleaning, "
                 "corpus building, tokenizer, model design, training on free GPUs, evaluation, instruction "
                 "tuning against a LoRA baseline, compression and responsible release.",
         topics=["Bangla NLP", "Tokenizers", "Pretraining", "Instruction tuning", "Model cards"],
         prereq="Course 3, or at least Course 1."),
    dict(n=5, folder="Course_5_Winning_Online_AI_Competitions",
         title="Winning Online AI Competitions", level="Practical",
         track="Build · can run alongside other courses",
         summary="A practical playbook for Kaggle-style contests: choosing a competition, metrics and "
                 "leaderboards, validation you can trust, leakage, tabular, time-series, vision, LLM and "
                 "reasoning competitions, ensembling and write-ups, ending in a live-competition capstone.",
         topics=["Validation", "Gradient boosting", "TTA", "Ensembling", "Kaggle"],
         prereq="Python and scikit-learn; Course 2 helps."),
    dict(n=6, folder="Course_6_Geometric_Deep_Learning_and_Graphs",
         title="Geometric Deep Learning and Graphs", level="Research",
         track="Research track",
         summary="Symmetry as the organising idea behind modern architectures: message passing, expressive "
                 "power, graph transformers, equivariant CNNs and E(3) models for atoms, curved spaces, "
                 "generative models on graphs, and graph learning in medicine.",
         topics=["GNNs", "Equivariance", "Graph transformers", "Hyperbolic embeddings", "Graph diffusion"],
         prereq="Comfort with PyTorch and basic linear algebra."),
    dict(n=7, folder="Course_7_Privacy_Preserving_ML",
         title="Privacy-Preserving Machine Learning", level="Research",
         track="Research track",
         summary="What models leak and how to stop it: differential privacy from first principles, DP-SGD and "
                 "accounting, privacy auditing, federated learning and its attacks, private LLM fine-tuning, "
                 "encrypted inference, unlearning and fairness.",
         topics=["Differential privacy", "DP-SGD", "Federated learning", "Homomorphic encryption", "Unlearning"],
         prereq="Course 6 or equivalent deep learning experience; Course 3 for session 7."),
    dict(n=8, folder="Course_8_Mathematics_and_AI",
         title="Mathematics and AI", level="Research",
         track="Research track",
         summary="Mathematics for AI and AI for mathematics: groups and representations, steerable kernels, "
                 "grokking, category theory and lenses, sheaves on graphs, Lean 4, AI theorem proving, "
                 "autoformalization and AI-driven mathematical discovery.",
         topics=["Group theory", "Category theory", "Sheaves", "Lean 4", "Theorem proving"],
         prereq="Undergraduate linear algebra; Course 6 helps."),
    dict(n=9, folder="Course_9_AI_Research_in_2026",
         title="AI Research in 2026", level="Current",
         track="Stay current · checked November 2026",
         summary="What AI research found from January to November 2026: agents' time horizons, RL for "
                 "reasoning, multi-turn reliability, diffusion language models, transformer expressivity, "
                 "Polar Express and Muon, provable grokking, high-accuracy sampling, deception probes, AI on "
                 "Erdős problems and 4D reconstruction, each with a toy lab.",
         topics=["Agents", "RL for reasoning", "Diffusion LMs", "Theory", "Safety", "AI for maths"],
         prereq="Course 1; Courses 2 and 3 recommended."),
    dict(n=10, folder="Course_10_Research_Engineering_Interviews",
         title="Research Engineering Interviews", level="Career",
         track="Get hired · any time after Course 1",
         summary="Prepare for research engineering interview loops: coding, tensor fluency, ML from scratch, "
                 "debugging rounds, fundamentals out loud, estimates, ML system design, research discussions, "
                 "behavioral rounds and take-homes, ending in a four-round mock loop.",
         topics=["Coding rounds", "ML from scratch", "Debugging", "System design", "Mock loop"],
         prereq="Course 1."),
]
BY_N = {c["n"]: c for c in COURSES}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def slug(c) -> str:
    return f"course-{c['n']}"


# ---------------------------------------------------------------------------
# Reading the notebooks
# ---------------------------------------------------------------------------
def load_sessions(c):
    sessions = []
    for path in sorted(glob.glob(os.path.join(ROOT, c["folder"], "notebooks", "s*.ipynb"))):
        nb = nbformat.read(path, as_version=4)
        first = "".join(nb.cells[0].source) if nb.cells else ""
        m = re.search(r"## Session (\d+): (.*)", first)
        g = re.search(r"\*\*Goal:\*\* (.*)", first)
        num = int(m.group(1)) if m else len(sessions) + 1
        not_run = sum(1 for cell in nb.cells
                      if cell.cell_type == "code" and "NOT RUN" in "".join(cell.source))
        code = sum(1 for cell in nb.cells if cell.cell_type == "code")
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        sessions.append(dict(
            num=num,
            title=m.group(2).strip() if m else os.path.basename(path),
            goal=g.group(1).strip() if g else "",
            path=path, rel=rel, nb=nb, not_run=not_run, code=code,
            page=f"session-{num:02d}.html",
        ))
    return sessions


def course_pdf(c):
    pdfs = glob.glob(os.path.join(ROOT, c["folder"], "*.pdf"))
    return os.path.relpath(pdfs[0], ROOT).replace(os.sep, "/") if pdfs else None


def colab_url(rel):
    return f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{rel}"


def kaggle_url(rel):
    return f"https://www.kaggle.com/kernels/welcome?src=https://github.com/{REPO}/blob/{BRANCH}/{rel}"


def github_url(rel):
    return f"https://github.com/{REPO}/blob/{BRANCH}/{rel}"


# ---------------------------------------------------------------------------
# Page chrome
# ---------------------------------------------------------------------------
ICON = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="currentColor"/>'
        '<path d="M9 22 16 9l7 13M11.6 17.5h8.8" fill="none" stroke="var(--bg)" stroke-width="2.6" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')

GH_ICON = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 '
           '3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23'
           '-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87'
           '.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64'
           '-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 '
           '2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 '
           '8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')


def page(title, body, depth, description="", extra_head=""):
    up = "../" * depth
    full = f"{title} · {SITE_TITLE}" if title != SITE_TITLE else f"{SITE_TITLE} · {TAGLINE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(description or TAGLINE)}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(description or TAGLINE)}">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{up}index.html">{ICON}<span>{SITE_TITLE}</span></a>
    <nav class="top-nav" aria-label="Main">
      <a href="{up}index.html#courses">Courses</a>
      <a href="{up}index.html#paths">Learning paths</a>
      <a href="{up}index.html#notebooks">Notebooks</a>
      <a class="gh" href="https://github.com/{REPO}" aria-label="Source on GitHub">{GH_ICON}<span>GitHub</span></a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <a class="brand small" href="{up}index.html">{ICON}<span>{SITE_TITLE}</span></a>
      <p>{TAGLINE}. {len(COURSES)} free courses with hands-on notebooks.</p>
    </div>
    <div class="footer-links">
      <a href="https://github.com/{REPO}">Source on GitHub</a>
      <a href="https://github.com/motiur">github.com/motiur</a>
    </div>
  </div>
</footer>
</body>
</html>
"""


def btn(href, label, kind="ghost", external=False, icon="", download=False):
    ext = ' target="_blank" rel="noopener"' if external else ""
    dl = " download" if download else ""
    return f'<a class="btn btn-{kind}" href="{esc(href)}"{ext}{dl}>{icon}{esc(label)}</a>'


ICONS = {
    "read": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 4.5h5a2 2 0 0 1 2 2V16a1.5 1.5 0 0 0-1.5-1.5H3zM17 4.5h-5a2 2 0 0 0-2 2V16a1.5 1.5 0 0 1 1.5-1.5H17z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "play": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 4.5v11l9-5.5z" fill="currentColor"/></svg>',
    "down": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 3.5v9m0 0-3.5-3.5M10 12.5l3.5-3.5M4 15.5h12" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "doc": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5 2.5h6.5L15 6v11.5H5zM11.5 2.5V6H15M7.5 10h5M7.5 13h5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "arrow": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m0 0-4.5-4.5M15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


def level_badge(level):
    return f'<span class="badge badge-{level.lower()}">{esc(level)}</span>'


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
def build_home(all_sessions):
    total_sessions = sum(len(v) for v in all_sessions.values())
    order = [c["n"] for c in COURSES]
    cards = []
    for n in order:
        c = BY_N[n]
        chips = "".join(f"<li>{esc(t)}</li>" for t in c["topics"])
        cards.append(f"""
      <a class="course-card" href="courses/{slug(c)}/index.html">
        <div class="card-top">
          <span class="course-num">Course {c['n']}</span>
          {level_badge(c['level'])}
        </div>
        <h3>{esc(c['title'])}</h3>
        <p>{esc(c['summary'])}</p>
        <ul class="chips">{chips}</ul>
        <div class="card-foot"><span>{len(all_sessions[n])} sessions · {len(all_sessions[n])} notebooks</span><span class="go">View course {ICONS['arrow']}</span></div>
      </a>""")

    def node(n, note=""):
        c = BY_N[n]
        return (f'<a class="path-node lvl-{c["level"].lower()}" href="courses/{slug(c)}/index.html">'
                f'<span class="pn-num">{c["n"]}</span><span class="pn-title">{esc(c["title"])}</span>'
                f'{f"<span class=pn-note>{esc(note)}</span>" if note else ""}</a>')

    body = f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Free · {len(COURSES)} courses · {total_sessions} hands-on sessions</p>
    <h1>Learn AI from first principles<br>to current research</h1>
    <p class="lead">Structured video courses with a runnable notebook for every session. Start as a beginner,
      learn the decade's core ideas, work through the research topics labs care about today, catch up on this
      year's results, and finish with a project and interview practice.</p>
    <div class="hero-cta">
      {btn('courses/course-1/index.html', 'Start with Course 1', 'primary', icon=ICONS['arrow'])}
      {btn('#courses', 'Browse all courses', 'ghost')}
    </div>
    <dl class="stats">
      <div><dt>Courses</dt><dd>{len(COURSES)}</dd></div>
      <div><dt>Sessions</dt><dd>{total_sessions}</dd></div>
      <div><dt>Notebooks</dt><dd>{total_sessions}</dd></div>
      <div><dt>Cost</dt><dd>Free</dd></div>
    </dl>
  </div>
</section>

<section id="paths" class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Learning paths</h2>
      <p>A suggested order. Every course stands on its own, so jump in wherever you are.</p>
    </div>
    <div class="paths">
      <div class="path-col">
        <h3><span class="step">1</span>Foundations</h3>
        {node(1, "Start here: research skills, maths, code and deep learning basics")}
        {node(2, "The decade's core deep learning ideas")}
      </div>
      <div class="path-col">
        <h3><span class="step">2</span>Build</h3>
        {node(3, "How today's language models work")}
        {node(4, "A project: your own Bangla model")}
        {node(5, "Practical · can run alongside the others")}
      </div>
      <div class="path-col">
        <h3><span class="step">3</span>Research</h3>
        <div class="path-chain">
          {node(6)}{node(7)}{node(8)}
        </div>
      </div>
      <div class="path-col">
        <h3><span class="step">4</span>Stay current and get hired</h3>
        {node(9, "Checked November 2026")}
        {node(10, "Any time after Course 1")}
      </div>
    </div>
  </div>
</section>

<section id="courses" class="section alt">
  <div class="wrap">
    <div class="section-head">
      <h2>All courses</h2>
      <p>Twelve sessions each. Every session has three video segments, a lab notebook, a quiz and an assignment.</p>
    </div>
    <div class="course-grid">{''.join(cards)}
    </div>
  </div>
</section>

<section id="notebooks" class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>How the notebooks work</h2>
      <p>Read any notebook in the browser, or open it in a free cloud environment with one click.</p>
    </div>
    <div class="features">
      <div class="feature">
        <div class="f-icon">{ICONS['play']}</div>
        <h3>One click to run</h3>
        <p>Every session has <em>Open in Colab</em> and <em>Open in Kaggle</em> links. No installation needed; run the cells from the top.</p>
      </div>
      <div class="feature">
        <div class="f-icon">{ICONS['read']}</div>
        <h3>Small, honest examples</h3>
        <p>Runnable cells use small built-in or synthetic data and finish in a minute or two on a CPU. Their numbers show how a method behaves; they are not benchmarks.</p>
      </div>
      <div class="feature">
        <div class="f-icon">{ICONS['doc']}</div>
        <h3>Clearly labelled</h3>
        <p>Cells marked <code>NOT RUN</code> need a GPU, a download or an account. Cells marked <code>TODO</code> are exercises for you to complete.</p>
      </div>
    </div>
  </div>
</section>
"""
    return page(SITE_TITLE, body, 0,
                description=f"{len(COURSES)} free AI courses with {total_sessions} runnable notebooks, "
                            "from beginner foundations to current research.")


# ---------------------------------------------------------------------------
# Course pages
# ---------------------------------------------------------------------------
md = mistune.create_markdown(escape=True)


def readme_html(c):
    p = os.path.join(ROOT, c["folder"], "notebooks", "README.md")
    if not os.path.exists(p):
        return ""
    text = open(p, encoding="utf-8").read()
    text = re.sub(r"^# .*\n+", "", text)  # drop the title line
    text = text.split("\n## ")[0]  # the side panel shows only the opening notes, not detailed sections
    return md(text)


def build_course(c, sessions):
    pdf = course_pdf(c)
    rows = []
    for s in sessions:
        flag = (f'<span class="flag" title="Cells that need a GPU, a download or an account">'
                f'{s["not_run"]} NOT RUN cell{"s" if s["not_run"] != 1 else ""}</span>') if s["not_run"] else \
               '<span class="flag ok">Runs fully on CPU</span>'
        rows.append(f"""
      <li class="session">
        <div class="s-num">{s['num']:02d}</div>
        <div class="s-body">
          <h3><a href="{s['page']}">{esc(s['title'])}</a></h3>
          <p>{esc(s['goal'][:1].upper() + s['goal'][1:])}</p>
          <div class="s-actions">
            {btn(s['page'], 'Read notebook', 'soft', icon=ICONS['read'])}
            {btn(colab_url(s['rel']), 'Colab', 'ghost', True, ICONS['play'])}
            {btn(kaggle_url(s['rel']), 'Kaggle', 'ghost', True, ICONS['play'])}
            {btn('../../' + s['rel'], '.ipynb', 'ghost', icon=ICONS['down'], download=True)}
            {flag}
          </div>
        </div>
      </li>""")

    prev_c = BY_N.get(c["n"] - 1)
    next_c = BY_N.get(c["n"] + 1)
    pager = '<nav class="pager" aria-label="Other courses">'
    pager += (f'<a class="prev" href="../{slug(prev_c)}/index.html"><span>Previous course</span>'
              f'{esc(prev_c["title"])}</a>') if prev_c else "<span></span>"
    pager += (f'<a class="next" href="../{slug(next_c)}/index.html"><span>Next course</span>'
              f'{esc(next_c["title"])}</a>') if next_c else "<span></span>"
    pager += "</nav>"

    chips = "".join(f"<li>{esc(t)}</li>" for t in c["topics"])
    body = f"""
<section class="course-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="../../index.html">Courses</a><span>/</span><span>Course {c['n']}</span></nav>
    <div class="ch-meta"><span class="course-num">Course {c['n']}</span>{level_badge(c['level'])}<span class="track">{esc(c['track'])}</span></div>
    <h1>{esc(c['title'])}</h1>
    <p class="lead">{esc(c['summary'])}</p>
    <ul class="chips">{chips}</ul>
    <div class="hero-cta">
      {btn(sessions[0]['page'], 'Start session 1', 'primary', icon=ICONS['arrow'])}
      {btn('../../' + pdf, 'Course document (PDF)', 'ghost', icon=ICONS['doc']) if pdf else ''}
      {btn('https://github.com/' + REPO + '/tree/' + BRANCH + '/' + c['folder'], 'Folder on GitHub', 'ghost', True, GH_ICON)}
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap course-layout">
    <div>
      <h2 class="list-title">Sessions</h2>
      <ol class="sessions">{''.join(rows)}
      </ol>
    </div>
    <aside class="side">
      <div class="side-card">
        <h3>At a glance</h3>
        <dl>
          <dt>Sessions</dt><dd>{len(sessions)}</dd>
          <dt>Level</dt><dd>{esc(c['level'])}</dd>
          <dt>Prerequisites</dt><dd>{esc(c['prereq'])}</dd>
          <dt>Each session</dt><dd>3 video segments, a lab, a quiz and an assignment</dd>
        </dl>
      </div>
      <div class="side-card prose small">
        <h3>Before you start</h3>
        {readme_html(c)}
      </div>
    </aside>
  </div>
  <div class="wrap">{pager}</div>
</section>
"""
    return page(c["title"], body, 2, description=c["summary"])


# ---------------------------------------------------------------------------
# Notebook pages
# ---------------------------------------------------------------------------
exporter = HTMLExporter(template_name="basic")
exporter.exclude_input_prompt = True
exporter.exclude_output_prompt = True

MATHJAX = """<script>
window.MathJax = {tex: {inlineMath: [['$','$'], ['\\\\(','\\\\)']], displayMath: [['$$','$$'], ['\\\\[','\\\\]']], processEscapes: true},
  options: {skipHtmlTags: ['script','noscript','style','textarea','pre','code']}};
</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-chtml.min.js"></script>"""


def strip_header(nb):
    nb = nbformat.from_dict(json.loads(json.dumps(nb)))  # deep copy
    if nb.cells and nb.cells[0].cell_type == "markdown":
        lines = nb.cells[0].source.splitlines()
        kept = [ln for ln in lines
                if not ln.startswith("# Course") and not ln.startswith("## Session")
                and not ln.startswith("**Goal:**")]
        nb.cells[0].source = "\n".join(kept).strip()
        if not nb.cells[0].source:
            nb.cells.pop(0)
    return nb


def build_session(c, sessions, i):
    s = sessions[i]
    nb_html, _ = exporter.from_notebook_node(strip_header(s["nb"]))
    prev_s = sessions[i - 1] if i > 0 else None
    next_s = sessions[i + 1] if i + 1 < len(sessions) else None
    pager = '<nav class="pager" aria-label="Other sessions">'
    pager += (f'<a class="prev" href="{prev_s["page"]}"><span>Previous session</span>'
              f'{prev_s["num"]:02d} · {esc(prev_s["title"])}</a>') if prev_s else \
             f'<a class="prev" href="index.html"><span>Back to</span>Course {c["n"]} overview</a>'
    pager += (f'<a class="next" href="{next_s["page"]}"><span>Next session</span>'
              f'{next_s["num"]:02d} · {esc(next_s["title"])}</a>') if next_s else \
             f'<a class="next" href="index.html"><span>Finished</span>Course {c["n"]} overview</a>'
    pager += "</nav>"

    toc = "".join(
        f'<li{" class=current" if t is s else ""}><a href="{t["page"]}"><span>{t["num"]:02d}</span>{esc(t["title"])}</a></li>'
        for t in sessions)

    goal = s["goal"][:1].upper() + s["goal"][1:]
    body = f"""
<section class="nb-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="../../index.html">Courses</a><span>/</span>
      <a href="index.html">Course {c['n']}: {esc(c['title'])}</a><span>/</span><span>Session {s['num']}</span></nav>
    <p class="eyebrow">Session {s['num']:02d} of {len(sessions)}</p>
    <h1>{esc(s['title'])}</h1>
    <p class="lead"><strong>Goal:</strong> {esc(goal)}</p>
    <div class="hero-cta">
      {btn(colab_url(s['rel']), 'Open in Colab', 'primary', True, ICONS['play'])}
      {btn(kaggle_url(s['rel']), 'Open in Kaggle', 'ghost', True, ICONS['play'])}
      {btn('../../' + s['rel'], 'Download .ipynb', 'ghost', icon=ICONS['down'], download=True)}
      {btn(github_url(s['rel']), 'View on GitHub', 'ghost', True, GH_ICON)}
    </div>
  </div>
</section>
<section class="section tight">
  <div class="wrap nb-layout">
    <aside class="nb-toc" aria-label="Sessions in this course">
      <p class="toc-title"><a href="index.html">Course {c['n']}</a></p>
      <ol>{toc}</ol>
    </aside>
    <article class="notebook prose">
      {nb_html}
      {pager}
    </article>
  </div>
</section>
"""
    return page(f"{s['title']} — Course {c['n']}", body, 2, description=goal, extra_head=MATHJAX)


# ---------------------------------------------------------------------------
# Assets
# ---------------------------------------------------------------------------
def write_assets(out):
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    css_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css")
    light = HtmlFormatter(style="friendly").get_style_defs(".highlight")
    dark = HtmlFormatter(style="github-dark").get_style_defs(":root:not([data-theme=light]) .highlight")
    with open(os.path.join(out, "assets", "site.css"), "w", encoding="utf-8") as f:
        f.write(open(css_src, encoding="utf-8").read())
        f.write("\n/* ---- code highlighting (generated) ---- */\n")
        f.write(light.replace(".highlight  { background: #f0f0f0; }", ""))
        f.write("\n@media (prefers-color-scheme: dark) {\n")
        f.write(dark)
        f.write("\n}\n.highlight, .highlight pre { background: transparent !important; }\n")
    with open(os.path.join(out, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" '
                'fill="#2f54eb"/><path d="M9 22 16 9l7 13M11.6 17.5h8.8" fill="none" stroke="#fff" '
                'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


MARKER = ".built-by-build_site"


def prepare_out(out):
    """Empty the output folder, but only if this script created it."""
    out = os.path.abspath(out)
    if os.path.abspath(ROOT) == out or os.path.abspath(ROOT).startswith(out + os.sep):
        sys.exit(f"Refusing to build into {out}: it contains the course sources.")
    if os.path.isdir(out) and os.listdir(out):
        if not os.path.exists(os.path.join(out, MARKER)):
            sys.exit(f"Refusing to build into {out}: the folder already has files that this script "
                     f"did not create (no {MARKER} file). Choose an empty or new folder.")
        shutil.rmtree(out)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, MARKER), "w", encoding="utf-8") as f:
        f.write("This folder is generated by tools/build_site.py in motiur/onlineCourses. "
                "Edit the sources there and rebuild instead of editing these files.\n")
    return out


def copy_downloads(out, all_sessions):
    """Copy each course PDF and notebook so the site's download links work on their own."""
    for c in COURSES:
        files = [s["rel"] for s in all_sessions[c["n"]]]
        pdf = course_pdf(c)
        if pdf:
            files.append(pdf)
        for rel in files:
            dst = os.path.join(out, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(ROOT, rel), dst)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True,
                    help="output folder, e.g. ../motiur.github.io/onlineCourses")
    out = prepare_out(ap.parse_args().out)

    write_assets(out)
    all_sessions = {c["n"]: load_sessions(c) for c in COURSES}
    for c in COURSES:
        cdir = os.path.join(out, "courses", slug(c))
        os.makedirs(cdir, exist_ok=True)
        sessions = all_sessions[c["n"]]
        with open(os.path.join(cdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(build_course(c, sessions))
        for i in range(len(sessions)):
            with open(os.path.join(cdir, sessions[i]["page"]), "w", encoding="utf-8") as f:
                f.write(build_session(c, sessions, i))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_home(all_sessions))
    copy_downloads(out, all_sessions)
    n = sum(len(v) for v in all_sessions.values())
    print(f"Built home page, {len(COURSES)} course pages and {n} notebook pages in {out}.")


if __name__ == "__main__":
    main()

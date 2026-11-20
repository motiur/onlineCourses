# onlineCourses

Materials for an AI teaching YouTube channel: sixteen courses running from beginner level to current research. Courses 1–15 are numbered in the order to take them; Course 16 was added later and fits any time after Course 1. Each course has 12 sessions, a course document (PDF) and one Jupyter notebook per session (192 notebooks in all).

**Website:** https://motiur.github.io/onlineCourses/

> **Instructor material.** The course documents include quiz answers and assignment solutions, and the Course 15 notebooks include reference solutions at the bottom.

## Courses, in the order to take them

| # | Course | Stage | Folder |
|---|---|---|---|
| 1 | From Beginner to an AI Research Lab | Foundations: start here | [Course_1_From_Beginner_to_an_AI_Research_Lab](Course_1_From_Beginner_to_an_AI_Research_Lab) |
| 2 | Mathematics for Machine Learning | Foundations: with or after Course 1 | [Course_2_Mathematics_for_Machine_Learning](Course_2_Mathematics_for_Machine_Learning) |
| 3 | Ten Years of Deep Learning Ideas | Foundations | [Course_3_Ten_Years_of_Deep_Learning_Ideas](Course_3_Ten_Years_of_Deep_Learning_Ideas) |
| 4 | Large Language Models | Build | [Course_4_Large_Language_Models](Course_4_Large_Language_Models) |
| 5 | Building a Small Bangla Language Model | Build: a project after Course 4 | [Course_5_Building_a_Small_Bangla_Language_Model](Course_5_Building_a_Small_Bangla_Language_Model) |
| 6 | Winning Online AI Competitions | Build: practical; can run alongside the others once Course 3 is done | [Course_6_Winning_Online_AI_Competitions](Course_6_Winning_Online_AI_Competitions) |
| 7 | Geometric Deep Learning and Graphs | Research | [Course_7_Geometric_Deep_Learning_and_Graphs](Course_7_Geometric_Deep_Learning_and_Graphs) |
| 8 | Privacy-Preserving Machine Learning | Research: uses Courses 4 and 7 | [Course_8_Privacy_Preserving_ML](Course_8_Privacy_Preserving_ML) |
| 9 | Mathematics and AI | Research: goes deeper on Course 7's symmetry | [Course_9_Mathematics_and_AI](Course_9_Mathematics_and_AI) |
| 10 | Deep Learning on Curved Spaces | Research: after Courses 2 and 7 | [Course_10_Deep_Learning_on_Curved_Spaces](Course_10_Deep_Learning_on_Curved_Spaces) |
| 11 | On-Device AI | Deploy and apply: after Course 3 | [Course_11_On_Device_AI](Course_11_On_Device_AI) |
| 12 | AI for Accessibility | Deploy and apply: after Course 3 | [Course_12_AI_for_Accessibility](Course_12_AI_for_Accessibility) |
| 13 | Machine Learning for Agriculture and Climate | Deploy and apply: after Course 1 | [Course_13_ML_for_Agriculture_and_Climate](Course_13_ML_for_Agriculture_and_Climate) |
| 14 | AI Research in 2026 | Stay current: checked November 2026 | [Course_14_AI_Research_in_2026](Course_14_AI_Research_in_2026) |
| 15 | Research Engineering Interviews | Get hired: any time after Course 1 | [Course_15_Research_Engineering_Interviews](Course_15_Research_Engineering_Interviews) |
| 16 | Algorithms Behind Modern AI | Foundations: for students who know data structures; any time after Course 1 | [Course_16_Algorithms_Behind_Modern_AI](Course_16_Algorithms_Behind_Modern_AI) |

The deploy-and-apply courses (11–13) do not need the research courses: take them any time after the courses named in the Stage column.

Course 16 was added on 20 November 2026 and keeps the number 16, so that no other course had to be renumbered. It belongs with the foundations: take it after a data structures course and Course 1. It also prepares for the coding rounds of Course 15.

The courses were renumbered into this order on 19 November 2026, when Courses 2 and 10–13 were added. Numbers before (18 November) → now: 1 → 1, 2 → 3, 3 → 4, 4 → 5, 5 → 6, 6 → 7, 7 → 8, 8 → 9, 9 → 14, 10 → 15, 11 → 2, and the new courses took 10–13. The text of the live Claude docs was updated to the new numbers on 19 November 2026, but their titles still show the original numbers until they are renamed on claude.ai, and the two planning PDFs keep the original numbers. Original → now: 1 → 7, 2 → 8, 3 → 4, 4 → 9, 5 → 6, 6 → 1, 7 → 5, 8 → 15.

Each course folder contains:

- `*_course_document.pdf`: session content (three video segments per session with pause-and-try questions, a lab, a quiz, a misconception to address, answers and sources; Courses 1–3, 5 and 10–16 also have talking pointers, lab guides and graded assignments).
- `notebooks/`: `s01_...` to `s12_...`, plus a `README.md` saying which cells were run and any extra `pip install` needed.
- Courses 2, 3, 10–14 and 16 also have `course_document.md`, the Markdown source of their PDF. Edit it, then rebuild the PDF with `python3 tools/build_course_pdf.py <course folder>`. Their notebooks are saved with their outputs, so the numbers can be read without running anything.

## Planning

- [planning/00_Channel_Research_and_Plan.pdf](planning/00_Channel_Research_and_Plan.pdf): channel research, audience, YouTube rules and monetization, curriculum and launch timeline.
- [planning/00_Syllabus_Courses_1-4.pdf](planning/00_Syllabus_Courses_1-4.pdf): syllabi for what are now Courses 7, 8, 4 and 9, written before the renumbering (its "Courses 1–4" are the original numbers).
- [planning/course-index.md](planning/course-index.md): index of the live docs, notebook notes and open items.

The PDFs for Courses 1, 4–9 and 15 are exports of the live docs, with their course numbers updated to the new order; the live docs' text now uses the same numbers. Courses 2, 3, 10–14 and 16 are edited as Markdown in this repository.

## How the notebooks were checked

- Every code cell not labelled **NOT RUN** (or left as a student TODO stub) was executed once, top to bottom, on CPU, and every notebook passes nbformat validation.
- Runnable cells use small built-in or synthetic data, so their numbers illustrate how a method behaves; they are not benchmark results.
- Cells labelled **NOT RUN** need a GPU, a download, an account, or a library that was not installed (for example PyTorch Geometric, escnn, e3nn, Opacus, Flower, TenSEAL, CatBoost, TabPFN, timm, transformers, peft, vLLM, LeanDojo, geoopt, pyRiemann, MediaPipe, Whisper, llama.cpp, LiteRT, xarray, tokenizers, tiktoken, Outlines, datasketch, FAISS, hnswlib). They were written from documented interfaces and have not been executed. Dry-run each one before recording, and expect to fix some calls.
- The Lean 4 code in Course 9 (sessions 9 and 11) was not compiled.
- Courses 2, 3, 10–14 and 16 were executed with `tools/run_notebook.py`, which runs every cell except NOT RUN cells and saves the outputs, then re-run independently: every printed number reproduced, apart from timings. Course 11 prints many latencies and speed-ups, and those change from run to run; its sizes, operation counts and accuracies reproduced exactly. Course 16 reports exact operation counts, which reproduced, next to timings, which vary.

## Running a notebook

Upload it to Kaggle Notebooks or Google Colab and run from the top. Course 11's sessions 2, 4, 7 and 11 first need `pip install onnx onnxscript onnxruntime`.

## The website

The site at https://motiur.github.io/onlineCourses/ is generated from the course folders by `tools/build_site.py` and published from the [motiur.github.io](https://github.com/motiur/motiur.github.io) repository, in its `onlineCourses/` folder. GitHub Pages is **not** switched on for this repository: leave it off, because a Pages site here would take over the same address.

To update the site after changing a notebook or course, check out both repositories side by side, then from this repository's root:

```bash
pip install nbconvert
```

```bash
python3 tools/build_site.py --out ../motiur.github.io/onlineCourses
```

Then commit and push `motiur.github.io`. The script only replaces a folder it built itself, so it will not overwrite anything else in that repository.

Course titles, summaries and topics shown on the site are set in the `COURSES` list at the top of the script; page styles are in `tools/site.css`.

# onlineCourses

Materials for an AI teaching YouTube channel: ten courses running from beginner level to current research, numbered in the order to take them. Each course has 12 sessions, a course document (PDF) and one Jupyter notebook per session (120 notebooks in all).

**Website:** https://motiur.github.io/onlineCourses/

> **Instructor material.** The course documents include quiz answers and assignment solutions, and the Course 10 notebooks include reference solutions at the bottom.

## Courses, in the order to take them

| # | Course | Stage | Folder |
|---|---|---|---|
| 1 | From Beginner to an AI Research Lab | Foundations: start here | [Course_1_From_Beginner_to_an_AI_Research_Lab](Course_1_From_Beginner_to_an_AI_Research_Lab) |
| 2 | Ten Years of Deep Learning Ideas | Foundations | [Course_2_Ten_Years_of_Deep_Learning_Ideas](Course_2_Ten_Years_of_Deep_Learning_Ideas) |
| 3 | Large Language Models | Build | [Course_3_Large_Language_Models](Course_3_Large_Language_Models) |
| 4 | Building a Small Bangla Language Model | Build: a project after Course 3 | [Course_4_Building_a_Small_Bangla_Language_Model](Course_4_Building_a_Small_Bangla_Language_Model) |
| 5 | Winning Online AI Competitions | Build: practical; can run alongside the others once Course 2 is done | [Course_5_Winning_Online_AI_Competitions](Course_5_Winning_Online_AI_Competitions) |
| 6 | Geometric Deep Learning and Graphs | Research | [Course_6_Geometric_Deep_Learning_and_Graphs](Course_6_Geometric_Deep_Learning_and_Graphs) |
| 7 | Privacy-Preserving Machine Learning | Research: uses Courses 3 and 6 | [Course_7_Privacy_Preserving_ML](Course_7_Privacy_Preserving_ML) |
| 8 | Mathematics and AI | Research: goes deeper on Course 6's symmetry | [Course_8_Mathematics_and_AI](Course_8_Mathematics_and_AI) |
| 9 | AI Research in 2026 | Stay current: checked November 2026 | [Course_9_AI_Research_in_2026](Course_9_AI_Research_in_2026) |
| 10 | Research Engineering Interviews | Get hired: any time after Course 1 | [Course_10_Research_Engineering_Interviews](Course_10_Research_Engineering_Interviews) |

The courses were renumbered into this order on 18 November 2026. Old number → new number: 1 → 6, 2 → 7, 3 → 3, 4 → 8, 5 → 5, 6 → 1, 7 → 4, 8 → 10, 9 → 2, 10 → 9. The folders, notebooks, PDFs and website use the new numbers; the live Claude docs and the two planning PDFs still use the old ones.

Each course folder contains:

- `*_course_document.pdf`: session content (three video segments per session with pause-and-try questions, a lab, a quiz, a misconception to address, answers and sources; Courses 1, 2, 4, 9 and 10 also have talking pointers, lab guides and graded assignments).
- `notebooks/`: `s01_...` to `s12_...`, plus a `README.md` saying which cells were run and any extra `pip install` needed.
- Courses 2 and 9 also have `course_document.md`, the Markdown source of their PDF. Edit it, then rebuild the PDF with `python3 tools/build_course_pdf.py <course folder>`. Their notebooks are saved with their outputs, so the numbers can be read without running anything.

## Planning

- [planning/00_Channel_Research_and_Plan.pdf](planning/00_Channel_Research_and_Plan.pdf): channel research, audience, YouTube rules and monetization, curriculum and launch timeline.
- [planning/00_Syllabus_Courses_1-4.pdf](planning/00_Syllabus_Courses_1-4.pdf): syllabi for what are now Courses 6, 7, 3 and 8, written before the renumbering (its "Courses 1–4" are the old numbers).
- [planning/course-index.md](planning/course-index.md): index of the live docs, notebook notes and open items.

The PDFs for Courses 1, 3–8 and 10 are exports of the live docs, with their course numbers updated to the new order; the live docs themselves still carry the old numbers. Courses 2 and 9 are edited as Markdown in this repository.

## How the notebooks were checked

- Every code cell not labelled **NOT RUN** (or left as a student TODO stub) was executed once, top to bottom, on CPU, and every notebook passes nbformat validation.
- Runnable cells use small built-in or synthetic data, so their numbers illustrate how a method behaves; they are not benchmark results.
- Cells labelled **NOT RUN** need a GPU, a download, an account, or a library that was not installed (for example PyTorch Geometric, escnn, e3nn, Opacus, Flower, TenSEAL, CatBoost, TabPFN, timm, transformers, peft, vLLM, LeanDojo). They were written from documented interfaces and have not been executed. Dry-run each one before recording, and expect to fix some calls.
- The Lean 4 code in Course 8 (sessions 9 and 11) was not compiled.
- Courses 2 and 9 were executed with `tools/run_notebook.py`, which runs every cell except NOT RUN cells and saves the outputs, then re-run independently: every printed number reproduced, apart from timings.

## Running a notebook

Upload it to Kaggle Notebooks or Google Colab and run from the top.

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

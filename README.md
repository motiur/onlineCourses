# onlineCourses

Materials for an AI teaching YouTube channel: eight courses running from beginner level to current research. Each course has 12 sessions, a course document (PDF) and one Jupyter notebook per session (96 notebooks in all).

**Website:** https://motiur.github.io/onlineCourses/

> **Instructor material.** The course documents include quiz answers and assignment solutions, and the Course 8 notebooks include reference solutions at the bottom. Remove these before sharing anything with students or making this repository public.

## Courses

| # | Course | Folder |
|---|---|---|
| 1 | Geometric Deep Learning and Graphs | [Course_1_Geometric_Deep_Learning_and_Graphs](Course_1_Geometric_Deep_Learning_and_Graphs) |
| 2 | Privacy-Preserving Machine Learning | [Course_2_Privacy_Preserving_ML](Course_2_Privacy_Preserving_ML) |
| 3 | Large Language Models | [Course_3_Large_Language_Models](Course_3_Large_Language_Models) |
| 4 | Mathematics and AI | [Course_4_Mathematics_and_AI](Course_4_Mathematics_and_AI) |
| 5 | Winning Online AI Competitions | [Course_5_Winning_Online_AI_Competitions](Course_5_Winning_Online_AI_Competitions) |
| 6 | From Beginner to an AI Research Lab | [Course_6_From_Beginner_to_an_AI_Research_Lab](Course_6_From_Beginner_to_an_AI_Research_Lab) |
| 7 | Building a Small Bangla Language Model | [Course_7_Building_a_Small_Bangla_Language_Model](Course_7_Building_a_Small_Bangla_Language_Model) |
| 8 | Research Engineering Interviews | [Course_8_Research_Engineering_Interviews](Course_8_Research_Engineering_Interviews) |

Each course folder contains:

- `*_course_document.pdf`: session content (three video segments per session with pause-and-try questions, a lab, a quiz, a misconception to address, answers and sources; Courses 6 to 8 also have talking pointers, lab guides and graded assignments).
- `notebooks/`: `s01_...` to `s12_...`, plus a `README.md` saying which cells were run and any extra `pip install` needed.

Suggested order: Course 6 is the entry course for beginners. Then Course 1, 3, 2, 4. Course 5 can run alongside any of them. Course 7 follows Course 6 (or 3), and Course 8 follows Course 6.

## Planning

- [planning/00_Channel_Research_and_Plan.pdf](planning/00_Channel_Research_and_Plan.pdf): channel research, audience, YouTube rules and monetization, curriculum and launch timeline.
- [planning/00_Syllabus_Courses_1-4.pdf](planning/00_Syllabus_Courses_1-4.pdf): syllabi for Courses 1 to 4.
- [planning/course-index.md](planning/course-index.md): index of the live docs, notebook notes and open items.

The PDFs are exports of the live docs; edit the live versions.

## How the notebooks were checked

- Every code cell not labelled **NOT RUN** (or left as a student TODO stub) was executed once, top to bottom, on CPU, and every notebook passes nbformat validation.
- Runnable cells use small built-in or synthetic data, so their numbers illustrate how a method behaves; they are not benchmark results.
- Cells labelled **NOT RUN** need a GPU, a download, an account, or a library that was not installed (for example PyTorch Geometric, escnn, e3nn, Opacus, Flower, TenSEAL, CatBoost, TabPFN, timm, transformers, peft, vLLM, LeanDojo). They were written from documented interfaces and have not been executed. Dry-run each one before recording, and expect to fix some calls.
- The Lean 4 code in Course 4 (sessions 9 and 11) was not compiled.

## Running a notebook

Upload it to Kaggle Notebooks or Google Colab and run from the top.

## The website

The site (`index.html`, `courses/`, `assets/`) is generated from the course folders by `tools/build_site.py`. After changing a notebook or course, rebuild and commit:

```bash
pip install nbconvert
python3 tools/build_site.py
```

Course titles, summaries and topics shown on the site are set in the `COURSES` list at the top of the script; page styles are in `tools/site.css`. GitHub Pages serves the `main` branch from the repository root.

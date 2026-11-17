# YouTube Course: index

Docs for Mohammad's AI teaching channel, which runs from beginner level to current research. Written by Claude, 17 November 2026.

## Docs

- [AI Teaching YouTube Channel: Research & Plan](https://claude.ai/artifact/5CZjPijrNbkTgZsKwTF6RM): research on what makes teaching videos work, the Bangladeshi audience, YouTube rules and monetization, a curriculum ladder and a launch timeline.
- [Four Courses on Current AI Research](https://claude.ai/artifact/N1vPB4dx5dB7hgC71M4f61): syllabi for four 12-session courses (geometric deep learning, privacy-preserving ML, LLMs, and mathematics and AI), the session format, capstones, instructor notes and sources.
- [Course 1 Content: Geometric Deep Learning and Graphs](https://claude.ai/artifact/Aj2tFgmHto718Pk26DLHeY): ready-to-teach content for all 12 sessions of Course 1.
- [Course 2 Content: Privacy-Preserving Machine Learning](https://claude.ai/artifact/3mxAS3bNFoYdw27ZngjMoz): ready-to-teach content for all 12 sessions of Course 2.
- [Course 3 Content: Large Language Models](https://claude.ai/artifact/QZ4fGnMa6DH7tb9NJA3bQ4): ready-to-teach content for all 12 sessions of Course 3.
- [Course 4 Content: Mathematics and AI](https://claude.ai/artifact/6P1AhAgPTfN7C5oHEyrY39): ready-to-teach content for all 12 sessions of Course 4.
- [Course 5: Winning Online AI Competitions](https://claude.ai/artifact/1Q1dA1MEUvrTKno5QDYVYn): its own syllabus (with readings, labs and a live-competition capstone) plus ready-to-teach content for all 12 sessions, from choosing a contest and validation through tabular, vision, LLM and reasoning competitions to ensembling and write-ups.
- [Course 6: From Beginner to an AI Research Lab](https://claude.ai/artifact/NLVeGztHw1T3K2WzqAxodX): its own syllabus (with readings, labs and a reproduce-and-extend capstone) plus ready-to-teach content for all 12 sessions, from lab types and foundations (math, code, ML, deep learning, transformers) through reading, reproducing, experiments, project scoping and writing to applications, cold emails and interviews. Every session also has talking pointers for the camera, a step-by-step lab guide (starter code, expected results, common problems) and a graded 10-point assignment. The doc also has a "Delivering the sessions on camera" section, a staged 12–18 month roadmap with gates, a readiness check, and a toolkit: catch-up and stretch tasks per session, a capstone paper shortlist, rubrics, templates, fallback plans and an interview question bank.
- [Course 7: Building a Small Bangla Language Model](https://claude.ai/artifact/EeFta9sLimwtx9t4D9aDRn): syllabus plus all 12 sessions, each with talking pointers, three segments, a lab guide, a quiz, a misconception and a graded assignment. Students take a 5–30M-parameter Bangla GPT from raw text to a public release: Unicode cleaning, corpus, tokenizer, model, training on free GPUs, evaluation, instruction tuning against a LoRA baseline, compression, responsible release.
- [Course 8: Research Engineering Interviews](https://claude.ai/artifact/XiiapdFjeF7Mc3tLeDqyna): syllabus plus all 12 sessions in the same full format. Covers the interview loop, coding, tensors, ML from scratch, debugging, fundamentals, estimates, system design, research discussion, behavioral rounds and take-homes, ending in a four-round mock loop.

Each content doc gives every session three video segments with pause-and-try questions, a lab, a three-question quiz and one misconception to address, with answers and a sources list.

## Notebooks

- All eight courses now have one Jupyter notebook per session (96 in all). They were delivered to Mohammad in chat on 17 November 2026 as one bundle, `AI_YouTube_Courses.zip`, which also holds a PDF export of every course document and a README. The notebooks are not stored in this project.
- Every code cell that is not labelled NOT RUN (or left as a student TODO stub) was executed once on CPU, and every notebook passes nbformat validation. Runnable cells use small built-in or synthetic data, so their numbers are illustrations, not benchmark results.
- Cells labelled NOT RUN need a GPU, a download, an account or a library that was not installed (PyTorch Geometric, escnn, e3nn, OGB, Boltz-2, Opacus, Flower, TenSEAL, CatBoost, cuDF, TabPFN, timm, transformers, peft, bitsandbytes, trl, vLLM, LeanDojo, nanoGPT, MNIST). They were written from documented interfaces and have not been executed.
- Course 1: hand-written GCN, GIN, WL test, positional encodings, C4-equivariant CNN, EGNN, Poincaré embeddings, a small graph diffusion model, graph retrieval, spatio-temporal forecasting and link prediction, all on synthetic or scikit-learn data.
- Course 2: hand-written DP-SGD with a Rényi accountant (checked against the value in Abadi et al. 2016), canary auditing, FedAvg and FedProx, gradient inversion, DP-LoRA on a tiny GPT, a toy Paillier scheme (teaching only), private graph aggregation, SISA and PATE.
- Course 3: a toy Bangla grammar language with a tiny GPT, used for scaling laws, quantization, KV cache, speculative decoding, QLoRA, DPO, masked diffusion, a sparse autoencoder and distillation; GRPO on arithmetic; a scripted stand-in model for the agent harness.
- Course 4: groups, characters, steerable kernel bases, grokking (p = 47, small MLP), categories of layers, lenses, weight sharing from symmetry, sheaf diffusion, pass@k, counterexample search for wrong formalizations, and an evolve-and-evaluate cap-set search. The Lean 4 snippets in sessions 9 and 11 were NOT compiled.
- Course 5: synthetic competitions for metrics, leaderboard shake-up, validation, leaks, target encoding (LightGBM and XGBoost were run), forecasting, TTA, preference prediction, time budgets, blending and reproduction.
- Course 6: the lab code from the course doc with expected values asserted (sessions 2–6 and 9), and worksheets with checking helpers for the other sessions.
- Course 7 notebooks run on a 16-sentence Bangla sample. Course 8 notebooks give stubs with tests and reference solutions at the bottom.
- Results that came out against expectation are stated in the notebooks: plain DPO breaks the toy model without an anchoring loss (C3 s6); fine-tuning did not generalize to held-out objects (C3 s5); the position-embedding ablation showed no measurable difference (C6 s6); random search matched the evolutionary loop on cap sets (C4 s12); equal-weight blends were worse than the best single model (C5 s10).

## Status

These are Claude's suggestions, not yet confirmed by Mohammad.

- Suggested teaching order: Course 1, then 3, then 2, then 4. Course 5 is practical and can run alongside any of them. Course 6 is the entry course for beginners and can come first. Course 7 follows Course 6 (or Course 3), and Course 8 follows Course 6.
- All eight courses now have full session content and notebooks.
- The content docs include all answers, so hide them before sharing with students. Course 8 notebooks include reference solutions at the bottom.
- Courses 1–5: the notebooks run small CPU versions of each lab. The labs as written in the syllabus (real datasets, GPU training, Kaggle submissions, Lean, real LLMs) have still not been run. Do a dry run of each NOT RUN cell before recording.
- The course docs for Courses 1–5 do not yet mention the notebooks, and some notebooks use a smaller stand-in than the lab the doc names (for example p = 47 instead of 113 for grokking, 8x8 digits instead of MNIST or Bengali.AI graphemes).
- Course 6: the starter code in sessions 2, 4, 5, 6 and 9 was run on CPU on 17 November 2026. The MNIST and nanoGPT runs, and the capstone shortlist's timings on free compute, have not been run.
- Courses 7 and 8: every runnable notebook cell was executed once on CPU on 17 November 2026. For Course 7 that was on a 16-sentence sample, so no real corpus was downloaded, no real model was trained, and the BanglaBERT and LoRA comparisons were not run; data sizes, training times and scores in the lab guides are estimates.
- Course 8's descriptions of lab interview formats come from candidate-reported and third-party guides, and formats change; recheck before each run.
- Course 5's competition facts were checked in November 2026; ARC Prize 2026 results are due on 4 December 2026, so update session 11 after that.
- Course 6's program, admissions and visa facts were checked in November 2026. They change every year, so recheck session 12 before each run.

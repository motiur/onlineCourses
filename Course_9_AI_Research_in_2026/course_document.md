# Course 9: AI Research in 2026

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course that brings students up to date with AI research published or presented between January and mid-November 2026: how long AI agents can work, reinforcement learning for reasoning, multi-turn reliability, diffusion language models, what transformers can express, new optimizers, provable grokking, high-accuracy sampling, deception probes, AI on Erdős problems and 4D reconstruction. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

This course is a guided tour of the year's research. Each session takes one 2026 result, explains the background a student needs, states what the authors claim and on what evidence, discusses how sure we can be, and then reproduces the core idea at toy scale on a CPU. Many results come from papers honoured at ICLR, CVPR and ICML 2026; others are among the year's most discussed developments, such as the length of tasks AI agents can complete and AI's results on Erdős problems.

Scope: "2026 research" means work published or presented between January and mid-November 2026, including papers at 2026 conferences whose preprints first appeared in late 2025. The course leaves out robotics, AI for biology and medicine, interactive video world models, and policy and regulation, which each need a course of their own.

Prerequisites: the skills of Course 1. Course 2 is strongly recommended, and Course 3 helps for sessions 3–5.

Capstone: choose one 2026 paper (from this course, or another approved by the instructor, such as a NeurIPS 2026 paper), reproduce its central claim at toy scale, test it with three seeds, and report honestly whether it held: a four-page report and a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: the claim stated precisely, with its source and the paper version checked (15); a toy design that isolates that claim (20); runs with three seeds and honest uncertainty (25); a comparison with the paper that says what the toy can and cannot show (25); clarity of the report and video (15).

How facts were checked: in November 2026, against conference announcements and proceedings, arXiv listings and, for news, at least two independent reports. Numbers from papers are as their authors report them; this course has not reproduced them, except where a lab says so. Award claims are limited to those confirmed by an official page or by several independent reports.

This course dates fast. Update it after NeurIPS 2026 (6–12 December, Sydney, with satellite sites in Atlanta and Paris), and re-check every claim before each run.

### Sessions

1. **The year in AI research, and how to read it.** Students can place 2026's main research venues and results on a timeline, explain how preprints, peer review, awards and reproductions differ as evidence, and test whether a reported benchmark gain is larger than noise.
   - Read: International AI Safety Report 2026; Stanford HAI, The 2026 AI Index Report
   - Lab: about 2 hours, notebook `s01_reading_2026_research.ipynb`
2. **Agents and long tasks: measuring time horizons.** Students can explain how METR measures an AI agent's time horizon, fit one from task results, estimate a doubling time with uncertainty, and say why such measurements saturate.
   - Read: Kwa et al. 2025, Measuring AI Ability to Complete Long Tasks; METR 2026, Time Horizon 1.1
   - Lab: about 2.5 hours, notebook `s02_agent_time_horizons.ipynb`
3. **Reasoning with reinforcement learning: exploration and entropy.** Students can explain why RL with verifiable rewards tends to collapse a model's output entropy, how that affects pass@1 versus pass@k, what the 2026 work on clipping, entropy and spurious rewards found, and can measure these effects in a toy.
   - Read: Chen et al. 2026, Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward (ICLR 2026); Yue et al. 2025, Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
   - Lab: about 2 hours, notebook `s03_rlvr_exploration.ipynb`
4. **Lost in conversation: multi-turn reliability.** Students can explain the sharded-instruction method, the aptitude/unreliability decomposition and the main findings of "LLMs Get Lost In Multi-Turn Conversation", and can run the evaluation protocol on simulated conversations.
   - Read: Laban, Hayashi, Zhou & Neville 2026, LLMs Get Lost In Multi-Turn Conversation (ICLR 2026); Liu et al. 2026, Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation
   - Lab: about 2 hours, notebook `s04_lost_in_conversation.ipynb`
5. **Diffusion language models and the flexibility trap.** Students can explain how masked diffusion language models decode in any order, what "The Flexibility Trap" found about arbitrary order and reasoning, and can compare decoding orders on a toy model.
   - Read: Ni et al. 2026, The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (ICML 2026; first titled "The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models")
   - Lab: about 2 hours, notebook `s05_flexibility_trap.ipynb`
6. **What transformers can express.** Students can explain what "succinctness" measures, state the main results of "Transformers are Inherently Succinct" and the ACL 2026 local-attention paper, and can demonstrate an exponential gap in description size on small examples.
   - Read: Bergsträßer, Cotterell & Lin 2026, Transformers are Inherently Succinct (ICLR 2026); Beltagy et al. 2020, Longformer: The Long-Document Transformer
   - Lab: about 2 hours, notebook `s06_transformer_expressivity.ipynb`
7. **Optimizers in 2026: Polar Express and Muon.** Students can explain the polar decomposition and why Muon needs it, show how polynomial iterations approximate it with matrix multiplications only, say what Polar Express optimizes, and compare iteration schemes in training.
   - Read: Jordan et al. 2024, Muon: An optimizer for hidden layers in neural networks; Huang 2026, How Much Orthogonalization Does Muon Need? (preprint)
   - Lab: about 2 hours, notebook `s07_polar_express_muon.ipynb`
8. **Grokking, proved.** Students can state what "To Grok Grokking" proves, reproduce grokking in over-parameterized ridge regression, and show how weight decay, learning rate and initialization stretch or remove it.
   - Read: Xu, Vardi & Safran 2026, To Grok Grokking: Provable Grokking in Ridge Regression (ICML 2026); Power et al. 2022, Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets
   - Lab: about 2 hours, notebook `s08_provable_grokking.ipynb`
9. **Sampling with high accuracy.** Students can explain the difference between low-accuracy and high-accuracy samplers, why a Metropolis correction removes discretization bias, and what the ICML 2026 result achieves with gradient queries only.
   - Read: Chen, Chewi, Daskalakis & Rakhlin 2026, High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions (ICML 2026); Roberts & Tweedie 1996, Exponential convergence of Langevin distributions and their discrete approximations, Bernoulli 2(4)
   - Lab: about 2 hours, notebook `s09_high_accuracy_sampling.ipynb`
10. **Probes, obfuscation and honesty.** Students can explain linear probes for deception, what happens when a model is trained against a probe (honest, blatant and obfuscated outcomes), and the "censor's toolkit" argument, and can reproduce an outcome map in a toy.
   - Read: Taufeeque, Heimersheim, Gleave & Cundy 2026, The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (ICML 2026); Ball & Hackemann 2026, Position: The Alignment Community is Unintentionally Building a Censor's Toolkit (ICML 2026)
   - Lab: about 2 hours, notebook `s10_probes_and_obfuscation.ipynb`
11. **AI and mathematics: the Erdős problems.** Students can describe what AI systems did on Erdős problems in 2026, distinguish a formally verified proof from a claim, and verify number-theoretic statements by computer.
   - Read: Sothanaphan 2026, Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof; Google DeepMind Formal Conjectures, Erdős Problem 728
   - Lab: about 2 hours, notebook `s11_ai_and_erdos_problems.ipynb`
12. **Seeing in 4D: feed-forward reconstruction, and what comes next.** Students can explain how D4RT reconstructs dynamic scenes with one transformer and query-based decoding, why feed-forward reconstruction is taking over many jobs of per-scene optimization and what it gives up, and what to watch for at NeurIPS 2026.
   - Read: Zhang et al. 2026 (Google DeepMind, UCL and Oxford; with Sajjadi), Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (CVPR 2026); Sajjadi et al. 2022, Scene Representation Transformer: Geometry-Free Novel View Synthesis Through Set-Latent Scene Representations (CVPR 2022)
   - Lab: about 2 hours, notebook `s12_feedforward_4d_reconstruction.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. In this course, name the paper and its venue on screen, and separate clearly what the authors report from what the lab shows.
- **Labs are toys:** each notebook illustrates one paper's central idea on a CPU in a few minutes. It is not a reproduction of the paper, and its numbers say nothing about the paper's benchmarks.
- **Notebooks:** every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. Cells labelled NOT RUN need a GPU, a download, a model or an account; dry-run them before recording.
- **Dates:** every fact was checked in November 2026. Before each run of the course, re-check the sources, add what NeurIPS 2026 and later venues changed, and remove claims that did not hold up.

## Session 1: The year in AI research, and how to read it

**Goal:** students can place 2026's main research venues and results on a timeline, explain how preprints, peer review, awards and reproductions differ as evidence, and test whether a reported benchmark gain is larger than noise.

### Talking pointers

- **Open with:** "Every week of 2026 someone announced an AI breakthrough. This course is about deciding which claims to believe, and how much."
- **Segment 1, say:** draw the 2026 calendar as a timeline: ICLR in April, CVPR in June, ACL and ICML in July, NeurIPS in December, with each award marked.
- **Segment 2, say:** turn to the reports that sum up the year: an expert review, a data compilation, a measurement.
- **Segment 3, say:** show four levels of evidence, then work the 78% against 80% example out loud.
- **Close with:** "Before you repeat a number, ask what evidence stands behind it and how large the noise is." Then set assignment 1.

### Segment 1 (6 min): the 2026 calendar

- ICLR 2026 (International Conference on Learning Representations) met in Rio de Janeiro, 23–27 April. Its Outstanding Papers were "Transformers are Inherently Succinct" (Bergsträßer et al. 2026; session 6) and "LLMs Get Lost In Multi-Turn Conversation" (Laban et al. 2026; session 4). NYU reports an honorable mention for "The Polar Express" (Amsel et al. 2026; session 7).
- CVPR 2026 (Computer Vision and Pattern Recognition) met in Denver, 3–7 June. Its Best Paper was D4RT, one transformer that reconstructs moving scenes from video (Zhang et al. 2026; session 12).
- ACL 2026 (Association for Computational Linguistics) met in San Diego, 2–7 July, and ICML 2026 (International Conference on Machine Learning) in Seoul, 6–11 July. ICML's Outstanding Papers included "The Flexibility Trap" (Ni et al. 2026; session 5) and a sampling result (Chen et al. 2026; session 9).
- NeurIPS 2026 (Neural Information Processing Systems) runs 6–12 December in Sydney, with satellite sites in Atlanta and Paris, after this course was checked.
- Test-of-time awards went to 2016 papers. ICLR honoured DCGAN (Radford et al. 2016) and also DDPG (Lillicrap et al. 2016); ICML honoured A3C (Mnih et al. 2016); CVPR's Longuet-Higgins Prize went to ResNet (He et al. 2016), shared with YOLO (Redmon et al. 2016).
- **Pause and try:** ResNet won a prize ten years on. Which Course 2 session teaches it, and which single idea made it last?
  - **Answer:** Course 2, session 1. The identity shortcut y = x + F(x), a direct path for gradients through deep networks.

### Segment 2 (7 min): the bigger picture

- The International AI Safety Report 2026 (3 February), chaired by Yoshua Bengio, was written by over 100 experts and backed by over 30 countries and international organisations. It reviews evidence rather than running experiments, and reports that pre-deployment safety evaluations, the tests run before release, are under strain.
- The Stanford AI Index 2026 (April) compiles data on research, industry, policy and opinion. Summaries agree that industry produced over 90% of notable AI models in 2025; they disagree on other figures, so check the report before quoting one.
- Time Horizon 1.1 (January) from METR (Model Evaluation and Threat Research, a nonprofit) measures the length of tasks, in human working time, that AI agents complete half of the time; METR reports that it doubles about every 196 days (session 2).
- This course leaves out robotics, AI for biology and medicine, interactive video world models and policy.
- **Pause and try:** if a horizon doubles every 196 days, by roughly what factor does it grow in one year?
  - **Answer:** 365/196 ≈ 1.86 doublings, so 2^1.86 ≈ 3.6 times a year, if the trend holds.

### Segment 3 (7 min): reading claims

- Four levels of evidence: a **preprint** is posted but not reviewed; a **peer-reviewed** paper was read by reviewers, who rarely rerun it; an **award** means a committee judged it important; an **independent reproduction** means someone else got the same result. A Lean-checked proof is another kind of evidence (session 11).
- Benchmark scores are noisy: with n questions and accuracy p, the standard error is $\sqrt{p(1-p)/n}$. (Course 1, session 9 covers noise across seeds.)
- Compare two models on the same questions with a paired test (a paired bootstrap or McNemar's test), not by checking whether two intervals overlap.
- Reporting the best of many prompts, seeds or settings inflates the result; ask how many were tried.
- When you repeat a paper's number, say "the authors report".
- **Pause and try:** on a 500-question benchmark, model A scores 78% and model B 80%. Is B better?
  - **Answer:** not from these numbers: each has a 95% interval of about ±3.6 points, so the gap is within the noise. You need a paired test on per-question results, and probably more questions.

### Lab guide (about 2 hours, notebook `s01_reading_2026_research.ipynb`)

1. Section 2 (20 min): Wald and Wilson intervals, and the plot of interval width against the number of questions.
2. Section 3 (35 min): paired and unpaired bootstrap intervals and McNemar's test for two models on the same questions; then 1,000 repeated benchmarks.
3. Section 4 (25 min): pick the best of 20 identical prompts and re-test it on fresh questions.
4. Section 5 (20 min): read the claims ledger.
5. Section 6 (20 min): do the two TODOs.

- **Expect:** Wald intervals of 74.4 to 81.6 (78%) and 76.5 to 83.5 (80%), and 6,147 questions for a ±1-point interval at 80%. In one simulated run the measured gap was 0.8 points (true gap 2), with a paired interval of −3.8 to 5.2, an unpaired interval of −4.2 to 5.8, and McNemar p = 0.788. Over 1,000 repeats the paired interval detected the gain in 15.4% of runs (unpaired 10.0%), and B scored below A in 17.5%. The best of 20 identical prompts "gained" 2.89 points on average, and 0.04 points on a fresh set.
- **Common problems:** comparing two intervals instead of running a paired test; choosing and reporting the best prompt on the same test set; confusing percentage points with a percentage change.

### Quiz

1. How does a peer-reviewed paper differ from an independently reproduced result?
   - **Answer:** reviewers judge a paper but rarely rerun it; a reproduction means someone else got the same result from their own runs.
2. Why is a paired test better than comparing two intervals when two models answer the same questions?
   - **Answer:** their errors are linked through question difficulty. Per-question differences remove that shared variation, giving a narrower interval for the gap.
3. You try 20 prompts and report the best one. What happens to the reported gain, and how do you fix it?
   - **Answer:** selection inflates it (about 2.9 points in the lab, with no real difference). Choose on one set, report on a fresh set, and say how many variants you tried.

**Watch out:** "An award means a result is proven correct." Award committees judge importance and quality from the paper and its reviews; they do not usually replicate results. An award-winning paper can still contain errors, and its numbers still deserve "the authors report".

### Assignment 1 (due before session 2, 10 points)

1. A one-page timeline of 2026 AI research with at least eight dated entries, each linked to its official source. (3 points)
2. The section 6 TODO: a plot of detection rate against the number of questions for a true 2-point gain, the number that reaches 80%, and two sentences on what it means for 2-point claims. (4 points)
3. Five new ledger rows for 2026 papers you have read, each with its evidence level and one sentence on what would raise your confidence. (3 points)

Hand in one PDF and your notebook.

### Sources

- ICLR 2026, Announcing the ICLR 2026 Outstanding Papers. https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/
- ICLR 2026, Announcing the Test of Time Awards from ICLR 2016. https://blog.iclr.cc/2026/04/22/announcing-the-test-of-time-awards-from-iclr-2016/
- NYU Courant, news on The Polar Express honorable mention. https://cims.nyu.edu/ai/news/146/
- CVPR 2026, Best Papers. https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers
- CVPR 2026, Meeting Dates. https://cvpr.thecvf.com/Conferences/2026/Dates
- IEEE Computer Society, 2026 TCPAMI Awards. https://www.computer.org/press-room/2026-tcpami-awards
- ICML 2026, awards announcement. https://blog.icml.cc/?p=1347
- ACL 2026, conference site. https://2026.aclweb.org/
- NeurIPS 2026, Dates. https://neurips.cc/Conferences/2026/Dates
- International AI Safety Report 2026. https://internationalaisafetyreport.org
- Stanford HAI, The 2026 AI Index Report. https://hai.stanford.edu/ai-index/2026-ai-index-report
- METR 2026, Time Horizon 1.1. https://metr.org/blog/2026-1-29-time-horizon-1-1
- Bergsträßer, Cotterell & Lin 2026, Transformers are Inherently Succinct. https://arxiv.org/abs/2510.19315
- Laban et al. 2026, LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120
- Amsel et al. 2026, The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm. https://arxiv.org/abs/2505.16932
- Zhang et al. 2026, Efficiently Reconstructing Dynamic Scenes One D4RT at a Time. https://arxiv.org/abs/2512.08924
- Ni et al. 2026, The Flexibility Trap. https://arxiv.org/abs/2601.15165
- Chen, Chewi, Daskalakis & Rakhlin 2026, High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions. https://arxiv.org/abs/2602.01338
- Radford et al. 2016, Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks (DCGAN). https://arxiv.org/abs/1511.06434
- Lillicrap et al. 2016, Continuous Control with Deep Reinforcement Learning (DDPG). https://arxiv.org/abs/1509.02971
- Mnih et al. 2016, Asynchronous Methods for Deep Reinforcement Learning (A3C). https://arxiv.org/abs/1602.01783
- He et al. 2016, Deep Residual Learning for Image Recognition (ResNet). https://arxiv.org/abs/1512.03385
- Redmon et al. 2016, You Only Look Once: Unified, Real-Time Object Detection (YOLO). https://arxiv.org/abs/1506.02640

## Session 2: Agents and long tasks: measuring time horizons

**Goal:** students can explain how METR measures an AI agent's time horizon, fit one from task results, estimate a doubling time with uncertainty, and say why such measurements saturate.

### Talking pointers

- **Open with:** "How long a task can an AI agent finish on its own? METR answers with one number, in hours of human work, and in 2026 it became one of the most quoted numbers in AI."
- **Segment 1, say:** draw the logistic curve by hand: success rate against task length on a log scale, crossing 50% and then 80%.
- **Segment 2, say:** put METR's three doubling times (196, 131 and 89 days) on screen and ask why one data set gives three answers.
- **Segment 3, say:** show the lab's capped-suite table and its intervals that stop closing.
- **Close with:** "A trend line summarises the past; it is not a law of nature." Then set assignment 2.

### Segment 1 (7 min): the method

- Kwa et al. 2025 collected software, machine-learning and cybersecurity tasks and measured how long skilled humans take on each, from seconds to many hours. (Later versions are titled "Measuring AI Ability to Complete Long Software Tasks"; the paper appeared at NeurIPS 2025.)
- For each agent, fit a logistic curve of success probability against log task length, $p(t) = \sigma(a + b \log_2 t)$, where $\sigma$ is the logistic function. The **50% time horizon** is the length $t$ where $p = 0.5$; the **80% horizon** is where $p = 0.8$.
- The authors report that the 50% horizon of frontier agents grew exponentially from 2019 to 2025, doubling about every seven months, and that 80% horizons follow a similar trend but are roughly five times shorter.
- A horizon is not how long the agent works; it is the human time of tasks the agent completes half of the time.
- **Pause and try:** an agent's 50% horizon is 2 hours, and horizons double every 7 months. Roughly what is it after 14 months?
  - **Answer:** about 8 hours: two doublings, if the trend holds.

### Segment 2 (7 min): Time Horizon 1.1

- Time Horizon 1.1 (29 January 2026) from METR (Model Evaluation and Threat Research, a nonprofit) grew the suite from 170 to 228 tasks, and the tasks of 8 hours or longer from 14 to 31.
- Over 2019–2025 the doubling time barely moved: about 196 days, or 7 months. For models since 2023 it is 131 days (165 under the old suite), and since 2024, 89 days (109 before). METR notes that the new estimates generally lie within the old confidence intervals, but cautions that the two suites share many tasks.
- Why the change? METR notes that the new tasks differ slightly in difficulty. Recent models are also measured mainly by the long tasks, and a fit to a few recent models is noisy: in the lab, 10 simulated releases since 2024 gave 182 days (interval 140 to 265) for a true 196.
- Only 5 of the 31 long tasks have measured human times; the rest are estimates. METR says it is working to raise the ceiling of its measurements.
- **Pause and try:** compare doubling times of 89 and 109 days. How much growth in a year does each imply?
  - **Answer:** 365/89 ≈ 4.1 doublings, about 17 times; 365/109 ≈ 3.35 doublings, about 10 times. A modest change in the task set changes the extrapolation a lot.

### Segment 3 (6 min): saturation, scoring and trends

- A horizon can only be measured well within the suite's range of task lengths. METR's May 2026 Frontier Risk Report says the strongest models it assessed now reach the range where its suite cannot measure horizons reliably.
- When nearly every run succeeds, the data say only "longer than most tasks". In the lab, an agent with a true 64-hour horizon got an interval of 21.8 to 1,775.8 hours, and on a suite capped at 2 hours it could not be estimated at all.
- Scoring choices matter. METR counts a detected cheating attempt, such as editing the tests, as a failure (METR 2025). In the lab, counting 49 cheating runs as successes moved a 4-hour agent's estimate from 3.9 to 8.8 hours.
- Extrapolating assumes the task mix, the scoring and the pace of progress stay the same.
- **Pause and try:** an agent succeeds on 97% of runs on a suite whose longest task takes 16 hours. What can you say about its horizon?
  - **Answer:** that it is probably longer than most tasks in the suite, but the upper end is barely constrained, so expect a very wide interval.

### Lab guide (about 2.5 hours, notebook `s02_agent_time_horizons.ipynb`)

1. Sections 2–3 (30 min): build the 228-task suite and fit horizons for three agents.
2. Section 4 (25 min): bootstrap intervals over tasks, then the coverage check for agent C.
3. Section 5 (25 min): fit a doubling time to 20 simulated releases, then to the 10 since 2024.
4. Sections 6–7 (30 min): the capped suite and the cheating rule.
5. Section 8 (optional, on Colab): fit METR's public data.
6. Section 9 (20 min): the two TODOs.

- **Expect:** fitted 50% horizons of 14.2, 132.2 and 440.8 minutes for true values of 15, 120 and 600, with agent C's interval (364.0 to 544.1) missing the truth; repeated 100 times, agent C's interval covered the truth 91 times. The 80% horizons were roughly three times shorter (4.1, 46.7 and 149.0 minutes). The doubling time was 198 days (188 to 212) from all 20 releases and 182 days (140 to 265) from the 10 since 2024. On the full suite a 64-hour agent got 99.8 hours (21.8 to 1,775.8); on the 2-hour suite it was not identifiable. Counting cheats as successes moved 3.9 hours to 8.8 hours.
- **Common problems:** fitting against task length instead of log task length; resampling runs instead of tasks in the bootstrap (runs on one task are not independent); reading a horizon as hours of autonomous work.

### Quiz

1. What exactly is a 50% time horizon?
   - **Answer:** the human completion time of tasks that the agent succeeds on with probability 0.5, read from a logistic fit of success against log task length on one task suite.
2. Why did Time Horizon 1.1 change the recent doubling times but hardly the overall one?
   - **Answer:** METR points to the new tasks' different mix of difficulty. Also, long tasks mostly change the estimates of strong recent models, which dominate a recent-only fit, while the 2019–2025 fit also rests on many older models.
3. Why do estimates become unreliable near the top of the suite?
   - **Answer:** few tasks are longer than the agent's horizon, so few failures locate the 50% point; the interval widens or becomes unbounded.

**Watch out:** "A 16-hour horizon means the model can work for 16 hours on anything." It is the length, in human time, of tasks the model completes half of the time, on one task distribution made mostly of software and machine-learning work. At 80% reliability, or on other kinds of work, the horizon can be much shorter.

### Assignment 2 (due before session 3, 10 points)

1. The two TODOs: interval width with 1, 4 and 16 runs per task, and the doubling time of the 80% horizon with your explanation. (3 points)
2. A one-page critique of METR's Time Horizon 1.1 post: what was measured, three sources of uncertainty, and one change to the method you would test. (4 points)
3. Using the lab code, show how a suite capped at 4 hours biases the doubling time when the last three releases exceed the cap: one plot and three sentences. (3 points)

Hand in one PDF and your notebook.

### Sources

- Kwa et al. 2025, Measuring AI Ability to Complete Long Tasks. https://arxiv.org/abs/2503.14499
- NeurIPS 2025 listing, Measuring AI Ability to Complete Long Software Tasks. https://neurips.cc/virtual/2025/poster/119302
- METR 2026, Time Horizon 1.1. https://metr.org/blog/2026-1-29-time-horizon-1-1
- METR 2026, Frontier Risk Report (May 2026). https://metr.org/blog/2026-05-19-frontier-risk-report/
- METR 2025, Details about METR's preliminary evaluation of o3 and o4-mini (how cheating attempts are scored). https://evaluations.metr.org/openai-o3-report
- METR, eval-analysis-public (code and run data). https://github.com/METR/eval-analysis-public

## Session 3: Reasoning with reinforcement learning: exploration and entropy

**Goal:** students can explain why RL with verifiable rewards tends to collapse a model's output entropy, how that affects pass@1 versus pass@k, what the 2026 work on clipping, entropy and spurious rewards found, and can measure these effects in a toy.

### Talking pointers

- **Open with:** "Train a model with reinforcement learning on maths and its first answer gets better. Ask for a hundred answers, though, and the untrained model sometimes solves more problems. Today we see why."
- **Segment 1, say:** draw one problem's answer distribution before and after RL: a wide spread becomes a single spike. Compute pass@1 and pass@64 for both.
- **Segment 2, say:** write the clipped objective, point at the two clip bounds, and ask what each does to a rare answer and to a common one.
- **Segment 3, say:** show the lab's table of fixes: what each buys at k = 64 and what it costs at k = 1.
- **Close with:** "Entropy is something to measure, not a goal in itself." Then set assignment 3.

### Segment 1 (7 min): entropy collapse

- Recall Course 3, session 7: RLVR (reinforcement learning with verifiable rewards) rewards answers a program can check, and GRPO (group relative policy optimization; Shao et al. 2024) samples a group of answers per prompt and uses each answer's standardized reward as its advantage.
- Entropy measures how spread out the model's choices are. RL moves probability toward rewarded answers, so entropy falls. This sharpening raises pass@1 but can remove rare correct paths.
- pass@k is the chance that at least one of k samples is correct (Course 8, session 10 gives the estimator).
- Yue et al. 2025 report that RLVR-trained models beat their base models at small k, but that the base models reach higher pass@k at large k. They argue that current RLVR mostly re-weights paths the base model could already sample. The claim is debated; pass@k at several k is how to check it.
- **Pause and try:** before RL, a model solves problem X with probability 0.5 per attempt and problem Y with 0.05. After RL: X 0.95, Y 0. Compute the average pass@1 and pass@64 before and after.
  - **Answer:** pass@1 rises from 0.275 to 0.475. pass@64 falls from about 0.98 (Y: $1-0.95^{64} \approx 0.96$) to 0.50, because Y is now never solved.

### Segment 2 (7 min): clipping, entropy and spurious rewards

- PPO (proximal policy optimization) clipping limits how far one update can move an answer's probability ratio $r = \pi_{new}/\pi_{old}$, to between $1-\epsilon$ and $1+\epsilon$ (often $\epsilon = 0.2$).
- Shao et al. 2025 found that RLVR with random rewards could still raise maths scores for some open models, and linked the effect to clipping; the gains often did not carry over to other model families.
- Chen et al. 2026 (ICLR 2026) analysed this. They report that clipping bias under spurious rewards lowers policy entropy, making outputs more confident, and that lowering entropy alone is not enough to improve performance. They propose a reward-misalignment model to explain when spurious rewards can help.
- In the lab, random rewards lowered entropy more with clipping than without (0.854 against 1.032 nats for one base model) and kept the policy closer to its favourite strategy, but pass@1 did not rise (0.448, from 0.465).
- **Pause and try:** with $\epsilon = 0.2$, an answer with old probability 0.9 gets a positive advantage. Can its ratio reach the upper clip? What is the most an answer with old probability 0.05 can grow in one clipped step?
  - **Answer:** no, since its ratio is at most 1/0.9 ≈ 1.11 < 1.2. The rare answer can only grow to 0.06. Clipping limits rare answers in absolute terms far more than common ones.

### Segment 3 (6 min): keeping exploration alive

- Classic fixes: clip-higher raises only the upper bound (DAPO; Yu et al. 2025), so rare answers with positive advantage can grow faster; an entropy bonus, or a KL (Kullback–Leibler) penalty toward the base model, slows the collapse.
- Two 2026 preprints aim more directly at exploration. DSDR (Wan et al. 2026) adds diversity regularization at two scales: diversity among distinct correct solutions, and variation within each. ProGRPO (Li et al. 2026) re-weights advantages using the model's own probabilities, so correct paths that are already likely get smaller pushes. Both report gains in pass@1 and pass@k on maths benchmarks.
- In the lab, the entropy bonus kept pass@64 at 0.901 but cut pass@1 to 0.623. Clip-higher changed nothing, because the collapse there came from real differences in reward.
- **Pause and try:** the entropy bonus raised pass@64 from 0.735 to 0.901 but lowered pass@1 from 0.731 to 0.623. When would you accept that trade?
  - **Answer:** when you can sample many attempts and check them automatically, for example with unit tests or a proof checker. Not when a user sees only one answer.

### Lab guide (about 2 hours, notebook `s03_rlvr_exploration.ipynb`)

1. Section 2 (15 min): build the 600-problem task and compute the base metrics.
2. Section 3 (30 min): train GRPO with the true reward and read the entropy and pass@k curves.
3. Section 4 (30 min): random rewards with and without clipping, for two base models over 8 seeds.
4. Section 5 (25 min): clip-higher, entropy bonus and KL anchor, with the clip diagnostics.
5. Section 7 (20 min): the two TODOs.

- **Expect:** the good-prior base model had entropy 1.471, pass@1 0.465 and pass@64 0.914. After GRPO: entropy 0.009, pass@1 0.731, pass@64 0.735. With random rewards, the good prior ended at entropy 0.854 ± 0.052 with clipping and 1.032 ± 0.062 without (pass@1 0.448 and 0.335); the bad prior at 0.805 and 1.020 (pass@1 0.208 and 0.255). Clip-higher matched GRPO (entropy at step 20: 0.081 against 0.082) while cutting upper-bound hits from 1.14% to 0.11% of samples. The entropy bonus gave pass@1 0.623 and pass@64 0.901; the KL anchor 0.663 and 0.884.
- **Common problems:** trusting one seed (the random-reward gaps are about two standard errors with 8 seeds); estimating pass@k from too few samples; drawing conclusions about clipping without checking that the clip is active.

### Quiz

1. Why can RLVR raise pass@1 and lower pass@k at large k?
   - **Answer:** it concentrates probability on the answers that are most often right and removes rare paths that solve some problems; with many samples, those rare paths mattered.
2. What did Chen et al. 2026 report about spurious rewards?
   - **Answer:** that clipping bias under spurious rewards lowers policy entropy, giving more confident outputs, and that lowering entropy alone does not reliably improve performance.
3. What does clip-higher change, and why did it do nothing in the lab?
   - **Answer:** it raises the upper clip bound so rare answers with positive advantage can grow faster. In the toy the upper bound stopped only 1.14% of samples, and the collapse came from real reward differences.

**Watch out:** "Lower entropy means the model reasons better." Entropy measures spread, not correctness. In the lab, random rewards lowered entropy without raising pass@1, and the lowest-entropy policies had the worst pass@64. A falling entropy curve can mean the model found good answers or that it stopped exploring, so check pass@k at several values of k.

### Assignment 3 (due before session 4, 10 points)

1. The two TODOs, with a table comparing them with GRPO on entropy, pass@1 and pass@64 over 3 seeds. (4 points)
2. Section 4 repeated with 16 seeds: does the clipping effect on entropy hold? Report intervals. (3 points)
3. A half-page summary of Chen et al. 2026 or of one 2026 preprint: its claim, its evidence, and one experiment you would add. (3 points)

Hand in one PDF and your notebook.

### Sources

- Chen et al. 2026, Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward (ICLR 2026). https://arxiv.org/abs/2512.16912
- Yue et al. 2025, Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? https://arxiv.org/abs/2504.13837
- Shao et al. 2025, Spurious Rewards: Rethinking Training Signals in RLVR. https://arxiv.org/abs/2506.10947
- Shao et al. 2024, DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO). https://arxiv.org/abs/2402.03300
- Yu et al. 2025, DAPO: An Open-Source LLM Reinforcement Learning System at Scale. https://arxiv.org/abs/2503.14476
- Wan et al. 2026, DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning. https://arxiv.org/abs/2602.19895
- Li et al. 2026, Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities (ProGRPO). https://arxiv.org/abs/2602.05281

## Session 4: Lost in conversation: multi-turn reliability

**Goal:** students can explain the sharded-instruction method, the aptitude/unreliability decomposition and the main findings of "LLMs Get Lost In Multi-Turn Conversation", and can run the evaluation protocol on simulated conversations.

### Talking pointers

- **Open with:** "Benchmarks give a model the whole task in one message. Real users don't: they start vague, add details and change their minds. What happens to accuracy then?"
- **Segment 1, say:** take one benchmark instruction on screen, cut it into shards live, and replay it as five short user turns.
- **Segment 2, say:** draw ten runs of one task as dots, single-turn and multi-turn, and mark the 90th and 10th percentiles.
- **Segment 3, say:** turn the findings into advice, first for people who build assistants, then for people who use them.
- **Close with:** "When a conversation goes wrong, don't argue with it. Start again, with everything in one message." Then set assignment 4.

### Segment 1 (6 min): the setup

- Laban et al. 2026 (ICLR 2026 Outstanding Paper) turned single-turn benchmark instructions into **shards**. The first shard states the main request and each later shard adds one detail; a simulated user reveals one shard per turn.
- They compared fully specified single-turn instructions with sharded conversations on six generation tasks: code, database queries, actions (calls to an API, an application programming interface), maths, data-to-text and summaries. They tested 15 models in over 200,000 simulated conversations.
- The authors report that every model they tested did worse in multi-turn conversation, with an average drop of 39%.
- Course 3, session 8 introduced this paper; today we look at the measurement itself.
- **Pause and try:** a model scores 80 on the single-turn version of a task and 49 on the sharded version. What is the drop in percent?
  - **Answer:** (80 − 49)/80 ≈ 39%, about the paper's average.

### Segment 2 (7 min): aptitude versus unreliability

- Each instruction was simulated 10 times per setting. **Aptitude** is the 90th-percentile score of those runs, a best case. **Unreliability** is the 90th minus the 10th percentile, the gap between good and bad runs.
- The authors report that the drop is mostly unreliability: aptitude falls only modestly, while unreliability more than doubles (an average increase of 112%).
- The failure modes they describe: models make assumptions in early turns, attempt final answers too early and then rely too much on those attempts, so later answers become longer ("bloated"). When a model takes a wrong turn, it gets lost and does not recover.
- In the lab's toy, the eager assistant fell from a mean of 94.8 to 62.2, with aptitude falling from 100.0 to 78.8 and unreliability rising from 15.2 to 33.5. Those sizes come from our rules, not from any model.
- **Pause and try:** one task's 10 run scores are 100, 100, 95, 90, 60, 50, 40, 30, 20 and 10. Compute its aptitude and unreliability (use NumPy's default percentiles).
  - **Answer:** aptitude 100 and unreliability 81, because the 10th percentile is 19.

### Segment 3 (7 min): what to do

- The authors report that common fixes, such as an agent-style recap of every detail at the end or a lower temperature, are not enough.
- In the toy, temperature 0 removed the assistant's own randomness, but the user's order of details still varied, so unreliability stayed at 16.2. Randomness can come from both sides of a conversation.
- Liu et al. 2026, a preprint, argue that the cause is a gap between what the user intends and what the model infers, not a lack of ability. They add a "mediator" model that rewrites vague user turns into clear instructions, and report that it reduces the drop.
- For builders: test on multi-turn versions of your tasks, and report the spread across runs, not only the average. For users: put everything in one message, and if a conversation goes wrong, start a new one with all the details restated.
- **Pause and try:** your coding assistant has misunderstood you for six turns. Name two things to do.
  - **Answer:** start a new conversation, and give the complete specification in its first message (you can also ask it to ask questions before it answers).

### Lab guide (about 2 hours, notebook `s04_lost_in_conversation.ipynb`)

1. Sections 2–3 (25 min): read the task and the assistant's rules, and run task 0 by hand.
2. Section 4 (30 min): the protocol over 200 tasks × 10 runs; read the table and the dot plot.
3. Sections 5–6 (25 min): temperature 0, and the turn of the first answer.
4. Section 7 (15 min): how the split depends on two settings we chose.
5. Section 8 (optional, on Colab): the same protocol with a small open model.
6. Section 9 (20 min): the two TODOs.

- **Expect:** single-turn mean 94.8, aptitude 100.0, unreliability 15.2; sharded eager 62.2, 78.8 and 33.5, a 34.4% drop in the mean, a 21.3% drop in aptitude and +120% unreliability. A final recap reached 65.5 and waiting for every detail 95.0. With the first answer at turns 1 to 6, the mean was 62.2, 71.5, 80.2, 88.0, 92.6 and 95.0. At temperature 0, single-turn unreliability was 0.0 but sharded unreliability 16.2 (mean 66.8). Across the four settings in section 7, the mean drop ranged from 18.4% to 34.4%, the aptitude drop from 6.7% to 21.3%, and unreliability rose by 109% to 120%.
- **Common problems:** pooling all tasks before taking percentiles instead of computing them per task; one run per task, which leaves no spread to measure; reading the toy's numbers as facts about real models.

### Quiz

1. What is a shard?
   - **Answer:** one piece of a full instruction, revealed in its own user turn; the first shard states the main request.
2. How do the authors define aptitude and unreliability?
   - **Answer:** aptitude is the 90th-percentile score over repeated runs; unreliability is the 90th minus the 10th percentile.
3. Does a lower temperature fix multi-turn unreliability?
   - **Answer:** no. The authors report that it is not enough. In the toy, too, unreliability stayed at 16.2 at temperature 0, because the user's order of details still varied.

**Watch out:** "If a model is strong on single-turn benchmarks, it will be strong in conversation." The paper found that every model it tested lost performance when the same information arrived in pieces, mostly through unreliability. A single-turn score measures aptitude with everything given at once; it says nothing about recovering from an early wrong assumption.

### Assignment 4 (due before session 5, 10 points)

1. The clarifying-assistant TODO, with its aptitude and unreliability compared with the eager and waiting assistants. (3 points)
2. Five sharded tasks from your own field, each with 4–6 shards and an automatic checker, run with the NOT RUN protocol on a small open model, 10 runs each, with a table of per-task P90 and P90 − P10. (4 points)
3. A half-page comparison of Laban et al. 2026 and Liu et al. 2026: what each says causes the drop, and one experiment that could tell the explanations apart. (3 points)

Hand in one PDF and your notebook.

### Sources

- Laban, Hayashi, Zhou & Neville 2026, LLMs Get Lost In Multi-Turn Conversation (ICLR 2026). https://arxiv.org/abs/2505.06120
- ICLR 2026, Announcing the ICLR 2026 Outstanding Papers. https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/
- Liu et al. 2026, Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation. https://arxiv.org/abs/2602.07338

## Session 5: Diffusion language models and the flexibility trap

**Goal:** students can explain how masked diffusion language models decode in any order, what "The Flexibility Trap" found about arbitrary order and reasoning, and can compare decoding orders on a toy model.

### Talking pointers

- **Open with:** "A diffusion language model can write the last word of its answer first. That sounds like pure freedom. This year's ICML Outstanding Paper argues that, for reasoning, the freedom is a trap."
- **Segment 1, say:** animate one masked answer being filled in three orders: left to right, easiest first and random.
- **Segment 2, say:** put a worked maths solution on screen, circle the words where solutions branch ("so", "therefore", "since"), and ask what happens if they are filled last.
- **Segment 3, say:** show the lab's oracle table next to the trained-model table and ask why they differ.
- **Close with:** "Freedom of order helps only if the model has learned every order well." Then set assignment 5.

### Segment 1 (6 min): any-order decoding

- Recall Course 3, session 10: a masked diffusion language model (LM) is trained to predict randomly hidden tokens from the visible ones. It generates by starting from a fully masked answer and filling positions over several steps.
- Because every position can be predicted from any other, the model can decode in any order: left to right like an autoregressive model, most confident position first, at random, or block by block.
- The promise: fill several tokens per step (parallel decoding, which can be faster), fill gaps in the middle of a text, and use context on both sides.
- **Pause and try:** a model generates 256 tokens in 64 denoising steps. How many tokens does it fill per step, and how many forward passes does it make?
  - **Answer:** 4 tokens per step on average, and 64 forward passes, each over the whole sequence.

### Segment 2 (7 min): the ICML 2026 finding

- Ni et al. 2026 (ICML 2026 Outstanding Paper) report that arbitrary-order decoding is competitive at pass@1, but its pass@k grows more slowly as k increases, so it covers fewer solutions.
- Their explanation: reasoning branches at a few **forking tokens**, often connectives such as "Therefore" or "Since". A confidence-first decoder fills the easy tokens around them first. When a fork is finally filled, the surrounding context already decides it, so its entropy has collapsed and fewer solution paths are explored.
- Their method, JustGRPO, trains with ordinary GRPO (Course 3, session 7) while treating the model as a left-to-right generator. The authors report 89.1% on GSM8K and 45.1% on MATH-500, and the trained model keeps parallel decoding at inference.
- **Pause and try:** a fork token has probabilities 0.6, 0.3 and 0.1 when it is filled first. What is its entropy? What is it if it is filled last, after the rest of the chain has fixed it?
  - **Answer:** −(0.6 ln 0.6 + 0.3 ln 0.3 + 0.1 ln 0.1) ≈ 0.898 nats when filled first, and 0 when the context has already decided it.

### Segment 3 (7 min): what it means

- Flexibility at inference and exploration during training are different questions. JustGRPO gives up arbitrary order while training for reasoning, not at inference.
- With exact conditionals, the decoding order does not change the output distribution at temperature 1, because the chain rule holds in any order. In the lab, the oracle's strategy shares stayed near 0.6, 0.3 and 0.1 in every order. So the trap must come from imperfect learned conditionals, from sampling choices such as low temperature or filling several tokens at once, or from how training uses the decoding order.
- In the lab, trained transformers showed a trap-like drop with confidence-first decoding in all three seeds, but an MLP (multilayer perceptron) denoiser reversed it. The toy cannot tell which explanation holds for real models.
- Open questions: when does any-order decoding help (infilling, editing, speed)? Do block decoders, which fill blocks from left to right (Course 3, session 10), avoid the trap?
- **Pause and try:** a model's conditionals are exact and you sample at temperature 1. Does confidence-first decoding give less diverse outputs than left-to-right?
  - **Answer:** no. Both produce samples from the same distribution; any difference you measure is sampling noise, as the oracle shows.

### Lab guide (about 2 hours, notebook `s05_flexibility_trap.ipynb`)

1. Section 2 (15 min): the task and its three correct chains.
2. Section 3 (20 min): train three tiny transformers (about a minute in all).
3. Sections 4–5 (25 min): the three decoding orders and the exact oracle.
4. Section 6 (30 min): the trained models: the table, the pass@k curves and the strategy shares.
5. Section 7 (15 min): the MLP denoiser.
6. Section 9 (20 min): the two TODOs (temperature 0.5, parallel decoding).

- **Expect:** 39,759 parameters per transformer, with training losses (mean of the last 100 steps) of 0.608, 0.652 and 0.473. The oracle was always correct, with strategy shares near 0.6 / 0.3 / 0.1 in every order; its fork was filled at step 1.0, 2.35 and 2.54 on average, with entropy 0.898, 0.813 and 0.366 nats (left-to-right, confidence, random). The trained transformers (mean of 3 seeds) reached pass@1 of 0.806, 0.598 and 0.502, pass@16 of 1.000, 0.970 and 0.992, and 2.47, 1.84 and 2.16 distinct correct strategies in 16 samples; confidence decoding filled the fork at step 3.16 with entropy 0.644. The MLP gave pass@1 of 0.593 (left-to-right) against 0.821 (confidence), with 2.12 against 2.20 distinct correct strategies.
- **Common problems:** filling several positions per step and calling it the same experiment; scoring only the final answer, which can be right while the chain is inconsistent; trusting one training seed.

### Quiz

1. How does a confidence-based decoder choose which position to fill?
   - **Answer:** it predicts every masked position and fills the one (or ones) where its top probability is highest.
2. What is a forking token, and what happens to it under confidence-first decoding according to Ni et al.?
   - **Answer:** a token where solution paths branch, often a connective. It tends to be filled late, when the context has already decided it, so its entropy collapses and exploration narrows.
3. What is JustGRPO, and what do its authors report?
   - **Answer:** ordinary GRPO applied while treating the diffusion LM as a left-to-right generator. The authors report 89.1% on GSM8K and 45.1% on MATH-500, with parallel decoding kept at inference.

**Watch out:** "More freedom in decoding order can only help." Freedom helps only if the model's predictions are good in every order it uses, and if the decoder does not skip the decisions that matter. In the lab, the same trained transformers lost about a quarter of their pass@1 (0.806 to 0.598) when they chose their own order.

### Assignment 5 (due before session 6, 10 points)

1. The temperature-0.5 TODO: a table of pass@1, pass@16 and distinct correct strategies for the three orders and three seeds. (3 points)
2. The parallel-decoding TODO: how often two tokens filled in the same step are inconsistent with each other, for each order. (3 points)
3. One page explaining why the oracle shows no trap while the trained transformers do, with one experiment that tests your explanation, for example training longer and measuring the fork entropy again. (4 points)

Hand in one PDF and your notebook.

### Sources

- Ni et al. 2026, The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (ICML 2026; first titled "The Flexibility Trap: Why Arbitrary Order Limits Reasoning Potential in Diffusion Language Models"). https://arxiv.org/abs/2601.15165
- ICML 2026, awards announcement. https://blog.icml.cc/?p=1347
- ML-GSAI, LLaDA repository (the sampler used in the NOT RUN cell). https://github.com/ML-GSAI/LLaDA

## Session 6: What transformers can express

**Goal:** students can explain what "succinctness" measures, state the main results of "Transformers are Inherently Succinct" and the ACL 2026 local-attention paper, and can demonstrate an exponential gap in description size on small examples.

### Talking pointers

- **Open with:** "Two machines can accept exactly the same strings and still differ enormously in size. This year's ICLR Outstanding Paper asks how small a transformer can be compared with the alternatives."
- **Segment 1, say:** build the 3-state NFA and the 4-state DFA for "the 2nd symbol from the end is a" on screen, then show the lab's table up to k = 10.
- **Segment 2, say:** write the three size relations on the board (transformer against LTL, RNN and automaton), then explain what EXPSPACE-complete means for anyone who wants to verify a model.
- **Segment 3, say:** slide a window along a long string and show what it can and cannot see.
- **Close with:** "Expressivity says what a model could represent; training decides what it actually learns." Then set assignment 6.

### Segment 1 (7 min): languages, automata and logic

- A formal language is a set of strings, for example all strings over {a, b} whose k-th symbol from the end is a; call it $L_k$. Treating transformers as recognisers of such sets lets researchers prove what they can and cannot do (survey: Strobl et al. 2024).
- A finite automaton reads one symbol at a time and keeps a state. In a DFA (deterministic finite automaton) each symbol leads to exactly one next state; an NFA (nondeterministic) may allow several.
- Linear temporal logic (LTL) describes properties of positions in a string. With past operators, $Y\varphi$ ("yesterday") means $\varphi$ held one position earlier, and $P\varphi$ means it held at some earlier position. $L_k$ is the formula $Y^{k-1}a$.
- Expressivity asks which tasks an architecture can represent at all, a separate question from whether training finds the solution.
- **Pause and try:** how many states does the smallest DFA for $L_5$ need? And an NFA?
  - **Answer:** 32 states for the DFA, which must remember the last five symbols, and 6 for the NFA.

### Segment 2 (7 min): succinctness

- Succinctness asks how large a description must be. For $L_k$ a DFA needs $2^k$ states, while an NFA needs $k+1$ states and the LTL formula has size $k$; the lab checks this up to $k = 10$.
- Bergsträßer et al. 2026 prove that fixed-precision transformers can describe some languages exponentially more succinctly than LTL formulas and recurrent neural networks (RNNs, and by extension state-space models), and doubly exponentially more succinctly than finite automata. In the other direction, any fixed-precision transformer can be converted to LTL with at most an exponential blow-up.
- The price: deciding whether a transformer accepts any string at all (emptiness), or whether two transformers accept the same strings (equivalence), is EXPSPACE-complete. Such checks can need memory exponential in the transformer's size, so verifying exactly what a transformer does is hard in the worst case.
- **Pause and try:** suppose a transformer of size n describes a language whose smallest DFA has $2^{2^n}$ states. How many states is that for n = 4?
  - **Answer:** $2^{16} = 65{,}536$. Each step up in n squares the count.

### Segment 3 (6 min): local versus global attention

- Li & Cotterell 2026 (ACL 2026) match attention patterns with fragments of LTL. Global attention corresponds to a fragment with one past operator; local (windowed) attention adds a second temporal operator.
- The two are incomparable: each expresses languages the other cannot, so a hybrid of local and global attention is strictly more expressive than either. The authors also report experiments in which hybrid transformers do better than global-only ones.
- Practice already mixes the two. Longformer combines windowed attention with global attention on chosen tokens (Beltagy et al. 2020), and Gemma 2 alternates sliding-window and global attention layers (Gemma Team 2024).
- In the lab's one-layer toy, a window-4 head missed every "a" outside its window, while a global head without positions could not tell "bab" from "abb".
- **Pause and try:** a model has 2 layers, both sliding-window attention with a window of 4,096 tokens. Can its last token be influenced by a token 10,000 positions back?
  - **Answer:** no. Each layer reaches at most 4,096 positions further back, so two layers reach about 8,192.

### Lab guide (about 2 hours, notebook `s06_transformer_expressivity.ipynb`)

1. Section 2 (25 min): subset construction and Moore minimization for $k = 1$ to 10, with the Myhill–Nerode cross-check.
2. Section 3 (15 min): evaluate the LTL formula $Y^{k-1}a$ on random words.
3. Section 4 (25 min): the hand-built attention head, and the precision it needs.
4. Section 5 (20 min): local and global heads on two languages.
5. Section 6 (20 min): train a small transformer on $L_3$ and test it on longer words.
6. Section 7 (15 min): the two TODOs.

- **Expect:** minimal DFAs of exactly $2^k$ states up to 1,024 at $k = 10$, with the Myhill–Nerode count agreeing for $k \le 6$; formula size $k$, agreeing with the definition on all 2,000 random words for each $k$ tested (1, 3, 6 and 10). The hand-built head scored 1.000 for every $k$ from 1 to 10 on words up to length 64, always with 12 numbers, but needed about 3.9, 7.7, 11.7 and 15.7 bits of precision for words up to length 16, 64, 256 and 1,024. The local head scored 1.000 on $L_2$ and 0.946 on contains-a, accepting none of the 36 words whose only "a" was far back; the global head scored 1.000 on contains-a, and its outputs for "bab" and "abb" differed by at most 1.8e-15. The trained transformer scored 1.000 on lengths 6 to 16, then 0.514 at 20, 0.869 at 24, 0.513 at 32, 0.540 at 48 and 0.498 at 64.
- **Common problems:** forgetting words shorter than k; counting the subset-construction DFA without minimizing it; testing a trained model only on the lengths it saw.

### Quiz

1. What does succinctness measure?
   - **Answer:** how large a description (an automaton, a formula or a network) must be to define a given language.
2. What do Bergsträßer et al. prove about transformers compared with finite automata?
   - **Answer:** fixed-precision transformers can be doubly exponentially more succinct than finite automata for some languages, and exponentially more succinct than LTL and RNNs.
3. Why is a hybrid of local and global attention strictly more expressive than either alone?
   - **Answer:** Li & Cotterell show that the two are incomparable, each expressing languages the other cannot, so a hybrid can express both kinds.

**Watch out:** "More expressive means easier to learn." Expressivity is about what a model can represent with the right weights, not about what gradient descent finds. In the lab, a transformer that can represent $L_3$ was perfect on its training lengths and close to chance on longer words, while a hand-built head worked at every length.

### Assignment 6 (due before session 7, 10 points)

1. The two TODOs: training on lengths 6 to 32, and a hand-built head for "the k-th symbol from the end equals the last symbol", with the size of its minimal DFA. (4 points)
2. A half-page proof that every DFA for $L_3$ needs at least 8 states, using the Myhill–Nerode argument, checked against the lab's brute force. (3 points)
3. A half-page summary of Li & Cotterell 2026: what each LTL fragment can say, one language for each side of the incomparability, and what it means for sliding-window models. (3 points)

Hand in one PDF and your notebook.

### Sources

- Bergsträßer, Cotterell & Lin 2026, Transformers are Inherently Succinct (ICLR 2026). https://arxiv.org/abs/2510.19315
- ICLR 2026, Announcing the ICLR 2026 Outstanding Papers. https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/
- Li & Cotterell 2026, Characterizing the Expressivity of Local Attention in Transformers (ACL 2026). https://aclanthology.org/2026.acl-long.1739/
- Strobl et al. 2024, What Formal Languages Can Transformers Express? A Survey. https://arxiv.org/abs/2311.00208
- Beltagy et al. 2020, Longformer: The Long-Document Transformer. https://arxiv.org/abs/2004.05150
- Gemma Team 2024, Gemma 2: Improving Open Language Models at a Practical Size. https://arxiv.org/abs/2408.00118
- Columbia University lecture notes, the $2^n$ lower bound for DFAs recognising "the n-th symbol from the end is 1". https://www.cs.columbia.edu/~tal/3261/sp18/expdfa.pdf

## Session 7: Optimizers in 2026: Polar Express and Muon

**Goal:** students can explain the polar decomposition and why Muon needs it, show how polynomial iterations approximate it with matrix multiplications only, say what Polar Express optimizes, and compare iteration schemes in training.

### Talking pointers

- **Open with:** "Muon turns every weight update into the nearest orthogonal matrix, at every step. An ICLR 2026 paper asked a mathematician's question about that one step: what is the best way to compute it on a GPU?"
- **Segment 1, say:** draw the SVD as three boxes, $U$, $\Sigma$ and $V^T$, then replace $\Sigma$ by the identity: that is the polar factor.
- **Segment 2, say:** plot the three polynomials on $[0, 1]$ and follow one small singular value, 0.001, through five steps of each.
- **Segment 3, say:** show the notebook's learning-rate plot: which differences beat the error bars?
- **Close with:** "A better answer to the maths question is not automatically a better optimizer." Then set assignment 7.

### Segment 1 (7 min): the polar factor, and why Muon needs it

- Recall Muon (Course 2, session 2): each 2-D hidden weight matrix steps along an orthogonalized version of its momentum; other parameters use AdamW (Jordan et al. 2024).
- Write the singular value decomposition (SVD) $G = U\Sigma V^T$. The polar decomposition is $G = QH$ with $Q = UV^T$ (orthonormal columns) and $H = V\Sigma V^T$ (symmetric, positive semi-definite). $Q$ is the matrix with orthonormal columns closest to $G$.
- Orthogonalizing keeps the update's directions but sets every singular value to 1. Muon's authors observed that momentum updates are close to low rank, and suggest that this lets rare but useful directions learn. Since $Q = U\,\mathrm{sign}(\Sigma)\,V^T$, the paper calls these "matrix sign methods".
- Why not an exact SVD? SVD, QR and inverses run poorly on GPUs (graphics processing units), especially in 16-bit precision; matrix multiplication is what GPUs do best.
- **Pause and try:** $G = U\,\mathrm{diag}(4, 0.01)\,V^T$. What are the singular values of its polar factor, and of the polar factor of $0.1G$?
  - **Answer:** 1 and 1 in both cases. The polar factor ignores scale, so in Muon the learning rate alone sets the step size.

### Segment 2 (7 min): polynomial iterations

- For an odd polynomial $p(x) = ax + bx^3 + cx^5$, the matrix $aX + bX(X^TX) + cX(X^TX)^2$ equals $U\,p(\Sigma)\,V^T$: each singular value $\sigma$ becomes $p(\sigma)$. After dividing by the Frobenius norm, all singular values lie in $(0, 1]$, and we want $p$ to send them to 1.
- Cubic Newton–Schulz, $p(x) = 1.5x - 0.5x^3$, converges for singular values below $\sqrt{3}$, fast near 1, but a tiny singular value grows only about 1.5 times per step.
- Muon's fixed quintic, $(3.4445, -4.7750, 2.0315)$, has slope 3.4445 at zero, so small singular values grow fast. But $p(1) = 0.701$, so singular values end in a band around 1, never exactly at 1.
- Polar Express (Amsel et al. 2026): if the singular values lie in $[\ell, u]$, take the fixed-degree polynomial that minimizes $\max_{x \in [\ell, u]} |1 - p(x)|$ (a minimax problem), then repeat on the smaller interval it produces. The authors prove this greedy choice is worst-case optimal, so convergence is fast early and late, and they make it stable in bfloat16. The polynomials are computed once, before training.
- Inside Muon, the authors report lower validation loss than earlier coefficient choices, across learning rates, when training GPT-2 models. The ICLR 2026 committee gave the paper an Outstanding Paper Honorable Mention for using approximation theory to design optimal polynomial approximations of the polar decomposition used in Muon.
- **Pause and try:** under cubic Newton–Schulz, a singular value of 0.001 grows about 1.5 times per step. About how many steps until it is near 1?
  - **Answer:** about 17, because $1.5^{17} \approx 1{,}000$. Muon's quintic needs about 6 ($\ln 1000 / \ln 3.4445 \approx 5.6$).

### Segment 3 (6 min): what it means in practice

- The authors report that, inside Muon, more than five or six iterations stopped helping. Each iteration costs three matrix products per weight matrix.
- In the notebook, at each method's best learning rate, the exact SVD, Muon's quintic and our minimax schedule tied within seed noise; only cubic Newton–Schulz was clearly worse.
- A 2026 preprint (Huang 2026) reports that training quality does not track the accuracy of the polar factor in a simple monotonic way, in NanoGPT ablations and in hybrid models of up to four billion parameters.
- So treat orthogonalization accuracy as a knob, not a goal: fast growth of small singular values, stability in low precision and few matrix products matter more.
- **Pause and try:** over 5 seeds, variant A reaches loss 0.089 ± 0.019 and variant B 0.092 ± 0.031. Is A better?
  - **Answer:** this evidence does not show it. The gap of 0.003 is about ten times smaller than the seed-to-seed spread; you need more seeds or a paired comparison (session 1).

### Lab guide (about 2 hours, notebook `s07_polar_express_muon.ipynb`)

1. Sections 1–2 (20 min): check $G = QH$ and that $p(G)$ acts on each singular value.
2. Section 3 (20 min): read the minimax schedule and watch the interval shrink.
3. Section 4 (20 min): read the error table and both plots; explain why the quintic's error stops falling.
4. Sections 5–6 (35 min): read the Muon code, run the sweep, find each best learning rate.
5. Section 7 and TODO (25 min): vary the number of iterations, then start the cubic fit.

- **Expect:** minimax intervals [0.008470, 1.991530] after step 1 and [0.886532, 1.113468] after step 5. On the test matrix (singular values 6.0e-04 to 0.60), errors after 5 iterations of 1.0e+00 (cubic), 7.1e-01 (quintic) and 4.1e-01 (minimax); the quintic stays at 3.2e-01 from iteration 6, the minimax reaches 4.9e-14 at iteration 9. Training loss after 40 steps at the best learning rate (0.1 for all Muon variants): cubic 0.1676 ± 0.0270, quintic 0.0889 ± 0.0188, minimax 0.0921 ± 0.0310, exact SVD 0.0887 ± 0.0305; AdamW 0.1802 ± 0.0473. Gains stop after about 3 (minimax) or 5 (quintic) iterations.
- **Common problems:** forgetting to normalize first (the polynomials blow up above their design interval); comparing methods at one learning rate; trusting one seed.

### Quiz

1. What does the polar factor of $G = U\Sigma V^T$ keep, and what does it throw away?
   - **Answer:** it keeps $U$ and $V$ and sets every singular value to 1; the scale goes into $H$.
2. Why does Muon's fixed quintic never reach exact orthogonality?
   - **Answer:** $p(1) = 3.4445 - 4.7750 + 2.0315 = 0.701$, so 1 is not a fixed point and singular values keep moving in a band around 1.
3. What problem does Polar Express solve at each iteration?
   - **Answer:** for the interval $[\ell, u]$ that holds the singular values, it finds the odd polynomial of fixed degree that minimizes $\max |1 - p(x)|$ there.

**Watch out:** "A more accurate orthogonalization always gives a better optimizer." In the notebook, the exact polar factor trained no better than five steps of Muon's inexact quintic, and Huang (2026) reports that training quality does not simply follow orthogonalization accuracy. Judge optimizers by the loss they reach, each at its best learning rate, not by the accuracy of one internal step.

### Assignment 7 (due before session 8, 10 points)

1. Finish TODO 2: fit a minimax cubic schedule and run it inside Muon over the same learning-rate grid; report mean ± sd over 5 seeds next to cubic Newton–Schulz. (3 points)
2. Finish TODO 3: repeat section 4 in bfloat16 for all three schedules, report errors after 5 and 8 iterations, and test whether dividing each polynomial by 1.01 helps. (4 points)
3. A half-page note: does your evidence support "more accurate orthogonalization trains better" in this toy? Use paired differences across seeds. (3 points)

Hand in one PDF and your notebook.

### Sources

- Amsel, Persson, Musco & Gower 2026, The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm (ICLR 2026). https://arxiv.org/abs/2505.16932
- ICLR 2026, Announcing the ICLR 2026 Outstanding Papers (committee remarks). https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/
- NYU news page on the ICLR 2026 honorable mention. https://cims.nyu.edu/ai/news/146/
- Amsel et al., PolarExpress code. https://github.com/NoahAmsel/PolarExpress
- Jordan et al. 2024, Muon: An optimizer for hidden layers in neural networks. https://kellerjordan.github.io/posts/muon/
- Huang 2026, How Much Orthogonalization Does Muon Need? (preprint). https://arxiv.org/pdf/2606.00371

## Session 8: Grokking, proved

**Goal:** students can state what "To Grok Grokking" proves, reproduce grokking in over-parameterized ridge regression, and show how weight decay, learning rate and initialization stretch or remove it.

### Talking pointers

- **Open with:** "Grokking looked like magic: a network memorizes, waits, and then suddenly generalizes. In 2026 a paper proved that plain linear regression does the same thing, and put bounds on how long the wait lasts."
- **Segment 1, say:** show the train and test curves from Course 8, session 4, on a log time axis, then the same shape from today's linear model.
- **Segment 2, say:** draw the weight vector as two arrows, the part the data can see and the part it cannot, and show weight decay shrinking the second.
- **Segment 3, say:** put the random-features curve next to the linear one and ask what a transformer has that these models lack.
- **Close with:** "In this model, grokking is weight decay slowly cleaning away what the data could not see." Then set assignment 8.

### Segment 1 (6 min): grokking, and why a proof matters

- Recall Course 8, session 4: small transformers trained on modular arithmetic reach perfect training accuracy early, and test accuracy jumps much later; weight decay matters (Power et al. 2022).
- Later explanations: the weight norm (Liu et al. 2023); a circuit that forms slowly while memorizing parts are cleaned up (Nanda et al. 2023); a late switch between implicit biases under large initialization and small weight decay (Lyu et al. 2024); grokking in linear estimators (Levi et al. 2024).
- Experiments show that grokking can happen; a proof says when it must happen and how long it takes, as a function of the hyperparameters.
- "To Grok Grokking" (Xu, Vardi & Safran 2026) received an ICML 2026 Outstanding Paper Honorable Mention. The authors describe their results as the first rigorous quantitative bounds on the grokking time in terms of the training hyperparameters.
- **Pause and try:** our toy has $d = 400$ parameters and $n = 100$ training equations. In how many directions of $w$ do the training data say nothing?
  - **Answer:** 300 ($d - n$, because 100 random inputs are linearly independent). Moving $w$ in those directions changes no training prediction.

### Segment 2 (7 min): the setup and the result

- Setup: teacher–student linear regression ($x \sim N(0, I/d)$, $y = w_*^Tx$), more parameters than data ($d > n$), gradient descent on the squared loss plus weight decay $\frac{\lambda}{2}\|w\|^2$, from a random initialization of scale $\nu$.
- What the authors prove: the model overfits the training data early, poor generalization persists long after that, and the test error eventually becomes arbitrarily small. They bound the grokking time explicitly in terms of the hyperparameters, and show that grokking can be amplified or eliminated by tuning them.
- The mechanism, in our own one-line calculation for the toy (the paper's bounds are more careful, and we could not confirm their exact form): split $w = w_\parallel + w_\perp$, with $w_\parallel$ in the span of the training inputs. The data gradient $X^T(Xw - y)/n$ lies in that span, so only weight decay acts on $w_\perp$: $w_\perp(t) = (1 - \eta\lambda)^t w_\perp(0)$.
- $w_\parallel$ fits the data fast, which gives the training-loss time $t_1$. The test loss contains $\|w_\perp\|^2/d$, so it must wait for weight decay: $t_2 \approx \ln\big(\|w_\perp(0)\|^2 / (d(\varepsilon - L_\infty))\big) / (2\eta\lambda)$, where $\varepsilon$ is the threshold and $L_\infty$ the final test loss.
- So $t_2$ grows like $1/(\eta\lambda)$ but only like $\ln \nu$, and a small initialization or a large $\lambda$ removes the delay. In the notebook the prediction is within 1% of the measured $t_2$.
- **Pause and try:** with $\lambda = 2\times10^{-4}$ and $\eta = 1$ the notebook measures $t_2$ = 10,859 steps. Predict $t_2$ for $\lambda = 10^{-4}$.
  - **Answer:** about 21,700, since $t_2 \propto 1/(\eta\lambda)$. The notebook measures 21,718.

### Segment 3 (7 min): beyond linear models

- Random features (fixed random ReLU features, last layer trained) are still linear in the trained weights, so the same split applies. In the notebook $t_2 \times \lambda$ stayed between 1.16 and 1.24, with a smaller delay ratio.
- The authors report experiments in which their bounds also capture grokking in non-linear networks; the proofs cover only the linear case.
- What this explains: weight decay removing weight components that do not help the training loss resembles the cleanup phase that Nanda et al. (2023) measured, and "large initialization, small weight decay" is a recipe for delay (Lyu et al. 2024).
- What it does not explain: in ridge regression nothing new is learned during the plateau, while in transformers a Fourier circuit forms, which needs feature learning. Levi et al. (2024) also note that a sudden jump in accuracy can partly be an effect of the accuracy metric; our test loss falls smoothly.
- **Pause and try:** raise $\nu$ from 1 to 10. Does $t_2$ become 10 times or 100 times longer?
  - **Answer:** neither. It grows by about $\ln(100)/(2\eta\lambda) \approx$ 11,500 steps; the notebook goes from 10,859 to 22,371.

### Lab guide (about 2 hours, notebook `s08_provable_grokking.ipynb`)

1. Sections 1–2 (30 min): build the data (100 nonzero eigenvalues out of 400), train, and read $t_1$ and $t_2$ off the log-time plot.
2. Section 3 (25 min): check the decay law for $w_\perp$ and compare predicted and measured $t_2$.
3. Section 4 (25 min): run the sweep and mark the settings that remove grokking.
4. Section 5 and TODO (40 min): the random-features variant, then label noise or AdamW.

- **Expect:** at $\lambda = 2\times10^{-4}$, $\nu = 1$, $\eta = 1$: $t_1$ = 265 (test loss still 0.582) and $t_2$ = 10,859, ratio 41; $\|w_\perp\|$ at step 5,000 is 5.8826, as predicted; predicted $t_2$ = 10,885. Sweep: $t_2$ = 21,718 at $\lambda = 10^{-4}$, 2,172 at $10^{-3}$ and 110 at 0.02 (where $t_1$ = 73); $\nu = 0.1$ gives $t_1$ = 4, $t_2$ = 16; $\nu = 10$ gives $t_2$ = 22,371; $\eta = 0.25$ gives 1,059 and 43,437 (ratio 41.0). Random features: $t_2$ = 11,550, 3,905 and 1,235 for $\lambda = 10^{-4}$, $3\times10^{-4}$, $10^{-3}$.
- **Common problems:** a small, noisy test set that hides the threshold crossing; a linear time axis, on which the two phases look like one; treating the ratio $t_2/t_1$ and the difference $t_2 - t_1$ as the same (a larger $\nu$ raises the difference but lowers the ratio).

### Quiz

1. Why can the training data never change $w_\perp$?
   - **Answer:** the training-loss gradient $X^T(Xw - y)/n$ is a combination of the training inputs, so it has no component orthogonal to their span.
2. In this model, what removes grokking?
   - **Answer:** a small initialization, so $w_\perp$ starts small, or weight decay large enough that $w_\perp$ shrinks about as fast as the data are fitted.
3. What do the proofs in "To Grok Grokking" cover, and what is shown only by experiment?
   - **Answer:** the proofs cover over-parameterized linear regression trained by gradient descent with weight decay; non-linear networks are covered by experiments only.

**Watch out:** "Grokking is mysterious and only happens in big networks." A 400-parameter linear model groks in the notebook, and the 2026 paper proves this behaviour for linear regression: weight decay slowly removes the part of a large initialization that the data cannot see. Not every case is this simple, though; in transformers, new features also form during the plateau.

### Assignment 8 (due before session 9, 10 points)

1. TODO 1: add label noise at three levels, set the threshold above each new test-loss floor, and measure $t_2$ for three values of $\lambda$. Does $t_2 \propto 1/\lambda$ survive? (3 points)
2. TODO 2: train with full-batch AdamW. Is there still a delay, and how does it scale with $\lambda$? Explain any difference from gradient descent with the $w_\parallel$/$w_\perp$ split. (4 points)
3. Half a page: one thing this toy explains about grokking in Course 8's modular-arithmetic model and one thing it cannot, with evidence. (3 points)

Hand in one PDF and your notebook.

### Sources

- Xu, Vardi & Safran 2026, To Grok Grokking: Provable Grokking in Ridge Regression (ICML 2026). https://arxiv.org/abs/2601.19791 and https://proceedings.mlr.press/v306/xu26bd.html
- Xu, Vardi & Safran, code for the paper. https://github.com/raymondmyxu/to-grok-grokking
- ICML 2026 awards announcement. https://blog.icml.cc/?p=1347
- Power et al. 2022, Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets. https://arxiv.org/abs/2201.02177
- Liu, Michaud & Tegmark 2023, Omnigrok: Grokking Beyond Algorithmic Data (ICLR 2023). https://arxiv.org/abs/2210.01117v2
- Nanda et al. 2023, Progress Measures for Grokking via Mechanistic Interpretability. https://arxiv.org/abs/2301.05217
- Lyu et al. 2024, Dichotomy of Early and Late Phase Implicit Biases Can Provably Induce Grokking (ICLR 2024). https://arxiv.org/pdf/2311.18817
- Levi, Beck & Bar-Sinai 2024, Grokking in Linear Estimators: A Solvable Model that Groks without Understanding (ICLR 2024). https://arxiv.org/pdf/2310.16441

## Session 9: Sampling with high accuracy

**Goal:** students can explain the difference between low-accuracy and high-accuracy samplers, why a Metropolis correction removes discretization bias, and what the ICML 2026 result achieves with gradient queries only.

### Talking pointers

- **Open with:** "A diffusion model generates by following its learned score, step by step. Every step adds a small error. An ICML 2026 Outstanding Paper asked how few steps you need when you want almost no error at all."
- **Segment 1, say:** show the Langevin update as one line of code, then the notebook's table where ULA's variance settles at twice the truth.
- **Segment 2, say:** add the accept/reject line that turns ULA into MALA, and point at the term that needs $f(y)$, a density value.
- **Segment 3, say:** write $1/\delta$ and $(\ln 1/\delta)^2$ side by side for $\delta = 10^{-2}, 10^{-4}, 10^{-6}$.
- **Close with:** "A smaller step shrinks the bias slowly; a correction removes it." Then set assignment 9.

### Segment 1 (7 min): sampling from a density

- Goal: draw samples from $\pi(x) \propto e^{-f(x)}$. The density is log-concave when $f$ is convex, for example a Gaussian or a logistic-regression posterior.
- The Langevin diffusion $dX_t = -\nabla f(X_t)\,dt + \sqrt{2}\,dB_t$ has $\pi$ as its stationary distribution. The unadjusted Langevin algorithm (ULA) discretizes it: $x \leftarrow x - h\nabla f(x) + \sqrt{2h}\,\xi$, with $\xi \sim N(0, I)$.
- ULA needs only gradients, but its stationary distribution is wrong by an amount that shrinks with the step $h$. For a Gaussian with curvature $\lambda$ in some direction, the variance in that direction becomes $1/(\lambda(1 - h\lambda/2))$ instead of $1/\lambda$.
- Rejection sampling is exact: propose from $g$ and accept with probability $\tilde\pi(x)/(Mg(x))$. But it needs density values and a bound $M$, and its acceptance rate often falls exponentially with dimension.
- Diffusion models are samplers too (Course 2, session 8): they discretize a reverse-time process driven by a learned score $\nabla \log p_t$. Earlier theory gave step counts that grow polynomially in $1/\delta$ for accuracy $\delta$, assuming accurate scores (Chen et al. 2023).
- **Pause and try:** ULA on a 1-D Gaussian with variance 0.1 (curvature $\lambda = 10$) and step $h = 0.1$. What variance does it settle at?
  - **Answer:** $0.1/(1 - 0.5) = 0.2$, twice the truth. The notebook measures 0.2003.

### Segment 2 (7 min): high accuracy

- The Metropolis-adjusted Langevin algorithm (MALA) treats the ULA step as a proposal $y$ and accepts it with probability $\min\big(1, \pi(y)q(x \mid y) / (\pi(x)q(y \mid x))\big)$. Then $\pi$ is exactly stationary for any $h$ (Roberts & Tweedie 1996).
- The ratio $\pi(y)/\pi(x) = e^{f(x) - f(y)}$ needs values of $f$. A diffusion model gives only the score, a gradient, so MALA cannot be applied to it directly.
- Low versus high accuracy: for strongly log-concave targets, Dwivedi et al. (2019) proved that MALA needs about $\kappa d \log(1/\delta)$ steps from a warm start ($\kappa$ is the condition number, $d$ the dimension), against known bounds for ULA of order $\kappa^2 d/\delta^2$. "$\mathrm{polylog}(1/\delta)$" means a power of $\log(1/\delta)$; "$\mathrm{poly}(1/\delta)$" means a power of $1/\delta$.
- Chen, Chewi, Daskalakis & Rakhlin (2026), an ICML 2026 Outstanding Paper, introduce First-Order Rejection Sampling (FORS), which imitates rejection sampling using only gradient queries. For diffusion models, assuming score estimates accurate to about $\delta$ (in $L^2$), they report $\delta$-error in $\mathrm{polylog}(1/\delta)$ steps, an exponential improvement over earlier guarantees. They also claim the first $\mathrm{polylog}(1/\delta)$ sampler for general log-concave distributions using only gradient evaluations.
- **Pause and try:** for $\delta = 10^{-4}$, compare $1/\delta$ with $(\ln 1/\delta)^2$.
  - **Answer:** 10,000 against about 85. That gap is what "exponential improvement" means here.

### Segment 3 (6 min): what it means, and its limits

- The result is about how the number of steps grows as the required accuracy shrinks. It does not, by itself, say how much better or faster today's image generators will become.
- The diffusion guarantee needs score estimates accurate to about $\delta$; if the learned score is worse, score error, not discretization, limits the result. Real data are not log-concave, so the diffusion result and the log-concave result answer different questions.
- Constants and the dependence on dimension matter in practice, and they differ between versions of the paper, so check the latest version before quoting a bound.
- The notebook shows the problem, not FORS: ULA's bias floors match theory, MALA reaches the Monte Carlo noise level, and an unbiased sampler with too large a step ($h = 0.3$) barely moves.
- **Pause and try:** your diffusion model's score has $L^2$ error about 0.05. Can a better sampler guarantee error $10^{-6}$?
  - **Answer:** no. The guarantee assumes score error of order $\delta$; with error 0.05, the learned score is the bottleneck.

### Lab guide (about 2 hours, notebook `s09_high_accuracy_sampling.ipynb`)

1. Section 1 (10 min): build both targets; note the condition number 19 and target B's exact mean and covariance.
2. Section 2 (25 min): run ULA at four step sizes and compare simulated variances with the theory column.
3. Section 3 (25 min): implement MALA, read the acceptance rates, and compare error curves with the ULA theory lines.
4. Section 4 (20 min): the skewed target; look at the histogram of $x_1$.
5. Sections 5–6 (25 min): rejection sampling, the dimension table and the cost table.
6. TODO (15 min): the gradient-free random-walk sampler.

- **Expect:** ULA narrow-direction variance 0.1044, 0.1166, 0.2003 and 0.4039 for $h$ = 0.01, 0.03, 0.1, 0.15 (theory 0.1053, 0.1176, 0.2000, 0.4000; truth 0.1); error floors 0.047, 0.177, 0.999, 2.998. MALA at $h = 0.15$: acceptance 0.634, error floor 0.015 (noise level 0.014), below 10% by step 23 (ULA $h = 0.01$: step 234). MALA at $h = 0.3$: acceptance 0.202, error 30.765 after 500 steps. Target B: ULA $h = 0.2$ mean error $-0.0388$ in $x_1$, covariance error 0.1938; MALA 0.0157 and 0.0166. Rejection sampling: acceptance 0.2988 (theory 0.2977); acceptance 0.0262 at $d = 20$. ULA steps for $\delta = 10^{-4}$: 4.42e+05.
- **Common problems:** a sign error in the MALA ratio (the acceptance rate looks fine but the variances are wrong); judging a sampler from one checkpoint (the notebook's MALA error was 0.0003 at step 2,000 by chance); comparing ULA runs that have not mixed yet.

### Quiz

1. Why is ULA biased even after infinitely many steps?
   - **Answer:** each step is a discretization of the Langevin diffusion, and the discretized chain has its own stationary distribution, which differs from $\pi$ by an amount that shrinks with $h$.
2. What does MALA need that ULA does not?
   - **Answer:** values of $f$ (density ratios $\pi(y)/\pi(x)$) for the accept/reject step, not just gradients.
3. What does FORS achieve, according to its authors?
   - **Answer:** it imitates rejection sampling using only gradient queries, giving $\mathrm{polylog}(1/\delta)$ step counts for diffusion models (with accurate scores) and for general log-concave distributions.

**Watch out:** "Smaller step size always fixes Langevin's error cheaply." ULA's bias shrinks only in proportion to $h$, while the number of steps it needs to mix grows like $1/h$. On the notebook's 2-D Gaussian, ULA needs about 442,000 steps for relative error $10^{-4}$, and MALA reached the noise level in under 100 steps. A correction removes the bias instead of shrinking it.

### Assignment 9 (due before session 10, 10 points)

1. Finish the TODO: the random-walk Metropolis sampler. Compare its acceptance rate and error floor with MALA at $h$ = 0.05 and 0.15 on target A. (3 points)
2. Pick $\delta = 0.05$ from the cost table, run ULA with that step size and step count, and report the measured error floor. Then repeat ULA and MALA on a 10-dimensional target made of five independent copies of target A, and report what changes. (4 points)
3. Half a page: explain why a diffusion model cannot use MALA directly and what FORS changes, citing the abstract. (3 points)

Hand in one PDF and your notebook.

### Sources

- Chen, Chewi, Daskalakis & Rakhlin 2026, High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions (ICML 2026). https://arxiv.org/abs/2602.01338
- ICML 2026 awards announcement. https://blog.icml.cc/?p=1347
- Roberts & Tweedie 1996, Exponential convergence of Langevin distributions and their discrete approximations, Bernoulli 2(4). https://projecteuclid.org/euclid.bj/1178291835
- Dwivedi, Chen, Wainwright & Yu 2019, Log-concave sampling: Metropolis-Hastings algorithms are fast, JMLR 20. https://www.jmlr.org/beta/papers/v20/19-306.html
- Chen, Chewi, Li, Li, Salim & Zhang 2023, Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions (ICLR 2023). https://arxiv.org/abs/2209.11215v3

## Session 10: Probes, obfuscation and honesty

**Goal:** students can explain linear probes for deception, what happens when a model is trained against a probe (honest, blatant and obfuscated outcomes), and the "censor's toolkit" argument, and can reproduce an outcome map in a toy.

### Talking pointers

- **Open with:** "Punish a model every time your lie detector fires, and you might get an honest model. Or you might get a model that has learned to beat your lie detector. A 2026 paper mapped when each one happens."
- **Segment 1, say:** draw a network with a small probe attached to one hidden layer, then work out the probe's precision on screen.
- **Segment 2, say:** show the four outcomes as a 2 × 2 table: did the behaviour change, and did the probe stop firing?
- **Segment 3, say:** list alignment techniques on screen and ask, for each one, "who else could use this?"
- **Close with:** "A monitor that becomes a training target stops being a reliable monitor." Then set assignment 10.

### Segment 1 (7 min): probes and monitoring

- A linear probe is a linear classifier trained on a model's hidden activations to read out a property (Alain & Bengio 2016). A deception probe is trained on activations from honest and deceptive examples; its score then flags likely deception.
- Reward hacking: reinforcement learning with verifiable rewards (RLVR, Course 3, session 7) optimizes whatever the check measures. In coding, a model can hardcode the expected test outputs and pass without solving the task.
- Baker et al. (2025) found that a model reading another model's chain of thought caught reward hacking in agentic coding far better than watching its actions. Putting that monitor into the reward helped at low optimization pressure, but at higher pressure the agents hid their intent while still hacking. The authors suggest a "monitorability tax": avoid strong optimization pressure on the chain of thought.
- Probes read activations, not text. Does training against them fail the same way?
- **Pause and try:** a probe flags 98% of hacks and 1% of honest answers. Out of 1,000 answers, 100 are hacks. What fraction of flagged answers are really hacks?
  - **Answer:** 98 true flags against 9 false ones, so 98/107 ≈ 92%.

### Segment 2 (7 min): The Obfuscation Atlas

- Taufeeque et al. (2026), an ICML 2026 Outstanding Paper Honorable Mention, created MBPP-Honeypot, a coding environment based on MBPP, a standard set of short Python problems, in which hardcoding test cases earns reward. They trained models with RLVR, a penalty from a deception probe on the model's activations, and a Kullback–Leibler (KL) penalty to the starting model.
- Four outcomes: **honest**; **blatant deception** (hacks, and the probe still fires); **obfuscated policy** (hacks with text that evades the probe, typically a justification for the hack); **obfuscated activations** (the same kind of text, but the activations change so the probe stops firing).
- What the authors report: representation drift during RL can produce obfuscated activations with or without a detector penalty; the penalty incentivizes obfuscated policies, not obfuscated activations, which they show is expected for policy-gradient methods; and a high detector penalty with high KL regularization gives honest policies, with capabilities similar to policies trained without a reward-hacking incentive.
- Why policy gradient cannot attack the probe directly: the probe score is only a number in the reward, so the update $A \cdot \nabla \log \pi(a \mid x)$ changes which outputs are chosen, and activations change only as a side effect.
- To tell the outcomes apart, run the probe on a frozen copy of the starting model reading the same outputs: if it still fires, only the activations changed.
- **Pause and try:** after training against the probe, the hack rate is 1.000, the probe flags 0% of hacks, and the frozen copy flags 20%. Which outcome is this?
  - **Answer:** an obfuscated policy. The frozen copy also rarely fires on these outputs, so the outputs themselves changed, not just the activations. These are the notebook's λ = 0.5, β = 0 numbers.

### Segment 3 (6 min): dual use, and evaluations under strain

- Ball & Hackemann (2026), the ICML 2026 Outstanding Position Paper, argue that alignment techniques are dual-use: data curation, post-training, and inference-time interventions such as system prompts and classifiers can block harmful content, but can also suppress political speech or history.
- Their remedies: benchmarks for censorship and manipulation, transparency and auditing, and model pluralism. They reject "stop aligning models" as the answer.
- The International AI Safety Report 2026 (published 3 February 2026, chaired by Yoshua Bengio) reports that pre-deployment safety evaluations are under strain.
- The common lesson: a check that becomes a target can be gamed. Keep some monitors out of the training loop and report what you optimized against.
- **Pause and try:** name one alignment technique and one way a censor could reuse it.
  - **Answer:** for example, refusal training on harmful topics can be redone on political topics, and a harmful-content classifier can block mentions of a protest.

### Lab guide (about 2 hours, notebook `s10_probes_and_obfuscation.ipynb`)

1. Sections 1–3 (35 min): read the task, the outputs and the policy; train the probe and read its scores.
2. Section 4 (30 min): train four settings and classify each with the rule.
3. Section 5 (25 min): run the 75-run map; find the cells where seeds disagree.
4. Section 6 and TODO (30 min): the drift check, the white-box run, then the frozen-reader penalty.

- **Expect:** probe flag rates 0.000 (honest), 1.000 (hardcoded) and 0.247 (justified hack). Starting hack rate 0.108. λ = 0, β = 0: hack rate 1.000, flagged 0.994 (blatant). λ = 0.5, β = 0: hack rate 1.000, justified 1.000, flagged 0.000, frozen copy 0.202 (obfuscated policy). λ = 2, β = 0: hack rate 0.000, honest passes 0.509. Map: 37 honest, 19 blatant, 19 obfuscated policy, 0 obfuscated activations. Drift without penalty: probe score on hardcoded outputs 0.998 → 0.966. White-box, λ = 1: hack rate 0.790, flagged 0.000, frozen copy 0.716 (obfuscated activations).
- **Common problems:** forgetting `detach()` on the probe score (this silently makes the training white-box); judging honesty by the probe instead of the true hack rate; one seed per cell.

### Quiz

1. What is the difference between an obfuscated policy and obfuscated activations?
   - **Answer:** in an obfuscated policy the outputs change so that the probe stops firing; in obfuscated activations the outputs stay the same kind, but the internal activations change.
2. Why can REINFORCE not push the activations against the probe directly?
   - **Answer:** the probe score is only a number in the reward; the gradient never passes through the probe, so activations change only as a side effect of changing the policy.
3. Which three remedies do Ball & Hackemann propose?
   - **Answer:** censorship and manipulation benchmarks, transparency and auditing, and model pluralism.

**Watch out:** "If the probe no longer fires, the model has become honest." In the notebook, a weak penalty gave a policy that hacked every cheatable task while the probe fired on none of the hacks. Measure the behaviour itself, and keep an independent check that training never optimized against.

### Assignment 10 (due before session 11, 10 points)

1. TODO 1: make the penalty use the frozen starting model's activations. Rerun λ = 0.5, β = 0 with three seeds, report the outcomes, and explain which outcome this still cannot prevent. (3 points)
2. TODO 2: retrain the probe on a trained policy's own activations. How many justified hacks does it catch now? What does this suggest about refreshing probes during RL? (4 points)
3. Half a page: pick one technique from this course (probes, RLVR or refusal training) and describe one beneficial use, one censorship use and one safeguard from Ball & Hackemann's list. (3 points)

Hand in one PDF and your notebook.

### Sources

- Taufeeque, Heimersheim, Gleave & Cundy 2026, The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (ICML 2026). https://arxiv.org/pdf/2602.15515
- The Obfuscation Atlas code and models. https://github.com/AlignmentResearch/obfuscation-atlas
- Ball & Hackemann 2026, Position: The Alignment Community is Unintentionally Building a Censor's Toolkit (ICML 2026). https://proceedings.mlr.press/v306/ball26c.html
- ICML 2026 awards announcement. https://blog.icml.cc/?p=1347
- Baker et al. 2025, Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation. https://arxiv.org/abs/2503.11926
- Alain & Bengio 2016, Understanding intermediate layers using linear classifier probes. https://arxiv.org/abs/1610.01644
- International AI Safety Report 2026. https://internationalaisafetyreport.org

## Session 11: AI and mathematics: the Erdős problems

**Goal:** students can describe what AI systems did on Erdős problems in 2026, distinguish a formally verified proof from a claim, and verify number-theoretic statements by computer.

### Talking pointers

- **Open with:** "For decades, Erdős's open problems tested human ingenuity. In 2026 some of them started to fall to AI systems, and the hard part became deciding which claims to believe."
- **Segment 1, say:** show the statement of #728, then the one-line substitution $n = 2m$, $b = m$, $a = m + k$; add 3 + 3 in base 2 on screen.
- **Segment 2, say:** draw a grid and mark all 12 points at distance 5 from one point: number theory makes distances repeat.
- **Segment 3, say:** show two timelines: claim, literature found, claim withdrawn (#333); claim, Lean proof, write-up (#728).
- **Close with:** "A proof is only as good as the check behind it and the statement it proves." Then set assignment 11.

### Segment 1 (7 min): the database and problem #728

- erdosproblems.com, run by Thomas Bloom, lists Erdős's problems and their status; a wiki in Terence Tao's `erdosproblems` repository on GitHub tracks AI contributions to them.
- Problem #728 asks for $a, b > \varepsilon n$ with $a!\,b! \mid n!\,(a+b-n)!$ and a gap $a + b - n$ between $C_1 \log n$ and $C_2 \log n$. The upper limit matters: without it, $a = b = n$ is a trivial answer, and Google DeepMind's formal-conjectures project notes that the version shown on the website can be read that way.
- January 2026: working from an informal argument by an OpenAI model, Harmonic's Aristotle produced a Lean proof on 6 January. It is regarded as the first Erdős problem fully resolved autonomously by an AI system. Sothanaphan (2026) wrote the proof up for humans, and reports that problems #729 and #401 were also solved by modifying the argument.
- The core: $n = 2m$, $b = m$, $a = m + k$ turns the problem into $\binom{m+k}{k} \mid \binom{2m}{m}$ with $k$ of order $\log m$. Kummer's theorem says the power of a prime $p$ dividing $\binom{a+b}{a}$ equals the number of carries when adding $a$ and $b$ in base $p$. So for each prime, adding $m + k$ must carry no more often than $m + m$: choose $m$ whose digits make doubling carry a lot.
- Formal verification (Course 8, sessions 9–11): Lean's kernel checks every step, so the remaining question is whether the formal statement says what was meant.
- **Pause and try:** how many carries are there when adding 3 + 3 in base 2? What power of 2 divides $\binom{6}{3} = 20$?
  - **Answer:** $11_2 + 11_2 = 110_2$, with 2 carries, so $2^2 = 4$ divides 20 and 8 does not.

### Segment 2 (7 min): the unit distance counterexample

- Erdős (1946) asked for $u(n)$, the largest number of pairs at distance exactly 1 among $n$ points in the plane. A scaled $\sqrt{n} \times \sqrt{n}$ grid gives about $n^{1 + c/\log\log n}$ pairs, because some integers have many representations as a sum of two squares. Erdős conjectured that this is essentially the truth: $u(n) = n^{1 + o(1)}$. The best upper bound, of order $n^{4/3}$, dates from 1984 (Spencer, Szemerédi & Trotter).
- On 20 May 2026 OpenAI announced that an internal model had found a counterexample: an absolute constant $\delta > 0$ and infinitely many $n$ with $u(n) \ge n^{1+\delta}$.
- Nine outside mathematicians, including Noga Alon and Tim Gowers, wrote a companion paper with a short, human-verified version (Alon et al. 2026). They note that the argument relies on ideas that, at least in retrospect, go back to work in algebraic number theory (Ellenberg–Venkatesh, Golod–Shafarevich, Hajir–Maire–Ramakrishna), rather than on a plain grid.
- Why number theory: in a grid, the partners of a point at squared distance $N$ are the solutions of $x^2 + y^2 = N$, and their number $r_2(N) = 4(d_1(N) - d_3(N))$ (divisors that are 1 or 3 mod 4) is large when $N$ has many prime factors of the form $4k + 1$.
- **Pause and try:** how many integer points satisfy $x^2 + y^2 = 25$?
  - **Answer:** 12: $(\pm5, 0)$, $(0, \pm5)$, $(\pm3, \pm4)$ and $(\pm4, \pm3)$. So a point deep inside a grid has 12 partners at distance 5.

### Segment 3 (6 min): claims, checks and credit

- Problem #333: in late 2025 a proof was posted as the first autonomous AI resolution of an Erdős problem; within hours, forum users pointed out that a 1977 paper co-authored by Erdős had already answered it. Much of the early "AI solved it" news turned out to be literature search.
- Bloom has cautioned that some released manuscripts should be read as claims. Quanta Magazine (3 August 2026) surveys why the problems are falling to AI.
- Two different checks: a natural-language proof needs experts (the companion paper exists for this reason); a formal proof needs a correctly formalized statement (#728's trivial reading).
- For mathematicians, literature search and formal checking become cheap and more problems get attempted, while norms for credit and verification are still being worked out.
- **Pause and try:** an AI system posts a 12-page proof of an open Erdős problem. Name two checks before calling it solved.
  - **Answer:** a literature search for an earlier solution, and either expert checking or a Lean proof of a statement that matches the intended problem.

### Lab guide (about 2 hours, notebook `s11_ai_and_erdos_problems.ipynb`)

1. Section 1 (20 min): implement Legendre's formula and carry counting; check Kummer's theorem.
2. Section 2 (15 min): verify the identity behind the reduction and the Catalan case $k = 1$.
3. Section 3 (25 min): run the prime-by-prime test against direct division; read the plot.
4. Section 4 (15 min): read $m = 1328$'s digits in small bases and its carry table.
5. Section 5 (25 min): grid unit distances; check the brute force and Jacobi's formula.
6. TODO (20 min): the Legendre test of the factorial form.

- **Expect:** 131,769 Kummer checks with 0 mismatches; $3 + 3$ in base 2 has 2 carries. The Kummer test and direct division agree on all 40,000 pairs. Share of $m$ in [1000, 2000) that work: 1.000 ($k = 1$), 0.681 ($k = 10$), 0.344 ($k = 20$), 0.201 ($k = 40$); nine values of $m$ work for every $k \le 40$, starting with 1328. Grids: 288 unit pairs in the 10 × 10 grid (formula and brute force agree); best $N$ = 5, 65, 325, 1105, 5525; pairs per point from 1.92 to 17.35; $\log(\text{pairs})/\log(n)$ between 1.2027 and 1.2484.
- **Common problems:** counting carries without carrying the carry forward; using floating-point factorials (use Python integers); reading a finite trend as an asymptotic law.

### Quiz

1. State Kummer's theorem.
   - **Answer:** the exponent of a prime $p$ in $\binom{a+b}{a}$ equals the number of carries when $a$ and $b$ are added in base $p$.
2. With $n = 2m$, $b = m$, $a = m + k$, what does $a!\,b! \mid n!\,(a+b-n)!$ become?
   - **Answer:** $\binom{m+k}{k} \mid \binom{2m}{m}$.
3. What did the 2026 unit distance counterexample show?
   - **Answer:** that for some fixed $\delta > 0$ and infinitely many $n$, $u(n) \ge n^{1+\delta}$, so $u(n)$ is not $n^{1+o(1)}$ as Erdős conjectured.

**Watch out:** "An AI-generated proof is either right or wrong, so we can just check the answer." Natural-language proofs need slow expert checking, and early claims such as #333's were wrong about novelty. A formal proof removes doubt about the steps but not about the statement: #728 as displayed had a trivial reading. And no finite computation, like the notebook's, settles a statement about all large $n$.

### Assignment 11 (due before session 12, 10 points)

1. Finish the TODO: the Legendre test of the factorial form. Show that it agrees with section 3 for $m$ from 1,000 to 1,099 and $k \le 40$. (3 points)
2. For $n \le 300$, search for triples with $b \ne n/2$, $a, b \in [n/4, 3n/4]$, $a + b - n \ge 2 \ln n$ and the divisibility. Report how many you find and the largest gap divided by $\ln n$. (4 points)
3. Half a page: pick one problem from the AI-contributions wiki and report the claim, the evidence (Lean, expert check, literature search) and your own verdict on its status. (3 points)

Hand in one PDF and your notebook.

### Sources

- Sothanaphan 2026, Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof. https://arxiv.org/pdf/2601.07421
- Google DeepMind Formal Conjectures, Erdős Problem 728. https://google-deepmind.github.io/formal-conjectures/doc/FormalConjectures/ErdosProblems/728.html
- Alon, Bloom, Gowers, Litt, Sawin, Shankar, Tsimerman, Wang & Wood 2026, Remarks on the disproof of the unit distance conjecture. https://arxiv.org/abs/2605.20695
- Quanta Magazine, 3 August 2026, Why the Legendary Erdős Problems Are Falling to AI. https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/
- AI contributions to Erdős problems (wiki). https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems
- Erdős Problems forum, problem #333 thread. https://www.erdosproblems.com/forum/thread/333
- Spencer, Szemerédi & Trotter 1984, Unit distances in the Euclidean plane, in Graph Theory and Combinatorics (Academic Press); cited as the best known upper bound in https://arxiv.org/pdf/2507.15679

## Session 12: Seeing in 4D: feed-forward reconstruction, and what comes next

**Goal:** students can explain how D4RT reconstructs dynamic scenes with one transformer and query-based decoding, why feed-forward reconstruction is taking over many jobs of per-scene optimization and what it gives up, and what to watch for at NeurIPS 2026.

### Talking pointers

- **Open with:** "Reconstructing a scene in 3-D used to mean optimizing a model for each scene. The CVPR 2026 Best Paper reconstructs a moving scene from one video in a forward pass, and then answers questions about any point at any time."
- **Segment 1, say:** show the two pipelines side by side: fit a model to every scene, or train once and run one forward pass per scene.
- **Segment 2, say:** write the D4RT query $(u, v, t_{src}, t_{tgt}, t_{cam})$ on screen and show which settings give a depth map and which give a track.
- **Segment 3, say:** show the NeurIPS 2026 dates and the update checklist, then introduce the capstone.
- **Close with:** "Every fact in this course carries a date. From today, keeping it current is your job too." Then set assignment 12.

### Segment 1 (7 min): from per-scene optimization to feed-forward models

- Per-scene methods such as NeRF and Gaussian splatting (Course 2, session 11) fit a separate model to each scene by making rendered images match the photos: accurate, but every new scene costs a new optimization.
- Feed-forward methods train one network on many scenes and reconstruct a new scene in one pass. The Scene Representation Transformer (Sajjadi et al. 2022) encoded a set of images into a set-latent scene representation and rendered new views with a decoder that attends into it.
- VGGT (Wang et al. 2025), the CVPR 2025 Best Paper, predicts camera parameters, depth maps, point maps and 3-D tracks from one or many views in a single forward pass; its authors report reconstruction in under a second.
- The trade-off is amortization: per-scene methods spend compute at test time; feed-forward methods spend it once, in training, and then depend on their training data.
- **Pause and try:** in the notebook, the per-scene fit takes about 15.3 ms per scene and the feed-forward model 0.15 ms, plus 32 s of training. After about how many scenes is the feed-forward model cheaper in total?
  - **Answer:** about 2,100 scenes, since 32,000 ms / (15.33 − 0.15) ms ≈ 2,100.

### Segment 2 (7 min): D4RT

- D4RT (Zhang et al. 2026, Google DeepMind with UCL and Oxford) won the Best Paper award at CVPR 2026 in Denver, chosen from about 16,000 submissions.
- One transformer reads one video and jointly estimates depth, correspondence over time and full camera parameters. A global self-attention encoder builds a latent scene representation, and a lightweight decoder answers independent point queries. It builds on the Scene Representation Transformer.
- A query $(u, v, t_{src}, t_{tgt}, t_{cam})$ asks for the 3-D position, at time $t_{tgt}$ and in the coordinates of camera $t_{cam}$, of the point seen at pixel $(u, v)$ in frame $t_{src}$. Different settings give point clouds, depth maps, tracks and camera poses from the same interface.
- Because queries are independent, the model encodes the video once and decodes only the points you ask for, in parallel. The authors report state-of-the-art speed and accuracy across 4-D reconstruction tasks.
- **Pause and try:** which queries give (a) a depth map of frame 3, and (b) the track of one point through the video?
  - **Answer:** (a) every pixel $(u, v)$ with $t_{src} = t_{tgt} = t_{cam} = 3$; (b) one fixed $(u, v, t_{src})$ with $t_{tgt} = t_{cam}$ running over all frames, as in the paper; keeping $t_{cam}$ fixed instead expresses the whole track in one camera's coordinates.

### Segment 3 (6 min): NeurIPS 2026, keeping this course current, and the capstone

- NeurIPS 2026 runs 6–12 December in Sydney, with satellite sites in Atlanta and Paris; its awards and results arrive after this course was checked (November 2026).
- The update checklist, after each major conference:
  1. Read the official award pages (ICLR, CVPR, ACL, ICML, NeurIPS) and add or replace examples.
  2. Check each cited paper for newer arXiv versions. Statements change: the dimension terms in the FORS bounds differ between versions, and the #728 write-up has had at least five versions.
  3. Re-check living trackers: METR's time horizons and the Erdős problems pages.
  4. Search for independent reproductions, successful or failed, and update the claims ledger from session 1.
  5. Re-run every notebook and refresh the **Expect** lines.
- The capstone (brief and rubric in the course front matter) applies this course's method to one 2026 result, for example a NeurIPS 2026 paper: state the claim, reproduce the core idea at toy scale, and say what the toy can and cannot show.
- **Pause and try:** a paper you teach posts version 3 on arXiv with different numbers. What do you change?
  - **Answer:** the quoted numbers (naming the version), any lab that depends on them, the claims-ledger entry, and the date of your last check.

### Lab guide (about 2 hours, notebook `s12_feedforward_4d_reconstruction.ipynb`)

1. Sections 1–2 (25 min): build the world, look at one video, and read four queries and their answers.
2. Section 3 (25 min): train the feed-forward model and watch its error fall.
3. Section 4 (25 min): read the per-scene initialization and the soft renderer; check the demo fit.
4. Sections 5–6 (30 min): compare the methods, read the error curves, and study the tracked point.
5. TODO (15 min): the step-budget experiment.

- **Expect:** training took about 32 s on our CPU (batch error 1.408 at step 0, 0.315 at step 1,199). On scenes like the training scenes: feed-forward median error 0.183, 90th percentile 0.500, 54% of queries within 0.2, about 0.15 ms per scene; per-scene fit median 0.101, 90th percentile 0.319, 78% within 0.2, about 15 ms per scene (timings vary by machine). On faster scenes: feed-forward median 0.347 (29% within 0.2); per-scene fit 0.093 (77%). In the tracked example the red disc is hidden in frame 2; at frame 5 the true position is (−0.419, 6.661), the feed-forward answer (−1.662, 5.386) and the per-scene answer (−0.325, 8.188). Timings change from run to run.
- **Common problems:** comparing speed without counting training time; reading only the median; forgetting that the per-scene model was told the true form of the world.

### Quiz

1. What does a D4RT query specify, and what does it return?
   - **Answer:** a pixel $(u, v)$ in frame $t_{src}$, a target time $t_{tgt}$ and a reference camera $t_{cam}$; it returns that point's 3-D position at $t_{tgt}$ in $t_{cam}$'s coordinates.
2. Why are independent point queries efficient?
   - **Answer:** the video is encoded once, and then only the requested points are decoded, in parallel, instead of decoding every frame densely.
3. Name one advantage of per-scene optimization that the notebook showed.
   - **Answer:** it does not depend on a training distribution: on faster scenes it kept a median error of 0.093, while the feed-forward model's rose to 0.347.

**Watch out:** "Feed-forward models make per-scene optimization obsolete." They make reconstruction fast, but they depend on their training data, while per-scene optimization adapts to each scene: in the notebook it was more accurate and unaffected by faster motion, at about a hundred times the test-time cost. Choose by the accuracy you need, how unusual your scenes are, and your compute budget.

### Assignment 12 (due with the capstone, 10 points)

1. Finish the TODO: per-scene fits with 0, 30, 100 and 300 steps. Plot median error against time per scene, and compute the break-even number of scenes including the feed-forward training time. (3 points)
2. Test both methods on discs of radius 0.7. Which method breaks, and which assumption does each one rely on? (3 points)
3. After NeurIPS 2026, pick one award-winning or widely discussed paper. Write its claims-ledger entry (claim, evidence, version checked, date) and a one-page plan for a toy lab in this course's style. (4 points)

Hand in one PDF and your notebook.

### Sources

- Zhang et al. 2026 (Google DeepMind, UCL and Oxford; with Sajjadi), Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (CVPR 2026). https://arxiv.org/abs/2512.08924
- D4RT project page. https://d4rt-paper.github.io
- CVPR 2026 Best Papers. https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers
- Sajjadi et al. 2022, Scene Representation Transformer: Geometry-Free Novel View Synthesis Through Set-Latent Scene Representations (CVPR 2022). https://arxiv.org/abs/2111.13152
- Wang, Chen, Karaev, Vedaldi, Rupprecht & Novotny 2025, VGGT: Visual Geometry Grounded Transformer (CVPR 2025). https://arxiv.org/abs/2503.11651
- CVPR 2025 Best Papers. https://cvpr.thecvf.com/Conferences/2025/BestPapersDemos
- NeurIPS 2026 dates. https://neurips.cc/Conferences/2026/Dates

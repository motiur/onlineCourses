# Course 3: Ten Years of Deep Learning Ideas

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on the big deep learning ideas of roughly 2016–2026 that the other courses in this series do not teach, from residual connections and µP to diffusion, flow matching, deep reinforcement learning and neural fields. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

In ten years deep learning gained a toolkit that every researcher now takes for granted: ways to train very deep and very wide networks, optimizers and schedules that work at scale, a better understanding of why huge networks generalize, new architectures for vision, learning without labels, learning from examples in a prompt, and new families of generative models. The other courses in this series teach many of the decade's ideas where they are needed, such as transformers, LoRA, mixture of experts, Mamba, CLIP and graph networks. This course collects the rest. Each session explains what problem an idea solved, how it works, what evidence supports it and where it is used now, and then reproduces it at toy scale on a CPU.

Prerequisites: the skills of Course 1 (Python, PyTorch training loops, basic deep learning and transformers). Course 4 helps for sessions 1, 2 and 6.

Capstone: reproduce one idea from this course at small scale, add one ablation run with three seeds, and report honestly whether the result held: a four-page report and a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: the idea and its source explained correctly (15); a faithful small-scale reproduction (25); the ablation, with three seeds and honest uncertainty (25); an interpretation that says what the toy can and cannot show (20); clarity of the report and video (15).

A note on scale: every lab runs on an ordinary CPU in a few minutes, so the results show how a method behaves, not how well it performs at full scale. Where a toy result disagrees with the papers, the lab says so.

### Sessions

1. **Making depth work: residuals, normalization and µP.** Students can explain why very deep networks were hard to train, how residual connections, normalization layers and width-aware parameterization (µP) fix it, and can run a coordinate check.
   - Read: He et al. 2015, Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification; He et al. 2016, Deep Residual Learning for Image Recognition
   - Lab: about 2 hours, notebook `s01_making_depth_work.ipynb`
2. **Optimizers, schedules and training at scale.** Students can choose and tune an optimizer and learning-rate schedule, explain decoupled weight decay, warmup and warmup-stable-decay, describe Lion, Shampoo/SOAP and Muon, and estimate the memory needed to train a large model.
   - Read: Kingma & Ba 2015, Adam: A Method for Stochastic Optimization; Loshchilov & Hutter 2019, Decoupled Weight Decay Regularization
   - Lab: about 2.5 hours, notebook `s02_optimizers_and_schedules.ipynb`
3. **The generalization puzzles.** Students can describe the evidence that over-parameterized networks generalize in ways classical theory did not predict (random labels, double descent, implicit bias, flat minima, edge of stability, lottery tickets), reproduce two of these on a CPU, and say what each result does and does not show.
   - Read: Zhang et al. 2017, Understanding Deep Learning Requires Rethinking Generalization; Belkin et al. 2019, Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off
   - Lab: about 2 hours, notebook `s03_generalization_puzzles.ipynb`
4. **Vision transformers and the modern ConvNet.** Students can explain how a vision transformer turns an image into tokens, why it needed lots of data or a strong training recipe, what Swin and ConvNeXt changed, and can train a tiny ViT and a small CNN on the same small images.
   - Read: Dosovitskiy et al. 2021, An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale; Touvron et al. 2021, Training Data-Efficient Image Transformers & Distillation through Attention
   - Lab: about 2 hours, notebook `s04_vision_transformers.ipynb`
5. **Self-supervised learning.** Students can explain how networks learn representations without labels (contrastive learning, self-distillation and masked prediction), recognize representation collapse, and evaluate features with a linear probe.
   - Read: Gidaris et al. 2018, Unsupervised Representation Learning by Predicting Image Rotations; van den Oord et al. 2018, Representation Learning with Contrastive Predictive Coding
   - Lab: about 2 hours, notebook `s05_self_supervised_learning.ipynb`
6. **In-context learning and learning to learn.** Students can explain meta-learning, how MAML and prototypical networks solve few-shot tasks, and what research shows about how transformers learn in context, and can train a tiny transformer to do in-context linear regression.
   - Read: Vinyals et al. 2016, Matching Networks for One Shot Learning; Finn et al. 2017, Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks
   - Lab: about 2 hours, notebook `s06_in_context_learning.ipynb`
7. **Generative models before diffusion: VAEs, VQ-VAE, flows and GANs.** Students can explain latent-variable models and the ELBO, discrete latents (VQ-VAE) that became today's image and audio tokenizers, invertible flows with exact likelihood, GANs and their failure modes, and how generative models are evaluated.
   - Read: Kingma & Welling 2014, Auto-Encoding Variational Bayes; Higgins et al. 2017, β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework
   - Lab: about 3 hours, notebook `s07_generative_models_before_diffusion.ipynb`
8. **Diffusion models.** Students can explain the forward noising process and the denoising objective, the link to score matching, how DDPM and DDIM sample, classifier-free guidance and latent diffusion, and can train a diffusion model on 2-D data.
   - Read: Sohl-Dickstein et al. 2015, Deep Unsupervised Learning using Nonequilibrium Thermodynamics; Ho et al. 2020, Denoising Diffusion Probabilistic Models
   - Lab: about 3 hours, notebook `s08_diffusion_models.ipynb`
9. **Flow matching, rectified flow and fast generation.** Students can explain flow matching as regression onto a velocity field, why straighter paths need fewer steps (rectified flow, consistency models, distillation), and why diffusion transformers replaced U-Nets, and can compare flow matching with diffusion on 2-D data.
   - Read: Lipman et al. 2023, Flow Matching for Generative Modeling; Liu et al. 2023, Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow
   - Lab: about 3 hours, notebook `s09_flow_matching.ipynb`
10. **Deep reinforcement learning, from AlphaGo to world models.** Students can explain the decade's deep RL milestones — search with self-play (AlphaGo Zero, AlphaZero), policy optimization (PPO), learned models (MuZero, Dreamer) and offline RL (Decision Transformer) — and implement PPO and Monte Carlo tree search on small problems.
   - Read: Silver et al. 2016, Mastering the Game of Go with Deep Neural Networks and Tree Search; Silver et al. 2017, Mastering the Game of Go without Human Knowledge
   - Lab: about 3 hours, notebook `s10_deep_reinforcement_learning.ipynb`
11. **Neural fields and 3D, from Fourier features to Gaussian splatting.** Students can explain coordinate networks and spectral bias, NeRF's volume rendering, and why hash grids and explicit Gaussians made 3D reconstruction fast, and can fit an image and a toy radiance field.
   - Read: Rahaman et al. 2019, On the Spectral Bias of Neural Networks; Tancik et al. 2020, Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains
   - Lab: about 3 hours, notebook `s11_neural_fields.ipynb`
12. **Robustness, uncertainty and calibration.** Students can explain adversarial examples and adversarial training, certified robustness, calibration and temperature scaling, ensembles, conformal prediction and distribution shift, and can measure each on a small model.
   - Read: Szegedy et al. 2014, Intriguing Properties of Neural Networks; Goodfellow et al. 2015, Explaining and Harnessing Adversarial Examples
   - Lab: about 3 hours, notebook `s12_robustness_and_uncertainty.ipynb`

### The rest of the decade, and where it is taught

| Idea | Where it is taught |
|---|---|
| Transformers and attention | Course 4 session 1; Course 1 session 6 |
| Tokenization | Course 4 session 2; Course 5 |
| Scaling laws | Course 4 session 3 |
| Mixture of experts, FlashAttention, quantization, KV cache, speculative decoding | Course 4 session 4 |
| LoRA and QLoRA | Course 4 session 5 |
| RLHF and direct preference optimization | Course 4 session 6 |
| Reasoning models and GRPO | Course 4 session 7 |
| Retrieval and agents | Course 4 session 8 |
| CLIP and vision-language models | Course 4 session 9 |
| State-space models (Mamba) and diffusion language models | Course 4 session 10 |
| Sparse autoencoders and interpretability | Course 4 session 11 |
| Distillation | Course 4 session 12; Course 5 session 10 |
| Graph neural networks, graph transformers and equivariant networks | Course 7 |
| Flow matching on curved spaces | Course 7 session 9 |
| Differential privacy, federated learning and unlearning | Course 8 |
| Grokking | Course 9 session 4 |
| Research from 2026 | Course 14 |

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. In this course, show at least one plot from the notebook in every video and say what it shows.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. Cells labelled NOT RUN need a GPU, a download or a library that was not installed; dry-run them before recording.
- **Papers:** each session lists its sources. Read at least the first two before recording.
- **Dates:** written in November 2026.

## Session 1: Making depth work: residuals, normalization and µP

**Goal:** students can explain why very deep networks were hard to train, how residual connections, normalization layers and width-aware parameterization (µP) fix it, and can run a coordinate check.

### Talking pointers

- **Open with:** "In 2015, a 56-layer network did worse than a 20-layer one, even on its own training data. Three ideas fixed that, and today you test all three."
- **Segment 1, say:** multiply 1 by 0.9 fifty times, then show the notebook's gradient plot.
- **Segment 2, say:** draw a batch × features tensor and shade what each norm averages over.
- **Segment 3, say:** show the coordinate check and the learning-rate sweep side by side.
- **Close with:** "Depth needs a clean path for the gradient; width needs the right scale for each layer." Then set assignment 1.

### Segment 1 (6 min): residual connections and signal propagation

- Signals and gradients are multiplied by every layer in turn, so a per-layer factor slightly below or above 1 compounds: gradients vanish or explode.
- Initialization sets that factor: for ReLU layers, weight variance 2/fan_in (fan_in = inputs per unit) keeps the activation variance constant (He et al. 2015).
- Even so, a 56-layer plain network had higher training error than a 20-layer one on CIFAR-10: an optimization problem, not overfitting (He et al. 2016).
- ResNet's fix: y = x + F(x). Since ∂y/∂x = I + ∂F/∂x, the gradient always has a direct identity path (He et al. 2016).
- Pre-activation ResNets keep the shortcut a pure identity and trained 1001 layers (He et al. 2016b); transformers use the same "pre-norm" layout.
- Without normalization, each block adds variance. Fixup rescales branches at initialization and zeroes each branch's last layer (Zhang et al. 2019); ReZero multiplies each branch by a learned scalar starting at 0 (Bachlechner et al. 2020).
- **Pause and try:** a 100-layer plain network multiplies the gradient by 0.9 at every layer. What fraction reaches layer 1?
  - **Answer:** 0.9^100 ≈ 2.7 × 10⁻⁵: the factors multiply. A residual shortcut adds a path that is not shrunk.

### Segment 2 (7 min): normalization layers

- BatchNorm normalizes each channel with the batch's mean and variance, then applies a learned scale and shift (Ioffe & Szegedy 2015); this allowed much higher learning rates.
- Weak points: tiny batches give noisy statistics, and testing uses running averages instead.
- The original paper credited reduced "internal covariate shift" (changes in each layer's input distribution); Santurkar et al. (2018) point to a smoother loss instead (see Watch out).
- LayerNorm normalizes each example over its features, with no batch dependence (Ba et al. 2016). GroupNorm normalizes groups of channels and works with 2 images per GPU (Wu & He 2018). RMSNorm drops the mean subtraction and divides by the root mean square (Zhang & Sennrich 2019); Course 4 session 1 shows it in a modern LLM.
- Placement matters: post-LN transformers (normalize after the addition) start with large gradients near the output and need warmup; pre-LN can drop it (Xiong et al. 2020).
- At very large scale, attention logits can grow until training diverges; normalizing queries and keys ("QK-norm") fixed this in ViT-22B (Dehghani et al. 2023).
- **Pause and try:** x = (2, 2, 2, 2). What do RMSNorm and LayerNorm output (gain 1, no bias)?
  - **Answer:** RMSNorm gives (1, 1, 1, 1), since the root mean square is 2. LayerNorm gives (0, 0, 0, 0), since every value equals the mean.

### Segment 3 (7 min): width and µP

- Under the standard parameterization (SP), weights start with variance about 1/fan_in and all layers share one learning rate. Adam moves each weight by about the learning rate per step, and a unit sums over `width` inputs, so its change grows with width: the best learning rate shifts.
- In the neural tangent kernel (NTK) limit of infinite width, weights move so little that features stay at their initial values: "lazy" training (Jacot et al. 2018).
- The maximal update parameterization, µP, sets per-layer initial scales and learning rates so features change by a width-independent amount each step (Yang & Hu 2021). For Adam: hidden and output learning rates scale as 1/width, the output layer starts smaller (variance 1/fan_in²), and attention divides by d instead of √d.
- µTransfer: tune on a small model and copy the hyperparameters to a large one. Transferring from 40M parameters beat the published GPT-3 6.7B results, with tuning that cost 7% of one pretraining run (Yang et al. 2022).
- Depth-µP scales each residual branch by 1/√L for transfer across depth L; the authors show limits when blocks have several layers, as in transformers (Yang et al. 2023).
- The coordinate check trains each width a few steps and plots activation sizes against width; flat lines mean the parameterization is right.
- **Pause and try:** with SP, Adam's best learning rate is 1e-3 at width 256. At width 4096, is it higher or lower for hidden layers, and by how much?
  - **Answer:** lower, by about 256/4096 = 1/16 (roughly 6e-5), because hidden-layer updates grow in proportion to width. µP builds this in.

### Lab guide (about 2 hours, notebook `s01_making_depth_work.ipynb`)

1. Sections 1–2 (25 min): signals at initialization. Read the gradient curves from layer 50 back to layer 1.
2. Section 3 (25 min): short training runs at two learning rates.
3. Section 4 (20 min): coordinate check. What grows with width under SP?
4. Section 5 (25 min): learning-rate sweep. Find each width's best rate.
5. TODO cells (25 min): rerun section 3 with Adam; write the post-LN block.

- **Expect:** default init's gradient RMS is 1.4e-23 at layer 1 against 1.4e-4 at layer 50 (He init: 8.6e-5 against 1.4e-4). Test accuracy at learning rates 0.003 / 0.03: default init 0.102 / 0.100, He init 0.771 / 0.096, unnormalized residual diverges, LayerNorm 0.927 / 0.962, RMSNorm 0.947 / 0.969, ReZero 0.931 / 0.960. SP logits grow from 0.62 (width 32) to 24.6 (width 2,048); µP stays between 0.62 and 0.81. Best log2 learning rate for widths 32, 128, 512: −7, −9, −10 under SP; −7, −7, −6 under µP. Runtime about 1 minute.
- **Common problems:** squaring tiny gradients in float32 underflows to 0 (the notebook uses float64); judging a network at one learning rate; one optimizer group for all µP parameters, which silently restores SP.

### Quiz

1. Why does y = x + F(x) help gradients reach early layers?
   - **Answer:** ∂y/∂x = I + ∂F/∂x, so there is always an identity path not multiplied by the branch's Jacobian.
2. Name one problem of BatchNorm that LayerNorm avoids.
   - **Answer:** batch dependence: it fails with tiny batches and uses different statistics in training and testing.
3. What does a coordinate check measure, and what result is correct?
   - **Answer:** activation sizes after a few steps against width; flat curves mean the parameterization is right.

**Watch out:** "BatchNorm works because it removes internal covariate shift." Santurkar et al. (2018) increased the shift on purpose and training still worked. Their evidence points to a smoother loss landscape that tolerates larger learning rates. Treat it as a historical hypothesis, not an established mechanism.

### Assignment 1 (due before session 2, 10 points)

1. Rerun section 3 with Adam (learning rate 1e-3) and three seeds for the plain He-init and residual + LayerNorm networks. Report mean and spread, and explain the difference from SGD. (3 points)
2. Complete the post-LN block and compare it with pre-LN at depth 32 at both learning rates. (4 points)
3. Repeat section 5 with three seeds. Does the best learning rate move more than the seed-to-seed noise under SP? Under µP? (3 points)

Hand in one PDF and your notebook.

### Sources

- He et al. 2015, Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification. https://arxiv.org/abs/1502.01852
- He et al. 2016, Deep Residual Learning for Image Recognition. https://arxiv.org/abs/1512.03385
- He et al. 2016b, Identity Mappings in Deep Residual Networks. https://arxiv.org/abs/1603.05027
- Ioffe & Szegedy 2015, Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. https://arxiv.org/abs/1502.03167
- Santurkar et al. 2018, How Does Batch Normalization Help Optimization? https://arxiv.org/abs/1805.11604
- Ba et al. 2016, Layer Normalization. https://arxiv.org/abs/1607.06450
- Wu & He 2018, Group Normalization. https://arxiv.org/abs/1803.08494
- Zhang & Sennrich 2019, Root Mean Square Layer Normalization. https://arxiv.org/abs/1910.07467
- Xiong et al. 2020, On Layer Normalization in the Transformer Architecture. https://arxiv.org/abs/2002.04745
- Zhang et al. 2019, Fixup Initialization: Residual Learning Without Normalization. https://arxiv.org/abs/1901.09321
- Bachlechner et al. 2020, ReZero is All You Need: Fast Convergence at Large Depth. https://arxiv.org/abs/2003.04887
- Dehghani et al. 2023, Scaling Vision Transformers to 22 Billion Parameters. https://arxiv.org/abs/2302.05442
- Jacot et al. 2018, Neural Tangent Kernel: Convergence and Generalization in Neural Networks. https://arxiv.org/abs/1806.07572
- Yang & Hu 2021, Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks. https://arxiv.org/abs/2011.14522
- Yang et al. 2022, Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer. https://arxiv.org/abs/2203.03466
- Yang et al. 2023, Tensor Programs VI: Feature Learning in Infinite-Depth Neural Networks. https://arxiv.org/abs/2310.02244

## Session 2: Optimizers, schedules and training at scale

**Goal:** students can choose and tune an optimizer and learning-rate schedule, explain decoupled weight decay, warmup and warmup-stable-decay, describe Lion, Shampoo/SOAP and Muon, and estimate the memory needed to train a large model.

### Talking pointers

- **Open with:** "Two people train the same model on the same data; one succeeds and one fails. Often the only difference is the optimizer settings and the schedule."
- **Segment 1, say:** write the L2 and weight-decay updates for SGD and for Adam, and circle the √v.
- **Segment 2, say:** show the Newton–Schulz printout: singular values squeezed close to 1.
- **Segment 3, say:** fill in a 7B model's memory table, then divide by the GPU count.
- **Close with:** "Tune every optimizer you compare, and count the bytes before you rent GPUs." Then set assignment 2.

### Segment 1 (7 min): AdamW, warmup and schedules

- Adam keeps running averages of the gradient (m) and of its square (v) and steps by m̂/(√v̂ + ε) (Kingma & Ba 2015).
- For SGD, L2 regularization equals weight decay. Under Adam the L2 gradient λw is divided by √v, so weights with large gradients are barely regularized; AdamW instead decays every weight by the same factor, separately from the gradient step: (1 − ηλ) per step in PyTorch (Loshchilov & Hutter 2019).
- Warmup: early in training, Adam's v is estimated from very few gradients, so steps are erratic (Liu et al. 2020, RAdam). Large-batch SGD also needed a gradual warmup (Goyal et al. 2017).
- Cosine annealing decays the learning rate along half a cosine wave (Loshchilov & Hutter 2017). But you must fix the total number of steps in advance.
- Warmup-stable-decay (WSD) keeps the rate constant and decays only at the end (Hu et al. 2024). It matches cosine, and short decays branched from its checkpoints give models for several budgets from one run (Hägele et al. 2024).
- Schedule-free optimization removes the schedule by averaging iterates (Defazio et al. 2024); it won the self-tuning track of the 2024 AlgoPerf competition.
- **Pause and try:** you double the batch size. What does the linear scaling rule say about the learning rate?
  - **Answer:** double it, with a warmup (Goyal et al. 2017). This was shown for SGD, with batches up to 8,192 images.

### Segment 2 (6 min): beyond Adam

- LARS and LAMB scale each layer's step by its weight norm over its update norm, which made very large batches work; LAMB trained BERT in 76 minutes (You et al. 2017; You et al. 2020).
- Lion was found by program search. It keeps only momentum and moves every weight by exactly ±η: update = sign(β₁m + (1 − β₁)g). It needs a 3–10 times smaller learning rate than AdamW (Chen et al. 2023).
- Shampoo preconditions each weight matrix from both sides with statistics of G Gᵀ and Gᵀ G (Gupta et al. 2018). SOAP runs Adam in Shampoo's eigenbasis and reported over 40% fewer iterations than AdamW in large-batch language-model training (Vyas et al. 2024).
- Muon, for the 2-D weights of hidden layers, replaces the momentum matrix with an approximately orthogonal one using five Newton–Schulz iterations, so no direction dominates the update (Jordan et al. 2024). Liu et al. (2025) added weight decay and update rescaling to train large language models; Course 14 covers later work.
- AlgoPerf compares optimizers fairly by time to a target on fixed hardware, with fixed tuning budgets (Dahl et al. 2023).
- **Pause and try:** a 1B-parameter model: how much fp32 memory do AdamW's and Lion's optimizer states take?
  - **Answer:** AdamW keeps m and v, 2 × 4 bytes × 10⁹ = 8 GB; Lion keeps only m, 4 GB.

### Segment 3 (7 min): training at scale

- Memory before activations: weights, gradients and Adam's two states. In mixed precision with fp32 master weights this is 2 + 2 + 12 = 16 bytes per parameter (Micikevicius et al. 2018). Mixed precision saves activation memory and time, not these 16 bytes. Loss scaling stops small fp16 gradients rounding to zero.
- Activation checkpointing stores only some activations and recomputes the rest in the backward pass (Chen et al. 2016).
- Data parallelism copies the model and splits the batch. Tensor parallelism splits each matrix multiplication across GPUs (Shoeybi et al. 2019). Pipeline parallelism splits the layers into stages fed with micro-batches (Huang et al. 2019).
- ZeRO removes the copies in data parallelism: stage 1 shards optimizer states, stage 2 also gradients, stage 3 also weights (Rajbhandari et al. 2020). PyTorch's FSDP works like stage 3 (Zhao et al. 2023).
- **Pause and try:** memory for training a 7B model with Adam in mixed precision, before activations?
  - **Answer:** 16 bytes × 7 × 10⁹ ≈ 112 GB, more than one 80 GB GPU; with ZeRO-3 over 8 GPUs, 14 GB each.

### Lab guide (about 2.5 hours, notebook `s02_optimizers_and_schedules.ipynb`)

1. Section 2 (25 min): the two-weight toy and the weight-decay sweep.
2. Section 3 (15 min): warmup at three peak learning rates.
3. Section 4 (30 min): three schedules and the WSD branch.
4. Section 5 (35 min): Lion and Muon, and the optimizer sweep.
5. Section 6 (20 min): the memory calculator and activation checkpointing.
6. TODO cells (25 min).

- **Expect:** toy: Adam + L2 gives 0.882 (large-gradient weight) and 0.000 (no-gradient weight); AdamW gives 0.541 and 0.606. At λ = 1, Adam + L2 collapses to 0.101 test accuracy and AdamW keeps 0.948. Warmup changes accuracy from 0.912 to 0.919, 0.905 to 0.932 and 0.191 to 0.555 at peak rates 0.01, 0.03 and 0.1. Excess loss: constant 0.170, cosine 0.113, WSD 0.116; the WSD branch 0.191 against 0.219 for a 750-step cosine run. Best excess loss: Muon 0.085, AdamW 0.113, Lion 0.119. Checkpointing: 35.8 MB → 12.0 MB saved, 16 → 28 layer calls, identical gradients. Runtime about 1 minute.
- **Common problems:** comparing optimizers at one shared learning rate; assuming PyTorch's `Adam(weight_decay=...)` is AdamW (it is L2); timing on a busy shared CPU.

### Quiz

1. Why does L2 regularization behave differently from weight decay under Adam?
   - **Answer:** Adam divides the L2 gradient λw by √v, so weights with large gradients are decayed less. AdamW shrinks every weight by the same factor.
2. What does WSD give a lab that wants models at several training budgets?
   - **Answer:** one long constant-rate run; a short decay from any checkpoint gives a finished model for that budget, without fixing the total length in advance.
3. Why can't mixed precision alone fit a 7B model's Adam training on one 80 GB GPU?
   - **Answer:** the 16 bytes per parameter (112 GB) for weights, gradients, master weights and Adam states remain; they must be sharded (ZeRO or FSDP).

**Watch out:** "Weight decay and L2 regularization are the same thing." They match only for plain SGD (with λ rescaled by the learning rate). In the notebook's Adam toy, L2 left a large-gradient weight almost untouched and drove a no-gradient weight to zero; AdamW shrank both alike.

### Assignment 2 (due before session 3, 10 points)

1. Repeat section 4 with three seeds. Report the mean and standard deviation of the final excess loss for each schedule and for the WSD branch. (3 points)
2. Repeat section 5 with three seeds and five learning rates per optimizer, and add wall-clock time per step. Rank the optimizers per step and per second, and explain any difference. (4 points)
3. Use the calculator for a 70B model on 64 GPUs at ZeRO stages 0–3. Optional: run the NOT RUN cell on a Colab GPU and compare its peak memory. (3 points)

Hand in one PDF and your notebook.

### Sources

- Kingma & Ba 2015, Adam: A Method for Stochastic Optimization. https://arxiv.org/abs/1412.6980
- Loshchilov & Hutter 2019, Decoupled Weight Decay Regularization. https://arxiv.org/abs/1711.05101
- Loshchilov & Hutter 2017, SGDR: Stochastic Gradient Descent with Warm Restarts. https://arxiv.org/abs/1608.03983
- Goyal et al. 2017, Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour. https://arxiv.org/abs/1706.02677
- Liu et al. 2020, On the Variance of the Adaptive Learning Rate and Beyond. https://arxiv.org/abs/1908.03265
- You et al. 2017, Large Batch Training of Convolutional Networks. https://arxiv.org/abs/1708.03888
- You et al. 2020, Large Batch Optimization for Deep Learning: Training BERT in 76 minutes. https://arxiv.org/abs/1904.00962
- Hu et al. 2024, MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies. https://arxiv.org/abs/2404.06395
- Hägele et al. 2024, Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations. https://arxiv.org/abs/2405.18392
- Defazio et al. 2024, The Road Less Scheduled. https://arxiv.org/abs/2405.15682
- Chen et al. 2023, Symbolic Discovery of Optimization Algorithms. https://arxiv.org/abs/2302.06675
- Gupta et al. 2018, Shampoo: Preconditioned Stochastic Tensor Optimization. https://arxiv.org/abs/1802.09568
- Vyas et al. 2024, SOAP: Improving and Stabilizing Shampoo using Adam. https://arxiv.org/abs/2409.11321
- Dahl et al. 2023, Benchmarking Neural Network Training Algorithms. https://arxiv.org/abs/2306.07179
- Jordan et al. 2024, Muon: An optimizer for hidden layers in neural networks. https://kellerjordan.github.io/posts/muon/
- Liu et al. 2025, Muon is Scalable for LLM Training. https://arxiv.org/abs/2502.16982
- Micikevicius et al. 2018, Mixed Precision Training. https://arxiv.org/abs/1710.03740
- Chen et al. 2016, Training Deep Nets with Sublinear Memory Cost. https://arxiv.org/abs/1604.06174
- Shoeybi et al. 2019, Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. https://arxiv.org/abs/1909.08053
- Huang et al. 2019, GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism. https://arxiv.org/abs/1811.06965
- Rajbhandari et al. 2020, ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. https://arxiv.org/abs/1910.02054
- Zhao et al. 2023, PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel. https://arxiv.org/abs/2304.11277

## Session 3: The generalization puzzles

**Goal:** students can describe the evidence that over-parameterized networks generalize in ways classical theory did not predict (random labels, double descent, implicit bias, flat minima, edge of stability, lottery tickets), reproduce two of these on a CPU, and say what each result does and does not show.

### Talking pointers

- **Open with:** "A network that can memorize pure noise still learns real patterns from real data. Classical theory says that should not happen. Today we look at five puzzles that changed how we think about generalization."
- **Segment 1, say:** show the notebook's two training curves (true and random labels), then the double-descent plot with its peak at p = 200.
- **Segment 2, say:** draw a ball rolling in a valley that is too narrow for its step; then show the sharpness curves sitting on the 2/η lines.
- **Segment 3, say:** show the pruning plot and stress the cost: seven full training runs to find one ticket.
- **Close with:** "Each puzzle is a real measurement, and each is easy to over-interpret. Say exactly what was shown." Then set assignment 3.

### Segment 1 (7 min): memorization and double descent

- Standard networks reach zero training error on CIFAR-10 even when every label is random, and explicit regularization does not prevent it (Zhang et al. 2017). So the same model class can memorize or generalize; parameter counts alone cannot explain which happens.
- Double descent: as model size grows, test error falls, rises to a peak where the model can just fit the training data (the interpolation threshold), then falls again (Belkin et al. 2019).
- Nakkiran et al. (2020) found model-wise, epoch-wise and sample-wise double descent in deep networks, strongest with label noise; near the threshold, more data can even hurt.
- Well-tuned regularization can remove the peak (Nakkiran et al. 2021).
- Benign overfitting: in linear regression, the minimum-norm interpolating solution can still predict well when the data have many weak directions that absorb the noise harmlessly (Bartlett et al. 2020).
- **Pause and try:** random-features regression with 200 training points. Where do you expect the test-error peak?
  - **Answer:** near 200 features, where the model has just enough parameters to fit all points, noise included. In the notebook it is at p = 200.

### Segment 2 (7 min): implicit bias and flatness

- The training method itself prefers some solutions over others; this preference is called implicit bias. For example, gradient descent from zero on an underdetermined least-squares problem finds the minimum-norm solution.
- Large-batch training reached sharper minima and generalized worse than small-batch training (Keskar et al. 2017). But sharpness depends on how weights are scaled: rescaling a ReLU network can make a minimum arbitrarily sharp without changing the function (Dinh et al. 2017). Flatness is a useful hint, not a proven cause.
- Sharpness-aware minimization (SAM) minimizes the worst loss within a small ball: it steps to w + ρg/‖g‖, takes the gradient there, and applies it at w (Foret et al. 2021). It improved image benchmarks and robustness to noisy labels, at twice the cost per step.
- Edge of stability: during full-batch gradient descent, the sharpness (the largest Hessian eigenvalue) rises until it reaches about 2/η, then hovers there while the loss falls non-monotonically (Cohen et al. 2021). Classical analysis assumes the sharpness stays below 2/η.
- **Pause and try:** η = 0.1. At what curvature does gradient descent on a quadratic diverge?
  - **Answer:** above 2/η = 20, because each step multiplies the error by |1 − ηa|, which exceeds 1 when a > 20.

### Segment 3 (6 min): sparse subnetworks

- The lottery ticket hypothesis: a dense network contains sparse subnetworks that, trained alone from their original initial values, reach the full network's accuracy. They are found by iterative magnitude pruning: train, prune the smallest weights, rewind the rest to initialization, repeat (Frankle & Carbin 2019).
- The control matters: the same sparse mask with a new random initialization trains worse, so the initial values matter, not only the structure.
- For larger networks, rewinding to iteration 0 fails; rewinding to an early point in training works. This succeeds once training is stable to SGD noise, meaning two runs from that point end in minima joined by a straight path of low loss (Frankle et al. 2020).
- What tickets do not show: a cheap way to train. Finding one costs several full training runs. Grokking, another training puzzle, is taught in Course 9 session 4 (Power et al. 2022).
- **Pause and try:** each round prunes 20% of the remaining weights. What fraction is left after 10 rounds?
  - **Answer:** 0.8^10 ≈ 0.107, about 11%.

### Lab guide (about 2 hours, notebook `s03_generalization_puzzles.ipynb`)

1. Section 2 (15 min): true versus random labels. Compare the epochs needed and the test accuracy.
2. Section 3 (25 min): double descent. Find the peak and explain why ridge removes it.
3. Section 4 (25 min): edge of stability. Compare each sharpness curve with its 2/η line.
4. Section 5 (20 min): SGD versus SAM with 28% wrong labels, three seeds.
5. Section 6 (20 min): lottery tickets and the re-initialization control.
6. TODO cells (15 min).

- **Expect:** 99.9% training accuracy at epoch 12 (true labels) and epoch 64 (random labels), test accuracy 0.973 and 0.129. Minimum-norm test error 0.30 at p = 50, 0.85 at p = 200, 0.30 at p = 2,000; ridge λ = 100 stays at 0.14–0.17 from p = 100. Mean sharpness over steps 1,000–2,000: 6.67 for η = 0.3 (2/η = 6.67) and 3.37 for η = 0.6 (3.33); for η = 0.15 it is still rising (11.21, below 13.33). SGD 0.778 ± 0.016 against SAM 0.776 ± 0.034 (ρ = 0.05) and 0.765 ± 0.002 (ρ = 0.1): no gain from SAM here. With 2.1% of weights left, the ticket gets 0.956 and the re-initialized mask 0.873. Runtime under 1 minute.
- **Common problems:** forgetting label noise, which makes the double-descent peak much smaller; using a mini-batch, not the full batch, for the sharpness experiment; judging SAM from one seed.

### Quiz

1. What does the random-label experiment show, and what does it not show?
   - **Answer:** the network can memorize anything, so its capacity alone cannot explain good generalization. It does not tell us what does explain it.
2. Why is test error worst near p = n in the random-features model?
   - **Answer:** there the model can only just fit every training point, noise included, which needs very large coefficients that predict badly on new data.
3. What is the edge of stability?
   - **Answer:** in full-batch gradient descent the top Hessian eigenvalue rises to about 2/η and hovers there, while the loss keeps decreasing non-monotonically.

**Watch out:** "More parameters always means more overfitting." Double descent and the random-label results show that test error can fall again past the interpolation threshold. The reverse claim, "bigger is always better", is also wrong: near the threshold more parameters, or more data, can hurt, and in our lab the regularized models beat the unregularized ones at every size.

### Assignment 3 (due before session 4, 10 points)

1. Rerun section 3 with label noise 0%, 10%, 20% and 40%. Plot the peak height against the noise level. (3 points)
2. Try to make SAM beat SGD in section 5: tune ρ and the learning rate with three seeds each. Report every setting you tried, including those that did not help. (4 points)
3. Repeat section 6 with three seeds, and add a random-pruning control (a random mask with the original initialization). (3 points)

Hand in one PDF and your notebook.

### Sources

- Zhang et al. 2017, Understanding Deep Learning Requires Rethinking Generalization. https://arxiv.org/abs/1611.03530
- Belkin et al. 2019, Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off. https://arxiv.org/abs/1812.11118
- Nakkiran et al. 2020, Deep Double Descent: Where Bigger Models and More Data Hurt. https://arxiv.org/abs/1912.02292
- Nakkiran et al. 2021, Optimal Regularization Can Mitigate Double Descent. https://arxiv.org/abs/2003.01897
- Bartlett et al. 2020, Benign Overfitting in Linear Regression. https://arxiv.org/abs/1906.11300
- Keskar et al. 2017, On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima. https://arxiv.org/abs/1609.04836
- Dinh et al. 2017, Sharp Minima Can Generalize For Deep Nets. https://arxiv.org/abs/1703.04933
- Foret et al. 2021, Sharpness-Aware Minimization for Efficiently Improving Generalization. https://arxiv.org/abs/2010.01412
- Cohen et al. 2021, Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability. https://arxiv.org/abs/2103.00065
- Frankle & Carbin 2019, The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks. https://arxiv.org/abs/1803.03635
- Frankle et al. 2020, Linear Mode Connectivity and the Lottery Ticket Hypothesis. https://arxiv.org/abs/1912.05671
- Power et al. 2022, Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets. https://arxiv.org/abs/2201.02177

## Session 4: Vision transformers and the modern ConvNet

**Goal:** students can explain how a vision transformer turns an image into tokens, why it needed lots of data or a strong training recipe, what Swin and ConvNeXt changed, and can train a tiny ViT and a small CNN on the same small images.

### Talking pointers

- **Open with:** "In 2020 a transformer with almost no knowledge of images matched the best CNNs. Two years later a CNN with a modern recipe matched the transformers again. Today we find out what really made the difference."
- **Segment 1, say:** cut a picture into a 4 × 4 grid on screen and line the pieces up as a sentence of tokens.
- **Segment 2, say:** show two images blended by mixup next to their blended label, then the DeiT recipe as a checklist.
- **Segment 3, say:** walk through ConvNeXt's steps from ResNet-50 as a staircase of accuracies.
- **Close with:** "Architecture, recipe and data scale come as a package. Change one and you must re-check the others." Then set assignment 4.

### Segment 1 (7 min): the vision transformer

- A vision transformer (ViT) cuts the image into fixed-size patches, flattens each patch and maps it to a vector with one shared linear layer (Dosovitskiy et al. 2021).
- A learned class token is put in front and learned position embeddings are added; a standard transformer encoder follows (Course 4 session 1, Course 1 session 6), and a linear head reads the class token.
- A ViT lacks two built-in assumptions (inductive biases) of CNNs: locality, meaning nearby pixels belong together, and translation equivariance, meaning the same detector works everywhere. It must learn them from data.
- Trained on ImageNet-1k alone without strong regularization, ViTs were a few points below comparable ResNets. Pre-trained on ImageNet-21k (14M images) or JFT-300M, they matched or beat the best CNNs at lower training cost (Dosovitskiy et al. 2021).
- **Pause and try:** a 224 × 224 image with 16 × 16 patches: how many tokens? If you halve the patch size, by how much does attention cost grow?
  - **Answer:** (224/16)² = 196 patches plus 1 class token = 197 tokens. Halving the patch size gives 4 times the tokens, and attention cost grows with the square of the token count, so 16 times.

### Segment 2 (6 min): the training recipe

- DeiT trained ViTs competitively on ImageNet-1k alone, on one machine in under three days; its 86M-parameter model reached 83.1% top-1 (Touvron et al. 2021). The key was the recipe, not the architecture.
- RandAugment applies N random image operations at magnitude M, with only those two numbers to tune (Cubuk et al. 2020).
- Mixup trains on blends λx₁ + (1 − λ)x₂ with the same blend of labels (Zhang et al. 2018). CutMix pastes a rectangle of one image into another and mixes the labels by area (Yun et al. 2019).
- Label smoothing replaces the one-hot target with 1 − ε on the true class and ε/K on all K classes (Szegedy et al. 2016). It improves calibration but can make a model a worse teacher for distillation (Müller et al. 2019).
- Stochastic depth randomly skips whole residual blocks during training (Huang et al. 2016).
- "How to train your ViT" found that augmentation and regularization, with enough compute, can be worth about ten times more data (Steiner et al. 2022).
- **Pause and try:** mixup with λ = 0.7 blends a cat image and a dog image. What is the training target?
  - **Answer:** 0.7 cat and 0.3 dog, the same blend as the images.

### Segment 3 (7 min): the ConvNet strikes back

- Swin computes attention inside local windows and shifts the windows between layers so information crosses window borders. It also builds a hierarchy of resolutions like a CNN, which suits detection and segmentation (Liu et al. 2021).
- MLP-Mixer uses no attention at all: one MLP mixes information across patches, another across channels. With large-scale pre-training it was competitive (Tolstikhin et al. 2021).
- ConvNeXt modernized ResNet-50 step by step. The training recipe alone raised it from 76.1% to 78.8%; then came a patchify stem, depthwise 7 × 7 convolutions, inverted bottlenecks and LayerNorm. It matched or beat Swin, reaching 87.8% top-1 with ImageNet-22k pre-training (Liu et al. 2022).
- Lesson: recipe and scale matter as much as the block. ViT encoders now sit inside CLIP and vision-language models (Course 4 session 9).
- **Pause and try:** Swin's first stage has 56 × 56 tokens and 7 × 7 windows. How many tokens does each token attend to, compared with global attention?
  - **Answer:** 49 instead of 3,136, which is 64 times fewer, so the cost grows linearly with image area instead of quadratically.

### Lab guide (about 2 hours, notebook `s04_vision_transformers.ipynb`)

1. Section 1 (10 min): generate the shapes and look at the examples.
2. Sections 2–3 (25 min): read the ViT and CNN code; check that the parameter counts match.
3. Section 4 (30 min): train both models at 500 and 5,000 images.
4. Section 5 (15 min): add mixup and label smoothing to the ViT.
5. Section 6 (15 min): attention maps of the class token.
6. TODO cells (25 min).

- **Expect:** 136,516 parameters (ViT) against 135,460 (CNN). Test accuracy at 500 images: CNN 0.961, ViT 0.640, both with training accuracy 1.000. At 5,000 images: CNN 0.992, ViT 0.846 (training accuracy 0.937, still underfitting). Mixup with label smoothing moves the ViT at 500 images from 0.640 to 0.651, too small to separate from seed noise. In the attention maps one square is predicted as a disc. Runtime about 1.5 minutes.
- **Common problems:** comparing models with different parameter counts or step budgets; judging the recipe from one seed; reading attention maps as explanations.

### Quiz

1. Why does a ViT need more data than a CNN of the same size?
   - **Answer:** it does not have locality and translation equivariance built in, so it must learn them from examples; with little data it overfits.
2. What did DeiT change to train ViTs on ImageNet-1k alone?
   - **Answer:** the training recipe: strong augmentation (RandAugment, mixup, CutMix), label smoothing, stochastic depth and long training, plus distillation from a CNN teacher.
3. What is the main lesson of ConvNeXt?
   - **Answer:** much of the gap between ViTs and CNNs came from the training recipe and design details, not from attention itself.

**Watch out:** "Transformers beat CNNs because attention is simply better." ConvNeXt matched Swin without attention, and in our lab the CNN won clearly at both data sizes. ViTs shine with large data and long training, and with pre-training that transfers widely.

### Assignment 4 (due before session 5, 10 points)

1. Repeat the ViT runs at 500 and 5,000 images with and without mixup and label smoothing, three seeds each. Report the mean and standard deviation, and say whether the recipe helps beyond the noise. (3 points)
2. Train the ViT with patch sizes 2, 4 and 8. Report accuracy, number of tokens and time per step, and relate the time to the token count. (4 points)
3. Make the CNN more like ConvNeXt (for example a 7 × 7 depthwise convolution, LayerNorm and an inverted bottleneck), keeping the parameter count close. Report what changed. (3 points)

Hand in one PDF and your notebook.

### Sources

- Dosovitskiy et al. 2021, An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. https://arxiv.org/abs/2010.11929
- Touvron et al. 2021, Training Data-Efficient Image Transformers & Distillation through Attention. https://arxiv.org/abs/2012.12877
- Cubuk et al. 2020, RandAugment: Practical Automated Data Augmentation with a Reduced Search Space. https://arxiv.org/abs/1909.13719
- Zhang et al. 2018, mixup: Beyond Empirical Risk Minimization. https://arxiv.org/abs/1710.09412
- Yun et al. 2019, CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features. https://arxiv.org/abs/1905.04899
- Szegedy et al. 2016, Rethinking the Inception Architecture for Computer Vision. https://arxiv.org/abs/1512.00567
- Müller et al. 2019, When Does Label Smoothing Help? https://arxiv.org/abs/1906.02629
- Huang et al. 2016, Deep Networks with Stochastic Depth. https://arxiv.org/abs/1603.09382
- Steiner et al. 2022, How to Train Your ViT? Data, Augmentation, and Regularization in Vision Transformers. https://arxiv.org/abs/2106.10270
- Liu et al. 2021, Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. https://arxiv.org/abs/2103.14030
- Tolstikhin et al. 2021, MLP-Mixer: An All-MLP Architecture for Vision. https://arxiv.org/abs/2105.01601
- Liu et al. 2022, A ConvNet for the 2020s. https://arxiv.org/abs/2201.03545

## Session 5: Self-supervised learning

**Goal:** students can explain how networks learn representations without labels (contrastive learning, self-distillation and masked prediction), recognize representation collapse, and evaluate features with a linear probe.

### Talking pointers

- **Open with:** "Labels are expensive and images are cheap. What if the data could label itself? Most strong vision encoders today were trained this way."
- **Segment 1, say:** show two augmented views of the same digit and ask "what should stay the same between them?"
- **Segment 2, say:** show the SimSiam collapse plot: the loss looks perfect while the outputs become identical.
- **Segment 3, say:** show the MAE row of 25%-visible digits next to the reconstructions.
- **Close with:** "A low self-supervised loss proves nothing. Always check the features with a probe." Then set assignment 5.

### Segment 1 (7 min): contrastive learning

- Self-supervised learning creates a training signal from the data itself. An early example, RotNet, rotates an image by 0, 90, 180 or 270 degrees and trains the network to predict the rotation (Gidaris et al. 2018).
- Contrastive learning pulls together two views of the same image and pushes apart views of different images. The InfoNCE loss is a cross-entropy that picks the positive among many negatives; it is linked to a lower bound on mutual information (van den Oord et al. 2018).
- SimCLR showed three ingredients matter: strong augmentations (crops and colour changes), a projection head that is discarded after training, and many negatives, hence large batches (Chen et al. 2020). A temperature τ scales the similarities.
- MoCo keeps negatives in a queue, encoded by a slowly updated momentum copy of the encoder, so the number of negatives does not depend on the batch size (He et al. 2020).
- **Pause and try:** SimCLR with a batch of 256 images. How many negatives does each view have, and what is the loss of a model that guesses at random?
  - **Answer:** 2 × 256 − 2 = 510 negatives; with one positive that is 511 candidates, so the loss is about log 511 ≈ 6.24.

### Segment 2 (7 min): learning without negatives

- BYOL trains an online network to predict a target network's output for another view; the target is a slow moving average of the online network, and no negatives are used (Grill et al. 2020).
- SimSiam removes the moving average too: two identical branches, a predictor, and a stop-gradient on the target branch. The stop-gradient is what prevents collapse (Chen & He 2021).
- Redundancy reduction is another route. Barlow Twins pushes the cross-correlation matrix between two views' embeddings towards the identity (Zbontar et al. 2021). VICReg keeps each dimension's variance up, matches the views, and decorrelates dimensions (Bardes et al. 2022).
- DINO is self-distillation: a student matches a momentum teacher's softmax output over views. Centering and sharpening the teacher's output prevent collapse, and its ViT attention maps outline objects (Caron et al. 2021).
- Collapse comes in two kinds: complete (all outputs identical) and dimensional (outputs use only a few dimensions). Contrastive methods can suffer the second (Jing et al. 2022).
- **Pause and try:** remove SimSiam's stop-gradient. What happens?
  - **Answer:** the outputs collapse towards a constant, which gives the perfect loss of −1 for every image. In the notebook the spread of the outputs falls from 0.105 to 0.010.

### Segment 3 (6 min): masked prediction

- BEiT masks image patches and predicts discrete visual tokens for them, much like BERT predicts masked words (Bao et al. 2022).
- MAE masks 75% of the patches at random, encodes only the visible 25%, and a small decoder reconstructs the pixels. Skipping masked patches in the encoder makes training three or more times faster (He et al. 2022).
- I-JEPA predicts the representations of hidden blocks, not their pixels, so the model does not spend effort on unpredictable detail (Assran et al. 2023).
- DINOv2 showed that with careful data curation and scale, frozen self-supervised features work across many tasks without fine-tuning (Oquab et al. 2024).
- Evaluation: a linear probe trains only a linear classifier on frozen features; fine-tuning trains everything. MAE does better with fine-tuning than with a linear probe. CLIP learns from image-text pairs instead (Course 4 session 9).
- **Pause and try:** MAE on a 224 × 224 image with 16 × 16 patches and 75% masking. How many patches does the encoder process?
  - **Answer:** 196 patches × 25% = 49.

### Lab guide (about 2 hours, notebook `s05_self_supervised_learning.ipynb`)

1. Section 1 (10 min): look at pairs of augmented views.
2. Section 2 (15 min): the baselines with 10% and 100% of labels.
3. Section 3 (25 min): SimCLR and its InfoNCE loss.
4. Section 4 (25 min): SimSiam with and without stop-gradient.
5. Section 5 (25 min): the tiny MAE and its reconstructions.
6. Sections 6–7 and TODO cells (20 min).

- **Expect:** linear probes with 134 labels: raw pixels 0.893, random encoder 0.862; supervised encoder 0.927 (10% of labels) and 0.978 (all labels). SimCLR probe 0.933 (final loss 3.156, against 6.236 at chance). SimSiam with stop-gradient: output spread 0.110, probe on the encoder 0.918; without: loss −0.997, spread 0.010, probe on the outputs 0.684 and on the encoder 0.902. MAE reconstruction loss 0.0527 and probe 0.787. Runtime under 1 minute.
- **Common problems:** probing the projection head's output instead of the encoder's; forgetting `model.eval()` before extracting features (BatchNorm); reading a falling loss as success when the outputs have collapsed.

### Quiz

1. What is SimCLR's projection head for, and why is it thrown away?
   - **Answer:** the contrastive loss is applied after it, so the head can discard information the loss does not need, such as augmentation details; the encoder's representation before the head keeps more general information.
2. Why does SimSiam not collapse, although it has no negatives?
   - **Answer:** the stop-gradient (with the predictor) stops the trivial constant solution from being reached; without it, the network collapses.
3. What does a linear probe measure?
   - **Answer:** how much label information can be read from frozen features with a linear classifier; it can underrate features, such as MAE's, that work best after fine-tuning.

**Watch out:** "Self-supervised features are always worse than supervised ones." At scale, DINOv2's frozen features match or beat supervised ones for transfer. In our tiny lab, SimCLR only tied a supervised model trained on the same 134 labels (0.933 against 0.927), the other methods scored lower, and nothing came close to supervised training with all labels (0.978). Both statements are true at their own scale.

### Assignment 5 (due before session 6, 10 points)

1. Sweep SimCLR's temperature (0.05, 0.1, 0.2, 0.5, 1.0) with three seeds and plot the probe accuracy. (3 points)
2. Complete the Barlow Twins TODO and compare it with SimCLR and SimSiam using probes with 1%, 10% and 100% of the labels. (4 points)
3. Fine-tune the MAE encoder with the 134 labels and compare with its linear probe. Does fine-tuning change the ranking of methods? (3 points)

Hand in one PDF and your notebook.

### Sources

- Gidaris et al. 2018, Unsupervised Representation Learning by Predicting Image Rotations. https://arxiv.org/abs/1803.07728
- van den Oord et al. 2018, Representation Learning with Contrastive Predictive Coding. https://arxiv.org/abs/1807.03748
- Chen et al. 2020, A Simple Framework for Contrastive Learning of Visual Representations. https://arxiv.org/abs/2002.05709
- He et al. 2020, Momentum Contrast for Unsupervised Visual Representation Learning. https://arxiv.org/abs/1911.05722
- Grill et al. 2020, Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning. https://arxiv.org/abs/2006.07733
- Chen & He 2021, Exploring Simple Siamese Representation Learning. https://arxiv.org/abs/2011.10566
- Zbontar et al. 2021, Barlow Twins: Self-Supervised Learning via Redundancy Reduction. https://arxiv.org/abs/2103.03230
- Bardes et al. 2022, VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning. https://arxiv.org/abs/2105.04906
- Caron et al. 2021, Emerging Properties in Self-Supervised Vision Transformers. https://arxiv.org/abs/2104.14294
- Jing et al. 2022, Understanding Dimensional Collapse in Contrastive Self-supervised Learning. https://arxiv.org/abs/2110.09348
- Bao et al. 2022, BEiT: BERT Pre-Training of Image Transformers. https://arxiv.org/abs/2106.08254
- He et al. 2022, Masked Autoencoders Are Scalable Vision Learners. https://arxiv.org/abs/2111.06377
- Assran et al. 2023, Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture. https://arxiv.org/abs/2301.08243
- Oquab et al. 2024, DINOv2: Learning Robust Visual Features without Supervision. https://arxiv.org/abs/2304.07193

## Session 6: In-context learning and learning to learn

**Goal:** students can explain meta-learning, how MAML and prototypical networks solve few-shot tasks, and what research shows about how transformers learn in context, and can train a tiny transformer to do in-context linear regression.

### Talking pointers

- **Open with:** "Show a child three photos of an animal they have never seen, and they will recognize the fourth. Today we look at three ways to build models that learn from a handful of examples, one of which never changes its weights at all."
- **Segment 1, say:** draw a 5-way 1-shot episode on screen: five support images in a row and one query image below.
- **Segment 2, say:** show a prompt of (x, y) pairs with the answer missing, then the notebook's error curves for the transformer and least squares.
- **Segment 3, say:** write "[A][B] … [A] → ?" on screen and let students predict the next token.
- **Close with:** "In-context learning is not magic and not fine-tuning. It is an algorithm the forward pass runs, and we are only starting to know which one." Then set assignment 6.

### Segment 1 (7 min): learning to learn

- Few-shot learning is tested with N-way K-shot episodes: N new classes, K labeled examples each (the support set), and query examples to classify. Training uses many such episodes built from other classes.
- Matching networks classify a query by attention over the embedded support examples, and are trained on episodes that match the test conditions (Vinyals et al. 2016).
- Prototypical networks average each class's support embeddings into a prototype and classify by squared distance to the prototypes (Snell et al. 2017).
- MAML learns an initialization from which a few gradient steps on a new task give a good model (Finn et al. 2017). Its first-order version drops second derivatives; Reptile simply moves the initialization towards the weights adapted on each task (Nichol et al. 2018).
- Meta-learning needs many diverse training tasks. In the notebook, a prototypical network trained on 80 glyph classes transfers to new ones, but one trained on only 5 digit classes does worse than raw pixels.
- **Pause and try:** a 5-way 1-shot episode. How many labeled support examples does the model get?
  - **Answer:** 5, one for each of the five classes.

### Segment 2 (6 min): in-context learning appears

- GPT-3 (175 billion parameters) could do new tasks from a few demonstrations in its prompt, with no weight updates: in-context learning (Brown et al. 2020).
- Garg et al. (2022) trained transformers from scratch on prompts (x₁, y₁, …, x_q) where y = w·x and every prompt has a new w. The trained models matched least squares closely and handled other function classes too.
- Which training data makes in-context learning appear? Chan et al. (2022) found that "bursty" data, where items appear in clusters, and many rare classes favour it; otherwise models store the knowledge in their weights instead.
- Task diversity matters: with too few distinct regression tasks in pre-training, a transformer only recognizes the tasks it has seen; above a threshold, it solves new tasks like ridge regression (Raventós et al. 2023).
- **Pause and try:** y = w·x in 20 dimensions with no noise. How many in-context examples does least squares need to find w exactly?
  - **Answer:** 20, one equation per unknown. In the notebook (dimension 4), least squares becomes exact at k = 4.

### Segment 3 (7 min): mechanisms

- Induction heads are attention heads that find an earlier occurrence of the current token and copy what followed it: [A][B] … [A] → [B]. They form in a sudden phase change early in training, at the same time as in-context learning improves (Olsson et al. 2022). Their evidence is causal in small attention-only models and mostly correlational in large ones.
- A single layer of linear self-attention can implement one step of gradient descent on a regression loss, and trained models can come close to such constructions (von Oswald et al. 2023).
- Transformers can also implement ridge regression exactly, and trained models move between gradient-descent-like and least-squares-like behaviour as depth and noise change (Akyürek et al. 2023).
- Limits: these results use linear regression with special token formats; how large language models learn in context from text is still mostly open.
- **Pause and try:** why call it "learning" if no weights change?
  - **Answer:** the forward pass runs an algorithm on the examples in the context, and its predictions improve as more examples arrive.

### Lab guide (about 2 hours, notebook `s06_in_context_learning.ipynb`)

1. Section 2 (30 min): prototypical networks on glyphs (80 training classes) and on digits (5 training classes).
2. Section 3 (30 min): first-order MAML on sine waves against a pre-trained network.
3. Section 4 (40 min): train the in-context regressor and compare it with three baselines.
4. TODO cells (20 min), including Reptile.

- **Expect:** glyphs, 5-way accuracy on unseen classes: raw pixels 0.216 (1-shot) and 0.234 (5-shot), untrained CNN 0.268 and 0.309, prototypical network 0.586 and 0.730. Digits: raw pixels 0.656 and 0.848, prototypical network only 0.532 and 0.694. Sine MSE after 0, 1 and 10 steps: first-order MAML 3.450, 1.473, 0.595; pre-trained 2.931, 2.428, 1.520. In-context regression (normalized error at k = 2, 4, 11): transformer 0.510, 0.186, 0.026; least squares 0.489, 0.000, 0.000; one gradient step 0.721, 0.533, 0.295. Runtime about 1.5 minutes.
- **Common problems:** testing on classes that were also used in training; calling an adaptation function inside `torch.no_grad()`; reading the in-context prediction at the wrong token (it is the x-token of the query).

### Quiz

1. What does MAML optimize, and why can its starting model look worse than a pre-trained one?
   - **Answer:** the loss after a few adaptation steps, not the loss of the starting weights; so its initialization is built for fast adaptation, not for direct prediction (MSE 3.450 against 2.931 before adaptation in the notebook).
2. How does a prototypical network classify a query?
   - **Answer:** it embeds the support examples, averages them per class into prototypes, and assigns the query to the nearest prototype in squared Euclidean distance.
3. What is an induction head?
   - **Answer:** an attention head that finds where the current token appeared before and copies the token that followed it.

**Watch out:** "In-context learning means the model fine-tunes itself on the prompt." No weights change: the same frozen network gives better predictions when the prompt holds more examples. The "gradient descent in the forward pass" picture is exact only for special cases such as linear self-attention on regression tokens, so do not assume large language models literally run gradient descent.

### Assignment 6 (due before session 7, 10 points)

1. Train prototypical networks on 5, 10, 20, 40 and 80 glyph classes and plot the 5-shot accuracy on the 20 held-out classes. Connect the curve to task diversity. (3 points)
2. Add Gaussian noise (standard deviation 0.5) to y in section 4, retrain, and compare the transformer with least squares and ridge regression. Which does it resemble? (4 points)
3. Complete the Reptile TODO and compare it with first-order MAML after 1 and 10 adaptation steps, with three seeds. (3 points)

Hand in one PDF and your notebook.

### Sources

- Vinyals et al. 2016, Matching Networks for One Shot Learning. https://arxiv.org/abs/1606.04080
- Finn et al. 2017, Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks. https://arxiv.org/abs/1703.03400
- Nichol et al. 2018, On First-Order Meta-Learning Algorithms. https://arxiv.org/abs/1803.02999
- Snell et al. 2017, Prototypical Networks for Few-shot Learning. https://arxiv.org/abs/1703.05175
- Brown et al. 2020, Language Models are Few-Shot Learners. https://arxiv.org/abs/2005.14165
- Garg et al. 2022, What Can Transformers Learn In-Context? A Case Study of Simple Function Classes. https://arxiv.org/abs/2208.01066
- Chan et al. 2022, Data Distributional Properties Drive Emergent In-Context Learning in Transformers. https://arxiv.org/abs/2205.05055
- Raventós et al. 2023, Pretraining Task Diversity and the Emergence of Non-Bayesian In-Context Learning for Regression. https://arxiv.org/abs/2306.15063
- Olsson et al. 2022, In-context Learning and Induction Heads. https://arxiv.org/abs/2209.11895
- von Oswald et al. 2023, Transformers Learn In-Context by Gradient Descent. https://arxiv.org/abs/2212.07677
- Akyürek et al. 2023, What Learning Algorithm is In-Context Learning? Investigations with Linear Models. https://arxiv.org/abs/2211.15661

## Session 7: Generative models before diffusion: VAEs, VQ-VAE, flows and GANs

**Goal:** students can explain latent-variable models and the ELBO, discrete latents (VQ-VAE) that became today's image and audio tokenizers, invertible flows with exact likelihood, GANs and their failure modes, and how generative models are evaluated.

### Talking pointers

- **Open with:** "Inside many modern image generators are older ideas: an autoencoder, a codebook of tokens, an adversarial loss. Today we meet them."
- **Segment 1, say:** write the ELBO as "reconstruct well" minus "stay close to the prior".
- **Segment 2, say:** compute a 2×2 triangular Jacobian's determinant on screen.
- **Segment 3, say:** the GAN as a game; then the lab table where a Gaussian blob beats both GANs on Fréchet distance.
- **Close with:** "Every generative model trades quality, diversity, speed and likelihood, so never trust a single number." Then set assignment 7.

### Segment 1 (7 min): VAEs and VQ-VAE

- A latent-variable model draws z from a prior p(z) = N(0, I), then x from a decoder p(x | z); p(x) = ∫ p(x | z) p(z) dz has no closed form.
- The variational autoencoder (VAE) adds an encoder q(z | x) and maximizes the evidence lower bound (ELBO): $\log p(x) \ge \mathbb{E}_q[\log p(x \mid z)] - \mathrm{KL}(q(z \mid x) \,\|\, p(z))$ (Kingma & Welling 2014), where KL is the Kullback–Leibler divergence. The gap is KL(q(z | x) ‖ p(z | x)). The reparameterization trick, z = μ(x) + σ(x)·ε with ε ~ N(0, I), lets gradients pass through the sampling.
- Weaknesses: blurry samples (the decoder predicts an average image) and posterior collapse (a strong decoder ignores z). β-VAE weights the KL term by β > 1 for more disentangled factors but worse reconstructions (Higgins et al. 2017).
- VQ-VAE (vector-quantized VAE) replaces the encoder's output with its nearest codebook vector, so an image becomes a grid of integers (van den Oord et al. 2017). Loss: reconstruction + ‖sg[z_e] − e‖² + β‖z_e − sg[e]‖², with sg the stop-gradient and β = 0.25. The paper applied it to speech as well as images.
- VQ-VAE-2 added a hierarchy of codes (Razavi et al. 2019); VQGAN added adversarial and perceptual losses and a transformer over the tokens (Esser et al. 2021). Images became token sequences, and latent diffusion (session 8) works in a similar compressed space.
- **Pause and try:** why can't you backpropagate through the nearest-codebook lookup?
  - **Answer:** it returns an integer that does not change when z_e moves slightly, so its gradient is zero almost everywhere. The straight-through estimator copies the decoder's gradient from z_q to z_e.

### Segment 2 (6 min): normalizing flows

- A flow is an invertible network z = f(x) with z ~ N(0, I). By the change of variables, $\log p(x) = \log N(f(x); 0, I) + \log |\det \partial f/\partial x|$: an exact likelihood. Sampling runs f⁻¹ on noise.
- A general determinant costs O(d³). A coupling layer keeps half the input and transforms the rest: y_b = x_b ⊙ exp(s(x_a)) + t(x_a) (RealNVP, Dinh et al. 2017). The Jacobian is triangular, so log|det J| = Σ s(x_a), and inverting is easy.
- Glow added invertible 1×1 convolutions (Kingma & Dhariwal 2018). But invertible layers must keep the dimension, so flows need many layers, and their samples fell behind GANs.
- A neural ODE (ordinary differential equation) dx/dt = v(x, t) is a continuous flow whose log-density changes at the rate −Tr(∂v/∂x) (Chen et al. 2018). Training it by solving the ODE is slow; flow matching (session 9) avoids that.
- **Pause and try:** a coupling layer keeps x₁ and maps x₂ to 3x₂ + x₁. What is log|det J|?
  - **Answer:** log 3 ≈ 1.10. The Jacobian [[1, 0], [1, 3]] is triangular, so its determinant is 1 × 3.

### Segment 3 (7 min): GANs and evaluation

- A generative adversarial network (GAN) plays min_G max_D E[log D(x)] + E[log(1 − D(G(z)))] (Goodfellow et al. 2014). Against the best discriminator, the generator minimizes the Jensen–Shannon divergence; in practice G maximizes log D(G(z)) for stronger early gradients.
- Fixes: the deep convolutional GAN, DCGAN (Radford et al. 2016); the Wasserstein GAN, whose critic still gives useful gradients when well trained (Arjovsky et al. 2017), and its gradient-penalty version (Gulrajani et al. 2017); StyleGAN (Karras et al. 2019).
- Mode collapse: the generator covers only part of the data, which a discriminator judging one sample at a time cannot see; minibatch discrimination compares samples (Salimans et al. 2016).
- Evaluation: the Inception Score uses a classifier's predictions (Salimans et al. 2016). The Fréchet Inception Distance (FID) compares Gaussians fitted to Inception features: ‖μ_r − μ_g‖² + Tr(Σ_r + Σ_g − 2(Σ_r Σ_g)^{1/2}) (Heusel et al. 2017). Precision (realistic samples?) and recall (variety covered?) separate what FID mixes (Kynkäänniemi et al. 2019).
- **Pause and try:** a GAN always outputs the same perfect image. Precision? Recall?
  - **Answer:** high precision, because the image is realistic, and near-zero recall, because it covers one point. In the lab, points from one mode only score 0.97 and 0.12.

### Lab guide (about 3 hours, notebook `s07_generative_models_before_diffusion.ipynb`)

1. VAE (40 min): the ELBO against the importance-sampled −log p(x); the latent map.
2. VQ-VAE (30 min): one digit as 16 tokens; reconstructions and code usage.
3. Coupling flow (30 min): likelihood against one Gaussian; both checks.
4. GANs (40 min): vanilla GAN and WGAN-GP, three seeds each, with the discriminator learning four times faster; mode counts during training.
5. Metrics and exercises (40 min): the metrics table, the sample-size check, the TODO cells.

- **Expect:** VAE negative ELBO 20.20 nats per image against −log p(x) ≈ 19.51; VQ-VAE mean squared error 0.0069, all 32 codes used (perplexity 26.3); flow −1.226 nats per point against −2.732 for one Gaussian. Vanilla GAN: 4 of 8 modes in every seed, about 60% of points near a mode; WGAN-GP: 7, 8 and 8 modes, 31–40% near a mode. A Gaussian blob scores Fréchet distance 0.004, better than the GANs (0.010, 0.006), with precision 0.00. Runtime about 100 seconds.
- **Common problems:** feeding z_q to the decoder without the straight-through line, so the encoder learns nothing from reconstruction; comparing Fréchet distances from different sample sizes (two real samples give 0.2123 at 50 points, 0.0017 at 5,000); judging a GAN from one seed.

### Quiz

1. Write the ELBO. What does its gap to log p(x) measure?
   - **Answer:** E_q[log p(x | z)] − KL(q(z | x) ‖ p(z)); the gap is KL(q(z | x) ‖ p(z | x)), the encoder's distance from the true posterior.
2. Why is a coupling layer's log-determinant cheap?
   - **Answer:** half the input is unchanged, so the Jacobian is triangular and log|det J| is the sum of the log-scales.
3. The lab's vanilla GAN covered 4 of 8 modes yet scored recall 0.91. Why?
   - **Answer:** recall uses a ball around each generated point; scattered points between modes get large balls that cover the missing modes, so the measure is sensitive to outliers.

**Watch out:** "A lower FID always means better images." FID depends on sample size, feature network and preprocessing, and folds fidelity and diversity into one number; in the lab, a blob that looks nothing like the data beat both GANs. Compare FIDs only under equal settings, with precision, recall and samples beside them.

### Assignment 7 (due before session 8, 10 points)

1. β-VAE: train with β = 0.5, 1 and 4; report reconstruction and KL terms, show the three decoded grids, and explain the trade-off in two sentences. (3 points)
2. Codebook size: train the VQ-VAE with K = 8, 32 and 256; report test MSE, codes used and perplexity, and say when dead codes appear. (3 points)
3. GAN balance: complete the balance TODO (equal learning rates, three seeds), compare modes, precision and recall with the notebook's run, and explain the difference. (4 points)

Hand in one PDF and your notebook.

### Sources

- Kingma & Welling 2014, Auto-Encoding Variational Bayes. https://arxiv.org/abs/1312.6114
- Higgins et al. 2017, β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. https://openreview.net/forum?id=Sy2fzU9gl
- van den Oord et al. 2017, Neural Discrete Representation Learning. https://arxiv.org/abs/1711.00937
- Razavi et al. 2019, Generating Diverse High-Fidelity Images with VQ-VAE-2. https://arxiv.org/abs/1906.00446
- Esser et al. 2021, Taming Transformers for High-Resolution Image Synthesis. https://arxiv.org/abs/2012.09841
- Dinh et al. 2017, Density Estimation Using Real NVP. https://arxiv.org/abs/1605.08803
- Kingma & Dhariwal 2018, Glow: Generative Flow with Invertible 1x1 Convolutions. https://arxiv.org/abs/1807.03039
- Chen et al. 2018, Neural Ordinary Differential Equations. https://arxiv.org/abs/1806.07366
- Goodfellow et al. 2014, Generative Adversarial Networks. https://arxiv.org/abs/1406.2661
- Radford et al. 2016, Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks. https://arxiv.org/abs/1511.06434
- Arjovsky et al. 2017, Wasserstein GAN. https://arxiv.org/abs/1701.07875
- Gulrajani et al. 2017, Improved Training of Wasserstein GANs. https://arxiv.org/abs/1704.00028
- Karras et al. 2019, A Style-Based Generator Architecture for Generative Adversarial Networks. https://arxiv.org/abs/1812.04948
- Salimans et al. 2016, Improved Techniques for Training GANs. https://arxiv.org/abs/1606.03498
- Heusel et al. 2017, GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium. https://arxiv.org/abs/1706.08500
- Kynkäänniemi et al. 2019, Improved Precision and Recall Metric for Assessing Generative Models. https://arxiv.org/abs/1904.06991

## Session 8: Diffusion models

**Goal:** students can explain the forward noising process and the denoising objective, the link to score matching, how DDPM and DDIM sample, classifier-free guidance and latent diffusion, and can train a diffusion model on 2-D data.

### Talking pointers

- **Open with:** "Destroying data is easy: add noise until nothing is left. A diffusion model learns to undo that one small step at a time, and that is enough to generate images, audio and video."
- **Segment 1, say:** show the lab's forward-process figure, a spiral dissolving into noise, and derive the one-line formula for x_t.
- **Segment 2, say:** the noise predictor is secretly a score estimate. Show the single sampling function in which η = 1 is DDPM and η = 0 is DDIM.
- **Segment 3, say:** guidance turns up the volume of the condition. Show the four guidance panels and ask what went wrong at scale 7.
- **Close with:** "A diffusion model is a denoiser plus a sampler, and much of the decade's progress came from choosing those two well." Then set assignment 8.

### Segment 1 (7 min): DDPM

- The forward process adds a little Gaussian noise at each of T steps: q(x_t | x_{t−1}) = N(√(1 − β_t) x_{t−1}, β_t I). With α_t = 1 − β_t and ᾱ_t = α_1 α_2 ⋯ α_t, it has a closed form: $x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1 - \bar\alpha_t}\,\varepsilon$, so training can jump to any t without simulating the chain.
- Sohl-Dickstein et al. 2015 proposed learning to reverse such a process. Ho et al. 2020 (denoising diffusion probabilistic models, DDPM) made it work for images by training a network to predict the added noise, $L = \mathbb{E}\,\|\varepsilon - \varepsilon_\theta(x_t, t)\|^2$, a reweighted form of the ELBO, and reached a Fréchet Inception Distance (FID) of 3.17 on CIFAR-10.
- Sampling starts from pure noise x_T ~ N(0, I) and removes the predicted noise step by step, adding a little fresh noise each time, for all T steps.
- Schedules: Ho et al. used β rising linearly from 0.0001 to 0.02 over T = 1,000 steps. The cosine schedule destroys information more evenly, and learning the variances let models sample with far fewer steps (Nichol & Dhariwal 2021).
- **Pause and try:** at some t, ᾱ_t = 0.25. What multiplies x_0, and what multiplies the noise?
  - **Answer:** √0.25 = 0.5 multiplies x_0 and √0.75 ≈ 0.87 multiplies ε, so the signal-to-noise ratio ᾱ/(1 − ᾱ) is 1/3.

### Segment 2 (6 min): the score view and faster samplers

- The score is ∇_x log p(x), the direction in which the data density rises fastest. Song & Ermon 2019 trained one network on data perturbed at many noise levels (denoising score matching) and sampled with annealed Langevin dynamics. The two views agree: the best noise predictor is $\varepsilon_\theta(x_t, t) = -\sqrt{1 - \bar\alpha_t}\,\nabla \log p_t(x_t)$.
- Song et al. 2021 described diffusion in continuous time as a stochastic differential equation. Each such equation has a probability-flow ODE (ordinary differential equation) with the same distributions at every time, which gives deterministic sampling and exact likelihoods.
- Denoising diffusion implicit models (DDIM; Song, Meng & Ermon 2021) use a different process with the same marginals q(x_t | x_0), so the same trained network works. Its deterministic update jumps from t to an earlier time s: predict $\hat x_0 = (x_t - \sqrt{1-\bar\alpha_t}\,\hat\varepsilon)/\sqrt{\bar\alpha_t}$, then set $x_s = \sqrt{\bar\alpha_s}\,\hat x_0 + \sqrt{1-\bar\alpha_s}\,\hat\varepsilon$. On images it gave similar quality 10 to 50 times faster than DDPM.
- EDM separated the design choices (noise levels, network scaling, loss weights, sampler) and reached FID 1.79 on class-conditional CIFAR-10 with 35 network evaluations (Karras et al. 2022).
- **Pause and try:** why can DDIM use 50 steps with a model trained with 1,000?
  - **Answer:** training only uses the marginals q(x_t | x_0). DDIM keeps those marginals, and its deterministic update can jump between any two noise levels.

### Segment 3 (7 min): control and scale

- Classifier guidance adds the gradient of a classifier trained on noisy images, scaled up, to the score; it trades diversity for fidelity, and with it diffusion beat GANs on ImageNet (Dhariwal & Nichol 2021).
- Classifier-free guidance trains one network with the condition replaced by a "no condition" token for 10–20% of examples, then mixes its two predictions: $\tilde\varepsilon = \varepsilon(x, \varnothing) + s\,[\varepsilon(x, c) - \varepsilon(x, \varnothing)]$ (Ho & Salimans 2022, who write the same rule with w = s − 1). A larger s follows the condition more closely and gives less variety; too large a value leaves the data.
- Latent diffusion trains an autoencoder that shrinks each image side by a factor such as 8, runs diffusion in that latent space, and feeds text in through cross-attention (Rombach et al. 2022). This is the design of Stable Diffusion; text encoders such as CLIP are in Course 4 s9.
- Related: graph diffusion (Course 7 s9) and masked diffusion language models (Course 4 s10).
- **Pause and try:** guidance scale 0 against 7: what changes?
  - **Answer:** at 0 the model ignores the condition and gives unconditional, varied samples; at 7 it follows the condition strongly, with less variety and often over-saturated results. In the lab, class confidence rose from 0.317 to 0.996, but 30.6% of samples at scale 7 lay off the data.

### Lab guide (about 3 hours, notebook `s08_diffusion_models.ipynb`)

1. Data and distance (15 min): note the noise floor, the sliced Wasserstein distance (SWD) between two real samples.
2. Forward process (20 min): read the ᾱ values and the 30-step check of the closed form.
3. Training (20 min): read the noise-prediction loss and train.
4. Sampling (50 min): compare DDPM and DDIM from 100 down to 2 steps; run the DDIM round trip.
5. Guidance (40 min): train the class-conditional model and read the guidance sweep.
6. Exercises (35 min): the cosine-schedule and averaged-guidance TODO cells.

- **Expect:** noise floor 0.046; the closed-form check gives mean 0.007 and standard deviation 1.004. SWD at 100 steps: DDPM 0.063, DDIM 0.070; at 10 steps 0.196 and 0.173; at 2 steps 0.623 and 0.640. So DDIM was not clearly better than DDPM here, unlike the paper's image results. The DDIM round trip returns points with mean error 0.031. Guidance scale 1 matches the data (confidence 0.861 against 0.863, spread 0.98, 1.0% off the data); scale 2 gives 0.993, 0.75 and 2.0%; scale 7 gives 0.996, 2.58 and 30.6%. Runtime about one minute.
- **Common problems:** an off-by-one in t (here abar[0] = 1 is the clean data); passing the integer t instead of t/T to the time features; and a schedule whose ᾱ_T is almost 0, which makes x̂_0 divide small errors by a tiny √ᾱ_T (the cosine-schedule TODO explores this).

### Quiz

1. Write x_t in terms of x_0 and the noise ε.
   - **Answer:** x_t = √ᾱ_t x_0 + √(1 − ᾱ_t) ε.
2. How are the noise predictor and the score related?
   - **Answer:** ε_θ(x_t, t) ≈ −√(1 − ᾱ_t) ∇ log p_t(x_t), so predicting noise is estimating the score.
3. Why is the condition dropped during training in classifier-free guidance?
   - **Answer:** so that one network also learns the unconditional prediction, and both predictions that guidance mixes come from the same model.

**Watch out:** "More sampling steps always give better samples." Extra steps only reduce the sampler's step-size error; they cannot fix the network's own error. In the lab, going from 50 to 100 DDPM steps improved SWD only from 0.074 to 0.063, still above the 0.046 floor. Nor is DDPM's added noise "creativity": DDIM adds none after the start and still gives varied samples, because the variety comes from the starting noise.

### Assignment 8 (due before session 9, 10 points)

1. Steps and quality: plot SWD against steps for DDPM and DDIM with five sampling seeds and error bars. Where does each stop improving? (3 points)
2. Complete the cosine-schedule TODO: report ᾱ_T and DDIM's 20-step SWD for both schedules, and explain the difference with the formula for x̂_0. (4 points)
3. Extend the guidance sweep to scales 0.5–10, plot class confidence and the off-the-data share, and choose a scale for this task with a reason. (3 points)

Hand in one PDF and your notebook.

### Sources

- Sohl-Dickstein et al. 2015, Deep Unsupervised Learning using Nonequilibrium Thermodynamics. https://arxiv.org/abs/1503.03585
- Ho et al. 2020, Denoising Diffusion Probabilistic Models. https://arxiv.org/abs/2006.11239
- Nichol & Dhariwal 2021, Improved Denoising Diffusion Probabilistic Models. https://arxiv.org/abs/2102.09672
- Song & Ermon 2019, Generative Modeling by Estimating Gradients of the Data Distribution. https://arxiv.org/abs/1907.05600
- Song et al. 2021, Score-Based Generative Modeling through Stochastic Differential Equations. https://arxiv.org/abs/2011.13456
- Song, Meng & Ermon 2021, Denoising Diffusion Implicit Models. https://arxiv.org/abs/2010.02502
- Karras et al. 2022, Elucidating the Design Space of Diffusion-Based Generative Models. https://arxiv.org/abs/2206.00364
- Dhariwal & Nichol 2021, Diffusion Models Beat GANs on Image Synthesis. https://arxiv.org/abs/2105.05233
- Ho & Salimans 2022, Classifier-Free Diffusion Guidance. https://arxiv.org/abs/2207.12598
- Rombach et al. 2022, High-Resolution Image Synthesis with Latent Diffusion Models. https://arxiv.org/abs/2112.10752

## Session 9: Flow matching, rectified flow and fast generation

**Goal:** students can explain flow matching as regression onto a velocity field, why straighter paths need fewer steps (rectified flow, consistency models, distillation), and why diffusion transformers replaced U-Nets, and can compare flow matching with diffusion on 2-D data.

### Talking pointers

- **Open with:** "Last session, generating took up to a hundred network calls. If every noise point travelled to its data point in a straight line, how many steps would we need? One."
- **Segment 1, say:** draw a noise point and a data point joined by a straight line; the training method is this picture plus a regression.
- **Segment 2, say:** show the lab's curved and straightened trajectories, then one-step SWD falling from 0.952 to 0.058.
- **Segment 3, say:** the network inside changed too, from U-Nets to transformers on patches. Count the tokens of a 256×256 image together.
- **Close with:** "Straight paths are cheap paths, and most fast samplers are ways of straightening them." Then set assignment 9.

### Segment 1 (7 min): flow matching

- The aim: a velocity field v(x, t) whose ordinary differential equation (ODE) dx/dt = v carries noise (t = 0) to data (t = 1).
- Pick noise x_0 ~ N(0, I), a data point x_1 and a time t between 0 and 1. The point x_t = (1 − t) x_0 + t x_1 moves along a straight line with velocity x_1 − x_0, so train with $L = \mathbb{E}\,\|v_\theta(x_t, t) - (x_1 - x_0)\|^2$. Training needs no ODE solver, only regression (Lipman et al. 2023; Liu et al. 2023, who call it rectified flow; Albergo & Vanden-Eijnden 2023, who call these paths interpolants).
- The best possible v is the average velocity of all pairs passing through x at time t, E[x_1 − x_0 | x_t = x], and following it from noise reproduces the data distribution. Lipman et al. show that the per-pair loss has the same gradients as a loss on this average field, which cannot be computed directly.
- To sample, integrate the ODE, for example with N Euler steps x ← x + v(x, t)/N.
- With Gaussian paths x_t = α_t x_1 + σ_t x_0, the velocity, the noise prediction and the score are linear functions of one another. Diffusion's path is one choice; the straight line is another. Course 7 s9 teaches the version on curved spaces.
- **Pause and try:** on a straight path, what is the regression target at t = 0.3?
  - **Answer:** x_1 − x_0, the same at every t, because the point moves at constant speed.

### Segment 2 (6 min): fewer steps

- Each training pair moves in a straight line, but lines from different pairs cross, and at a crossing the network can only learn their average. So the learned paths curve, and big Euler steps miss. In the lab, one step sends every sample to the data mean.
- Reflow runs the trained model to get pairs (noise, generated point) and trains again on them (Liu et al. 2023). Paths of an ODE never cross, so the new targets agree and the new paths are straighter.
- Minibatch optimal-transport pairing matches noise and data inside each batch to minimize the total squared distance, so pairs cross less from the start (Tong et al. 2024).
- Consistency models learn a function that maps any point on a trajectory directly to its end, allowing one-step sampling, either distilled from a diffusion model or trained alone (Song et al. 2023). Progressive distillation trains a student to do two teacher steps in one, halving repeatedly from thousands of steps down to 4 (Salimans & Ho 2022).
- **Pause and try:** with perfectly straight paths and the exact velocity, how many Euler steps reach the data exactly?
  - **Answer:** one. The velocity is constant along each path, so a single step of size 1 lands on the end point.

### Segment 3 (7 min): architectures at scale

- DiT (Diffusion Transformer) replaces the U-Net with a standard transformer on patches of a latent-diffusion latent (Peebles & Xie 2023). The timestep and class enter through adaptive layer norm: the scale and shift of each LayerNorm are predicted from the conditioning, and each residual block starts as the identity (adaLN-Zero). Quality improved steadily with compute, and DiT-XL/2 reached a Fréchet Inception Distance of 2.27 on class-conditional ImageNet 256×256.
- Stable Diffusion 3 is a rectified-flow transformer with separate weights for text and image tokens, which attend to each other (Esser et al. 2024). It samples t more often in the middle of the path, and the authors scaled it to 8 billion parameters with predictable gains.
- The Flow Matching Guide and Code is a tutorial and an open PyTorch library covering these variants (Lipman et al. 2024).
- As with language models (Course 4 s3), a simple block that scales predictably won.
- **Pause and try:** a 256×256 image, an autoencoder that shrinks each side by 8, and DiT patches of 2×2. How many tokens?
  - **Answer:** the latent is 32×32, so (32/2)² = 256 tokens. With 4×4 patches there are 64, and attention cost falls by about 16 times.

### Lab guide (about 3 hours, notebook `s09_flow_matching.ipynb`)

1. Setup (10 min): session 8's data, distance and noise floor.
2. Flow matching (30 min): the loss; Euler sampling with 1 to 32 steps.
3. DDPM comparison (20 min): session 8's model, sampled with DDIM.
4. Straightness (15 min): the path-length measure.
5. Reflow (25 min): pairs from the first model, then fine-tuning.
6. Minibatch OT (25 min): pairs within blocks of 256.
7. Comparison and exercises (55 min): the table, both plots, the TODO cells.

- **Expect:** noise floor 0.046. Flow matching sliced Wasserstein distance (SWD): 0.952, 0.437, 0.219, 0.118 and 0.063 at 1, 2, 4, 8 and 32 steps; DDPM with DDIM: 6.775, 0.640, 0.484, 0.233 and 0.091. Path length over end-to-end distance: 2.049 for flow matching, 1.001 after one reflow, 1.005 with OT pairs. Reflow gives 0.058 at one step but no better at 32 (0.057). OT pairing cuts the mean squared pair distance from 3.97 to 0.32 and gives 0.060 at one step and 0.049–0.050 from two steps on. Runtime 70 to 80 seconds.
- **Common problems:** mixing up the direction of time (here t = 0 is noise; the Stable Diffusion 3 paper uses the opposite convention); expecting reflow to beat the model that made its pairs; and comparing samplers by steps instead of network evaluations (Heun's method costs two per step).

### Quiz

1. What is the regression target in flow matching with straight paths?
   - **Answer:** the velocity x_1 − x_0 of the pair.
2. Why do the learned paths curve when every training path is straight?
   - **Answer:** paths from different pairs cross, and the network learns their average, which changes direction along the way.
3. What does reflow fix, and what can it not fix?
   - **Answer:** it straightens paths so that one or two steps suffice; it cannot make samples better than those of the model that produced its pairs.

**Watch out:** "Flow matching and diffusion are unrelated families." With Gaussian paths they are close relatives: for the same path, velocity, noise prediction and score are linear transforms of one another, and DDIM is one way to integrate the probability-flow ODE. They differ in the path chosen and in how the loss weights different times. The lab's gap (0.063 against 0.091 at 32 steps) compares two particular setups, not two families.

### Assignment 9 (due before session 10, 10 points)

1. Complete the Heun TODO and compare Heun with Euler at 2, 4, 8 and 16 network evaluations for the first model, in a table with one paragraph of explanation. (3 points)
2. Complete the second-reflow TODO: report straightness and one-step SWD for the 3-rectified flow. Did a second round help? (3 points)
3. Repeat the minibatch-OT experiment with blocks of 16, 64 and 256 points; plot straightness and one-step SWD against block size and explain the trend. (4 points)

Hand in one PDF and your notebook.

### Sources

- Lipman et al. 2023, Flow Matching for Generative Modeling. https://arxiv.org/abs/2210.02747
- Liu et al. 2023, Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow. https://arxiv.org/abs/2209.03003
- Albergo & Vanden-Eijnden 2023, Building Normalizing Flows with Stochastic Interpolants. https://arxiv.org/abs/2209.15571
- Tong et al. 2024, Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport. https://arxiv.org/abs/2302.00482
- Song et al. 2023, Consistency Models. https://arxiv.org/abs/2303.01469
- Salimans & Ho 2022, Progressive Distillation for Fast Sampling of Diffusion Models. https://arxiv.org/abs/2202.00512
- Peebles & Xie 2023, Scalable Diffusion Models with Transformers. https://arxiv.org/abs/2212.09748
- Esser et al. 2024, Scaling Rectified Flow Transformers for High-Resolution Image Synthesis. https://arxiv.org/abs/2403.03206
- Lipman et al. 2024, Flow Matching Guide and Code. https://arxiv.org/abs/2412.06264

## Session 10: Deep reinforcement learning, from AlphaGo to world models

**Goal:** students can explain the decade's deep RL milestones — search with self-play (AlphaGo Zero, AlphaZero), policy optimization (PPO), learned models (MuZero, Dreamer) and offline RL (Decision Transformer) — and implement PPO and Monte Carlo tree search on small problems.

### Talking pointers

- **Open with:** "In 2016 DeepMind reported the first Go program to beat a professional player; a year later its successor learned Go from nothing but the rules. Two engines drove this decade of reinforcement learning: search and policy optimization."
- **Segment 1, say:** draw the four steps of tree search on a small tree, then point at the visit counts: they are the training targets.
- **Segment 2, say:** build PPO from REINFORCE in three moves (add a baseline, reuse data with a ratio, clip the ratio), then show the lab's learning curves without the clip.
- **Segment 3, say:** without trial and error, a learned model lets the agent imagine, and offline RL learns from a fixed log.
- **Close with:** "Search improves a policy, and learning makes search cheaper. Most of the decade's successes combine the two." Then set assignment 10.

### Segment 1 (7 min): search plus learning

- AlphaGo combined three parts: a policy network trained on human expert games and then by self-play, a value network, and Monte Carlo tree search (MCTS) with rollouts. It beat the European Go champion 5–0 (Silver et al. 2016).
- AlphaGo Zero learned from self-play alone, with one network giving both a policy and a value and no rollouts; it beat the earlier AlphaGo 100–0 (Silver et al. 2017). AlphaZero ran the same algorithm on chess, shogi and Go and reached superhuman play in each within 24 hours of training (Silver et al. 2018).
- Each simulation selects moves with the PUCT rule $Q(s,a) + c\,P(s,a)\sqrt{N(s)}/(1 + N(s,a))$, expands a new position, evaluates it with the value network, and backs the value up the path. The network then learns to predict the root's visit counts (policy) and the game result (value).
- MuZero learns a model of how its hidden state changes and plans with it, without being given the rules. It matched AlphaZero on the board games and set a new state of the art on 57 Atari games (Schrittwieser et al. 2020).
- **Pause and try:** what are AlphaZero's policy training targets?
  - **Answer:** the visit counts of the search at the root. Search improves on the raw policy, and the network learns to imitate the search.

### Segment 2 (7 min): policy gradients and PPO

- REINFORCE raises the log-probability of each action in proportion to the return that followed. Subtracting a baseline V(s) lowers the variance without adding bias, giving the advantage A = return − V(s).
- Generalized advantage estimation (GAE) mixes one-step errors $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ as $\hat A_t = \sum_l (\gamma\lambda)^l \delta_{t+l}$; λ trades bias against variance (Schulman et al. 2016).
- Trust region policy optimization (TRPO) limits how far each update moves the policy with a Kullback–Leibler (KL) divergence constraint, solved with second-order methods (Schulman et al. 2015). Proximal policy optimization (PPO) keeps the idea with a simple clipped objective, $\mathbb{E}[\min(r_t \hat A_t,\ \mathrm{clip}(r_t, 1-\varepsilon, 1+\varepsilon)\,\hat A_t)]$ with $r_t = \pi_\theta(a_t|s_t)/\pi_{\text{old}}(a_t|s_t)$ and ε = 0.2, and runs several epochs on each batch (Schulman et al. 2017).
- Implementation details matter: code-level choices explain most of PPO's gain over TRPO (Engstrom et al. 2020), and Huang et al. 2022 list 37 such details. PPO also sits inside RLHF, and GRPO is a variant without a critic (Course 4 s6–s7).
- **Pause and try:** the ratio is 1.5, the advantage A is positive and ε = 0.2. Which value does the clipped objective use?
  - **Answer:** min(1.5A, 1.2A) = 1.2A. Its gradient with respect to the ratio is zero, so nothing pushes the ratio further.

### Segment 3 (6 min): models and offline data

- World Models compress frames with a VAE, predict the next code with a recurrent network, and train a tiny controller, even inside the model's own "dream" (Ha & Schmidhuber 2018).
- DreamerV3 learns a world model and trains an actor-critic on imagined trajectories. One fixed configuration worked across more than 150 tasks, and it was the first algorithm to collect diamonds in Minecraft from scratch without human data (Hafner et al. 2023, later published in Nature).
- Offline RL learns from a fixed dataset with no new interaction. Q-learning then overestimates actions that never appear in the data, and the policy exploits those errors. Conservative Q-learning (CQL) pushes down the values of actions outside the data, so its estimates are cautious (Kumar et al. 2020).
- Decision Transformer treats a trajectory as a sequence of (return-to-go, state, action) tokens and trains a causal transformer to predict the actions; at test time you ask for a high return (Chen et al. 2021).
- **Pause and try:** an offline dataset never contains the action "jump". Why might a Q-learner believe jumping is excellent?
  - **Answer:** no data ever corrects the value of "jump", so its random errors remain, and taking the maximum picks out whichever errors happen to be too high.

### Lab guide (about 3 hours, notebook `s10_deep_reinforcement_learning.ipynb`)

1. CartPole (30 min): the equations; random pushes against the one-line rule.
2. GAE (20 min): the λ = 1 check.
3. PPO (40 min): three seeds and their summary lines.
4. Ablation (30 min): the same runs without clipping; the learning curves.
5. MCTS (40 min): visit shares; games against random play and itself.
6. Exercises (40 min): the TODO cells.

- **Expect:** random pushes average 22.7 steps; the rule "push toward the side the pole leans" scores 500.0. PPO with clipping ends at 500 in all three seeds (lowest second-half return 500, 500 and 433), with mean KL per update about 0.003 and 3.0–3.4% of ratios outside [0.8, 1.2]. Without clipping, returns crash to 166, 15 and 9 in the second half (final 500, 500 and 137), with KL 0.033–0.085 and 9.0–24.5% of ratios outside. MCTS puts 67% of visits on the centre of an empty board and 95% on the blocking move; against random play it scores 77-10-13 (wins-draws-losses) with 10 simulations, 90-10-0 with 100 and 94-5-1 with 1,000, and it draws 19 of 20 games against itself. Runtime about one and a half minutes.
- **Common problems:** treating the 500-step time limit as a failure instead of bootstrapping from V; forgetting to normalize advantages per minibatch; and backing up values from the wrong player's point of view in MCTS.

### Quiz

1. What do λ = 0 and λ = 1 mean in GAE?
   - **Answer:** λ = 0 uses only the one-step error (low variance, biased by V); λ = 1 uses the full return minus V (no bias from V, high variance).
2. What does MuZero learn that AlphaZero is given?
   - **Answer:** a model of the dynamics, so it can plan without knowing the rules.
3. In the lab, what happened when clipping was turned off?
   - **Answer:** each update moved the policy 12 to 30 times further (by KL), and returns crashed during training in all three seeds.

**Watch out:** "PPO is stable out of the box." Its results depend on code-level details (advantage normalization, learning-rate decay, gradient clipping, initialization) and on hyperparameters. In the lab the same code without the clip crashed at a large learning rate, and Engstrom et al. 2020 found that such details explain most of PPO's gain over TRPO. Use a known-good implementation and at least three seeds.

### Assignment 10 (due before session 11, 10 points)

1. Complete the gentle-step TODO (learning rate 0.001, three seeds each, with and without clipping). Report final returns, KL and ratios outside [0.8, 1.2]: does clipping still matter? (3 points)
2. Remove one implementation detail (advantage normalization or learning-rate decay) and compare three seeds with the full version in a plot. (3 points)
3. Complete the mini-AlphaZero TODO and report wins, draws and losses with 20 simulations, with and without the learned prior. (4 points)

Hand in one PDF and your notebook.

### Sources

- Silver et al. 2016, Mastering the Game of Go with Deep Neural Networks and Tree Search. https://www.nature.com/articles/nature16961
- Silver et al. 2017, Mastering the Game of Go without Human Knowledge. https://www.nature.com/articles/nature24270
- Silver et al. 2018, Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm. https://arxiv.org/abs/1712.01815
- Schrittwieser et al. 2020, Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model. https://arxiv.org/abs/1911.08265
- Schulman et al. 2015, Trust Region Policy Optimization. https://arxiv.org/abs/1502.05477
- Schulman et al. 2016, High-Dimensional Continuous Control Using Generalized Advantage Estimation. https://arxiv.org/abs/1506.02438
- Schulman et al. 2017, Proximal Policy Optimization Algorithms. https://arxiv.org/abs/1707.06347
- Engstrom et al. 2020, Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO. https://arxiv.org/abs/2005.12729
- Huang et al. 2022, The 37 Implementation Details of Proximal Policy Optimization (ICLR Blog Track). https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
- Ha & Schmidhuber 2018, World Models. https://arxiv.org/abs/1803.10122
- Hafner et al. 2023, Mastering Diverse Domains through World Models. https://arxiv.org/abs/2301.04104
- Kumar et al. 2020, Conservative Q-Learning for Offline Reinforcement Learning. https://arxiv.org/abs/2006.04779
- Chen et al. 2021, Decision Transformer: Reinforcement Learning via Sequence Modeling. https://arxiv.org/abs/2106.01345

## Session 11: Neural fields and 3D, from Fourier features to Gaussian splatting

**Goal:** students can explain coordinate networks and spectral bias, NeRF's volume rendering, and why hash grids and explicit Gaussians made 3D reconstruction fast, and can fit an image and a toy radiance field.

### Talking pointers

- **Open with:** "What if a photo were not a grid of pixels but a function, and a 3D scene were a function you could ask about any point in space? That idea, plus a renderer you can differentiate, changed 3D vision in five years."
- **Segment 1, say:** show the lab's image panels (blurry ReLU, sharp Fourier features, noisy σ = 10), then name the cause: spectral bias.
- **Segment 2, say:** draw one ray through a scene and compute the rendering weights by hand, as in the pause question.
- **Segment 3, say:** put the speed-ups on one slide: one big MLP (NeRF), a hash grid plus a tiny MLP (Instant-NGP), no network (Plenoxels), explicit Gaussians (splatting).
- **Close with:** "All these methods blend colours with the same weights, T times alpha; they differ in where density and colour are stored." Then set assignment 11.

### Segment 1 (6 min): coordinate networks

- A neural field maps coordinates to values, for example f(x, y) = colour. The signal lives in the weights, at any resolution, and it is differentiable.
- Spectral bias: networks trained by gradient descent learn low frequencies first and fine detail much later (Rahaman et al. 2019). A ReLU multilayer perceptron (MLP) on raw coordinates therefore draws blurry images.
- Fourier features first map v to [cos(2πBv), sin(2πBv)] with random frequencies B ~ N(0, σ²) (Tancik et al. 2020). σ sets the bandwidth: too small blurs, too large fits noise. The paper explains the effect with the neural tangent kernel.
- SIREN (sinusoidal representation network) uses sine activations sin(ω₀(Wx + b)), with ω₀ = 30 and a careful initialization (Sitzmann et al. 2020). Its derivatives are also SIRENs, so it can fit gradients and solve differential equations.
- **Pause and try:** why does a plain ReLU MLP fit an image blurrily?
  - **Answer:** spectral bias. Within a fixed budget it has fitted the low frequencies but not the fine detail; in the lab it scored 20.54 dB on held-out pixels against 24.45 dB for Fourier features.

### Segment 2 (7 min): NeRF

- NeRF (neural radiance field) is an MLP from a 3D position and a viewing direction to a density σ and a colour c (Mildenhall et al. 2020). Density depends only on position; colour also depends on direction, which allows reflections.
- A pixel's colour comes from points sampled along its ray: $C = \sum_i T_i\,(1 - e^{-\sigma_i \delta_i})\,c_i$, with $T_i = \exp(-\sum_{j<i} \sigma_j \delta_j)$ and δ the spacing. α_i = 1 − e^{−σ_i δ_i} is the chance that the ray stops in segment i, and T_i the chance it gets that far.
- Each coordinate goes through a positional encoding, (sin(2^k πp), cos(2^k πp)) for k < L, with L = 10 for position and 4 for direction. Without it NeRF is blurry: the same spectral bias.
- Training needs photographs with known camera poses, usually computed with structure-from-motion software, and minimizes the colour error of random rays. One network holds one scene; the paper reports about 1–2 days per scene on one GPU.
- Mip-NeRF renders cones instead of thin rays, with an encoding integrated over each cone section, which removes aliasing when a scene is seen at different scales (Barron et al. 2021).
- **Pause and try:** three samples along a ray each have α = 0.5, with colours red, green and blue in that order, and the background is white. What are the weights? What if every α were 0?
  - **Answer:** T is 1, 0.5 and 0.25, so the weights are 0.5 red, 0.25 green, 0.125 blue, and 0.125 for the white background. With zero density everywhere, the background gets weight 1.

### Segment 3 (7 min): making it fast

- Instant-NGP stores trainable feature vectors at the corners of grids at many resolutions, in hash tables of fixed size, and feeds the interpolated features to a tiny MLP (Müller et al. 2022). Training takes seconds and rendering at 1920×1080 tens of milliseconds.
- Plenoxels drop the network entirely: a sparse voxel grid stores density and spherical-harmonic colour coefficients, optimized directly with a smoothness penalty, two orders of magnitude faster than NeRF with no loss in quality (Fridovich-Keil et al. 2022).
- 3D Gaussian splatting represents the scene with millions of explicit 3D Gaussians, each with a position, an anisotropic shape (rotation and scale), an opacity and a view-dependent colour (Kerbl et al. 2023). They start from structure-from-motion points, are added and removed during training, and are rendered by projecting, sorting and alpha-blending them on screen tiles, giving real-time rendering (at least 30 frames per second) at 1080p.
- Trade-offs: an MLP field is compact but slow; grids are fast but use more memory; Gaussians render in real time and are easy to edit, but need many primitives and large files. All need many posed photos.
- **Pause and try:** why can splatting render much faster than NeRF?
  - **Answer:** it rasterizes a list of explicit primitives (project, sort, blend) instead of evaluating a network at many points along every ray.

### Lab guide (about 3 hours, notebook `s11_neural_fields.ipynb`)

1. An image as a function (15 min): the target and the pixel split.
2. Coordinate networks (40 min): ReLU, Fourier features (σ = 1, 10), SIREN.
3. Volume rendering in 2-D (35 min): the scene, cameras and training images.
4. Radiance fields (40 min): with and without positional encoding; held-out views.
5. Exercises (50 min): the NOT RUN cell and the TODO cells.

- **Expect:** training/held-out peak signal-to-noise ratio (PSNR) of 21.21/20.54 dB for the ReLU MLP, 30.32/24.45 for Fourier features with σ = 1, 42.81/10.41 with σ = 10, and 31.41/24.61 for SIREN. 24% of training pixels see only background. The radiance field reaches 39.28 dB on training views and 26.85 dB on held-out views with positional encoding, against 19.93 and 19.72 dB without. The central ray's weights peak where it enters the blue disc and sum to 1.000. Runtime about one minute.
- **Common problems:** coordinates not scaled to [−1, 1], which changes what the encoding frequencies mean; choosing σ by training PSNR instead of held-out PSNR; and leaving out the background term, so rays that hit nothing render black.

### Quiz

1. What do α_i and T_i mean in volume rendering?
   - **Answer:** α_i is the chance that the ray stops in segment i; T_i is the chance that it reaches segment i without stopping.
2. Why can Fourier features with a large σ score high on training pixels and low on held-out pixels?
   - **Answer:** they can represent very high frequencies, so they pass through every training pixel with noise in between; in the lab, 42.81 dB against 10.41 dB.
3. Name one idea that makes Instant-NGP fast and one that makes Gaussian splatting fast.
   - **Answer:** Instant-NGP: trainable multiresolution hash-grid features with a tiny MLP. Splatting: explicit Gaussians drawn by rasterization, with no network evaluations along rays.

**Watch out:** "NeRF reconstructs a 3D mesh." It learns a volumetric field of density and colour; a surface must be extracted afterwards, for example by thresholding the density, and the result depends on the threshold. In the lab, the learned discs render correctly but their insides are patchy, because images only constrain what the cameras see. A set of Gaussians is not a mesh either.

### Assignment 11 (due before session 12, 10 points)

1. Complete the bandwidth-sweep TODO, plot training and held-out PSNR against σ, and choose σ with a reason. (3 points)
2. Complete the depth TODO: show the true and learned depth images for the held-out view at 99° and report the mean error. (3 points)
3. Give one disc a colour that depends on the viewing direction, add the direction as an input to the field, and compare held-out PSNR with and without it. (4 points)

Hand in one PDF and your notebook.

### Sources

- Rahaman et al. 2019, On the Spectral Bias of Neural Networks. https://arxiv.org/abs/1806.08734
- Tancik et al. 2020, Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains. https://arxiv.org/abs/2006.10739
- Sitzmann et al. 2020, Implicit Neural Representations with Periodic Activation Functions. https://arxiv.org/abs/2006.09661
- Mildenhall et al. 2020, NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. https://arxiv.org/abs/2003.08934
- Barron et al. 2021, Mip-NeRF: A Multiscale Representation for Anti-Aliasing Neural Radiance Fields. https://arxiv.org/abs/2103.13415
- Müller et al. 2022, Instant Neural Graphics Primitives with a Multiresolution Hash Encoding. https://arxiv.org/abs/2201.05989
- Fridovich-Keil et al. 2022, Plenoxels: Radiance Fields without Neural Networks. https://arxiv.org/abs/2112.05131
- Kerbl et al. 2023, 3D Gaussian Splatting for Real-Time Radiance Field Rendering. https://arxiv.org/abs/2308.04079

## Session 12: Robustness, uncertainty and calibration

**Goal:** students can explain adversarial examples and adversarial training, certified robustness, calibration and temperature scaling, ensembles, conformal prediction and distribution shift, and can measure each on a small model.

### Talking pointers

- **Open with:** "A model that is right 96% of the time can still be dangerous. It can be fooled by changes you cannot see, it can be sure when it is wrong, and it can fail quietly when the world changes. Today we measure all three."
- **Segment 1, say:** show the clean and attacked digit side by side, then the accuracy curves against ε. Ask why a single step in the sign direction works so well.
- **Segment 2, say:** draw a reliability diagram and say what "calibrated" promises; then show why temperature scaling cannot change accuracy.
- **Segment 3, say:** compute q̂ with the class (the pause question), then show the rotation plot where the promise breaks.
- **Close with:** "Every guarantee comes with assumptions, and a deployed model must keep checking them." Then set assignment 12, which is due with the capstone.

### Segment 1 (7 min): adversarial examples

- Szegedy et al. 2014 found small, hard-to-see changes to an image that flip a network's prediction, and such changes often fool other networks too.
- The fast gradient sign method (FGSM) steps once: x′ = x + ε·sign(∇_x L(x, y)) (Goodfellow et al. 2015). Their explanation is linearity: changing each of n inputs by ε can move a linear score by ε‖w‖₁, which grows with n.
- Projected gradient descent (PGD) takes many smaller steps from a random start and projects back into the ε-box. Adversarial training minimizes the loss on such worst cases, $\min_\theta \mathbb{E}[\max_{\|\delta\|_\infty \le \varepsilon} L(x + \delta, y)]$ (Madry et al. 2018), and usually costs some clean accuracy.
- Ilyas et al. 2019 argue that adversarial examples exploit "non-robust features": real, predictive patterns in the data that humans do not use.
- Randomized smoothing classifies by a majority vote over Gaussian-noise copies of the input and proves that no change smaller than an L2 radius, σ·Φ⁻¹(p_A) in the simplest case, can flip the vote, where p_A is a lower bound on the probability that a noisy copy is given the top class (Cohen et al. 2019).
- **Pause and try:** a linear model on 64 pixels has weights of size 1. How much can FGSM with ε = 0.1 move its score?
  - **Answer:** ε·Σ|w_i| = 0.1 × 64 = 6.4, a large change, although no pixel moves by more than 0.1.

### Segment 2 (7 min): calibration and uncertainty

- A model is calibrated if, among the inputs where it says 0.8, it is right 80% of the time. Guo et al. 2017 found modern networks overconfident; they measured expected calibration error (ECE), the bin-weighted gap between confidence and accuracy, and fixed most of it with temperature scaling, softmax(z/T) with T fitted on validation data.
- Deep ensembles average several networks trained from different random starts, improving likelihood and uncertainty on unfamiliar inputs (Lakshminarayanan et al. 2017). Monte Carlo (MC) dropout keeps dropout on at test time and averages many passes, an approximation to Bayesian inference (Gal & Ghahramani 2016).
- Under distribution shift these measures degrade. ImageNet-C applies 15 corruptions at 5 severities (Hendrycks & Dietterich 2019). Ovadia et al. 2019 found calibration worsening with shift, temperature scaling fitted on clean data not carrying over, and ensembles holding up best. WILDS collects real shifts, such as new hospitals (Koh et al. 2021).
- **Pause and try:** does temperature scaling change accuracy?
  - **Answer:** no. Dividing all logits by the same T > 0 keeps their order, so the predicted class is unchanged; in the lab, 0.957 before and after.

### Segment 3 (6 min): conformal prediction

- Split conformal prediction: compute a score s(x, y), for example 1 − p̂_y(x), on n calibration points; take q̂ = the ⌈(n + 1)(1 − α)⌉-th smallest; predict the set C(x) = {y : s(x, y) ≤ q̂}. If calibration and test points are exchangeable, P(Y ∈ C(X)) ≥ 1 − α (Angelopoulos & Bates 2021).
- It works with any model: a worse model gets larger sets, not lower coverage. Adaptive scores add up probability mass, and RAPS (regularized adaptive prediction sets) adds a penalty that keeps sets small and stable for ImageNet classifiers (Angelopoulos et al. 2021).
- What it does not promise: coverage for each example or each class (only on average), coverage for one particular calibration set, or coverage under distribution shift.
- **Pause and try:** α = 0.1 with 1,000 calibration points. Which score sets q̂?
  - **Answer:** the ⌈1001 × 0.9⌉ = 901st smallest.

### Lab guide (about 3 hours, notebook `s12_robustness_and_uncertainty.ipynb`)

1. Splits (10 min): why four roles, and why the test set is used last.
2. Attacks (30 min): FGSM and PGD against ε.
3. Adversarial training (25 min): robust and clean accuracy.
4. Calibration (25 min): temperature, ECE and the reliability diagrams.
5. Ensemble (20 min): members against the average.
6. Conformal sets (30 min): coverage, set sizes, 1,000 splits, coverage by class.
7. Shift and exercises (40 min): rotation, then the TODO cells.

- **Expect:** clean accuracy 0.957. At ε = 0.1, FGSM leaves 0.447 and PGD 0.393; at 0.2, PGD leaves 0.000. Adversarial training raises PGD accuracy to 0.787 at 0.1 and 0.300 at 0.2, and clean accuracy does not drop (0.960). T = 1.27 lowers the negative log-likelihood (NLL) from 0.139 to 0.126, but ECE barely moves (0.028 to 0.027). The ensemble's NLL is 0.126, its ECE 0.033. Threshold sets: q̂ = 0.1060, coverage 0.917, mean size 0.93, 7.3% empty; mean coverage over 1,000 splits 0.9011, and from 0.83 to 1.00 by class. Rotating by 10°, 20° and 30° gives accuracy 0.787, 0.650 and 0.417, ECE 0.084, 0.181 and 0.360, and coverage 0.587, 0.440 and 0.247. Runtime about 20 seconds.
- **Common problems:** fitting T or q̂ on the test set; testing robustness with FGSM only (it reported 0.413 for the robust model at 0.2, where PGD found 0.300); and treating an ECE from 300 points as exact.

### Quiz

1. Why is PGD a better test of robustness than FGSM?
   - **Answer:** it searches harder, with many steps from a random start, so it finds attacks that FGSM misses; FGSM gives an optimistic estimate.
2. What does ECE measure?
   - **Answer:** the gap between confidence and accuracy, averaged over confidence bins and weighted by the number of points in each bin.
3. A conformal method promises 90% coverage. Name two things this does not mean.
   - **Answer:** any two of: 90% for every example or class; 90% under distribution shift; 90% for every calibration set.

**Watch out:** "A softmax output of 0.99 means a 99% chance of being right." That holds only for a calibrated model on data like its validation data: after a 10° rotation, the lab's model lost accuracy while its ECE tripled. And conformal "90%" is a promise about the average over many test points, not about any single prediction.

### Assignment 12 (due with the capstone, 10 points)

1. Complete the randomized-smoothing TODO and write one paragraph on what a certificate would add to your numbers. (3 points)
2. Complete the MC-dropout TODO and compare it with the ensemble on clean and rotated digits. (3 points)
3. Take your capstone model (or one from this course) and report its calibration (ECE and a reliability diagram) and conformal coverage on held-out data and under one shift you design. (4 points)

Hand in one PDF and your notebook.

### Sources

- Szegedy et al. 2014, Intriguing Properties of Neural Networks. https://arxiv.org/abs/1312.6199
- Goodfellow et al. 2015, Explaining and Harnessing Adversarial Examples. https://arxiv.org/abs/1412.6572
- Madry et al. 2018, Towards Deep Learning Models Resistant to Adversarial Attacks. https://arxiv.org/abs/1706.06083
- Ilyas et al. 2019, Adversarial Examples Are Not Bugs, They Are Features. https://arxiv.org/abs/1905.02175
- Cohen et al. 2019, Certified Adversarial Robustness via Randomized Smoothing. https://arxiv.org/abs/1902.02918
- Guo et al. 2017, On Calibration of Modern Neural Networks. https://arxiv.org/abs/1706.04599
- Lakshminarayanan et al. 2017, Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles. https://arxiv.org/abs/1612.01474
- Gal & Ghahramani 2016, Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning. https://arxiv.org/abs/1506.02142
- Hendrycks & Dietterich 2019, Benchmarking Neural Network Robustness to Common Corruptions and Perturbations. https://arxiv.org/abs/1903.12261
- Ovadia et al. 2019, Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. https://arxiv.org/abs/1906.02530
- Koh et al. 2021, WILDS: A Benchmark of in-the-Wild Distribution Shifts. https://arxiv.org/abs/2012.07421
- Angelopoulos et al. 2021, Uncertainty Sets for Image Classifiers using Conformal Prediction. https://arxiv.org/abs/2009.14193
- Angelopoulos & Bates 2021, A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. https://arxiv.org/abs/2107.07511

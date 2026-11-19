# Course 14: On-Device AI

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on making models small, fast and frugal enough to run on phones and microcontrollers, offline: measuring cost, efficient architectures, quantization, pruning, distillation, model formats and runtimes, memory, small language models and speech on phones, TinyML, honest benchmarking, and learning on the device. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Many students in Bangladesh, and many of the people their apps will serve, use low-cost Android phones with little memory and paid, patchy mobile data. A model that only runs on a cloud GPU does not reach them. This course teaches how to fit models onto devices and how to measure what each technique really saves: bytes, operations, peak memory, latency and energy. Every technique is measured in a notebook rather than taken on trust. Courses 3 and 4 touch on quantization for language models; this course gives the full treatment for any model, and Courses 12 and 15 point here when they deploy their tools.

Prerequisites: Python and PyTorch at the level of Course 1, including how to train a small network. Course 11 helps with the numerical parts (session 10 on floating point).

Capstone: take a model you care about (a Bangla language model from Course 4, an assistive model from Course 12, a crop-disease model from Course 15, or your own), shrink it with at least two techniques from the course, run it on a real phone or microcontroller, and report size, peak memory, latency distribution, an energy estimate and accuracy before and after, in a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a clear target device and budget (15); correct use of at least two compression techniques (25); honest measurements on the device with a proper benchmark protocol (25); accuracy and error analysis after compression (20); clarity of the report and video (15).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English.

### Sessions

1. **Why on-device AI, and how to measure cost.** Students can explain why models run on devices, count parameters, bytes and MACs, and use the roofline model to predict whether a layer is limited by compute or memory.
   - Read: Williams, Waterman & Patterson 2009, Roofline: An Insightful Visual Performance Model for Multicore Architectures, Communications of the ACM; Hard et al. 2018, Federated Learning for Mobile Keyboard Prediction
   - Lab: about 2 hours, notebook `s01_measuring_cost.ipynb`
2. **Efficient architectures for small devices.** Students can compute the savings of depthwise separable convolutions, build a small MobileNet-style network, and compare accuracy, size, MACs and latency.
   - Read: Howard et al. 2017, MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications; Sandler et al. 2018, MobileNetV2: Inverted Residuals and Linear Bottlenecks
   - Lab: about 2 hours, notebook `s02_efficient_architectures.ipynb`
3. **Quantization I: integers instead of floats.** Students can quantize and dequantize tensors, choose scales and zero points, calibrate activation ranges, and run an integer-only matrix multiply.
   - Read: Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference; Krishnamoorthi 2018, Quantizing Deep Convolutional Networks for Efficient Inference: A Whitepaper
   - Lab: about 2 hours, notebook `s03_quantization_basics.ipynb`
4. **Quantization II: training-aware and LLM quantization.** Students can train with fake quantization and the straight-through estimator, quantize weights in groups, and handle activation outliers as LLM quantization methods do.
   - Read: Bengio, Léonard & Courville 2013, Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation; Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference
   - Lab: about 2 hours, notebook `s04_qat_and_llm_quantization.ipynb`
5. **Pruning and sparsity.** Students can prune networks by magnitude and by channel, measure what sparsity does to accuracy and latency, and test a lottery-ticket claim on a small scale.
   - Read: Han, Pool, Tran & Dally 2015, Learning both Weights and Connections for Efficient Neural Networks; Frankle & Carbin 2019, The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks
   - Lab: about 2 hours, notebook `s05_pruning.ipynb`
6. **Knowledge distillation.** Students can train a small student from a large teacher's soft labels, tune temperature and loss weights, and judge when distillation is worth it.
   - Read: Hinton, Vinyals & Dean 2015, Distilling the Knowledge in a Neural Network; Romero et al. 2015, FitNets: Hints for Thin Deep Nets
   - Lab: about 2 hours, notebook `s06_distillation.ipynb`
7. **Model formats and runtimes.** Students can fold layers, export a PyTorch model to ONNX, run and quantize it with ONNX Runtime, and check that the converted model still gives the right answers.
   - Read: Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference; ONNX, Open Neural Network Exchange
   - Lab: about 2 hours, notebook `s07_formats_runtimes.ipynb`
8. **Memory: weights, activations and the KV cache.** Students can compute peak memory from tensor lifetimes, reduce it by changing execution order or tiling, and size an LLM's KV cache for a phone.
   - Read: Lin et al. 2021, MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning; Ainslie et al. 2023, GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
   - Lab: about 2 hours, notebook `s08_memory.ipynb`
9. **Small language models and speech on the phone.** Students can estimate decoding speed from memory bandwidth, measure the effect of a KV cache and quantization, and choose a small model and runtime for a phone.
   - Read: Leviathan, Kalman & Matias 2023, Fast Inference from Transformers via Speculative Decoding; Radford et al. 2022, Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)
   - Lab: about 2.5 hours, notebook `s09_small_lms_on_phone.ipynb`
10. **TinyML on microcontrollers.** Students can design a keyword-spotting model that fits a microcontroller's flash and RAM, quantize it to int8, and set a detection threshold.
   - Read: David et al. 2021, TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems; Lin et al. 2020, MCUNet: Tiny Deep Learning on IoT Devices
   - Lab: about 2 hours, notebook `s10_tinyml.ipynb`
11. **Benchmarking latency and energy honestly.** Students can build a benchmark harness, report latency distributions correctly, and estimate energy per inference from stated assumptions.
   - Read: Janapa Reddi et al. 2022, MLPerf Mobile Inference Benchmark; Efron & Tibshirani 1993, An Introduction to the Bootstrap (Chapman & Hall)
   - Lab: about 2 hours, notebook `s11_benchmarking.ipynb`
12. **Learning on the device, privacy, and the capstone.** Students can estimate the memory cost of training on a device, personalize a model with few examples by updating only part of it, and plan a deployment capstone.
   - Read: Cai et al. 2020, TinyTL: Reduce Activations, Not Trainable Parameters for Efficient On-Device Learning (NeurIPS 2020 title: TinyTL: Reduce Memory, Not Parameters for Efficient On-Device Learning); Lin et al. 2022, On-Device Training Under 256KB Memory
   - Lab: about 2 hours, notebook `s12_on_device_learning.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. Where you can, show the same model running on a cheap phone on camera.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. Sizes and operation counts are exact; latencies come from one run on a shared server CPU, not a phone, so expect different numbers on your machine. A few notebooks use onnx, onnxscript and onnxruntime, which need `pip install onnx onnxscript onnxruntime` on Colab or Kaggle.
- **Sources:** read the papers cited for a session before recording it. Tool names and versions change quickly; check the current documentation before recording.
- **Dates:** written in November 2026.

## Session 1: Why on-device AI, and how to measure cost

**Goal:** students can explain why models run on devices, count parameters, bytes and MACs, and use the roofline model to predict whether a layer is limited by compute or memory.

### Talking pointers

- **Open with:** "Your phone can suggest the next word, caption a video and translate a sentence with no internet at all. This course is about building models like that, small and fast enough for a low-cost phone."
- **Segment 1, say:** give the four reasons, then show the bytes table.
- **Segment 2, say:** count the CNN's MACs on the board, then show the three counts agreeing.
- **Segment 3, say:** draw the roofline by hand, then show the measured one and the two equal-MAC layers.
- **Close with:** "Count bytes and MACs exactly, but measure time; the roofline tells you which limit you will hit." Then set assignment 1.

### Segment 1 (6 min): why run models on the device

- On-device AI means the model runs on the phone, watch or microcontroller itself, not on a server. Four reasons: **latency** (no network round trip), **privacy** (the data stays on the device), **offline use**, and **cost at scale** (millions of phones do the computing, not your servers).
- Examples: Gboard's next-word prediction runs a 1.4-million-parameter recurrent language model on the phone, trained with federated learning (Hard et al. 2018). Android's Live Caption transcribes audio entirely on the device (Google 2019). In 2018 Google Translate's offline mode moved to on-device neural translation for 59 languages (Google 2018).
- Bangladesh: DataReportal counted 77.7 million internet users in January 2025, under half the population, with a median mobile download speed of 28.26 Mbit/s (Ookla data). Data costs money: 1 GB cost more than 2% of monthly income for the poorest 40% of people (A4AI 2021). A model that works offline reaches more people.
- The price: tight limits on storage, RAM, compute and battery, which sessions 2–8 attack.
- **Pause and try:** Whisper base is a 74-million-parameter speech recognition model (Radford et al. 2022). How big is it in float32 and in int8, and how long does each take to download at 28.26 Mbit/s?
  - **Answer:** 296 MB and 74 MB. One megabyte is 8 megabits, so int8 takes 74 × 8 ÷ 28.26 ≈ 21 seconds and float32 about 84 seconds.

### Segment 2 (7 min): the budget

- **Bytes** = parameters × bytes per parameter: 4 in float32, 2 in float16, 1 in int8, 0.5 in int4. MobileNetV2 has 3.4 million parameters (Sandler et al. 2018): 13.6 MB in float32, 3.4 MB in int8. Course 4 session 10 does this for a small Bangla model.
- A **multiply–accumulate operation** (MAC) is $a \leftarrow a + wx$, two floating-point operations (FLOPs). A linear layer has $n\,d_{in}d_{out}$ MACs on n tokens; a k × k convolution has $H_{out}W_{out}C_{out}C_{in}k^2$; attention adds $2n^2d$. MobileNetV2 needs 300 million MACs per 224 × 224 image.
- **Peak memory** = weights + live activations (+ scratch space). In a chain of layers, the live activations are one layer's input and output; at large batches they dominate.
- **Latency** is the time for one request: warm up, repeat, and report the median, on one thread. Phone apps mostly run at batch 1, where fixed overheads matter most.
- **Energy** = average power × time. Moving data costs more than arithmetic: on a 45 nm chip, reading 32 bits from DRAM (main memory) cost about 640 picojoules (pJ), a 32-bit float multiply 3.7 pJ (Horowitz's figures, quoted by Han et al. 2015).
- **Pause and try:** how many MACs does a 3 × 3 convolution from 8 to 16 channels need for an 8 × 8 output?
  - **Answer:** 8 × 8 × 16 × 8 × 9 = 73,728, the second convolution of the lab's CNN.

### Segment 3 (7 min): the roofline model

- Two limits: peak arithmetic (FLOP/s) and memory bandwidth (bytes/s). The **arithmetic intensity** I is FLOPs per byte moved, and attainable FLOP/s = min(peak, I × bandwidth) (Williams, Waterman & Patterson 2009).
- The **ridge point**, peak ÷ bandwidth, separates memory-bound operations from compute-bound ones. On one thread of the lab CPU: about 155 GFLOP/s and 29 GB/s for 64 MB of data, a ridge near 5 FLOPs per byte.
- A matrix–vector product does 2 FLOPs per weight and reads every weight once: I = 0.5 in float32. A language model does this for every generated token, so decoding is memory-bound on any device; Course 3 session 4 covers the KV cache, quantization and speculative decoding that follow from this.
- An n × n matrix product does $2n^3$ FLOPs on $12n^2$ bytes, so I = n/6 grows with n: big batches and wide convolutions are compute-bound.
- FLOPs alone do not predict latency: bytes moved, kernels that use the hardware badly (the lab's depthwise convolution reached 4% of its roof), operations with no MACs (26% of a Transformer block's time) and fixed overheads all count.
- Counts and the roofline's shape transfer to a phone; the numbers do not. A phone core has narrower vector units, less bandwidth and smaller caches, and slows down when hot.
- **Pause and try:** a 4,096 × 4,096 linear layer on one token, with float16 weights. What is its arithmetic intensity, and is it memory-bound on the lab CPU?
  - **Answer:** 2 FLOPs per 2 bytes, about 1 FLOP per byte, far below the ridge of about 5: memory-bound.

### Lab guide (about 2 hours, notebook `s01_measuring_cost.ipynb`)

1. Section 1 (10 min): the bytes table. Why must the thread settings come before NumPy is imported?
2. Sections 2–3 (35 min): train the multi-layer perceptron (MLP), convolutional neural network (CNN) and tiny Transformer; count the CNN's MACs on paper first.
3. Section 4 (10 min): peak memory at batch 1 and 256. Which part dominates?
4. Section 5 (20 min): latency against batch size, and each model's effective GFLOP/s.
5. Sections 6–7 (25 min): the roofline, the two layers with equal MACs, and the Transformer block's time shares.
6. TODO cells (20 min): a depthwise-separable block's cost, and a roofline prediction checked by measurement.

- **Expect:** accuracy 0.978 (MLP), 0.987 (CNN), 0.972 (Transformer); parameters 41,802, 3,818 and 52,874; MACs 41,600, 94,720 and 836,224 by all three counts. Timings from the saved run (they vary): first call 0.858 ms against a median of 0.168 ms; batch-1 latency 0.033, 0.070 and 0.187 ms. Peak 155 GFLOP/s; bandwidth 29.0 GB/s for 64 MB; matrix–vector 13.4 GFLOP/s (93% of its roof); depthwise convolution 6.7 GFLOP/s (4%); equal-MAC layers 2.688 against 0.334 ms. Runtime about 20 seconds.
- **Common problems:** letting NumPy use all cores; timing the first call; counting a view such as `Flatten` as new memory.

### Quiz

1. A model has 25 million parameters. How big is it in float16 and in int4?
   - **Answer:** 50 MB and 12.5 MB.
2. Why is generating one token with a language model memory-bound?
   - **Answer:** each weight is read once and used for one multiply–add, so the arithmetic intensity (0.5 FLOPs per byte in float32) is far below the ridge point; the time is about bytes ÷ bandwidth.
3. Why measure a phone app's latency at batch 1, after a warm-up, as a median?
   - **Answer:** the app answers one request at a time, the first calls include one-off setup, and the median ignores occasional slow runs.

**Watch out:** "Fewer FLOPs always means faster." In the lab, two layers with identical MACs differed 8.1 times in time, and the CNN, with 8.8 times fewer MACs than the Transformer, took almost as long per image at batch 256. Bytes moved, kernel quality and fixed overheads decide the time. Count MACs, but measure time.

### Assignment 1 (due before session 2, 10 points)

1. By hand, find the parameters, the bytes in float32 and int8, and the MACs of the lab's CNN with 16 and 32 channels instead of 8 and 16. Check them with the notebook's counters. (3 points)
2. Complete both TODO cells. Report the predicted and measured times of Linear(2048, 2048) on 1 and 64 tokens, and explain any gap using the roofline. (4 points)
3. Add a 1 × 1 convolution and an attention score product with 256 tokens to the roofline table. Predict whether each is memory-bound or compute-bound, then check by measurement. (3 points)

Hand in one PDF and your notebook.

### Sources

- Williams, Waterman & Patterson 2009, Roofline: An Insightful Visual Performance Model for Multicore Architectures, Communications of the ACM. https://doi.org/10.1145/1498765.1498785
- Hard et al. 2018, Federated Learning for Mobile Keyboard Prediction. https://arxiv.org/abs/1811.03604
- Google 2019, On-Device Captioning with Live Caption (Google Research blog). https://research.google/blog/on-device-captioning-with-live-caption/
- Google 2018, Offline translations are now a lot better thanks to on-device AI. https://blog.google/products/translate/offline-translations-are-now-lot-better-thanks-device-ai/
- DataReportal 2025, Digital 2025: Bangladesh. https://datareportal.com/reports/digital-2025-bangladesh
- Alliance for Affordable Internet (A4AI) 2021, Bangladesh brief. https://adi.a4ai.org/wp-content/uploads/2021/08/Bangladesh-Brief.pdf
- Sandler et al. 2018, MobileNetV2: Inverted Residuals and Linear Bottlenecks. https://arxiv.org/abs/1801.04381
- Radford et al. 2022, Robust Speech Recognition via Large-Scale Weak Supervision (Whisper). https://arxiv.org/abs/2212.04356
- Han, Pool, Tran & Dally 2015, Learning both Weights and Connections for Efficient Neural Networks. https://arxiv.org/abs/1506.02626

## Session 2: Efficient architectures for small devices

**Goal:** students can compute the savings of depthwise separable convolutions, build a small MobileNet-style network, and compare accuracy, size, MACs and latency.

### Talking pointers

- **Open with:** "Today we cut a network's multiply–accumulates by a factor of seven for a small cost in accuracy. Then we time it, and find that whether it got faster depends on who runs it."
- **Segment 1, say:** draw a standard convolution next to a depthwise and a pointwise one, and derive 1/N + 1/k² on the board.
- **Segment 2, say:** draw the MobileNetV2 block (thin, wide, thin), then show the width sweep plot.
- **Segment 3, say:** show the PyTorch against ONNX Runtime (the runtime for Open Neural Network Exchange files) latency numbers, then the attention table as n doubles.
- **Close with:** "Design with MACs, decide with measurements on the runtime you will ship." Then set assignment 2.

### Segment 1 (7 min): depthwise separable convolutions

- A standard k × k convolution from M to N channels on an H × W output costs $HWNMk^2$ MACs: every output channel looks at every input channel.
- MobileNets (Howard et al. 2017) split it in two. A **depthwise** convolution applies one k × k filter to each input channel separately ($HWMk^2$ MACs). A **pointwise** 1 × 1 convolution then mixes the channels ($HWMN$ MACs).
- The cost ratio is $1/N + 1/k^2$. With k = 3 and many channels it approaches 1/9: the paper reports 8 to 9 times less computation for a small loss of accuracy.
- In MobileNetV1, 1 × 1 convolutions hold about 95% of the multiply-adds, and they run as plain matrix multiplications, which every runtime does well.
- Two knobs scale a network: the **width multiplier** α scales every channel count (MACs and parameters by about α²), and the **resolution multiplier** ρ shrinks the input (MACs by ρ², parameters unchanged).
- **Pause and try:** what is the MAC ratio of a standard 3 × 3 convolution to a separable one with N = 32 output channels?
  - **Answer:** 1/(1/32 + 1/9) ≈ 7.0. The notebook prints 7.0 for 32 channels.

### Segment 2 (7 min): from MobileNetV2 to MobileNetV4

- **MobileNetV2** (Sandler et al. 2018) uses **inverted residual** blocks: a 1 × 1 convolution expands the channels (usually 6 times), a depthwise 3 × 3 convolution works in the wide space, and a 1 × 1 convolution projects back down. The final projection has no ReLU (a **linear bottleneck**), because ReLU in a thin layer destroys information; the residual connects the thin ends. It reached 72.0% ImageNet top-1 with 3.4 million parameters and 300 million MACs.
- **MobileNetV3** (Howard et al. 2019) was found partly by automated architecture search that included measured phone latency. It adds **squeeze-and-excitation** (a small branch that pools each channel and rescales the channels) and **hard-swish**, $x \cdot \text{ReLU6}(x + 3)/6$, a cheap approximation of swish with no exponential.
- **EfficientNet** (Tan & Le 2019) scales depth, width and resolution together: by $1.2^\phi$, $1.1^\phi$ and $1.15^\phi$, chosen so that FLOPs roughly double with each step of φ.
- **MobileNetV4** (Qin et al. 2024) introduces the Universal Inverted Bottleneck, one block that can become an inverted bottleneck, a ConvNeXt-like block or a feed-forward block, plus **Mobile MQA**, attention whose heads share one set of keys and values. Its goal is a family that is efficient across phone CPUs, GPUs, digital signal processors (DSPs) and neural accelerators at once. Course 2 session 4 shows depthwise convolutions and inverted bottlenecks inside ConvNeXt.
- **Pause and try:** EfficientNet's FLOPs grow with depth × width² × resolution². By how much do they grow when φ increases by 1?
  - **Answer:** 1.2 × 1.1² × 1.15² ≈ 1.92, about 2 times.

### Segment 3 (6 min): Transformers on phones, and designing for the hardware

- One self-attention layer costs $4nd^2$ MACs for its projections and $2n^2d$ for the scores and weighted values, and stores an n × n score matrix per head. Above n = 2d the quadratic term dominates.
- **MobileViT** (Mehta & Rastegari 2022) mixes convolutions, for local patterns, with attention between patches of a small feature map, for global context, which keeps the token count small.
- Design for the hardware: use operations every runtime and accelerator supports (3 × 3 and 1 × 1 convolutions, ReLU, ReLU6, hard-swish), keep channel counts at multiples of 8, and avoid operations that an accelerator cannot run, because they fall back to the slower CPU. Measure on the target, with the runtime you will ship (sessions 7 and 11).
- The lab shows why. In PyTorch eager, the separable network ran slower than the standard one at batch 1; in ONNX Runtime it was 3.69 times faster. Same weights, same MACs, different kernels.
- **Pause and try:** for d = 64, at what number of tokens do the attention products cost as much as the projections?
  - **Answer:** $4nd^2 = 2n^2d$ gives n = 2d = 128. The notebook prints 2,097,152 MACs for both.

### Lab guide (about 2 hours, notebook `s02_efficient_architectures.ipynb`)

1. Sections 1–2 (20 min): the ratio on paper, then the per-layer MACs and times. When does the separable pair win?
2. Section 3 (25 min): read `make_net`, train both networks, compare parameters and MACs.
3. Section 4 (20 min): export to ONNX, check the outputs agree, and compare batch-1 latency in both runtimes.
4. Section 5 (25 min): the width sweep and its two plots.
5. Section 6 (10 min): attention time as n doubles.
6. TODO cells (20 min): the inverted residual block's cost, and the channels-last layout. Section 7 is optional, on Colab.

- **Expect:** MAC ratios 5.8 to 8.7, matching the formula; per-layer time ratios 0.44, 0.90, 0.99, 1.89 and 1.62 for 16 to 256 channels. Standard network 0.993 accuracy, 70,330 parameters, 7,115,392 MACs; separable 0.985, 10,474 and 989,824. From the saved run (timings vary): PyTorch 0.457 ms (standard) against 0.635 ms (separable); ONNX Runtime 0.167 against 0.045 ms (3.69 times); outputs agree within 2.9e-06. Width sweep accuracies 0.791, 0.950, 0.985 and 0.994. Attention time ratio 3.66 from 512 to 1,024 tokens. Runtime about 75 seconds.
- **Common problems:** timing in PyTorch eager and concluding the architecture is slow; comparing networks trained with different recipes; forgetting `groups=c_in`, which makes a full convolution instead of a depthwise one.

### Quiz

1. Why does a depthwise convolution need a pointwise convolution after it?
   - **Answer:** the depthwise convolution never mixes channels; the 1 × 1 pointwise convolution combines them.
2. Why does MobileNetV2 leave out the ReLU after the projection?
   - **Answer:** the projection is low-dimensional, and a ReLU there throws away information; a linear bottleneck keeps it.
3. A network has 4 times fewer MACs than another. Name two reasons it might not be 4 times faster.
   - **Answer:** fixed per-layer overheads, kernels that run some operations (such as depthwise convolutions) inefficiently, memory traffic, and operations with no MACs. Any two.

**Watch out:** "Depthwise separable convolutions are always faster in practice." In the lab, the separable network had 7.2 times fewer MACs but ran slower in PyTorch eager (speed-up 0.72), and only 3.69 times faster in ONNX Runtime. Depthwise layers do little work per byte and per call, so their speed depends on the runtime's kernels and the hardware.

### Assignment 2 (due before session 3, 10 points)

1. Complete the inverted residual TODO for c = 32 and t = 6. Compare its parameters and MACs with one separable block of the lab network, and explain the difference. (3 points)
2. Complete the channels-last TODO, then measure both networks at batch 64 in both runtimes. Does the ranking change with batch size? Explain using session 1's ideas. (4 points)
3. Use the resolution multiplier instead of the width multiplier: train the separable network on the original 8 × 8 digits and compare accuracy, MACs and ONNX Runtime latency with the 16 × 16 version. (3 points)

Hand in one PDF and your notebook.

### Sources

- Howard et al. 2017, MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. https://arxiv.org/abs/1704.04861
- Sandler et al. 2018, MobileNetV2: Inverted Residuals and Linear Bottlenecks. https://arxiv.org/abs/1801.04381
- Howard et al. 2019, Searching for MobileNetV3. https://arxiv.org/abs/1905.02244
- Tan & Le 2019, EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. https://arxiv.org/abs/1905.11946
- Qin et al. 2024, MobileNetV4: Universal Models for the Mobile Ecosystem. https://arxiv.org/abs/2404.10518
- Mehta & Rastegari 2022, MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer. https://arxiv.org/abs/2110.02178
- ONNX Runtime documentation. https://onnxruntime.ai/docs/

## Session 3: Quantization I: integers instead of floats

**Goal:** students can quantize and dequantize tensors, choose scales and zero points, calibrate activation ranges, and run an integer-only matrix multiply.

### Talking pointers

- **Open with:** "A float32 weight takes 4 bytes; an int8 weight takes 1. Today we turn a trained network into integers, run it with integer arithmetic only, and see exactly what that costs."
- **Segment 1, say:** work the hand example on the board: s, z and the integer for 0.31, then show the plot of signal-to-quantization-noise ratio (SQNR) against bits.
- **Segment 2, say:** draw two weight rows with very different ranges sharing one step size, then show the 3-bit calibration rows with and without the glitched image.
- **Segment 3, say:** write one requantization step on the board, from int32 accumulator to uint8 output, then show that the integer model agrees with the float one on all but one test image.
- **Close with:** "Quantization is choosing ranges, not just rounding numbers." Then set assignment 3.

### Segment 1 (7 min): uniform affine quantization

- A quantizer maps a real number x to an integer q with a **scale** s (the step between levels) and a **zero point** z (the integer that stands for 0.0): q = clamp(round(x/s) + z, q_min, q_max), and back, x̂ = s(q − z) (Jacob et al. 2018).
- **Asymmetric** quantization maps the range [α, β] onto all $2^b$ levels, for example uint8 0…255, with s = (β − α)/255 and z = round(−α/s). The range is widened to include 0, so that zero padding and ReLU outputs are exact.
- **Symmetric** quantization fixes z = 0 and maps [−max|x|, max|x|] onto −127…127 (int8) or −7…7 (int4). It wastes one level, but the arithmetic is simpler, so it is the usual choice for weights.
- Inside the range, rounding moves a value by at most s/2; for values spread over many levels the error is close to uniform, with mean square $s^2/12$. Each extra bit halves s: about 6 dB less noise per bit. Values outside the range are clipped.
- Integers win twice: 4 times fewer bytes than float32, and cheaper arithmetic when the hardware has integer instructions. Course 11 session 10 covers the float formats being replaced.
- **Pause and try:** with s = 0.008314 and z = 75, what integer does 0.31 become, and what value comes back?
  - **Answer:** round(0.31/0.008314) + 75 = 37 + 75 = 112, and 0.008314 × 37 = 0.3076.

### Segment 2 (7 min): choosing ranges for weights and activations

- **Per-tensor** quantization uses one scale for a whole weight matrix; **per-channel** uses one scale per output channel (row). When rows have very different ranges, one shared step wastes levels on the small rows. Quantizing weights per channel and activations per tensor to 8 bits after training kept a wide range of CNNs within 2% of float accuracy (Krishnamoorthi 2018).
- Activations depend on the input, so their ranges are **calibrated** on a few hundred representative inputs. Common choices are min–max, a high percentile, or the clipping value that minimizes the mean squared error (Nagel et al. 2021).
- Clipping trades rounding error for clipping error. Heavy tails make this hard: in the lab, a heavy-tailed tensor reached only 20.1 dB at 8 bits, no better than a 5-bit Gaussian.
- One outlier stretches the range for everyone. One glitched calibration image (pixels × 10) did no harm at 8 bits, but at 3 bits min–max calibration fell to 0.178 accuracy, while the MSE-chosen range kept 0.961.
- **Pause and try:** a weight matrix's rows have largest weights between 0.12 and 0.45. With int4 symmetric per-tensor quantization (levels −7…7), how many levels does the 0.12 row use?
  - **Answer:** the step is 0.45/7 ≈ 0.064, so the row spans about ±1.9 steps: 5 levels (−2…2) out of 15. Per channel, its step is 0.12/7 ≈ 0.017 and it uses all 15.

### Segment 3 (6 min): integer-only inference

- Jacob et al. (2018) run a whole network in integers. A layer multiplies 8-bit weights by 8-bit activations (int8 by uint8 in the lab) and **accumulates in int32**; the bias is stored in int32 at the accumulator's scale, $s_w s_x$.
- **Requantization** turns the int32 sum into the next layer's uint8 input: multiply by $M = s_w s_x / s_y$, round and clamp. M is stored as a 31-bit integer and a bit shift, so the device never needs floating point.
- **Fused ReLU:** clamping at zero is the ReLU, so it is free.
- In the lab, the integer MLP scored 0.974 against 0.976 for float and agreed with it on 539 of 540 test images.
- Speed needs integer kernels. NumPy has none, and its integer pass was 10 times slower than its float pass. Phone runtimes use the CPU's int8 dot-product instructions; Krishnamoorthi (2018) measured 2–3 times speed-ups over float on CPUs.
- **Static** quantization calibrates activation scales in advance, as here. **Dynamic** quantization stores int8 weights and computes activation scales at run time; Course 4 session 10 applies it to a small Bangla model.
- **Pause and try:** a layer has 64 inputs. Why can its accumulator not be 16 bits?
  - **Answer:** one product can reach 127 × 255 = 32,385, and 64 of them sum to about 2.07 million, far beyond the int16 limit of 32,767.

### Lab guide (about 2 hours, notebook `s03_quantization_basics.ipynb`)

1. Section 1 (15 min): the hand example on paper, then in code.
2. Section 2 (20 min): error against bits; compare each MSE with $s^2/12$ and explain where the formula fails.
3. Section 3 (20 min): train the MLP and quantize its weights per tensor and per channel.
4. Section 4 (25 min): activation calibration, with and without the glitched image.
5. Sections 5–6 (25 min): the integer-only forward pass, its accumulator sizes, and the byte counts.
6. TODO cells (15 min): asymmetric per-channel weights, and a percentile sweep.

- **Expect:** hand example s = 0.008314, z = 75, q = (0, 63, 75, 112, 255). Gaussian SQNR 39.3 dB at 8 bits down to 6.8 dB at 3 bits, with MSE matching $s^2/12$; heavy-tailed 20.1 dB at 8 bits. Float MLP 0.976; 2-bit weights 0.087 per-tensor and 0.752 per-channel. At 3-bit activations with the glitch: 0.178 (min–max), 0.830 (99.99th percentile), 0.961 (MSE). Integer-only accuracy 0.974, agreement 0.998, largest accumulator 421,667. NumPy time from the saved run: 0.78 ms float, 8.11 ms integer. Sizes 104,488 bytes (float32), 27,984 (int8) and 15,056 (int4). Runtime about 10 seconds.
- **Common problems:** a zero point that does not represent 0.0 exactly; an int16 accumulator that overflows; calibrating on data that do not look like real inputs.

### Quiz

1. When is symmetric quantization a poor fit?
   - **Answer:** when the values are far from centred on zero, for example ReLU outputs, which are never negative: half the levels are never used.
2. Why is the bias stored as int32 at scale $s_w s_x$?
   - **Answer:** so that it can be added directly to the int32 accumulator, which has that scale, with no extra rescaling.
3. Your 4-bit model works with min–max calibration on clean data but fails in the field. Name one likely cause.
   - **Answer:** the calibration data were not representative (real inputs are larger or differently distributed), or one outlier set a huge range; a percentile or MSE range on representative data is safer.

**Watch out:** "Quantization is just rounding the weights." Rounding needs ranges: scales and zero points for weights and for activations, calibrated on real data, plus int32 biases and requantization between layers. In the lab, 2-bit weights with one scale per tensor scored 0.087, and 3-bit activations calibrated with one glitched image scored 0.178.

### Assignment 3 (due before session 4, 10 points)

1. By hand, compute s, z and the integers for x = (−0.4, 0.05, 0.7, 2.2) with 4-bit asymmetric and 4-bit symmetric quantization, and the largest error of each. Check with the notebook. (3 points)
2. Complete both TODO cells and explain when a zero point helps weights, and which percentiles are safe with the glitched calibration set. (4 points)
3. Change the integer-only pass to int4 weights (per channel, levels −7…7) with uint8 activations. Report accuracy, agreement with float and the byte count. (3 points)

Hand in one PDF and your notebook.

### Sources

- Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. https://arxiv.org/abs/1712.05877
- Krishnamoorthi 2018, Quantizing Deep Convolutional Networks for Efficient Inference: A Whitepaper. https://arxiv.org/abs/1806.08342
- Nagel et al. 2021, A White Paper on Neural Network Quantization. https://arxiv.org/abs/2106.08295

## Session 4: Quantization II: training-aware and LLM quantization

**Goal:** students can train with fake quantization and the straight-through estimator, quantize weights in groups, and handle activation outliers as LLM quantization methods do.

### Talking pointers

- **Open with:** "At 8 bits, quantization after training usually just works. Below 4 bits it breaks, and in large language models (LLMs) a few huge activations break it even at 8. Today we fix both."
- **Segment 1, say:** write `w + (wq - w).detach()` on the board and explain its value and its gradient, then show the PTQ against QAT table.
- **Segment 2, say:** draw one weight row cut into groups of 32, each with its own scale, then show the group-size errors and the bits-per-weight table.
- **Segment 3, say:** draw one input channel 30 times taller than the rest, then show the W8A8 errors before and after SmoothQuant.
- **Close with:** "Report the true bits per weight, and test the quantized model on the task and the language you care about." Then set assignment 4.

### Segment 1 (7 min): quantization-aware training

- **Post-training quantization** (PTQ) quantizes a trained model with a little calibration data. **Quantization-aware training** (QAT) trains with **fake quantization**: the forward pass uses rounded weights and activations, while the optimizer updates float copies (Jacob et al. 2018).
- Rounding has zero gradient almost everywhere. The **straight-through estimator** (STE) treats it as the identity in the backward pass (Bengio, Léonard & Courville 2013), so the float weights keep learning to sit where rounding hurts least.
- At 8 bits PTQ is normally enough; QAT is often needed at 4 bits and below (Nagel et al. 2021). Our small CNN still managed W4A8 PTQ (4-bit weights, 8-bit activations: 0.978, as float), but W3A8 PTQ gave 0.948 against QAT 0.981, and W2A8 PTQ 0.372 against QAT 0.957.
- A cheaper alternative is **mixed precision**: keep the most sensitive layers, often the first and last, at 8 bits. In the lab this alone lifted W2A8 PTQ to 0.963, as good as QAT.
- Compare fairly: a control with 8 extra float epochs, then PTQ, scored 0.350 at 2 bits, so QAT's gain came from training with quantization.
- **Pause and try:** the loss gradient with respect to a fake-quantized weight is −0.8. What gradient reaches the float weight with the STE, and without it?
  - **Answer:** −0.8 with the STE, which passes it straight through; 0 without, because rounding is flat between levels.

### Segment 2 (7 min): quantizing language models

- Decoding one token is a matrix–vector product, which is memory-bound (session 1). So LLMs are usually quantized **weight-only**: int4 weights, 16-bit activations, and weights expanded just before the multiply. Fewer bytes means faster tokens.
- At 4 bits one scale per row is too coarse, so rows are cut into **groups** of 32 to 128 weights with a scale each. Lab, synthetic LLM-like layer: output error 0.313 with one scale per row, 0.148 with groups of 128, 0.094 with groups of 32.
- **GPTQ** (Frantar et al. 2023) quantizes the weights one column at a time and adjusts the remaining weights to cancel the error, using second-order information from calibration data. **AWQ** (Lin et al. 2024) finds the few weight channels that meet large activations and scales them up before quantization, so they get finer steps.
- **NF4** (4-bit NormalFloat; Dettmers et al. 2023) places 16 levels at quantiles of a normal distribution, which suits normally distributed weights; in the lab it beat uniform int4 (output error 0.0885 against 0.1178).
- llama.cpp stores models in GGUF files with block formats such as Q8_0, Q4_0 and the "K-quants" (for example Q4_K_M, which mixes block types across tensors). Course 3 session 4 quantizes a 1B-parameter model with GPTQ or bitsandbytes through Hugging Face.
- Measure the speed: on one token, ONNX Runtime's int4 kernel was 3.23 and 4.04 times faster than float32 (blocks of 32 and 128) for 6.4 and 7.5 times fewer bytes (saved run, busy machine).
- **Pause and try:** int4 weights in groups of 64 with a float16 scale per group. How many bits per weight, and how big is a 3-billion-parameter model?
  - **Answer:** 4 + 16/64 = 4.25 bits, so 3 × 10⁹ × 4.25 / 8 ≈ 1.59 GB, before any tensors kept at higher precision.

### Segment 3 (6 min): activation outliers and evaluation

- Large Transformers develop a few input channels with huge activations. With one int8 scale per tensor, those channels set the range and the rest get few levels. **LLM.int8()** (Dettmers et al. 2022) multiplies the outlier channels in 16-bit floats and the rest in int8.
- **SmoothQuant** (Xiao et al. 2023) divides each activation channel by $s_j = \max|X_j|^\alpha / \max|W_j|^{1-\alpha}$ and multiplies the matching weight column by $s_j$. The product is unchanged, and the factors fold into the previous layer. Lab W8A8 (8-bit weights and activations) output error: 0.0722 baseline, 0.0301 with SmoothQuant (α = 0.5), 0.0071 with the LLM.int8()-style split.
- Keep sensitive layers (embeddings, the output layer, sometimes the first layers) at higher precision, and count them in the size.
- Evaluate a quantized model on the tasks and languages you care about, not only perplexity: Course 3 session 4 warns that a small perplexity change can hide large losses in Bangla, and Course 4 session 10 notes that small models can lose more from quantization. Read Bangla outputs side by side.
- **Pause and try:** with α = 0.5, an input channel has max|X_j| = 100 and its weight column max|W_j| = 0.04. What is $s_j$, and what are the two maxima afterwards?
  - **Answer:** $s_j = \sqrt{100}/\sqrt{0.04} = 10/0.2 = 50$. The activations' maximum becomes 100/50 = 2 and the weights' 0.04 × 50 = 2: α = 0.5 balances them.

### Lab guide (about 2 hours, notebook `s04_qat_and_llm_quantization.ipynb`)

1. Sections 1–2 (40 min): the float CNN and `fq_weight` (find the STE line); the PTQ, mixed-precision, control and QAT table.
2. Sections 3–4 (40 min): group sizes and NF4; W8A8 errors with three treatments of outliers.
3. Sections 5–6 (20 min): bits per weight, then the 4-bit kernel timings.
4. TODO cells (20 min): SmoothQuant's α, and AWQ-style scaling.

- **Expect:** float CNN 0.978. PTQ / first-and-last-8-bit / control / QAT: 0.978 / 0.974 / 0.970 / 0.976 (W4A8); 0.948 / 0.976 / 0.969 / 0.981 (W3A8); 0.372 / 0.963 / 0.350 / 0.957 (W2A8). Int4 output errors 0.684 (per tensor), 0.313 (per row), 0.148, 0.118 and 0.094 (groups of 128, 64, 32); NF4 0.0885 against 0.1178. W8A8 errors 0.0722, 0.0071 and 0.0301. Saved-run timings at one token: float32 4.727 ms, int4 1.462 ms (blocks of 32) and 1.171 ms (blocks of 128). Runtime about 17 seconds.
- **Common problems:** forgetting `.detach()`, so no gradient reaches the weights; comparing QAT with PTQ without a same-epochs control; ignoring scales in the model size.

### Quiz

1. Why does QAT need the straight-through estimator?
   - **Answer:** rounding has zero gradient almost everywhere, so without the STE no gradient would reach the weights.
2. Why are LLMs usually quantized weight-only to 4 bits, rather than to W8A8?
   - **Answer:** decoding is memory-bound, so the time is set by the bytes of the weights; 4-bit weights cut those bytes most, and activations can stay in 16 bits.
3. What does SmoothQuant move, and from where to where?
   - **Answer:** quantization difficulty, from the activations (outlier channels) to the weights, by rescaling each channel; the layer's output is unchanged.

**Watch out:** "Bits per weight tells you the model size." A 4-bit model also stores scales (llama.cpp's Q4_0 costs 4.5 bits per weight: 562.5 MB per billion weights, not 500 MB), sometimes zero points, and some tensors at higher precision. At run time it also needs RAM for the key–value (KV) cache and activations (session 8).

### Assignment 4 (due before session 5, 10 points)

1. Complete both TODO cells: report the W8A8 error for α from 0 to 1 and the int4 error for the AWQ-style factors, and explain both curves. (4 points)
2. Repeat section 2 with three seeds and report the mean and range for PTQ, mixed precision and QAT at 3 and 2 bits. Which conclusions survive? (3 points)
3. A phone has 2 GB of free RAM. Choose a format from section 5 for a 1.5-billion-parameter model, show your size calculation, and list what else must fit in that RAM. (3 points)

Hand in one PDF and your notebook.

### Sources

- Bengio, Léonard & Courville 2013, Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. https://arxiv.org/abs/1308.3432
- Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. https://arxiv.org/abs/1712.05877
- Nagel et al. 2021, A White Paper on Neural Network Quantization. https://arxiv.org/abs/2106.08295
- Dettmers et al. 2022, LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale. https://arxiv.org/abs/2208.07339
- Xiao et al. 2023, SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. https://arxiv.org/abs/2211.10438
- Frantar et al. 2023, GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers. https://arxiv.org/abs/2210.17323
- Lin et al. 2024, AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration. https://arxiv.org/abs/2306.00978
- Dettmers et al. 2023, QLoRA: Efficient Finetuning of Quantized LLMs (NF4). https://arxiv.org/abs/2305.14314
- llama.cpp (GGUF format and quantization types). https://github.com/ggml-org/llama.cpp
- ONNX Runtime documentation. https://onnxruntime.ai/docs/

## Session 5: Pruning and sparsity

**Goal:** students can prune networks by magnitude and by channel, measure what sparsity does to accuracy and latency, and test a lottery-ticket claim on a small scale.

### Talking pointers

- **Open with:** "Most weights in a trained network can be removed with little loss of accuracy. The hard question is whether removing them makes anything faster. Today we measure both."
- **Segment 1, say:** show the accuracy-against-sparsity plot: where does each method break?
- **Segment 2, say:** draw a CSR matrix on the board (values, column indices, row pointers), then show the speed-up plot against the ideal curve.
- **Segment 3, say:** show the channel-pruning table, especially the small network trained from scratch.
- **Close with:** "Report sparsity, real speed and accuracy together, against the strongest simple baseline." Then set assignment 5.

### Segment 1 (7 min): magnitude pruning and lottery tickets

- **Pruning** removes weights; **sparsity** is the fraction removed. **Magnitude pruning** removes the weights with the smallest absolute values, then fine-tunes the rest (Han et al. 2015). Pruned weights stay at zero through a 0/1 mask.
- Han et al. (2015) cut AlexNet's parameters 9 times (61 million to 6.7 million) and VGG-16's 13 times with no loss of accuracy, by pruning and retraining in several rounds.
- **One-shot** pruning removes everything at once; **iterative** pruning removes a little, fine-tunes, and repeats. Lab MLP (dense 0.983), same 12 fine-tuning epochs: up to 90% both kept 0.980; at 98% one-shot fell to 0.481 and iterative kept 0.787. Without fine-tuning, 90% sparsity already gave 0.804.
- The **lottery ticket hypothesis** (Frankle & Carbin 2019): a dense network contains a sparse subnetwork that, trained alone from its original initial weights, matches the dense network. The test needs a control: the same mask with new random initial weights. Course 2 session 3 runs the iterative version.
- In our one-shot test at 95% sparsity, the rewound ticket averaged 0.961 against 0.943 for the control (ahead in all three seeds), but neither matched the dense 0.980.
- **Pause and try:** the lab's iterative schedule keeps a fraction $(1-s)^{r/4}$ of the weights after round r. For a 90% target, what is the sparsity after round 2?
  - **Answer:** $1 - 0.1^{0.5} = 1 - 0.316 ≈ 68\%$.

### Segment 2 (7 min): unstructured, structured and N:M sparsity

- **Unstructured** sparsity removes single weights anywhere. A sparse format such as CSR (compressed sparse row) stores each kept value with its column index, so in float32 it needs about 8 bytes per kept weight against 4 per weight when dense, and its memory accesses are irregular.
- Lab, 4,096 × 4,096 matrix–vector product on one thread: SciPy's CSR was slower than dense at 50% sparsity (0.54), broke even between 70% and 80%, and was 2.37 times faster at 90% and 10.14 times at 98%, always far below the ideal 1/(1 − sparsity).
- Phone CPUs and accelerators are built for dense, regular blocks of data, so unstructured sparsity rarely speeds them up unless it is very high and the runtime has sparse kernels for that layer.
- **Structured** pruning removes whole filters or channels, leaving a smaller dense network. Li et al. (2017) remove the filters with the smallest **L1 norms**. In the lab, halving every convolution cut the MACs 3.96 times and ran 1.87 times faster at batch 1, 3.26 times at batch 64, in plain PyTorch.
- **N:M sparsity** keeps N of every M consecutive weights. 2:4 sparsity is exactly 50% and lets NVIDIA's Ampere GPUs skip the zeros in hardware (Mishra et al. 2021); phone CPUs lack such hardware, so check what your phone's accelerator supports. In the lab, 2:4 matched unstructured 50% after fine-tuning (0.981 against 0.980).
- **Pause and try:** a 4,096 × 4,096 float32 matrix at 90% sparsity in CSR with int32 indices. Roughly how many bytes, against 67.1 MB dense?
  - **Answer:** 1.68 million kept values × (4 + 4) bytes ≈ 13.4 MB, plus 16 kB of row pointers: 5 times smaller, not 10. The notebook prints 13.4 MB.

### Segment 3 (6 min): fair evaluation, and pruning with quantization

- Blalock et al. (2020) reviewed 81 pruning papers and found that results were hard to compare: different architectures, metrics and baselines, and few repeated runs. Report accuracy, size and measured latency together, with several seeds.
- Compare with the simplest strong baseline: the small architecture trained from scratch for as many epochs. In the lab it scored 0.983, better than pruning plus fine-tuning (0.972): here, pruning was not worth its cost.
- Deep Compression (Han, Mao & Dally 2016) chained pruning, quantization with shared weights, and Huffman coding, shrinking AlexNet 35 times and VGG-16 49 times without loss of accuracy.
- In the lab, the 90%-sparse MLP kept 0.980 with int8 values; in CSR with one-byte indices it took 23,172 bytes, 14.7 times less than dense float32.
- **Pause and try:** that MLP keeps 8,448 weights. How many bytes do its int8 values and one-byte column indices need?
  - **Answer:** 8,448 × 2 = 16,896 bytes. Row pointers, scales and biases bring the total to 23,172.

### Lab guide (about 2 hours, notebook `s05_pruning.ipynb`)

1. Sections 1–2 (30 min): train the dense MLP; read `magnitude_masks`; compare the three pruning curves and 2:4.
2. Section 3 (20 min): dense against CSR products; find the break-even sparsity.
3. Section 4 (25 min): channel pruning, batch-norm re-estimation, fine-tuning, and the from-scratch baseline.
4. Section 5 (15 min): the lottery ticket and its control over three seeds.
5. Section 6 (10 min): bytes for pruning plus quantization.
6. TODO cells (20 min): layer-wise against global pruning, and keeping 25% of the channels.

- **Expect:** dense MLP 0.983 with 84,480 weights. One-shot without fine-tuning 0.804 at 90%; with 12 epochs 0.980 at 90%, 0.954 at 95%, 0.481 at 98%; iterative 0.959 and 0.787 at 95% and 98%. 2:4 0.981. Saved-run CSR speed-ups: 0.54 (50%), 1.27 (80%), 2.37 (90%), 10.14 (98%). Channel pruning: 0.993 to 0.098, 0.394 after batch-norm re-estimation, 0.972 after fine-tuning; from scratch 0.983; speed-ups 1.87 (batch 1) and 3.26 (batch 64). Ticket 0.961 against control 0.943. Sizes 340,008, 71,772 and 23,172 bytes. Runtime about 1 minute.
- **Common problems:** forgetting to re-apply the mask after each optimizer step; reporting sparsity without a timing; comparing a pruned model only with the dense one, not with a small model trained directly.

### Quiz

1. Why can a 50%-sparse matrix in CSR be as large as the dense one?
   - **Answer:** CSR stores a 4-byte column index next to every kept 4-byte value, so 50% of the values cost as many bytes as all of them dense.
2. Why does structured pruning give real speed-ups more reliably than unstructured pruning?
   - **Answer:** it leaves a smaller dense network, which every runtime and accelerator runs with its ordinary fast kernels.
3. What does the re-initialized control show in a lottery-ticket experiment?
   - **Answer:** whether the original initial values matter. If the ticket and the control train equally well, the mask alone explains the result.

**Watch out:** "90% sparse means 10 times faster." In the lab, 90% unstructured sparsity made the matrix–vector product 2.37 times faster, and 50% made it slower. The kept weights carry indices, their memory accesses are irregular, and the kernels are less optimized. Speed comes from structure (channels, or N:M on hardware that supports it) or from very high sparsity with good sparse kernels.

### Assignment 5 (due before session 6, 10 points)

1. Complete both TODO cells. Report accuracy for layer-wise and global pruning at 90% and 95%, and the results of keeping 25% of the channels. (4 points)
2. Repeat the lottery-ticket test with five seeds and add a third arm: a random mask with the same sparsity, rewound to $\theta_0$. Which differences are larger than the seed-to-seed spread? (3 points)
3. Repeat section 3 with a 1,024 × 1,024 matrix, which fits in the cache. Does the break-even sparsity move? Explain using session 1's roofline. (3 points)

Hand in one PDF and your notebook.

### Sources

- Han, Pool, Tran & Dally 2015, Learning both Weights and Connections for Efficient Neural Networks. https://arxiv.org/abs/1506.02626
- Han, Mao & Dally 2016, Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding. https://arxiv.org/abs/1510.00149
- Frankle & Carbin 2019, The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks. https://arxiv.org/abs/1803.03635
- Li et al. 2017, Pruning Filters for Efficient ConvNets. https://arxiv.org/abs/1608.08710
- Mishra et al. 2021, Accelerating Sparse Deep Neural Networks. https://arxiv.org/abs/2104.08378
- Blalock et al. 2020, What is the State of Neural Network Pruning? https://arxiv.org/abs/2003.03033

## Session 6: Knowledge distillation

**Goal:** students can train a small student from a large teacher's soft labels, tune temperature and loss weights, and judge when distillation is worth it.

### Talking pointers

- **Open with:** "A large model knows more than its answers show: when it reads a 7, it also knows the 7 looks a little like a 1. Distillation passes that knowledge to a model small enough for a phone. Today we test when that is worth doing."
- **Segment 1, say:** compute the teacher's softmax for logits (4, 2, 0) at T = 1 and T = 2 on the board, then write the loss and explain the T².
- **Segment 2, say:** draw the teacher and the student side by side, with a hint arrow between their middle layers for FitNets.
- **Segment 3, say:** show the two tables: all labels (no clear gain) and 50 labels (a large gain).
- **Close with:** "Always compare a distilled student with the same student trained directly." Then set assignment 6.

### Segment 1 (7 min): soft targets and temperature

- A **teacher** (large, accurate) trains a **student** (small, fast) by giving it targets. The teacher's softmax over classes says more than the label: which wrong answers it finds plausible. Hinton called this **dark knowledge** in his talks on this work (Hinton, Vinyals & Dean 2015).
- Dividing the logits by a **temperature** T > 1 before the softmax softens both distributions. In the lab, the teacher's top probability averaged 0.998 at T = 1 and 0.468 at T = 8.
- The loss is α·CE(labels) + (1 − α)·T²·KL(teacher ‖ student): the cross-entropy (CE) with the labels, at T = 1, plus the Kullback–Leibler (KL) divergence between the teacher's and the student's distributions, both softened with temperature T (Course 11 session 11 covers CE and KL).
- Why T²: the soft term's gradient with respect to a student logit is $(q_i - p_i)/T$, and $q_i - p_i$ itself shrinks like 1/T, so the gradient shrinks like 1/T². The factor T² restores its size, so α keeps its meaning. In the lab, without the factor the gradient fell 3.65 times from T = 4 to T = 8, and accuracy at T = 8 dropped from 0.957 to 0.906.
- On MNIST, a small network's test errors fell from 146 to 74 when it also matched a large network's soft targets at T = 20 (Hinton et al. 2015).
- **Pause and try:** a teacher's logits are (4, 2, 0). What are its probabilities at T = 1 and at T = 2?
  - **Answer:** about (0.87, 0.12, 0.02) and (0.67, 0.24, 0.09). At T = 2 it is clear that the second class is far more plausible than the third.

### Segment 2 (7 min): variants

- **Feature distillation:** FitNets (Romero et al. 2015) also asks a middle layer of a thinner, deeper student to predict a middle layer of the teacher (a "hint"), through a small learned regressor, which helps train students that are hard to optimize.
- **DistilBERT** (Sanh et al. 2019) halves BERT's layers, starts the student from the teacher's weights, and trains it with a distillation loss, the masked-language-model loss and a cosine loss on hidden states. It is 40% smaller and 60% faster, and keeps 97% of BERT's language-understanding score.
- **Sequence-level distillation** for large language models (LLMs) trains the student on text that the teacher generates, which works even without the teacher's probabilities. Course 3 session 12 uses it to design a small Bangla LLM.
- The student need not copy the teacher's shape: it can be shallower, narrower, or a different kind of network, as long as it produces the same outputs.
- **Pause and try:** a FitNets hint maps the student's 16 hidden units to the teacher's 512 through a linear regressor. How many weights does the regressor have, and does it ship with the student?
  - **Answer:** 16 × 512 = 8,192 weights plus 512 biases. No: it is used only during training.

### Segment 3 (6 min): data, baselines and the pipeline

- Distillation needs inputs, not labels, so the **transfer set** can be unlabelled or augmented data. Lab, 50 labelled images: the student alone scored 0.840; distilled on the same 50 images, 0.892; with shifted copies added, 0.948; with 1,207 unlabelled images, 0.962.
- With all 1,257 labels, distillation gave 0.976 against 0.972 for the student trained directly, inside the seed ranges. When labels are plentiful and the student is close to the teacher, the gain can vanish. Course 4 session 10 makes the same point: compare with an undistilled student trained for as long.
- Against expectation, temperature barely mattered in the lab (0.957 to 0.965 for T from 1 to 8): with many transfer images, even near-one-hot teacher outputs are good labels.
- Pipeline: distil, then quantize. The int8 student kept 0.967 in 1,392 bytes, 865 times smaller than the float32 teacher (0.985). But 249 times fewer parameters made it only 3.5 times faster at batch 1, where fixed overheads dominate.
- **Pause and try:** the 50-label student gains 12 points from distillation, but the teacher was trained on 1,257 labels. What exactly does this comparison show?
  - **Answer:** the value of a strong teacher plus unlabelled data for a student with few labels, not that distillation beats labels. The teacher's training labels did the work indirectly.

### Lab guide (about 2 hours, notebook `s06_distillation.ipynb`)

1. Section 1 (15 min): the teacher, the student and `train_student`; find the T² in the loss.
2. Section 2 (15 min): all labels, three seeds. Is there a gain beyond the seed spread?
3. Section 3 (20 min): 50 labels with three kinds of transfer set.
4. Section 4 (20 min): the temperature and α sweeps and their plot.
5. Section 5 (15 min): gradient sizes with and without T².
6. Section 6 (15 min): quantize the student; sizes and latency.
7. TODO cells (20 min): a FitNets-style hint, and a weak teacher.

- **Expect:** teacher 0.985 (301,066 parameters); student 1,210 parameters. All labels: 0.972 alone, 0.976 distilled (α = 0.5), 0.972 (α = 0.1). 50 labels: 0.840, 0.892, 0.948 and 0.962. Temperature sweep 0.965, 0.965, 0.962, 0.957; α sweep 0.957 to 0.962, then 0.952 at α = 0.9. Gradient norm without T²: 0.0595 (T = 1) to 0.0033 (T = 8); at T = 8, 0.957 with T² and 0.906 without. Student 0.967 (float32), 0.967 (int8, 1,392 bytes), 0.956 (int4, 800 bytes). Saved-run latency at batch 1: teacher 0.0490 ms, student 0.0139 ms. Runtime about 1 minute.
- **Common problems:** comparing the student with the teacher instead of with the same student trained directly; forgetting T², so large temperatures silently switch the soft term off; using `F.kl_div` with probabilities instead of log-probabilities as its first argument.

### Quiz

1. What does the temperature T do to the teacher's targets?
   - **Answer:** dividing the logits by T > 1 flattens the softmax, so the small probabilities of wrong classes become visible to the student.
2. Why multiply the soft loss by T²?
   - **Answer:** its gradients shrink like 1/T², so without the factor a high temperature would make the soft term almost vanish.
3. When is distillation most likely to be worth it?
   - **Answer:** when the student has few labels but there is a strong teacher and plenty of unlabelled or augmented inputs; with abundant labels and a capable student, the gain can be negligible.

**Watch out:** "Distillation always beats training the small model directly." In the lab, with all labels, distillation gave 0.976 against 0.972, inside the seed spread; it helped only with few labels and a large transfer set (0.840 to 0.962). Always report the student trained directly, with the same data and steps, over several seeds.

### Assignment 6 (due before session 7, 10 points)

1. Complete both TODO cells: the FitNets-style hint and the weak teacher. Report three-seed results and explain where distillation's gains came from. (4 points)
2. Repeat sections 2 and 3 with students of 8, 32 and 64 hidden units. Plot the gain from distillation against student size in both settings. (3 points)
3. Make a table of teacher and student, each in float32 and int8: accuracy, bytes and batch-1 latency. Choose one for a phone app with a 50 kB model budget, and justify the choice. (3 points)

Hand in one PDF and your notebook.

### Sources

- Hinton, Vinyals & Dean 2015, Distilling the Knowledge in a Neural Network. https://arxiv.org/abs/1503.02531
- Romero et al. 2015, FitNets: Hints for Thin Deep Nets. https://arxiv.org/abs/1412.6550
- Sanh et al. 2019, DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. https://arxiv.org/abs/1910.01108

## Session 7: Model formats and runtimes

**Goal:** students can fold layers, export a PyTorch model to ONNX, run and quantize it with ONNX Runtime, and check that the converted model still gives the right answers.

### Talking pointers

- **Open with:** "A model that works in your notebook is not yet a model on a phone. In between sits a conversion step, where silent bugs live. Today we convert a model and prove it still gives the same answers."
- **Segment 1, say:** fold a convolution and its batch normalization into one convolution on the board, then show the exported graph without BatchNormalization.
- **Segment 2, say:** draw the paths from PyTorch to ONNX Runtime, LiteRT, ExecuTorch and Core ML, each ending in a CPU, GPU or NPU.
- **Segment 3, say:** show the failed batch-8 call, the quantizer error, and the table of difference, agreement and accuracy.
- **Close with:** "Every conversion gets a test: real inputs, both models, a tolerance, and the version numbers written down." Then set assignment 7.

### Segment 1 (7 min): from a training graph to a deployable model

- A training framework runs a model as Python code, one operator at a time (eager mode). A deployable model is a fixed graph of operators and weights in a file that a small runtime loads without Python.
- ONNX (Open Neural Network Exchange) is an open format for such graphs, with standard operators in versioned sets (opsets); the notebook used opset 20. Since PyTorch 2.9, `torch.onnx.export` captures the model with `torch.export` (`dynamo=True`), specialized to the example input's shape.
- Graph optimizations make the graph cheaper: constant folding (compute ahead of time anything that does not depend on the input), operator fusion (one kernel does a convolution and its ReLU in one pass), and layout changes.
- Folding batch normalization (BN): at inference BN is a fixed scale and shift per channel, so convolution plus BN is one convolution with $W' = sW$ and $b' = s(b - \mu) + \beta$, where $s = \gamma/\sqrt{\sigma^2 + \epsilon}$ (Jacob et al. 2018 fold BN this way before quantizing).
- **Pause and try:** after a convolution with bias $b = 3$, a BN channel has $\gamma = 2$, $\beta = 0.5$, $\mu = 1$, $\sigma^2 = 3.99$ and $\epsilon = 0.01$. What are the folded scale $s$ and bias $b'$?
  - **Answer:** $s = 2/\sqrt{4} = 1$, so $W' = W$ and $b' = 1 \times (3 - 1) + 0.5 = 2.5$.

### Segment 2 (7 min): runtimes and delegates

- ONNX Runtime (Microsoft) runs ONNX files on servers, browsers and phones through execution providers: its Android package includes XNNPACK and NNAPI, its iOS package XNNPACK and Core ML, and a QNN provider targets Qualcomm NPUs.
- LiteRT is Google's runtime, renamed from TensorFlow Lite in 2024, for `.tflite` files. PyTorch models convert with `litert-torch` (formerly `ai-edge-torch`). As of November 2026, Google recommends its CompiledModel API, which picks the CPU (through XNNPACK), the GPU or a supported NPU.
- ExecuTorch is PyTorch's on-device runtime (version 1.0, October 2025). After `torch.export`, parts of the graph are lowered to a backend (XNNPACK for Arm CPUs, Vulkan GPUs, Core ML, or Qualcomm, MediaTek and Arm NPUs) and saved as a `.pte` file.
- On iPhones, Core ML runs models converted with `coremltools`; at WWDC 2026 Apple introduced Core AI, a new framework for running AI models on Apple silicon.
- A delegate (ONNX Runtime says execution provider, ExecuTorch says backend) takes the operators the accelerator supports; the rest fall back to the CPU, and every switch copies activations. Android's NNAPI was deprecated in Android 15 in favour of LiteRT.
- **Pause and try:** an NPU delegate supports 95% of your model's operators, but the unsupported 5% are spread through the network and split it into 10 pieces. Can you count on a speed-up?
  - **Answer:** no. Each boundary copies activations between NPU and CPU, and the CPU pieces still run slowly. Measure, and consider replacing the unsupported operators.

### Segment 3 (6 min): checking the converted model

- Kernels add numbers in different orders, so a float32 conversion changes outputs by rounding ($4 \times 10^{-6}$ in the notebook). Compare outputs on real inputs with a tolerance, then check top-1 agreement and the task metric.
- Unsupported operators stop the export or run on a slow fallback path. Shapes matter too: the notebook's batch-1 model rejected a batch of 8 until it was re-exported with a symbolic batch dimension.
- Quantized models cannot pass a float tolerance; judge them by agreement and accuracy (sessions 3 and 4).
- Pin versions: record the PyTorch, ONNX and ONNX Runtime versions and the opset. In the notebook, quantizing the exported file directly failed with a shape-inference error; ONNX Runtime's pre-processing step fixed it.
- Repeat the check on the phone, whose kernels differ again.
- **Pause and try:** after a float32 conversion, the largest logit difference is 0.15 but all 450 predictions agree. Is the conversion correct? And after int8 quantization?
  - **Answer:** for float32, no: rounding differences should be near $10^{-5}$, so 0.15 points to a bug, such as different preprocessing. For int8, it is normal quantization error (the notebook saw 0.155); judge by agreement and accuracy.

### Lab guide (about 2 hours, notebook `s07_formats_runtimes.ipynb`)

1. Section 1 (15 min): on Colab or Kaggle, first run `pip install onnx onnxscript onnxruntime`. Train the CNN.
2. Section 2 (15 min): derive the BN folding on paper, then check it in code.
3. Sections 3–4 (25 min): export, read the node list, check the conversion, compare latency.
4. Section 5 (15 min): the five optimization levels and their node lists.
5. Section 6 (20 min): dynamic int8 quantization.
6. Section 7 (10 min): the batch-8 failure and the dynamic-batch export.
7. TODO cells (20 min): static quantization; folding BN into a linear layer.

- **Expect:** test accuracy 0.9867 throughout; 38,378 parameters, 365,184 MACs. Folding: largest difference 3.81e-06, 38,282 parameters, 89.8 µs against 111.9 µs. The ONNX graph has 10 nodes and no BatchNormalization; the file was 163,913 bytes in the saved run. ONNX Runtime matches to 3.81e-06 and takes 23.3 µs against PyTorch's 109.3 µs. Optimization levels: 31.5 µs (none) to 29.2 µs (Extended, 7 nodes) to 16.5 µs (All, NCHWc). Direct `quantize_dynamic` fails with a ShapeInferenceError; after pre-processing, int8 is 48,174 bytes with 100% agreement but 93.2 µs against 17.9 µs; linear layers only, 62,839 bytes and 19.7 µs. Per image, batch 1 takes 26.9 µs and batch 64 takes 6.6 µs. Runtime about 13 seconds. Latencies are from the saved run on a shared server CPU and vary; ONNX file sizes can change by a few bytes from one export to the next.
- **Common problems:** exporting without `model.eval()`, so BN uses batch statistics; checking a conversion on random noise instead of real inputs; reading ONNX Runtime's speed-up over PyTorch at batch 1 as a property of phones.

### Quiz

1. Why can batch normalization be folded into the convolution before it at inference, but not during training?
   - **Answer:** at inference BN uses fixed running statistics, so it is a fixed per-channel scale and shift that merges into the weights and bias. In training it uses each batch's statistics, which change every step.
2. What does a delegate or execution provider do, and what happens to the operators it does not support?
   - **Answer:** it runs the part of the graph that the accelerator supports, such as a GPU or NPU. Unsupported operators run on the CPU, with copies at every boundary.
3. Why was dynamic int8 quantization slower than float32 for the notebook's CNN?
   - **Answer:** its convolutions became `ConvInteger` and each layer quantized its input at run time, which was slower than the optimized float32 convolution. ONNX Runtime recommends static quantization for CNNs.

**Watch out:** "Conversion is exact, so the converted model needs no testing." In the notebook, the batch-1 model rejected a batch of 8, and the quantizer failed until the file was pre-processed. Even a good float32 conversion changes the numbers slightly. Test every converted model on real inputs, with a tolerance, and again on the device.

### Assignment 7 (due before session 8, 10 points)

1. Complete the BN-into-linear TODO, and derive the folding formula on paper for one channel. (3 points)
2. Complete the static quantization TODO. Tabulate file size, accuracy, top-1 agreement and batch-1 latency for float32, both dynamic int8 versions and static int8, and explain the latencies. (4 points)
3. Write a reusable conversion test (real inputs, a tolerance, an agreement threshold, printed versions). Run it on the dynamic-batch model and one int8 model; say which checks each passes. (3 points)

Hand in one PDF and your notebook.

### Sources

- Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. https://arxiv.org/abs/1712.05877
- ONNX, Open Neural Network Exchange. https://onnx.ai/
- ONNX Runtime documentation: graph optimizations, quantization, and deploying on mobile. https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html ; https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html ; https://onnxruntime.ai/docs/tutorials/mobile/
- PyTorch documentation, torch.onnx. https://docs.pytorch.org/docs/stable/onnx.html
- Google AI Edge, LiteRT overview. https://developers.google.com/edge/litert/overview ; LiteRT Torch converter. https://github.com/google-ai-edge/litert-torch
- PyTorch 2025, Introducing ExecuTorch 1.0. https://pytorch.org/blog/introducing-executorch-1-0/ ; ExecuTorch documentation, model export. https://docs.pytorch.org/executorch/stable/using-executorch-export.html
- Apple, Core ML Tools: PyTorch conversion workflow. https://apple.github.io/coremltools/docs-guides/source/convert-pytorch-workflow.html ; Core AI documentation. https://developer.apple.com/documentation/coreai
- Android Developers, NNAPI migration guide. https://developer.android.com/ndk/guides/neuralnetworks/migration-guide

## Session 8: Memory: weights, activations and the KV cache

**Goal:** students can compute peak memory from tensor lifetimes, reduce it by changing execution order or tiling, and size an LLM's KV cache for a phone.

### Talking pointers

- **Open with:** "A phone with 4 GB of RAM does not give your app 4 GB, and an app that asks for too much is closed. Today we count exactly how much memory a model needs while it runs, and how to make that number smaller."
- **Segment 1, say:** list what RAM must hold, then show the per-layer bar chart with its red peak and the weights line.
- **Segment 2, say:** draw the two-branch block, write the live memory after each step for both orders, then draw one patch and its halo.
- **Segment 3, say:** write the KV-cache formula, work out example A at 4,096 tokens by hand, then show the plot with the 1 GB line.
- **Close with:** "Memory is a schedule, not a file size: count what is alive at the worst moment." Then set assignment 8.

### Segment 1 (6 min): what has to be in RAM

- Storage (flash) holds the model file; RAM holds what is in use. Peak memory = weights + live activations + workspace (temporary buffers inside kernels) + the runtime itself.
- On a low-cost phone the app shares a few gigabytes with the operating system and other apps; when memory runs short, Android closes apps.
- Memory-mapping: llama.cpp maps the weight file instead of copying it. Pages are read when first touched, and the system can drop them and re-read them later. In the notebook, a mapped 100 MB file cost nothing until read; `np.load` copied all 100.0 MB into app memory.
- For the notebook's CNN on 96 × 96 images, the int8 weights take 17,040 bytes but one layer's input and output take 138,240 bytes. For a language model, the weights and the KV cache dominate.
- **Pause and try:** a layer reads a 48 × 48 × 48 int8 tensor and writes a 24 × 24 × 48 one. How much activation memory is live while it runs?
  - **Answer:** 110,592 + 27,648 = 138,240 bytes, the notebook's peak.

### Segment 2 (7 min): lifetimes, order and patches

- A tensor is live from the operator that writes it until the last operator that reads it. The peak is the largest total of live tensors at any moment; runtimes plan buffers from this in advance.
- A graph with branches has many valid orders. Finishing one branch before starting the next (depth-first) frees its large tensors sooner. In-place operators, such as a ReLU that overwrites its input, save a buffer; a skip connection keeps its input alive until the add.
- Patch-based inference (MCUNetV2, Lin et al. 2021) runs the high-resolution first stage on one spatial patch at a time and writes each result into the stage's output. Patches overlap at their borders (the halo), so work is repeated; MCUNetV2 also redesigns the network's receptive field to cut that overhead.
- In the notebook, 4 × 4 patches gave the same output with a peak of 65,136 bytes instead of 138,240, for 29.8% more MACs, and ran about ten times slower on this CPU (80 small convolution calls from Python).
- **Pause and try:** input `x` is 9,216 bytes; each branch makes an expansion (55,296 bytes), a depthwise output (55,296) and a projection (9,216). What is the peak if both expansions run first, and if branch 1 finishes first?
  - **Answer:** both expansions first: `x`, two expansions and a depthwise output, 9,216 + 3 × 55,296 = 175,104 bytes. Branch 1 first: `x`, projection 1, expansion 2 and depthwise 2, 2 × 9,216 + 2 × 55,296 = 129,024 bytes.

### Segment 3 (7 min): the KV cache

- A Transformer that generates text keeps the keys and values of every past token (Course 3 session 4): KV bytes = 2 × layers × KV heads × head dimension × tokens × bytes per value, for one sequence.
- Grouped-query attention (GQA; Ainslie et al. 2023) lets several query heads share one key–value head. Example A in the notebook, with 32 query heads sharing 8 KV heads, needs 134.2 MB at 4,096 tokens in float16; without GQA it would need 536.9 MB.
- Quantizing the cache to int8 or int4 halves or quarters it again (plus scales, session 4). Sliding-window layers keep only the last $w$ tokens (512 in example C); Gemma 2 alternates sliding-window and global layers (Gemma Team 2024; Course 9 session 6).
- On a phone, the cache comes on top of the weights (about 0.5 GB for a 1-billion-parameter model at 4 bits). A 1 GB cache holds 30,517 tokens of example A in float16, but only 8,719 of example B, which has more layers and larger heads. These are labelled example configurations; for a real model, read its official `config.json`.
- **Pause and try:** example B has 28 layers and 8 KV heads of dimension 128. With an int8 cache, how many bytes does one token take, and how many tokens fit in 1 GB ($10^9$ bytes)?
  - **Answer:** 2 × 28 × 8 × 128 × 1 = 57,344 bytes per token, so about 17,438 tokens, as the notebook prints.

### Lab guide (about 2 hours, notebook `s08_memory.ipynb`)

1. Section 1 (20 min): find the peak layer by hand from the shapes, then check the printout.
2. Section 2 (20 min): write the depth-first live-memory trace by hand; compare with the code.
3. Section 3 (30 min): draw the input region that one 6 × 6 output patch needs (31 × 31 pixels); run the patch sizes.
4. Section 4 (20 min): the KV-cache table and plot.
5. Section 5 (10 min): memory-mapping (Linux, Colab or Kaggle).
6. TODO cells (20 min): real model configurations; an in-place add.

- **Expect:** 17,040 int8 weights, 5,249,088 MACs; peak 138,240 bytes at layer 5 (366,912 if every activation is kept). Breadth-first 175,104 bytes, depth-first 129,024, the best of 20 orders. Patches match to 6.0e-08, with peaks of 92,208 (2 × 2), 65,136 (4 × 4) and 58,080 bytes (8 × 8) for 14.3%, 29.8% and 65.0% extra MACs; 4 × 4 took 5.63 ms against 0.56 ms (saved run). KV cache at 4,096 tokens in float16: A 134.2 MB (allocated: 134,217,728 bytes, as the formula says), B 469.8 MB, C 28.3 MB; tokens in 1 GB: A 30,517 / 61,035 / 122,070 (float16 / int8 / int4), B 8,719 / 17,438 / 34,877. Memory-mapping: 0.0, 25.2 and 100.0 MB file-backed; `np.load` 100.0 MB of app memory. Runtime about 6 seconds.
- **Common problems:** counting KV heads as query heads; mixing up MB and MiB (the notebook uses $10^6$ bytes); forgetting that a skip connection keeps its input alive; expecting `/proc/self/status` on Windows or macOS.

### Quiz

1. Why does the high-resolution start of a CNN usually set its peak activation memory?
   - **Answer:** an activation has height × width × channels values. Early layers have large height and width, and expansion layers multiply the channels, so the largest input + output pairs come there.
2. How can two valid execution orders of the same graph need different peak memory?
   - **Answer:** a tensor stays live until its last reader runs. An order that finishes one branch before starting another frees large tensors sooner, so fewer are alive at once.
3. A model has 32 query heads and 8 KV heads. How does its KV cache compare with full multi-head attention?
   - **Answer:** it is four times smaller, because keys and values are stored for 8 heads instead of 32.

**Watch out:** "The model's file size is all the memory it needs." The notebook's CNN stores 17,040 bytes of int8 weights but needs 138,240 bytes of activations at its peak, and example B's KV cache reaches 469.8 MB at 4,096 tokens in float16. Add workspace and the runtime itself, and measure peak memory on the device.

### Assignment 8 (due before session 9, 10 points)

1. Predict, by hand, the peak activation memory of the section 1 network for a 128 × 128 input, then check it in code. (3 points)
2. Complete both TODO cells: configurations of two real models from their official `config.json` files (give the links), and the in-place add. (4 points)
3. A phone app may use 1.5 GB. For one model from task 2, choose weight and KV-cache formats and find the longest context that fits with 20% spare memory. Explain the trade-off. (3 points)

Hand in one PDF and your notebook.

### Sources

- Lin et al. 2021, MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning. https://arxiv.org/abs/2110.15352
- Ainslie et al. 2023, GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints. https://arxiv.org/abs/2305.13245
- Gemma Team 2024, Gemma 2: Improving Open Language Models at a Practical Size. https://arxiv.org/abs/2408.00118
- Sandler et al. 2018, MobileNetV2: Inverted Residuals and Linear Bottlenecks. https://arxiv.org/abs/1801.04381
- llama.cpp (memory-mapped GGUF weights). https://github.com/ggml-org/llama.cpp

## Session 9: Small language models and speech on the phone

**Goal:** students can estimate decoding speed from memory bandwidth, measure the effect of a KV cache and quantization, and choose a small model and runtime for a phone.

### Talking pointers

- **Open with:** "Can a low-cost phone run a language model with no internet connection? The answer is a calculation, not an opinion, and today we do it."
- **Segment 1, say:** write tokens per second ≈ bandwidth ÷ bytes per token, work out a 1 B model at 4.5 bits on 34.1 GB/s, then show the plot.
- **Segment 2, say:** show the tokens-per-second table, name the runtimes, and read one Bangla answer from a small model aloud.
- **Segment 3, say:** list Whisper's sizes, then run whisper.cpp's tiny model on a laptop or phone and talk about battery and heat.
- **Close with:** "On a phone, memory sets the speed: read fewer bytes per token, and keep the cache." Then set assignment 9.

### Segment 1 (7 min): what sets the speed of decoding

- Generation has two phases. **Prefill** processes the whole prompt at once with matrix–matrix products, so each weight read is reused for many tokens. **Decode** produces one token at a time with matrix–vector products: every weight is read once per token for about 2 floating-point operations, so the processor waits for memory (the roofline model, session 1).
- So an upper bound is tokens per second ≈ memory bandwidth ÷ bytes read per token, where the bytes are the weights plus the KV cache (session 8).
- In the notebook, one 403 MB matrix times one token vector streamed at 14.6 GB/s but computed only 7.3 GFLOP/s; 128 tokens at once reached 116.7 GFLOP/s.
- Phone memory bandwidth, as assumed theoretical peaks: LPDDR4X on a 32-bit or 64-bit bus gives 17.1 or 34.1 GB/s, LPDDR5X on a 64-bit bus 68.3 GB/s. Real phones reach less, and the screen, camera and other apps share it.
- Quantization speeds up decoding mainly by reading fewer bytes: a 1 B model needs 2 GB in float16 (at most 8.6 tokens per second at 17.1 GB/s) but 0.56 GB at 4.5 bits per weight (30.4).
- **Pause and try:** a 3 B model at 4.5 bits per weight runs on a phone with 34.1 GB/s. What is the upper bound on tokens per second?
  - **Answer:** 3 × 10⁹ × 4.5 / 8 = 1.69 GB per token, and 34.1 / 1.69 ≈ 20 tokens per second (the table says 20.2).

### Segment 2 (7 min): runtimes and small models

- llama.cpp runs models stored in its GGUF format, with many quantization types and memory-mapped weights, on CPUs and GPUs, and it builds for Android. ExecuTorch exports language models too (session 7), and Google's LiteRT-LM runs them on top of LiteRT.
- Open models of 0.5–3 billion parameters fit this budget, for example Llama 3.2 (1B, 3B), Gemma 3 (1B) and Qwen3 (0.6B, 1.7B). Check each model card for the licence, the languages and the exact size.
- Bangla is the weak point. Small multilingual models make more grammatical errors in Bangla than in English (Course 4 session 1), and their tokenizers spend more tokens per Bangla word (Course 3 session 2), so each Bangla word is also slower. TituLLMs and the 1B TigerLLM adapt Llama 3.2 to Bangla (Course 4 session 1), and Course 4 builds a small Bangla model from scratch.
- Speculative decoding (Leviathan et al. 2023; Course 3 session 4): a small draft model proposes several tokens and the large model checks them in one pass, with exactly the same output distribution. On a phone, the draft model's weights and cache also cost memory.
- **Pause and try:** a tokenizer needs 1.3 tokens per English word and three times as many per Bangla word. At 20 tokens per second, how long does a 50-word answer take in each language?
  - **Answer:** English: 65 tokens, about 3.3 seconds. Bangla: 195 tokens, about 9.8 seconds.

### Segment 3 (6 min): speech on the phone

- Whisper (Radford et al. 2022) is an encoder–decoder Transformer trained on 680,000 hours of multilingual audio. Its sizes are tiny (39 million parameters), base (74 M), small (244 M), medium (769 M) and large (1,550 M).
- whisper.cpp runs Whisper the same way llama.cpp runs language models, with quantized weights, on CPUs, including phone CPUs.
- Whisper reads audio in 30-second windows; for live captions, apps run it again and again on a sliding window. Smaller models are faster but make more errors, and accuracy depends on how much training audio a language had, so measure Bangla yourself (Course 12 session 2).
- Battery and heat: long generation or transcription keeps the processor busy, and a hot phone slows itself down (session 11). Keep outputs short, stop early, and use an NPU when the runtime supports it.
- **Pause and try:** how large is Whisper tiny in float16, and at 4.5 bits per weight?
  - **Answer:** 39 × 10⁶ × 2 bytes = 78 MB, and 39 × 10⁶ × 4.5 / 8 ≈ 22 MB.

### Lab guide (about 2.5 hours, notebook `s09_small_lms_on_phone.ipynb`)

1. Section 1 (15 min): compute the GB/s from the printed one-token time by hand, then read the plot.
2. Section 2 (15 min): the tokens-per-second table; add a row for your own phone.
3. Sections 3–4 (35 min): train the tiny model, read its text, compare generation with and without the cache.
4. Section 5 (20 min): dynamic int8 quantization.
5. Section 6 (40 min, NOT RUN here): llama.cpp and whisper.cpp on Colab, Kaggle, a laptop or a phone.
6. TODO cells (20 min): speculative decoding; your phone's bound.

- **Expect:** one token on the 403 MB matrix 27.49 ms (14.6 GB/s); 128 tokens 116.7 GFLOP/s, 15.9 times cheaper per token. Bounds for 1 B at 4.5 bits: 30.4, 60.6 and 121.4 tokens/s at 17.1, 34.1 and 68.3 GB/s. Tiny model: 121,253 parameters, validation loss 0.3255 nats (0.470 bits) per character, sentences such as "the farmer in sylhet paid 12 taka for tea on thursday."; identical text with and without the cache, about 0.3 ms per token with it and 0.55 to 2.09 ms without. Int8: 494,281 to 198,931 bytes, loss +4.29%, 0.543 ms against 0.395 ms per token. Measured 2,529 tokens/s against a bound of 30,202. Runtime about 38 seconds; timings from the saved run on a shared server CPU.
- **Common problems:** comparing tokens per second at different prompt lengths or thread counts; forgetting that prefill delays the first token; applying the bandwidth rule to a tiny model; quantizing the embedding table by accident.

### Quiz

1. Why is decoding one token at a time limited by memory bandwidth rather than arithmetic?
   - **Answer:** each weight is read once per token and used for only about 2 floating-point operations, so the processor waits for memory. Prefill reuses each weight for many tokens.
2. What does a KV cache save, and what does it cost?
   - **Answer:** it saves recomputing the keys and values of all earlier tokens at every step, so the time per token stays almost flat (only reading the cache grows with the context). It costs memory that grows with the context (session 8).
3. Why was int8 slower for the notebook's tiny model, and should you expect the same for a 1 B model on a phone?
   - **Answer:** its matrices are tiny, so quantizing activations at every step costs more than it saves. A 1 B model's decoding is memory-bound, and int8 or int4 weights cut the bytes read per token, so it usually speeds up; measure on the device.

**Watch out:** "A 1-billion-parameter model needs a GPU." Decoding speed is set by memory bandwidth, not by arithmetic: at 4.5 bits per weight a 1 B model takes 0.56 GB, with an upper bound of 30.4 tokens per second at an assumed 17.1 GB/s. Phone CPUs run such models with llama.cpp and similar runtimes. The real limits are RAM, battery, heat and quality in Bangla.

### Assignment 9 (due before session 10, 10 points)

1. Complete both TODO cells: the speculative decoding speed-ups, and the bound for your phone with the source of its bandwidth or your assumption. (3 points)
2. Run `llama-bench` on one small GGUF model at two quantization levels (Colab, Kaggle, a laptop or a phone). Report prompt and generation tokens per second with 1 and 4 threads, and compare with the bandwidth bound. (4 points)
3. Ask the same model five Bangla and five English questions. Rate the answers and report tokens per word for each language. (3 points)

Hand in one PDF and your notebook.

### Sources

- Leviathan, Kalman & Matias 2023, Fast Inference from Transformers via Speculative Decoding. https://arxiv.org/abs/2211.17192
- Radford et al. 2022, Robust Speech Recognition via Large-Scale Weak Supervision (Whisper). https://arxiv.org/abs/2212.04356
- llama.cpp. https://github.com/ggml-org/llama.cpp
- whisper.cpp. https://github.com/ggml-org/whisper.cpp
- ExecuTorch documentation, exporting language models. https://docs.pytorch.org/executorch/1.2/llm/export-custom-llm.html
- Google Developers Blog, on-device generative AI with LiteRT-LM. https://developers.googleblog.com/blazing-fast-on-device-genai-with-litert-lm/

## Session 10: TinyML on microcontrollers

**Goal:** students can design a keyword-spotting model that fits a microcontroller's flash and RAM, quantize it to int8, and set a detection threshold.

### Talking pointers

- **Open with:** "A phone has gigabytes of memory. The chip inside a smart switch or a soil sensor may have 256 kilobytes, no operating system, and a battery that must last a year. Today we fit a neural network into that chip."
- **Segment 1, say:** show a microcontroller board, compare its numbers with a phone's, then show the five log-mel images.
- **Segment 2, say:** write the flash and RAM formulas for the DS-CNN, then show the grid plot with the two budget lines.
- **Segment 3, say:** slide a one-second window along a waveform on the board, then show the false accepts against misses plot.
- **Close with:** "On a microcontroller you design for the budget first and for accuracy second, and you judge a detector by its false accepts per hour, not its clip accuracy." Then set assignment 10.

### Segment 1 (6 min): what a microcontroller is

- A microcontroller (MCU) is a small processor with its memory on the same chip: typically about 100 KB to 1 MB of RAM (SRAM), 1 to 2 MB of flash for code and constants, a clock of tens to hundreds of megahertz, power in milliwatts, and no operating system. MCUNet's experiments used an STM32F746, with 320 KB of SRAM and 1 MB of flash.
- Uses: keyword spotting, detecting a person in a low-resolution image, gestures from an accelerometer, and anomalies in machine vibration. TinyML runs all day on a battery, and the data never leaves the device.
- TensorFlow Lite Micro (David et al. 2021), which Google now calls LiteRT for Microcontrollers (as of November 2026), runs models on bare metal: no operating system and no dynamic memory allocation. All tensors live in one fixed block of RAM, the tensor arena, planned in advance as in session 8.
- Fast int8 kernels come from libraries such as Arm's CMSIS-NN for Cortex-M processors, which TensorFlow Lite Micro can use.
- **Pause and try:** a model has 50,000 weights. How much flash does it need in float32 and in int8, and does either fit in a 64 KB budget?
  - **Answer:** 200,000 bytes in float32 (too big) and 50,000 bytes in int8, plus biases and scales; only the int8 version fits.

### Segment 2 (7 min): fitting the budget

- Two separate budgets: **flash** holds the int8 weights, int32 biases and scales, plus the code; **RAM** holds the activations that are alive at the same time, plus buffers for the input.
- For the notebook's DS-CNN, flash grows with the square of the width $C$ (the pointwise layers have $C^2$ weights each), but RAM grows with $C$ times the size of the feature map: $\max(980 + 250C,\ 500C)$ bytes.
- With a budget of 64 KB of flash and 32 KB of RAM, RAM ruled out width 96 (48,000 bytes) while its flash was only 39,976 bytes. Activations, not weights, set the limit.
- MCUNet (Lin et al. 2020) designs the network and the inference engine together: its search first narrows the space to networks that fit the memory, then searches inside it. It reported above 70% ImageNet top-1 accuracy on an off-the-shelf microcontroller.
- MLPerf Tiny (Banbury et al. 2021) is the standard benchmark: keyword spotting, visual wake words (is a person in the picture?), image classification and anomaly detection, each with a reference model.
- The best candidate need not be the biggest that fits: width 32 scored 0.986 on validation and width 64 0.972, at three times the MACs (one run each, so the gap may be noise).
- **Pause and try:** with $C = 48$ channels on 25 × 10 maps, what is the peak activation memory of a depthwise layer in int8?
  - **Answer:** its input and output each hold 25 × 10 × 48 = 12,000 bytes, so 24,000 bytes, as in the grid.

### Segment 3 (7 min): keyword spotting

- Keyword spotting (KWS) listens continuously for a few words. Speech Commands (Warden 2018) is the standard dataset of one-second spoken words; Zhang et al. (2017) found depthwise-separable CNNs gave the best accuracy for the memory on microcontrollers.
- Features: 30 ms frames every 20 ms, a power spectrum, 20 mel bands and a logarithm, so one second becomes a 49 × 20 image. Real systems compute frames as the audio arrives instead of storing a second of audio.
- On a device, a one-second window slides along the audio (every 0.24 s in the notebook), and a keyword fires when its probability passes a threshold; a refractory second prevents double counting.
- Two numbers describe a detector: false accepts per hour on audio without keywords, and the hit rate on keywords. In the notebook, 98.8% clip accuracy still gave 74 false accepts per hour at threshold 0.5; at 0.9 it gave 6 per hour with 79.6% of keywords found.
- A rate near one per hour needs many hours of test audio: zero false accepts in 30 minutes does not prove the rate is below 2 per hour.
- **Pause and try:** a detector makes 3 false accepts in 30 minutes of background audio. How many per hour, and per 16-hour day?
  - **Answer:** 6 per hour, so about 96 a day: far too many for a product that wakes up on its own.

### Lab guide (about 2 hours, notebook `s10_tinyml.ipynb`)

1. Sections 1–2 (20 min): read how each class is made, then compare the five log-mel images.
2. Section 3 (20 min): check the flash and RAM formulas on paper for $C = 32$, $B = 3$, then read the grid.
3. Section 4 (25 min): train the four candidates and read the grid plot.
4. Section 5 (15 min): int8 post-training quantization.
5. Section 6 (20 min): the streams, the threshold table and the plot.
6. TODO cells (20 min): posterior smoothing; a smaller microcontroller.

- **Expect:** widths 96 and 128 fail on RAM (48,000 and 64,000 bytes); only width 128 with 3 or 4 blocks also fails on flash. Validation accuracy 0.672, 0.966, 0.986 and 0.972 for widths 8, 16, 32 and 64. Chosen: width 32, 3 blocks, test accuracy 0.988, 7,208 bytes of flash, 16,000 bytes of RAM, 1,304,160 MACs. Int8: 0.988, 100.0% agreement. False accepts per hour 74.0, 32.0, 18.0, 6.0 and 2.0 at thresholds 0.5, 0.7, 0.8, 0.9 and 0.95, with hit rates 1.000, 1.000, 0.889, 0.796 and 0.630; none at 0.98 (hit rate 0.500). Runtime about 1 minute.
- **Common problems:** counting the weights but forgetting the activations; normalizing features with statistics that include the test set; judging a detector by clip accuracy; claiming a false-accept rate from too little background audio.

### Quiz

1. Why did RAM, not flash, limit the width of the notebook's DS-CNN?
   - **Answer:** after the first convolution every layer works on 25 × 10 maps, so the activations take 500C bytes, which passes 32 KB at width 96, while the weights still fit in 64 KB of flash.
2. What does a tensor arena hold, and why is it fixed in size?
   - **Answer:** it holds all the model's tensors in one block of RAM, planned in advance. There is usually no operating system to allocate memory at run time, and with a fixed plan a model that starts cannot run out of memory halfway through.
3. Why is false accepts per hour a better measure for keyword spotting than clip accuracy?
   - **Answer:** the device runs on continuous audio, thousands of windows per hour, most without any keyword. Even a small error rate per window adds up to many false wake-ups.

**Watch out:** "TinyML is phone ML, only smaller." A microcontroller has no operating system, no file system and no dynamic memory, and its RAM is thousands of times smaller than a phone's. Here the activations, not the weights, decided which networks fit, and the runtime has to plan every byte in advance. The design starts from the flash and RAM budget, not from a phone model to shrink.

### Assignment 10 (due before session 11, 10 points)

1. Complete the posterior-smoothing TODO and plot both curves of misses against false accepts per hour. Did smoothing help? (3 points)
2. Complete the smaller-microcontroller TODO: the grid for 16 KB of flash and 8 KB of RAM, and the 10-band model's accuracy and false accepts per hour. (4 points)
3. Choose a threshold for a product that may wake up wrongly at most once per hour. Say how many hours of background audio you would need to support that claim, and why. (3 points)

Hand in one PDF and your notebook.

### Sources

- David et al. 2021, TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems. https://arxiv.org/abs/2010.08678
- Lin et al. 2020, MCUNet: Tiny Deep Learning on IoT Devices. https://arxiv.org/abs/2007.10319
- Banbury et al. 2021, MLPerf Tiny Benchmark. https://arxiv.org/abs/2106.07597
- Zhang et al. 2017, Hello Edge: Keyword Spotting on Microcontrollers. https://arxiv.org/abs/1711.07128
- Warden 2018, Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition. https://arxiv.org/abs/1804.03209
- Google AI Edge, LiteRT for Microcontrollers overview (formerly TensorFlow Lite Micro). https://developers.google.com/edge/litert/microcontrollers/overview

## Session 11: Benchmarking latency and energy honestly

**Goal:** students can build a benchmark harness, report latency distributions correctly, and estimate energy per inference from stated assumptions.

### Talking pointers

- **Open with:** "'Our model runs in 5 milliseconds.' On which phone, with how many threads, measured how many times, and including what? Today we learn to measure speed so that someone else can trust the number."
- **Segment 1, say:** show the four histograms, point at the medians and the tails, then show the four-thread rows of the thread table.
- **Segment 2, say:** write $E = Pt$, do the battery arithmetic for 5,000 mAh at 3.85 V, then work the race-to-idle example.
- **Segment 3, say:** show the ten per-run speed-ups and the bootstrap interval, then list what a fair comparison must hold fixed.
- **Close with:** "A latency without its hardware, software, threads, input size and distribution is not a measurement." Then set assignment 11.

### Segment 1 (7 min): measuring latency

- Use a monotonic high-resolution clock (`time.perf_counter_ns` in Python), warm up first, time many single calls, and keep every measurement. Report the median and high percentiles: the p99 is the time within which 99% of calls finish.
- The mean is pulled by rare slow calls. In the notebook, a synthetic 10 ms delay on 1% of calls doubled the int8 model's mean (0.0926 to 0.1926 ms) and left its median at 0.0897 ms.
- Phones add their own variation: other apps and background services, frequency scaling (the system changes the clock speed with load), thermal throttling (a hot phone slows down after minutes of work), and a mix of fast and slow cores (Arm's big.LITTLE design).
- The first call after loading is slower (a cold start). ONNX Runtime's first call took 0.396 ms against 0.091 ms later, after 2.8 ms to create the session.
- More threads are not automatically faster: on the shared 4-core server, four PyTorch threads took 96.36 ms per call against 0.59 ms with one.
- **Pause and try:** of 1,000 calls, 980 take 2 ms and 20 take 52 ms. What are the median, the mean and the p99?
  - **Answer:** median 2 ms; mean (980 × 2 + 20 × 52) / 1,000 = 3 ms; p99 52 ms, because more than 1% of calls are slow.

### Segment 2 (6 min): energy and battery

- Energy is power times time, $E = Pt$: a part drawing 1 W for 5 ms uses 5 mJ. Battery capacity is charge times voltage: 5,000 mAh at 3.85 V is 19.25 Wh, and 1 Wh is 3,600 J, so 69,300 J.
- With those assumed numbers, 1% of the battery pays for 138,600 inferences of 5 mJ, and 10 inferences per second for an hour use 0.26% of the battery.
- Phones are measured with an external power monitor connected in place of the battery, with the screen and radios held fixed. The model's energy is the extra over the idle phone.
- Race to idle: a faster unit that draws more power can use less energy because it finishes sooner. With assumed numbers, a CPU at 1 W for 20 ms uses 20 mJ; an NPU at 2 W for 2 ms uses 4 mJ.
- MLPerf Mobile (Janapa Reddi et al. 2022) runs fixed tasks with accuracy targets through an app on phones from different vendors, so that chips are compared on the same work.
- **Pause and try:** a model takes 8 ms at an assumed 1.5 W of extra power. How much energy is one inference, and how many inferences does 1% of a 69,300 J battery pay for?
  - **Answer:** 1.5 × 0.008 = 12 mJ, and 693 J ÷ 0.012 J = 57,750 inferences.

### Segment 3 (7 min): fair comparisons

- Hold fixed: the input size and pre-processing, the threads and cores, the batch size, warm or cold, and the accuracy (or report it next to the time). Measure end to end when the user waits for the whole pipeline: in the notebook the model was 74% of it.
- Change one thing at a time. In the notebook, PyTorch to ONNX Runtime on the same float32 model cut the median from 0.6611 to 0.1386 ms (4.8 times), and int8 then cut it to 0.0897 ms (1.5 times more).
- Count MACs, but measure time: the depthwise-separable CNN had 6.6 times fewer MACs yet the same batch-1 latency in PyTorch (0.6525 against 0.6611 ms).
- Repeat runs, interleave the variants, and give an interval (Course 1 session 9; the bootstrap, Course 11 session 7). Ten runs gave int8 speed-ups from 1.149 to 1.561; the mean was 1.463, with a 95% interval of 1.380 to 1.519.
- Report the device, operating system, runtime and version, threads, input shape, batch, warm-up, repetitions, median, p90 and p99. A server's numbers, and even its ratios, may not transfer to a phone.
- **Pause and try:** a report says "int8 is 3 times faster", comparing a PyTorch float32 model with an ONNX Runtime int8 model. What is wrong, and what do you ask for?
  - **Answer:** two things changed at once, the runtime and the precision. Ask for ONNX Runtime float32 on the same device and settings, plus the distribution and the hardware.

### Lab guide (about 2 hours, notebook `s11_benchmarking.ipynb`)

1. Section 1 (15 min): on Colab or Kaggle, first run `pip install onnx onnxscript onnxruntime`. Train, export and quantize; note the accuracies.
2. Section 2 (20 min): the harness, the table and the histograms.
3. Sections 3–4 (15 min): cold start; mean, median and outliers.
4. Section 5 (20 min): threads and batch size.
5. Section 6 (15 min): ten runs and the bootstrap interval.
6. Sections 7–8 (15 min): end-to-end time; the energy table.
7. TODO cells (20 min): an interval for p99; a fair dense against depthwise-separable comparison.

- **Expect:** test accuracy 0.9778 (PyTorch dense and ONNX Runtime float32), 0.9867 (depthwise-separable), 0.9756 (int8); ONNX files of 466,411 and 132,701 bytes in the saved run (a new export can differ by a few bytes). Batch-1 medians 0.6611, 0.6525, 0.1386 and 0.0897 ms; dense p99 1.5892 ms. First calls 0.971 ms (PyTorch) and 0.396 ms (ONNX Runtime). Four PyTorch threads: 96.36 ms per call. Int8 throughput 11,052 to 12,277 images per second from batch 1 to 64. Int8 speed-up 1.149 to 1.561 per run, mean 1.463, interval 1.380 to 1.519. Model 74% of the pipeline. Energy at 1 W and 5 ms: 5 mJ and 138,600 inferences per 1% of battery. Runtime about 33 seconds; timings from the saved run on a shared server CPU.
- **Common problems:** timing a few calls with `time.time()`; including the first call in an average without saying so; comparing runtimes at different thread counts; quoting a laptop's speed as a phone's.

### Quiz

1. Why report the median and p99 rather than only the mean?
   - **Answer:** the mean is pulled by rare slow calls. The median describes a typical call and the p99 the slow calls that users notice; in the notebook, delaying 1% of calls doubled the mean and left the median unchanged.
2. A model runs fast for the first minute on a phone, then 30% slower after ten minutes. Why, and what do you report?
   - **Answer:** thermal throttling: the phone lowers its clock speed as it heats. Report both the cold and the sustained latency, with the duration of the load.
3. What is the energy of one inference at an assumed 2 W for 4 ms?
   - **Answer:** 2 × 0.004 = 0.008 J, that is 8 mJ.

**Watch out:** "One timing run is enough." In the notebook, ten runs of the same comparison gave speed-ups from 1.149 to 1.561, and the depthwise-separable model's mean was 19% above its median. One run measures the machine's state at that moment as much as the model. Warm up, repeat, interleave the variants, report the distribution with an interval, and list the hardware and software.

### Assignment 11 (due before session 12, 10 points)

1. Complete the p99 TODO: bootstrap intervals for p99 from 1,000 and from 100 calls, and say how many calls you would need. (3 points)
2. Complete the second TODO: a fair comparison of the dense and depthwise-separable CNNs in ONNX Runtime. (3 points)
3. Benchmark one model from this course on your own phone or laptop, cold and after 5 minutes of continuous load, with a full report and an energy estimate from stated assumptions. (4 points)

Hand in one PDF and your notebook.

### Sources

- Janapa Reddi et al. 2022, MLPerf Mobile Inference Benchmark. https://arxiv.org/abs/2012.02328
- Efron & Tibshirani 1993, An Introduction to the Bootstrap (Chapman & Hall).
- ONNX Runtime documentation, quantization (static and dynamic). https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
- Google AI Edge, LiteRT performance measurement (benchmark tools). https://developers.google.com/edge/litert/performance/measurement

## Session 12: Learning on the device, privacy, and the capstone

**Goal:** students can estimate the memory cost of training on a device, personalize a model with few examples by updating only part of it, and plan a deployment capstone.

### Talking pointers

- **Open with:** "A model shipped in an app meets users it has never seen. Can it learn from them without their data leaving the phone, and can it fit in the phone's memory while it learns? Today we measure both, and plan your capstone."
- **Segment 1, say:** write the four parts of training memory, show the stacked bars, and ask why biases only was hardly cheaper in PyTorch.
- **Segment 2, say:** draw five phones and a server, run one FedAvg round on the board, then show the table for 20 and 150 examples per phone.
- **Segment 3, say:** walk through the capstone checklist with one example, such as a small Bangla model from Course 4 on a low-cost phone.
- **Close with:** "Measure what you ship, ship what you measured, and keep the user's data on the user's phone." Then set assignment 12.

### Segment 1 (7 min): what training on a device costs

- Training memory = weights + activations saved for the backward pass + gradients of the trained parameters + optimizer state (Adam keeps two numbers per trained parameter). The saved activations grow with the batch size.
- In the notebook (float32, batch of 20), full fine-tuning of a 38,282-parameter CNN needed 1,994,596 bytes, of which 1,382,084 were saved activations; training only the last layer needed 170,852 bytes.
- TinyTL (Cai et al. 2020) observed that activations, not parameters, dominate training memory, and that bias gradients do not need the layer inputs: going backward through a ReLU needs one bit per value. It freezes the weights and learns the biases, plus small extra modules.
- PyTorch did not find that saving by itself: with only the biases trainable, autograd still saved 1,341,124 bytes, against a minimum of 24,000. Lin et al. (2022) trained under 256 KB of memory on a microcontroller by updating only selected layers and channels (sparse updates), with a training engine built to store only what those gradients need.
- Few labels suffice for personalization: 20 examples of a new user's style raised accuracy from 0.589 to 0.806 (full), 0.735 (last layer) and 0.690 (biases).
- **Pause and try:** a model has 1 million parameters, trained in float32 with Adam. How much memory do the weights, gradients and Adam state take, without activations? And if only 1% of the parameters are trained?
  - **Answer:** 4 + 4 + 8 = 16 MB. With 1% trained, 4 MB of weights plus 0.04 MB of gradients and 0.08 MB of Adam state, about 4.1 MB.

### Segment 2 (6 min): privacy and federated learning

- Training on the phone keeps the raw data there. Federated learning (FedAvg; McMahan et al. 2017) shares learning without moving data: phones train locally and a server averages their models (Course 7 sessions 5 and 6).
- Updates are not automatically private: shared updates can reveal training data (Course 7 session 6), so real systems add secure aggregation (also Course 7 session 6) or differential privacy (Course 7 sessions 2 and 3).
- Mobile data is slow and costs money, so updates are compressed. In the notebook, int8 updates cut each upload from 153,128 to 38,314 bytes with the same accuracy (0.737 against 0.738).
- One shared model is a compromise: with 150 labelled digits per phone, each phone alone reached 0.953 on its own style against 0.868 for FedAvg; with only 20, FedAvg did slightly better (0.738 against 0.719).
- **Pause and try:** each of five phones uploads a 153,128-byte float32 model every round for 10 rounds. How much does each phone upload in total, and with int8 updates of 38,314 bytes?
  - **Answer:** 1,531,280 bytes (about 1.5 MB) against 383,140 bytes (about 0.38 MB).

### Segment 3 (7 min): shipping, and the capstone

- App size: app stores limit the download size, and users on paid data avoid large apps. Ship a small quantized model inside the app, and larger ones as optional downloads after installation.
- Updates: version each model with its pre-processing, test it on a fixed test set and real phones, release it to a few users first, and keep the old version for rollback.
- Monitoring without collecting data: send only aggregates counted on the device (latency percentiles, crashes, low-confidence answers), with consent; differential privacy (Course 7) can protect even those.
- Extraction: anyone who unpacks the app can copy the model file. Encryption helps only partly, since the app must decrypt the model to run it, so never put secrets into a shipped model.
- The capstone: put one model on a low-cost Android phone, for example a small Bangla model (Course 4), an assistive model (Course 12) or a crop-disease classifier (Course 15). Report accuracy before and after conversion, file size, peak memory, latency (median and p90, cold and warm) and an energy estimate, naming the phone and versions.
- **Pause and try:** your model file is 40 MB in float32 and your users pay for mobile data. Give two ways to cut what they download.
  - **Answer:** quantize it (about 10 MB in int8, less in 4 bits, if accuracy holds), and download it once after installation over Wi-Fi, updating it rarely, or only the layers that changed.

### Lab guide (about 2 hours, notebook `s12_on_device_learning.ipynb`)

1. Section 1 (15 min): pretrain; compare the two rows of digits and the two accuracies.
2. Section 2 (20 min): personalize three ways; read all five draws, not only the means.
3. Section 3 (25 min): the training-memory table; work out the 24,000-byte minimum by hand.
4. Section 4 (30 min): FedAvg with 20 and 150 examples per phone, with and without int8 updates.
5. Section 5 (10 min): read the capstone checklist and choose your model and phone.
6. TODO cells (20 min): memory against batch size; FedAvg followed by last-layer personalization.

- **Expect:** accuracy 0.960 in the standard style, 0.588 in the user's. With 20 examples (means of 5 draws): full 0.806, last layer 0.735, biases 0.690, no update 0.589. Training memory: full 1,994,596 bytes, last layer 170,852, biases 1,495,716 (minimum 178,592). FedAvg, means of 3 seeds, 20 per phone: alone 0.719, FedAvg 0.738, then local 0.733, int8 updates 0.737; 150 per phone: 0.953, 0.868, 0.905 and 0.868. Over 10 rounds a phone transfers 3.06 MB, or 1.91 MB with int8 updates. Runtime about 38 seconds.
- **Common problems:** testing personalization on the same 20 examples used to train; reporting one lucky draw of examples; counting the weights but not the saved activations; calling federated learning private without secure aggregation or differential privacy.

### Quiz

1. Why do saved activations, not parameters, usually dominate training memory?
   - **Answer:** every layer's output for every example in the batch is kept for the backward pass, while the parameters are stored once. In the notebook the saved activations were 1,382,084 bytes against 153,128 bytes of weights.
2. Why can a biases-only update need much less memory in principle, and why did it not in PyTorch?
   - **Answer:** bias gradients need only the backward signal, which through a ReLU needs one bit per value, not the layer inputs. PyTorch's standard operators still save full tensors, so only a purpose-built training engine gets the saving.
3. In the notebook, why did each phone training alone beat FedAvg when phones had 150 examples?
   - **Answer:** each phone was tested on its own style, and 150 examples were enough to learn it; FedAvg learns one compromise model for five styles.

**Watch out:** "Training on a phone is impossible." In the notebook, full fine-tuning of a small CNN needed about 2 MB and last-layer training 171 KB, and Lin et al. (2022) trained under 256 KB on a microcontroller. The real limits are activation memory, battery and the few labels a user provides, so update a small part of the model and measure it.

### Assignment 12 (due with the capstone, 10 points)

1. Complete both TODO cells: training memory against batch size for the three methods, and FedAvg followed by last-layer personalization. (3 points)
2. A one-page capstone plan: task and user, phone (model, RAM, chip), model and format, memory and latency budgets, and how data stays private and the model is updated. (3 points)
3. The capstone measurement table on the real phone: accuracy before and after conversion, file size, peak memory, median and p90 latency (cold and warm), and an energy estimate from stated assumptions. (4 points)

Hand in one PDF and your notebook.

### Sources

- Cai et al. 2020, TinyTL: Reduce Activations, Not Trainable Parameters for Efficient On-Device Learning (NeurIPS 2020 title: TinyTL: Reduce Memory, Not Parameters for Efficient On-Device Learning). https://arxiv.org/abs/2007.11622
- Lin et al. 2022, On-Device Training Under 256KB Memory. https://arxiv.org/abs/2206.15472
- McMahan et al. 2017, Communication-Efficient Learning of Deep Networks from Decentralized Data. https://arxiv.org/abs/1602.05629

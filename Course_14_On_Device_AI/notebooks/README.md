# Course 14 notebooks: On-Device AI

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, PyTorch 2.15, NumPy 2.5, SciPy 1.18, scikit-learn 1.9 and matplotlib 3.11, plus onnx 1.23, onnxscript 0.7 and ONNX Runtime 1.29 in sessions 2, 4, 7 and 11), and the outputs are saved in the notebooks.
- Sizes in bytes, operation counts and accuracies are exact and reproduce on a second run. Latencies do not: they come from one run on a shared server CPU, often with other jobs running, not from a phone. Treat the printed speed-ups as rough, and measure on your own device (session 11 shows how).
- The runnable parts use scikit-learn's digits (upsampled to 16 × 16 or 32 × 32 where a session needs bigger images), synthetic keyword audio, or a short text written into the notebook, so each notebook finishes in about a minute on a CPU.
- On Google Colab or Kaggle, sessions 2, 4, 7 and 11 need `pip install onnx onnxscript onnxruntime` first; everything else is preinstalled there.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a phone, a download or a library that is not installed here (the table below says what each needs). They were written from the tools' documented interfaces and have not been executed, so run each one before recording.
- Results that went against expectation are stated in each notebook's "What to notice" cell and in the course document. Examples: the depthwise-separable CNN, with 7.2 times fewer operations, was slower than the ordinary CNN in PyTorch at batch 1 but 3.69 times faster in ONNX Runtime (session 2); at 90% sparsity a sparse matrix product was only 2.37 times faster than the dense one (session 5); distillation helped only when labels were scarce (session 6); dynamic int8 quantization made a small CNN's file 3.4 times smaller but about 5 times slower (session 7); patch-based execution cut peak memory 2.12 times but ran about 10 times slower here (session 8); int8 quantization slowed the tiny language model down (session 9); RAM, not flash, limited the microcontroller model (session 10); updating only the biases was the least accurate way to personalize a model (session 12).

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_measuring_cost.ipynb](s01_measuring_cost.ipynb) | Why on-device AI, and how to measure cost | 9 | nothing (all cells run) |
| 2 | [s02_efficient_architectures.ipynb](s02_efficient_architectures.ipynb) | Efficient architectures for small devices | 9 | torchvision and a weights download (run on Colab or Kaggle) |
| 3 | [s03_quantization_basics.ipynb](s03_quantization_basics.ipynb) | Quantization I: integers instead of floats | 8 | nothing (all cells run) |
| 4 | [s04_qat_and_llm_quantization.ipynb](s04_qat_and_llm_quantization.ipynb) | Quantization II: training-aware and LLM quantization | 8 | nothing (all cells run) |
| 5 | [s05_pruning.ipynb](s05_pruning.ipynb) | Pruning and sparsity | 8 | nothing (all cells run) |
| 6 | [s06_distillation.ipynb](s06_distillation.ipynb) | Knowledge distillation | 8 | nothing (all cells run) |
| 7 | [s07_formats_runtimes.ipynb](s07_formats_runtimes.ipynb) | Model formats and runtimes | 10 | litert-torch and executorch (pip install litert-torch executorch) and an Android phone with adb |
| 8 | [s08_memory.ipynb](s08_memory.ipynb) | Memory: weights, activations and the KV cache | 7 | nothing (all cells run) |
| 9 | [s09_small_lms_on_phone.ipynb](s09_small_lms_on_phone.ipynb) | Small language models and speech on the phone | 9 | git, cmake, a C++ compiler and a downloaded GGUF model file (run on Colab, Kaggle or a laptop); git, cmake, a C++ compiler and a model download (whisper.cpp; run on Colab, Kaggle or a laptop) |
| 10 | [s10_tinyml.ipynb](s10_tinyml.ipynb) | TinyML on microcontrollers | 8 | nothing (all cells run) |
| 11 | [s11_benchmarking.ipynb](s11_benchmarking.ipynb) | Benchmarking latency and energy honestly | 10 | nothing (all cells run) |
| 12 | [s12_on_device_learning.ipynb](s12_on_device_learning.ipynb) | Learning on the device, privacy, and the capstone | 6 | nothing (all cells run) |

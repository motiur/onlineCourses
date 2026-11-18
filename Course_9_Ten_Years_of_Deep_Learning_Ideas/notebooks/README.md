# Course 9: Ten Years of Deep Learning Ideas: notebooks

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, PyTorch 2.15, NumPy, SciPy, scikit-learn 1.9, matplotlib 3.11), and the outputs are saved in the notebooks. A second, independent run reproduced every printed number; only timings differ.
- The runnable parts use small built-in or synthetic data (scikit-learn's digits, two moons, swiss roll and sample image, or data generated in the notebook), so each notebook finishes in about two minutes or less on a CPU. The numbers show how a method behaves; they are not benchmark results.
- Several notebooks call `torch.set_num_threads(1)`. For these small models it is as fast as more threads and keeps results identical between runs; remove it if you move a lab to a GPU.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a GPU, a download, an account or a library that is not installed here. They were written from the libraries' documented interfaces and have not been executed, so run each one before recording (the table below says what each needs).
- Nothing extra needs installing for the runnable cells on Google Colab or Kaggle.
- Results that went against the papers are stated in each notebook's "What to notice" cell and in the course document. Examples: a vanilla GAN covered 4 of 8 modes while WGAN-GP covered 7–8 (session 7); DDIM was not clearly better than DDPM at few steps on 2-D data (session 8); PPO without clipping crashed only at a deliberately large learning rate (session 10); temperature scaling barely changed the calibration error, and the ensemble's calibration error was worse than a single model's (session 12).

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_making_depth_work.ipynb](s01_making_depth_work.ipynb) | Making depth work: residuals, normalization and µP | 7 | `pip install mup` (Microsoft's µP package); for a real transformer, also a GPU. |
| 2 | [s02_optimizers_and_schedules.ipynb](s02_optimizers_and_schedules.ipynb) | Optimizers, schedules and training at scale | 12 | a CUDA GPU (CPU memory cannot be measured this way). |
| 3 | [s03_generalization_puzzles.ipynb](s03_generalization_puzzles.ipynb) | The generalization puzzles | 7 | nothing (all cells run) |
| 4 | [s04_vision_transformers.ipynb](s04_vision_transformers.ipynb) | Vision transformers and the modern ConvNet | 8 | `pip install timm torchvision`, a download of CIFAR-10 and the DeiT weights, and a GPU. |
| 5 | [s05_self_supervised_learning.ipynb](s05_self_supervised_learning.ipynb) | Self-supervised learning | 8 | downloads (DINOv2 weights through torch.hub, CIFAR-10 through torchvision) and preferably a GPU. |
| 6 | [s06_in_context_learning.ipynb](s06_in_context_learning.ipynb) | In-context learning and learning to learn | 9 | `pip install transformers` and a download of GPT-2 small (124M parameters); runs on a CPU in seconds. |
| 7 | [s07_generative_models_before_diffusion.ipynb](s07_generative_models_before_diffusion.ipynb) | Generative models before diffusion: VAEs, VQ-VAE, flows and GANs | 16 | `pip install torchmetrics[image]` and the Inception weights (a download of about 100 MB) |
| 8 | [s08_diffusion_models.ipynb](s08_diffusion_models.ipynb) | Diffusion models | 12 | a GPU and `pip install diffusers transformers accelerate` (the model is a download of about 4 GB and too slow on a CPU) |
| 9 | [s09_flow_matching.ipynb](s09_flow_matching.ipynb) | Flow matching, rectified flow and fast generation | 12 | a GPU, `pip install diffusers transformers accelerate sentencepiece` and a Hugging Face account (the model is gated behind a licence and is a download of about 15 GB) |
| 10 | [s10_deep_reinforcement_learning.ipynb](s10_deep_reinforcement_learning.ipynb) | Deep reinforcement learning, from AlphaGo to world models | 11 | a GPU and `pip install "gymnasium[atari]>=1.0" ale-py` (each game takes hours to learn) |
| 11 | [s11_neural_fields.ipynb](s11_neural_fields.ipynb) | Neural fields and 3D, from Fourier features to Gaussian splatting | 11 | a GPU and `pip install nerfstudio` (real scenes are a dataset download; your own photos also need COLMAP) |
| 12 | [s12_robustness_and_uncertainty.ipynb](s12_robustness_and_uncertainty.ipynb) | Robustness, uncertainty and calibration | 12 | a GPU and `pip install wilds` (the dataset is a download of about 10 GB) |

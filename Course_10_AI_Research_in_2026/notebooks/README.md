# Course 10: AI Research in 2026: notebooks

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Each notebook is a toy illustration of one 2026 paper's or report's central idea, named in its first section. It is not a reproduction, and its numbers say nothing about the paper's benchmarks.
- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, PyTorch 2.15, NumPy, SciPy, scikit-learn 1.9, matplotlib 3.11), and the outputs are saved in the notebooks. A second, independent run reproduced every printed number; only timings differ.
- The runnable parts use synthetic data generated in the notebook, so each notebook finishes in under two minutes on a CPU.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a GPU, a download, a model or internet access (for example to fetch a paper's released code or data). They were written from documented interfaces and have not been executed; check that the links still work and run each one before recording.
- Nothing extra needs installing for the runnable cells on Google Colab or Kaggle.
- Results that went against the papers are stated in each notebook's "What to notice" cell and in the course document. Examples: a higher upper clipping bound made no measurable difference to entropy in the RLVR toy (session 3); the "flexibility trap" toy showed the drop with small transformers but the opposite with an MLP denoiser, so it does not isolate the paper's mechanism (session 5); training against a probe with REINFORCE gave no obfuscated-activation runs, unlike the paper (session 10); per-scene fitting was more accurate than the feed-forward model, partly because it was given the true form of the world (session 12).
- Facts in the notebooks were checked in November 2026. Re-check them after NeurIPS 2026, as the course document's update checklist describes.

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_reading_2026_research.ipynb](s01_reading_2026_research.ipynb) | The year in AI research, and how to read it | 8 | nothing (all cells run) |
| 2 | [s02_agent_time_horizons.ipynb](s02_agent_time_horizons.ipynb) | Agents and long tasks: measuring time horizons | 11 | internet access and git (clones https://github.com/METR/eval-analysis-public) |
| 3 | [s03_rlvr_exploration.ipynb](s03_rlvr_exploration.ipynb) | Reasoning with reinforcement learning: exploration and entropy | 8 | a GPU and `pip install trl transformers datasets` (downloads a small open model and GSM8K) |
| 4 | [s04_lost_in_conversation.ipynb](s04_lost_in_conversation.ipynb) | Lost in conversation: multi-turn reliability | 10 | `pip install transformers accelerate` and a model download (a GPU makes it much faster) |
| 5 | [s05_flexibility_trap.ipynb](s05_flexibility_trap.ipynb) | Diffusion language models and the flexibility trap | 10 | a large GPU and the 8B-parameter LLaDA weights (too big for a CPU; about 20 GB of GPU memory or more) |
| 6 | [s06_transformer_expressivity.ipynb](s06_transformer_expressivity.ipynb) | What transformers can express | 8 | nothing (all cells run) |
| 7 | [s07_polar_express_muon.ipynb](s07_polar_express_muon.ipynb) | Optimizers in 2026: Polar Express and Muon | 10 | a CUDA GPU (the point is how matrix products compare with an SVD on GPU hardware) |
| 8 | [s08_provable_grokking.ipynb](s08_provable_grokking.ipynb) | Grokking, proved | 7 | internet access (to clone the authors' repository) |
| 9 | [s09_high_accuracy_sampling.ipynb](s09_high_accuracy_sampling.ipynb) | Sampling with high accuracy | 7 | nothing (all cells run) |
| 10 | [s10_probes_and_obfuscation.ipynb](s10_probes_and_obfuscation.ipynb) | Probes, obfuscation and honesty | 8 | internet access and a GPU (to clone the authors' code and run their released language models) |
| 11 | [s11_ai_and_erdos_problems.ipynb](s11_ai_and_erdos_problems.ipynb) | AI and mathematics: the Erdős problems | 7 | internet access (to clone the Erdős problems tracker) |
| 12 | [s12_feedforward_4d_reconstruction.ipynb](s12_feedforward_4d_reconstruction.ipynb) | Seeing in 4D: feed-forward reconstruction, and what comes next | 8 | a GPU and downloads (the VGGT code from github.com/facebookresearch/vggt and its pretrained weights) |

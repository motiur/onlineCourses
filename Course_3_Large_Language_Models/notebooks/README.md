# Course 3 notebooks: Large Language Models

One notebook per session. Open them in Kaggle Notebooks or Google Colab.

- Every cell without a NOT RUN label was run once on a CPU on 17 November 2026 (Python 3, NumPy 2.5, scikit-learn 1.9, PyTorch 2.15, tokenizers).
- Most notebooks use a toy Bangla language made from a small grammar (1,600 possible sentences). Because the grammar is known, a notebook can check exactly whether a generated sentence is valid and what the best possible loss is. The models have about 100,000 parameters and train in under a minute.
- LoRA, QLoRA, DPO, GRPO, the KV cache, speculative decoding, masked diffusion, the sparse autoencoder and distillation are written by hand at that scale. Numbers from the toy language show how a method behaves; they are not benchmark results.
- Cells labelled NOT RUN use real models and libraries (transformers, peft, bitsandbytes, trl, CLIP). They were written from the libraries' documented interfaces but not executed. Model names in angle brackets are for you to fill in. Run these cells once before recording.
- Session 8 uses a scripted stand-in for a language model so the agent loop and the test harness can be checked without a GPU.
- Session 2 needs `pip install tokenizers`.

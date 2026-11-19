# Course 6 notebooks: Winning Online AI Competitions

One notebook per session. Open them in Kaggle Notebooks or Google Colab.

- Every cell without a NOT RUN label was run once on a CPU on 17 November 2026 (Python 3, NumPy 2.5, pandas, SciPy 1.18, scikit-learn 1.9, LightGBM 4.7, XGBoost 3.4, PyTorch 2.15).
- The runnable parts use synthetic data built inside each notebook, so that leaks, shake-ups and validation mistakes can be planted on purpose and measured against a known truth. Scores from them are illustrations, not benchmarks.
- Cells labelled NOT RUN need a Kaggle account and a competition's data, a GPU, or a library that was not installed here (CatBoost, cuDF, TabPFN, timm, transformers, peft, vLLM). They were written from documented interfaces but not executed. Run them once before recording.
- Session 8 uses a small text model on synthetic 'chatbot arena' pairs, and session 11 uses simulated solvers. Both say so in the notebook; the real-model versions are in the last cell of each.
- Sessions 5 and 6 need `pip install lightgbm xgboost`.
- Before using any competition's data or sharing code, read that competition's rules.

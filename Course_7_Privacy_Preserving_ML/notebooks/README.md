# Course 7 notebooks: Privacy-Preserving Machine Learning

One notebook per session. Open them in Kaggle Notebooks or Google Colab.

- Every cell without a NOT RUN label was run once on a CPU on 17 November 2026 (Python 3, NumPy 2.5, SciPy 1.18, scikit-learn 1.9, PyTorch 2.15). These cells use small built-in or synthetic data.
- DP-SGD, the Renyi accountant, FedAvg, FedProx, gradient inversion, SISA and PATE are written by hand so students can read every line. The accountant was checked against the value published by Abadi et al. (2016). For real work use a maintained library (Opacus, Flower, TenSEAL) and its accountant.
- Cells labelled NOT RUN use those libraries or larger datasets (CIFAR-10, TOFU). They were written from the libraries' documented interfaces but not executed. Run them once yourself before recording.
- The Paillier code in session 8 is a teaching toy with short keys. It must never be used to protect real data.
- All patient data is synthetic. The clinical notes in session 7 are generated from templates, and the 'secret' in them is invented.
- Privacy numbers here come from tiny datasets and a large delta. They show the method, not a result to cite.

# Course 11 notebooks: Mathematics for Machine Learning

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, NumPy 2.5, SciPy 1.18, scikit-learn 1.9 and matplotlib 3.11, plus PyTorch 2.15 in sessions 5 and 10), and the outputs are saved in the notebooks. A second, independent run reproduced every printed number; only timings differ.
- Each notebook starts with a small example to work by hand, then checks it in code. The runnable parts use scikit-learn's built-in data (wine, digits, diabetes, breast cancer, a sample image and the two-moons generator), a short text, or data generated in the notebook, so each notebook finishes in under half a minute on a CPU.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a GPU, a download or a library that is not installed here. They were written from the libraries' documented interfaces and have not been executed, so run each one before recording (the table below says what each needs).
- Nothing extra needs installing for the runnable cells on Google Colab or Kaggle.
- Results that went against expectation are stated in each notebook's "What to notice" cell and in the course document. Examples: cosine similarity did not beat Euclidean distance on the original digits, 0.981 against 0.983 (session 1); with a duplicated feature the normal equations raised an error for only 2 of 10 features and returned meaningless weights without warning for the other 8 (session 2); power iteration needed about 200 steps on the digits covariance (session 3); a correlation that should have been near 0 came out as 0.027 by chance, so the notebook repeats the simulation (session 6); heavy-ball momentum needed 85 steps where its rate alone suggests 69 (session 8); SGD with a decaying step was still level with gradient descent after 30 passes (session 9); conjugate gradients needed only 2.5 times as many iterations when √κ grew tenfold (session 10); two estimators of the same mutual information disagreed by about 0.3 bits (session 11); spectral clustering scored only 0.650 on noisier moons although the true split had the smaller normalized cut (session 12).

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_vectors_and_matrices.ipynb](s01_vectors_and_matrices.ipynb) | Vectors, matrices and NumPy | 9 | a download of MNIST (70,000 images) from OpenML through fetch_openml |
| 2 | [s02_least_squares.ipynb](s02_least_squares.ipynb) | Linear systems, rank and least squares | 10 | a download of the California housing data through fetch_california_housing |
| 3 | [s03_eigen_svd_pca.ipynb](s03_eigen_svd_pca.ipynb) | Eigenvalues, SVD and PCA | 10 | a download of the Labeled Faces in the Wild photos through fetch_lfw_people |
| 4 | [s04_gradients.ipynb](s04_gradients.ipynb) | Calculus for ML: gradients, Jacobians and the chain rule | 9 | JAX (pip install jax), which is not installed here |
| 5 | [s05_autodiff.ipynb](s05_autodiff.ipynb) | Automatic differentiation and backpropagation | 9 | nothing (all cells run) |
| 6 | [s06_probability.ipynb](s06_probability.ipynb) | Probability for ML | 7 | nothing (all cells run) |
| 7 | [s07_estimation.ipynb](s07_estimation.ipynb) | Statistics and estimation: MLE, MAP and uncertainty | 10 | a download of MNIST from OpenML (about 50 MB) and a few minutes of CPU time |
| 8 | [s08_gradient_descent.ipynb](s08_gradient_descent.ipynb) | Optimization I: gradient descent and convexity | 8 | nothing (all cells run) |
| 9 | [s09_sgd_newton_constraints.ipynb](s09_sgd_newton_constraints.ipynb) | Optimization II: SGD, Newton's method and constraints | 11 | a download of MNIST from OpenML (about 50 MB) and a few minutes of CPU time |
| 10 | [s10_numerical_methods.ipynb](s10_numerical_methods.ipynb) | Numerical methods for ML | 10 | a CUDA GPU (float16 autocast and loss scaling run on the GPU) |
| 11 | [s11_information_theory.ipynb](s11_information_theory.ipynb) | Information theory for ML | 9 | the transformers library and a download of GPT-2 (about 500 MB) |
| 12 | [s12_graphs_and_matrices.ipynb](s12_graphs_and_matrices.ipynb) | Graphs and matrices: from PageRank to graph neural networks | 9 | torch_geometric and a download of the Cora citation graph (a few MB) |

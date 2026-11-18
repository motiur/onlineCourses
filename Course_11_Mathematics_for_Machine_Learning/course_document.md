# Course 11: Mathematics for Machine Learning

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on the mathematics that machine learning actually uses: linear algebra, calculus, probability, statistics, optimization, numerical methods, information theory and graphs, each taught through a machine learning question and checked in NumPy. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Machine learning papers and libraries assume a toolkit of mathematics that many students met in separate courses without seeing why machine learning needs it. This course teaches that toolkit through machine learning questions: why PCA works, why gradient descent zig-zags, why cross-entropy is the loss, why softmax needs a stable formula, and why PageRank and graph neural networks are matrix products. Each session gives the minimum theory with a worked example small enough to check by hand, then the same idea in NumPy.

Prerequisites: Python basics and school mathematics (algebra, functions and a little calculus). Take it alongside Course 1 or right after it. It prepares students for Course 2 and everything after it; Course 8 (Mathematics and AI) is the advanced follow-on.

Capstone: build one machine learning method from first principles, such as PCA followed by logistic regression, a small neural network, or spectral clustering. Derive it on paper, implement it in NumPy with gradient or result checks, compare it with a library implementation, and explain it in a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a correct, clearly explained derivation (25); a correct implementation with checks (25); a comparison with a library and an honest account of any differences (20); one experiment that shows a mathematical property at work, such as conditioning or a step-size limit (15); clarity of the report and video (15).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English. Many sessions match parts of university courses in linear algebra, calculus, probability, numerical methods and discrete mathematics, so they also work as flipped-classroom material.

### Sessions

1. **Vectors, matrices and NumPy.** Students can represent data as vectors and matrices, compute and interpret dot products, norms and matrix–vector products, and write vectorized NumPy instead of loops.
   - Read: Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 2 and 3; Boyd & Vandenberghe 2018, Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares
   - Lab: about 2 hours, notebook `s01_vectors_and_matrices.ipynb`
2. **Linear systems, rank and least squares.** Students can explain column space and rank, solve $Ax = b$ properly, derive least squares, and fit linear regression three ways.
   - Read: Strang, MIT 18.06 Linear Algebra, lecture videos and notes; Boyd & Vandenberghe 2018, Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares
   - Lab: about 2 hours, notebook `s02_least_squares.ipynb`
3. **Eigenvalues, SVD and PCA.** Students can explain eigenvectors and the SVD, compute them with power iteration and NumPy, and use the SVD for low-rank approximation and PCA.
   - Read: Strang, MIT 18.06 Linear Algebra, lecture videos and notes; Strang 2019, Linear Algebra and Learning from Data
   - Lab: about 2.5 hours, notebook `s03_eigen_svd_pca.ipynb`
4. **Calculus for ML: gradients, Jacobians and the chain rule.** Students can compute partial derivatives, gradients and Jacobians of ML losses by hand, apply the chain rule, and check gradients numerically.
   - Read: Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 5; Parr & Howard 2018, The Matrix Calculus You Need for Deep Learning
   - Lab: about 2 hours, notebook `s04_gradients.ipynb`
5. **Automatic differentiation and backpropagation.** Students can explain computational graphs, forward and reverse mode, and why backpropagation is reverse-mode automatic differentiation, and can build a tiny autodiff engine.
   - Read: Baydin, Pearlmutter, Radul & Siskind 2018, Automatic Differentiation in Machine Learning: a Survey; Karpathy, micrograd
   - Lab: about 2.5 hours, notebook `s05_autodiff.ipynb`
6. **Probability for ML.** Students can use random variables, common distributions, expectation, variance, covariance, conditional probability and Bayes' rule, and can sample from a multivariate Gaussian.
   - Read: Blitzstein & Hwang, Introduction to Probability (Stat 110, free materials); Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 6
   - Lab: about 2 hours, notebook `s06_probability.ipynb`
7. **Statistics and estimation: MLE, MAP and uncertainty.** Students can derive maximum likelihood and MAP estimates, connect priors to regularization and losses to likelihoods, and put uncertainty on an estimate.
   - Read: Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 8–9; Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 5
   - Lab: about 2 hours, notebook `s07_estimation.ipynb`
8. **Optimization I: gradient descent and convexity.** Students can run and analyse gradient descent, explain step-size limits, convexity and conditioning, and see why momentum helps.
   - Read: Boyd & Vandenberghe 2004, Convex Optimization, chapters 3 and 9; Bottou, Curtis & Nocedal 2018, Optimization Methods for Large-Scale Machine Learning
   - Lab: about 2 hours, notebook `s08_gradient_descent.ipynb`
9. **Optimization II: SGD, Newton's method and constraints.** Students can explain stochastic gradients, second-order methods and Lagrange multipliers, and choose between them.
   - Read: Bottou, Curtis & Nocedal 2018, Optimization Methods for Large-Scale Machine Learning; Nocedal & Wright 2006, Numerical Optimization (Springer), chapters 3, 6, 7 and 12
   - Lab: about 2.5 hours, notebook `s09_sgd_newton_constraints.ipynb`
10. **Numerical methods for ML.** Students can explain floating-point formats and their failures, write numerically stable ML code, and pick a stable way to solve linear systems.
   - Read: Goldberg 1991, What Every Computer Scientist Should Know About Floating-Point Arithmetic; Micikevicius et al. 2018, Mixed Precision Training
   - Lab: about 2 hours, notebook `s10_numerical_methods.ipynb`
11. **Information theory for ML.** Students can compute entropy, cross-entropy, KL divergence and mutual information, and explain where each appears in ML.
   - Read: Shannon 1948, A Mathematical Theory of Communication, Bell System Technical Journal 27; MacKay 2003, Information Theory, Inference, and Learning Algorithms, chapters 2, 4, 5 and 8
   - Lab: about 2 hours, notebook `s11_information_theory.ipynb`
12. **Graphs and matrices: from PageRank to graph neural networks.** Students can represent graphs as adjacency and Laplacian matrices, compute PageRank and spectral clusters, and see message passing as matrix multiplication.
   - Read: Page, Brin, Motwani & Winograd 1999, The PageRank Citation Ranking: Bringing Order to the Web; Ng, Jordan & Weiss 2001, On Spectral Clustering: Analysis and an Algorithm, Advances in Neural Information Processing Systems 14
   - Lab: about 2 hours, notebook `s12_graphs_and_matrices.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. In this course, work one pause-and-try example by hand on camera before showing the code.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**.
- **Sources:** the textbooks cited are free online where a link is given; read the matching chapter before recording.
- **Dates:** written in November 2026.

## Session 1: Vectors, matrices and NumPy

**Goal:** students can represent data as vectors and matrices, compute and interpret dot products, norms and matrix–vector products, and write vectorized NumPy instead of loops.

### Talking pointers

- **Open with:** "Every dataset you will train on is a table of numbers. Today we read that table as geometry: lengths, angles and functions."
- **Segment 1, say:** show one digit as an 8 × 8 picture and as 64 numbers (the notebook's first plot), then write the shape of the dataset, 1,797 × 64.
- **Segment 2, say:** work out the dot product and cosine of (3, 4) and (4, 3) on the board, then show the wine result: 0.722 accuracy before standardizing, 1.000 after.
- **Segment 3, say:** shear the unit square and then rotate it, then do it in the other order, and show the two pictures side by side.
- **Close with:** "A vector is a point, a matrix is a function, and NumPy applies the function to a whole dataset at once." Then set assignment 1.

### Segment 1 (6 min): data as vectors and matrices

- A vector is an ordered list of numbers that describes one thing: a student's marks (78, 85, 62), the word counts of a sentence, or the 64 pixel values of an 8 × 8 image.
- A dataset is a matrix $X$ with one row per example and one column per feature. scikit-learn's digits form a 1,797 × 64 matrix (Boyd & Vandenberghe 2018).
- Shapes are the first check on any formula: $(n \times d)$ times $(d \times k)$ gives $n \times k$ (Course 1 session 2).
- In NumPy: `X.shape`, `X[i]` (one example) and `X[:, j]` (one feature for every example).
- **Pause and try:** you store one week of hourly temperatures for the 64 districts of Bangladesh, one row per district. What is the shape of the matrix, and what does one column mean?
  - **Answer:** 64 × 168, since a week has 7 × 24 = 168 hours. One column is every district's temperature at one hour.

### Segment 2 (7 min): dot products, norms and similarity

- The dot product $u \cdot v = \sum_i u_i v_i$ is large when two vectors point the same way. It equals $\|u\| \|v\| \cos\theta$, where $\theta$ is the angle between them.
- Norms measure length (Goodfellow et al. 2016, chapter 2): $\|u\|_1 = \sum_i |u_i|$, $\|u\|_2 = \sqrt{\sum_i u_i^2}$ and $\|u\|_\infty = \max_i |u_i|$. For $u = (3, 4)$ they are 7, 5 and 4. A distance is the norm of a difference, $\|u - v\|_2$.
- Cosine similarity, $u \cdot v / (\|u\| \|v\|)$, ignores length. It is widely used to compare text and image embeddings.
- Projection: the part of $a$ along $b$ is $(a \cdot b / b \cdot b)\, b$, and what is left over is orthogonal to $b$. Least squares (session 2) and PCA (session 3) are projections too (Deisenroth et al. 2020, chapter 3).
- Normalizing matters twice. Scaling a whole vector changes its Euclidean distances but not its cosines. And when features have different scales, the largest dominates every distance: in the wine data, proline (278 to 1,680) swamps hue (0.48 to 1.42).
- **Pause and try:** for $u = (3, 4)$ and $v = (4, 3)$, compute $u \cdot v$ and $\cos(u, v)$.
  - **Answer:** $u \cdot v = 12 + 12 = 24$ and $\cos(u, v) = 24 / (5 \times 5) = 0.96$, an angle of about 16°.

### Segment 3 (7 min): matrices as functions, and the cost of computing

- A matrix $A$ is a function $x \mapsto Ax$. Its columns are where $e_1 = (1, 0)$ and $e_2 = (0, 1)$ land, and linearity, $A(x_1 e_1 + x_2 e_2) = x_1 A e_1 + x_2 A e_2$, moves every other point (3Blue1Brown, Essence of Linear Algebra).
- Written row by row as in NumPy: rotation by 90°, `[[0, -1], [1, 0]]`; scaling, `[[1.5, 0], [0, 0.5]]`; shear, `[[1, 1], [0, 1]]`. The area of the unit square is multiplied by $|\det A|$.
- A matrix product is composition: $(AB)x = A(Bx)$, "first $B$, then $A$" (Strang, MIT 18.06). In general $AB \ne BA$ (see Watch out).
- Cost: for $n \times n$ matrices, $Ax$ takes $n^2$ multiply-adds and $AB$ takes $n^3$, so compute $A(Bx)$, not $(AB)x$.
- Vectorize: one matrix product replaces three nested Python loops and runs in compiled code. Broadcasting stretches axes of size 1, so `X - X.mean(axis=0)` centres every row, but it also silently turns shapes (n,) and (n, 1) into (n, n) (Course 10 session 3).
- **Pause and try:** where does `M = [[2, 1], [1, 2]]` send (1, 1), and what is the area of the image of the unit square?
  - **Answer:** (3, 3), the sum of the two columns. The area is $|\det M| = 4 - 1 = 3$.

### Lab guide (about 2 hours, notebook `s01_vectors_and_matrices.ipynb`)

1. Section 1 (10 min): say what each row and column of every printed array means.
2. Section 2 (15 min): the dot product, norms, cosine and projection on paper, then in code.
3. Section 3 (15 min): raw against standardized wine features.
4. Section 4 (25 min): estimate the multiply-adds by hand, then compare the three searches' times and accuracies, and the effect of lighter ink.
5. Sections 5–6 (20 min): predict where $M$ sends $e_1$, $e_2$ and (1, 1), and compute $RS$ and $SR$, before running.
6. Section 7 (15 min): $(AB)x$ against $A(Bx)$, and broadcasting.
7. TODO cells (20 min): k-nearest neighbours and the L1 distance.

- **Expect:** the hand values (24.0; 7.0, 5.0, 4.0; cos 0.9600). Wine 1-nearest-neighbour accuracy on 54 test wines: 0.722 raw, 1.000 standardized. Digits: 33,108,480 multiply-adds; the three searches agree; loops 4.452 ms per query, one matrix product 0.00827 ms (timings vary). Accuracy: cosine 0.981, Euclidean 0.983; with ink × 0.25, 0.5 and 2.0, cosine stays 0.981 and Euclidean gives 0.656, 0.914 and 0.942. Areas 1.00, 0.75, 1.00, 3.00, equal to $|\det|$. $(AB)x$ 10.4 ms, $A(Bx)$ 0.56 ms. The shape bug gives a mean squared error of 2.543 instead of 0.018. Runtime about 5 seconds.
- **Common problems:** `argmin` on similarities or `argmax` on distances; standardizing with test-set statistics; `np.linalg.norm(X)` without `axis=1`, which returns one number for the whole matrix.

### Quiz

1. $X$ has shape (1797, 64). What are the shapes of `X @ w` for `w` of shape (64,), and of `X.T @ X`?
   - **Answer:** (1797,), one score per image, and (64, 64), one number per pair of pixels.
2. Why does cosine similarity still find the right neighbour for a lightly written digit when Euclidean distance fails?
   - **Answer:** scaling a vector does not change its direction, so its cosines stay the same, but it moves the point, so its distances change.
3. For $n \times n$ matrices $A$, $B$ and a vector $x$, which is cheaper, $(AB)x$ or $A(Bx)$?
   - **Answer:** $A(Bx)$: about $2n^2$ multiply-adds against $n^3 + n^2$, about 500 times fewer for $n = 1000$.

**Watch out:** "Matrix multiplication is commutative, like multiplying numbers." It is not. For the lab's rotation $R$ and shear $S$, $RS$ = `[[0, -1], [1, 1]]` and $SR$ = `[[1, -1], [1, 0]]`: $RS$ sends (1, 0) to (0, 1), while $SR$ sends it to (1, 1). The mistake survives because some pairs do commute, such as two diagonal matrices or two rotations of the plane.

### Assignment 1 (due before session 2, 10 points)

1. By hand, for $u = (1, 2, 2)$ and $v = (2, 0, 1)$: $u \cdot v$, the three norms of $u$, $\cos(u, v)$, $\|u - v\|_2$ and the projection of $v$ onto $u$. Check each in NumPy. (3 points)
2. Complete both TODO cells and report the accuracy of 1-, 3- and 5-nearest neighbours (cosine) and of 1-nearest neighbour (L1). Compute the memory that the (360, 1437, 64) array of your L1 search needs in float64, and rewrite the search to process the queries in blocks. (4 points)
3. Find two 2 × 2 matrices that commute and two that do not, other than those in the notebook. For each pair, draw the unit square under $AB$ and $BA$ and explain the pictures in two sentences. (3 points)

Hand in one PDF and your notebook.

### Sources

- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 2 and 3. https://mml-book.github.io/
- Boyd & Vandenberghe 2018, Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares. https://web.stanford.edu/~boyd/vmls/
- Strang, MIT 18.06 Linear Algebra, lecture videos and notes. https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- 3Blue1Brown, Essence of Linear Algebra (linear transformations; matrix multiplication as composition). https://www.3blue1brown.com/topics/linear-algebra
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 2. https://www.deeplearningbook.org/

## Session 2: Linear systems, rank and least squares

**Goal:** students can explain column space and rank, solve $Ax = b$ properly, derive least squares, and fit linear regression three ways.

### Talking pointers

- **Open with:** "Linear regression is one line of linear algebra. Today you derive that line by hand, solve it three ways, and watch one of them fail without telling you."
- **Segment 1, say:** draw the columns (1, 1) and (1, 2) as arrows, and show that $b = (3, 5)$ is 1 times the first plus 2 times the second.
- **Segment 2, say:** fit the line through (0, 1), (1, 1) and (2, 4) on the board, then show the residual plot and check $A^\top r = 0$ aloud.
- **Segment 3, say:** run the duplicated-feature loop live: two errors and eight silent, arbitrary answers.
- **Close with:** "Never invert; factorize. And when columns repeat, ask which answer the solver chose." Then set assignment 2.

### Segment 1 (6 min): Ax = b as combining columns

- $Ax$ is a mix of the columns of $A$ with weights $x$, so solving $Ax = b$ asks which mix of the columns gives $b$. For $x_1 + x_2 = 3$ and $x_1 + 2x_2 = 5$, $x = (1, 2)$: $b = 1 \cdot (1, 1) + 2 \cdot (1, 2)$.
- The column space is the set of all $Ax$. The rank is the number of independent columns, the dimension of the column space (Strang, MIT 18.06).
- For $A$ with $n$ columns there is no solution if $b$ is outside the column space, exactly one if $b$ is inside and the rank is $n$, and infinitely many if $b$ is inside and the rank is below $n$. Then some $z \ne 0$ has $Az = 0$ (the null space), and adding $z$ to a solution gives another.
- In data, a feature that copies other features, or adds them up, lowers the rank.
- **Pause and try:** $A$ has rows (1, 2) and (2, 4). How many solutions are there for $b = (3, 6)$? For $b = (1, 3)$?
  - **Answer:** infinitely many for (3, 6), such as $(3, 0) + t(2, -1)$; none for (1, 3), because every $Ax$ is a multiple of (1, 2).

### Segment 2 (7 min): least squares is a projection

- With more equations than unknowns, as in regression with many examples and few features, $Ax = b$ usually has no solution. Least squares picks the $\hat x$ that minimizes $\|Ax - b\|^2$.
- Expand: $\|Ax - b\|^2 = x^\top A^\top A x - 2 b^\top A x + b^\top b$. Setting the gradient $2A^\top A x - 2A^\top b$ to zero gives the normal equations $A^\top A \hat x = A^\top b$ (session 4 derives such gradients).
- Geometry: $A\hat x$ is the point of the column space closest to $b$, its orthogonal projection. The residual $r = b - A\hat x$ is orthogonal to every column: $A^\top r = 0$ (Boyd & Vandenberghe 2018). With a column of ones, this says the residuals sum to zero.
- For independent columns the projection matrix is $P = A(A^\top A)^{-1}A^\top$, with $P^2 = P$: projecting twice changes nothing (Deisenroth et al. 2020, chapter 3).
- **Pause and try:** fit $y = c + mt$ to (0, 1), (1, 1), (2, 4).
  - **Answer:** $A^\top A$ has rows (3, 3) and (3, 5), $A^\top b = (6, 9)$, so $(c, m) = (0.5, 1.5)$. The residuals (0.5, −1, 0.5) sum to 0, and $0(0.5) + 1(-1) + 2(0.5) = 0$.

### Segment 3 (7 min): how libraries solve it

- QR writes $A = QR$, with orthonormal columns in $Q$ and an upper-triangular $R$. The normal equations become $R\hat x = Q^\top b$, solved by back substitution without forming $A^\top A$. Gram–Schmidt builds $Q$ column by column; libraries use Householder reflections, which keep $Q$ orthogonal to rounding level (Trefethen & Bau 1997).
- Forming $A^\top A$ squares the condition number: 227 became 51,631 in the lab. On ill-conditioned data the normal equations lose about twice as many digits as QR (session 10).
- `np.linalg.lstsq` uses the SVD (session 3). It treats tiny singular values as zero and, when columns are dependent, returns the minimum-norm solution.
- Do not invert to solve: forming $A^{-1}$ takes about $2n^3$ floating-point operations against $\tfrac{2}{3}n^3$ for the LU factorization behind `np.linalg.solve`, and its rounding errors are larger (Higham 2002).
- With a duplicated feature, only the sum of the two weights is determined. A near-duplicate gives huge, meaningless weights; ridge regression (session 7) fixes that.
- **Pause and try:** two columns of your data are identical, and a fit with one copy gave it weight 6. What does `lstsq` give each copy, and why?
  - **Answer:** 3 and 3. Every split that sums to 6 fits equally well, and (3, 3) has the smallest length: $3^2 + 3^2 = 18$, against 36 for (6, 0).

### Lab guide (about 2 hours, notebook `s02_least_squares.ipynb`)

1. Sections 1–2 (20 min): solve by hand, then predict each rank verdict before running.
2. Section 3 (20 min): the three-point fit by hand, then the code and the residual plot.
3. Section 4 (15 min): Gram–Schmidt by hand for the same points.
4. Section 5 (20 min): the diabetes fit three ways; check $A^\top r$ and the condition numbers.
5. Section 6 (10 min): inverse against `solve`.
6. Section 7 (20 min): duplicated and near-duplicated features; read both plots.
7. TODO (15 min): polynomial least squares.

- **Expect:** $x = (1, 2)$; verdicts "infinitely many solutions" and "no solution"; `solve` on $A_1$ raises "Singular matrix". The hand fit gives $A^\top b = (6, 9)$, $\hat x = (0.5, 1.5)$, residual (0.5, −1, 0.5), sum of squares 1.5; Gram–Schmidt's $R$ has diagonal 1.7321 and 1.4142, and $Q^\top b = (3.4641, 2.1213)$. Diabetes: every method within 3.4e-12 of `lstsq`, largest $|A^\top r|$ 6.2e-13, $R^2$ 0.518, condition numbers 227 and 51,631. Inverse 57.7 ms against 19.4 ms for `solve` (timings vary); Hilbert relative residual 1.6e-16 with `solve` and 3.4e-05 with the inverse. Duplicates: `LinAlgError` only for `s4` and `s5`; the normal equations split `s1` into 2225.61 and −3017.79, `lstsq` into −396.09 each (weight lengths 3918.5 and 1268.0). The near-copy gets weights −4,131,612 and 4,130,820. Runtime about 3 seconds.
- **Common problems:** forgetting the column of ones for the intercept; forgetting that `np.linalg.lstsq` returns a tuple (take `[0]`); comparing QR factors entry by entry when only their signs differ.

### Quiz

1. When does $Ax = b$ have no solution, exactly one, or infinitely many?
   - **Answer:** none when $b$ is outside the column space; one when $b$ is inside and the columns are independent; infinitely many when $b$ is inside and the rank is below the number of columns.
2. Why is the least-squares residual orthogonal to the columns of $A$?
   - **Answer:** the normal equations say $A^\top(b - A\hat x) = 0$. Geometrically, the closest point of a subspace is reached along a perpendicular.
3. Why is QR safer than the normal equations?
   - **Answer:** forming $A^\top A$ squares the condition number; QR works with $A$ itself.

**Watch out:** "To solve $Ax = b$, compute $A^{-1}$ first." In the lab the inverse was about three times slower on a 1000 × 1000 system, and on the Hilbert matrix its residual was 3.4e-05 against 1.6e-16 for `solve`. Factorize instead (LU for square systems, QR or the SVD for least squares) and solve triangular systems. Compute an inverse only when you need its entries.

### Assignment 2 (due before session 3, 10 points)

1. By hand, fit $y = c + mt$ to (0, 1), (1, 1), (2, 4), (3, 4) with the normal equations, give the residuals and check $A^\top r = 0$. Check it in code. (3 points)
2. Complete the TODO. Fit polynomials of degree 1, 3 and 9 to the 30 points; report the training sum of squares and the condition number of each Vandermonde matrix, and explain both trends. (4 points)
3. Add a feature equal to `bmi + bp` to the diabetes data. Report the rank, what the normal equations and `lstsq` return, and whether the predictions change. Explain with the null space. (3 points)

Hand in one PDF and your notebook.

### Sources

- Strang, MIT 18.06 Linear Algebra, lecture videos and notes. https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Boyd & Vandenberghe 2018, Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares. https://web.stanford.edu/~boyd/vmls/
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 3 and 9. https://mml-book.github.io/
- Trefethen & Bau 1997, Numerical Linear Algebra (SIAM; book).
- Higham 2002, Accuracy and Stability of Numerical Algorithms (SIAM; book).

## Session 3: Eigenvalues, SVD and PCA

**Goal:** students can explain eigenvectors and the SVD, compute them with power iteration and NumPy, and use the SVD for low-rank approximation and PCA.

### Talking pointers

- **Open with:** "Why does PCA work? Because every matrix, and every dataset, has a few directions that matter most, and the SVD finds them."
- **Segment 1, say:** show the unit circle and its image under `[[2, 1], [1, 2]]`: an ellipse whose axes are the eigenvectors, stretched by 3 and 1 (the notebook's first plot).
- **Segment 2, say:** show the image at ranks 5, 20 and 50 next to the original, with the fraction of numbers stored under each.
- **Segment 3, say:** show the cumulative explained-variance curve and read off 21 components for 90% of the variance.
- **Close with:** "Eigenvectors for symmetric matrices, the SVD for every matrix, PCA for centred data: one idea, three times." Then set assignment 3.

### Segment 1 (6 min): eigenvectors and power iteration

- An eigenvector is a direction that $A$ only stretches: $Av = \lambda v$ (3Blue1Brown, Essence of Linear Algebra). The eigenvalues solve $\det(A - \lambda I) = 0$.
- Example: for `[[2, 1], [1, 2]]`, $(2 - \lambda)^2 - 1 = 0$ gives $\lambda = 3$ and $1$, with eigenvectors $(1, 1)/\sqrt 2$ and $(1, -1)/\sqrt 2$.
- Symmetric matrices ($A = A^\top$), such as covariance matrices, have real eigenvalues and orthonormal eigenvectors: $A = V \Lambda V^\top$ (Strang, MIT 18.06). Other matrices may have complex eigenvalues (a rotation) or too few eigenvectors (a shear).
- Power iteration repeats $x \leftarrow Ax / \|Ax\|$. The part along the top eigenvector grows fastest, and the direction error shrinks like $|\lambda_2 / \lambda_1|^k$. For the digits covariance $\lambda_2/\lambda_1 = 0.915$, so it needed about 200 steps. Session 12 uses power iteration for PageRank.
- **Pause and try:** run power iteration for `[[2, 1], [1, 2]]` from (1, 0) without normalizing. Give $x_1$, $x_2$ and $x_3$.
  - **Answer:** (2, 1), (5, 4), (14, 13): the direction approaches (1, 1). The Rayleigh quotient $x^\top A x / x^\top x$ of (5, 4) is $122/41 \approx 2.976$, close to $\lambda_1 = 3$.

### Segment 2 (7 min): the SVD and low-rank approximation

- Every $m \times n$ matrix has a singular value decomposition $B = U \Sigma V^\top$: $U$ and $V$ have orthonormal columns, and $\Sigma$ holds the singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$. The $\sigma_i^2$ are the eigenvalues of $B^\top B$.
- Read it as rotate, stretch, rotate, or as a sum of rank-1 pieces: $B = \sum_i \sigma_i u_i v_i^\top$ (Strang 2019).
- Eckart–Young: keeping the first $k$ pieces gives the closest rank-$k$ matrix in the Frobenius norm, with error $\sqrt{\sigma_{k+1}^2 + \sigma_{k+2}^2 + \dots}$ (Eckart & Young 1936). In the spectral norm the error is $\sigma_{k+1}$.
- Image compression: rank $k$ stores $k(m + n + 1)$ numbers instead of $mn$. For the 427 × 640 grey image, rank 20 stores 7.8% of the numbers with a relative error of 0.139; keeping 20 columns and their best least-squares mix gave 0.177.
- **Pause and try:** for $B$ = `[[3, 0], [4, 5]]`, find $\sigma_1$ and $\sigma_2$ from $B^\top B$, and the error of the best rank-1 approximation.
  - **Answer:** $B^\top B$ = `[[25, 20], [20, 25]]` has eigenvalues 45 and 5, so $\sigma_1 = \sqrt{45} \approx 6.708$ and $\sigma_2 = \sqrt 5 \approx 2.236$. The rank-1 error is $\sigma_2 \approx 2.236$, and it keeps $45/50 = 90\%$ of $\|B\|_F^2$.

### Segment 3 (7 min): PCA is the SVD of centred data

- PCA finds the directions of largest variance. Centre the data, $X_c = X - \bar x$, and take $X_c = U \Sigma V^\top$. The columns of $V$ are the principal directions: the eigenvectors of the covariance $C = X_c^\top X_c / (n - 1)$ (Shlens 2014).
- The variance along direction $i$ is $\sigma_i^2/(n - 1)$, and the explained-variance ratio is $\sigma_i^2 / \sum_j \sigma_j^2$. The scores $X_c V = U \Sigma$ are the new coordinates.
- Choosing $k$: the smallest $k$ that keeps a target share of the variance (21 of 64 for 90% on digits), or the $k$ that works best for the model that uses the features.
- Reconstruction: $\hat x = \bar x + V_k V_k^\top (x - \bar x)$. The mean squared error per example is the sum of the dropped $\sigma_i^2$ divided by $n$ (Deisenroth et al. 2020, chapter 10).
- When features have different units, standardize first, or the feature with the largest numbers takes over the first component.
- **Pause and try:** a 3 × 3 covariance matrix has eigenvalues 6, 3 and 1. What fraction of the variance do the first two components keep?
  - **Answer:** $(6 + 3)/(6 + 3 + 1) = 0.9$, so 90%.

### Lab guide (about 2.5 hours, notebook `s03_eigen_svd_pca.ipynb`)

1. Section 1 (15 min): the eigenvalues of $A$ by hand, then `eigh`.
2. Section 2 (25 min): three steps of power iteration by hand, then the digits covariance; read the convergence plot.
3. Section 3 (15 min): the SVD of $B$ by hand.
4. Section 4 (25 min): image compression; compare the errors with the formula and with the column method.
5. Sections 5–6 (30 min): PCA from the SVD, the check against scikit-learn, and reconstructions.
6. Section 7 (15 min): the centring and feature-selection tests.
7. TODO (25 min): deflation.

- **Expect:** eigenvalues 1 and 3; Rayleigh quotients 2.800000, 2.975610, 2.997260, 2.999695. Digits covariance: largest eigenvalues 179.0069 and 163.7177 (ratio 0.9146); after 50 steps the eigenvalue error is 4.7e-04 and the direction error 5.6e-03, and after 200 steps both are at rounding level. $B$: 6.7082 and 2.2361, rank-1 error 2.2361, 90% kept. Image errors 0.1867, 0.1386, 0.1041, 0.0742 at ranks 5, 20, 50, 100 (storage 2.0%, 7.8%, 19.5%, 39.1%), equal to the formula; the column method gives 0.2404, 0.1766, 0.1373, 0.1046. PCA: the first two components hold 0.285; 5, 21, 29 and 41 components reach 50, 90, 95 and 99%. Reconstruction errors 858.945, 314.515 and 49.158 for $k$ = 2, 10, 30. Uncentred first direction: $|\cos|$ 0.99998 with the mean image. Runtime about 4 seconds.
- **Common problems:** `np.linalg.eigh` returns eigenvalues in increasing order; `np.linalg.svd` returns $V^\top$, whose rows are the directions; eigenvectors are defined only up to sign, so compare absolute values.

### Quiz

1. Why are the eigenvectors of a covariance matrix orthogonal?
   - **Answer:** a covariance matrix is symmetric, and symmetric matrices have orthonormal eigenvectors (the spectral theorem).
2. What does Eckart–Young guarantee?
   - **Answer:** no rank-$k$ matrix is closer to $B$ in the Frobenius norm than the truncated SVD; the error is the square root of the sum of the dropped $\sigma_i^2$.
3. How do you get principal directions and explained-variance ratios from the SVD?
   - **Answer:** centre the data and take $X_c = U\Sigma V^\top$; the rows of $V^\top$ are the directions and $\sigma_i^2 / \sum_j \sigma_j^2$ are the ratios.

**Watch out:** "PCA needs no centring" and "PCA keeps the most important original features." Without centring, the lab's first direction had $|\cos|$ 0.99998 with the mean image: it described where the digits sit, not how they vary. And the first principal component gave weight to 61 of the 64 pixels (the other 3 are blank in every image). PCA builds new, mixed directions; to choose original features, use a feature-selection method.

### Assignment 3 (due before session 4, 10 points)

1. By hand, the eigenvalues and unit eigenvectors of `[[4, 1], [1, 4]]`, and three steps of power iteration from (1, 0). Check in NumPy. (3 points)
2. Complete the deflation TODO, report how many steps the second eigenvector needs, and explain the number with $\lambda_3 / \lambda_2$. Then compress `flower.jpg` from scikit-learn and give the smallest rank with a relative error below 0.1. (4 points)
3. Run PCA on the wine data with and without standardizing. Report the explained-variance ratio of the first two components and the feature with the largest weight in PC 1 in each case, and explain the difference in two sentences. (3 points)

Hand in one PDF and your notebook.

### Sources

- Strang, MIT 18.06 Linear Algebra, lecture videos and notes. https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Strang 2019, Linear Algebra and Learning from Data. https://math.mit.edu/~gs/learningfromdata/
- Eckart & Young 1936, The approximation of one matrix by another of lower rank, Psychometrika 1(3).
- Shlens 2014, A Tutorial on Principal Component Analysis. https://arxiv.org/abs/1404.1100
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 4 and 10. https://mml-book.github.io/
- 3Blue1Brown, Essence of Linear Algebra (eigenvectors and eigenvalues). https://www.3blue1brown.com/topics/linear-algebra

## Session 4: Calculus for ML: gradients, Jacobians and the chain rule

**Goal:** students can compute partial derivatives, gradients and Jacobians of ML losses by hand, apply the chain rule, and check gradients numerically.

### Talking pointers

- **Open with:** "Every model in this course learns by following a gradient. Today you compute gradients by hand, and you learn the one test that tells you whether your gradient code is right."
- **Segment 1, say:** show the contour plot with its arrows and the descent path, and point out that each arrow crosses the contours at a right angle.
- **Segment 2, say:** write the softmax Jacobian for three classes at $z = 0$ on the board, then multiply it by the loss gradient to reach $p - \text{onehot}(y)$.
- **Segment 3, say:** show the V-shaped error plot and find the best step $h$ for each method.
- **Close with:** "Derive by hand, check with central differences in float64, and only then train." Then set assignment 4.

### Segment 1 (6 min): slopes, partial derivatives and gradients

- The derivative $f'(x)$ is the local slope: $f(x + h) \approx f(x) + f'(x)\,h$ for small $h$ (3Blue1Brown, Essence of Calculus).
- A partial derivative $\partial f / \partial x_i$ moves only $x_i$. The gradient $\nabla f$ collects them all: for $f = x_1^2 + 3x_2^2$, $\nabla f = (2x_1, 6x_2)$.
- The gradient points in the direction of steepest increase, and its length is that rate of increase. It is perpendicular to the contours, the curves on which $f$ is constant (Deisenroth et al. 2020, chapter 5).
- Gradient descent steps against it: $w \leftarrow w - \eta \nabla L(w)$, with step size (learning rate) $\eta$. Course 1 session 2 did this for a straight line's weight and bias; sessions 8 and 9 analyse it.
- **Pause and try:** for $f = x_1^2 + 3x_2^2$, what is $\nabla f(1, 1)$, and which way does gradient descent move?
  - **Answer:** (2, 6). It moves along −(2, 6), mostly in $x_2$, where $f$ is steeper.

### Segment 2 (7 min): Jacobians, the chain rule and matrix calculus

- For $g: \mathbb{R}^n \to \mathbb{R}^m$, the Jacobian $J_g$ is the $m \times n$ matrix of $\partial g_i / \partial x_j$. The chain rule multiplies Jacobians: $J_{f \circ g}(x) = J_f(g(x))\, J_g(x)$. For $h(x) = \tanh(Wx)$, $J_h = \operatorname{diag}(1 - \tanh^2(Wx))\, W$.
- Three rules cover most ML derivations (Parr & Howard 2018): $\nabla_x (a^\top x) = a$; $\nabla_x (x^\top A x) = (A + A^\top)x$, which is $2Ax$ only for symmetric $A$; and $\nabla_x \|Ax - b\|^2 = 2A^\top(Ax - b)$.
- The softmax Jacobian is $\operatorname{diag}(p) - pp^\top$, and the gradient of the cross-entropy with respect to the logits is $p - \text{onehot}(y)$: predicted minus true probabilities.
- Logistic regression: with $z = Xw$, $L = \frac{1}{n}\sum_i [\log(1 + e^{z_i}) - y_i z_i]$ and $\partial L / \partial z_i = (\sigma(z_i) - y_i)/n$. The chain rule through $z = Xw$ gives $\nabla L = X^\top(\sigma(Xw) - y)/n$.
- Books differ on whether a gradient is a row or a column. Keep one rule: the gradient has the same shape as $w$.
- **Pause and try:** for one example $x = (1, 2)$, $y = 1$ and $w = (0, 0)$, compute $\nabla_w L$.
  - **Answer:** $z = 0$, so $p = \sigma(0) = 0.5$ and $\nabla_w L = (p - y)\,x = -0.5 \times (1, 2) = (-0.5, -1)$.

### Segment 3 (7 min): Taylor expansion and gradient checks

- Taylor: $L(w + \delta) = L(w) + \nabla L(w)^\top \delta + O(\|\delta\|^2)$. With $\delta = -\eta \nabla L$ the first-order change is $-\eta \|\nabla L\|^2 < 0$, so a small enough step always lowers the loss (Goodfellow et al. 2016, chapter 4). In the lab the actual decrease was 0.25 of this prediction at $\eta = 1$ and 0.9985 at $\eta = 0.001$.
- A gradient check compares your formula with central differences, $(f(w + h e_i) - f(w - h e_i))/2h$, using the relative error $\|g_a - g_n\| / (\|g_a\| + \|g_n\|)$.
- Truncation error is about $\frac{h}{2}|f''|$ for forward differences and $\frac{h^2}{6}|f^{(3)}|$ for central ones. Rounding error is about $\varepsilon |f| / h$, with $\varepsilon \approx 2.2 \times 10^{-16}$ in float64. Balancing the two gives $h \approx 10^{-8}$ (forward) and $h \approx 10^{-5}$ (central) (Nocedal & Wright 2006).
- Check in float64: in float32 ($\varepsilon \approx 1.2 \times 10^{-7}$) the best central error in the lab was only $10^{-5}$. And check at a random point, not at a minimum, where both gradients are close to zero.
- **Pause and try:** the central-difference error for $\sin'(1)$ is $9.0 \times 10^{-4}$ at $h = 0.1$. What do you expect at $h = 0.001$?
  - **Answer:** about $9 \times 10^{-8}$. Truncation error falls like $h^2$, so 100 times smaller $h$ gives 10,000 times smaller error while rounding stays below it.

### Lab guide (about 2 hours, notebook `s04_gradients.ipynb`)

1. Section 1 (15 min): both gradients by hand, then numerically.
2. Section 2 (20 min): contours, arrows and the descent path; the 39° example.
3. Section 3 (15 min): $x^\top A x$ by hand, then the three rules.
4. Section 4 (20 min): the softmax Jacobian and the chain rule by hand.
5. Section 5 (25 min): derive the logistic gradient, run the check and the three planted bugs, then the Taylor test.
6. Section 6 (15 min): mark truncation and rounding on the error plot.
7. TODO (15 min): the regularized gradient.

- **Expect:** hand values (2, 6), (−0.5, −1) and (4, 8); softmax Jacobian with 0.2222 and −0.1111; chain rule (−0.6667, 0.3333, 0.3333). Descent: loss 1.5478 to 0.3266 in 30 steps; angle 39.29 degrees. Matrix rules and tanh chain rule: relative errors 3.8e-12 to 1.1e-11; logistic gradient 9.1e-12; bugs 1.000, 0.996 and 0.612. Actual/predicted decrease: 0.2493, 0.8514, 0.9847, 0.9985 for step sizes 1 to 0.001; after 500 steps, training loss 0.0531 and accuracy 0.988. Best errors: forward 3.0e-09 at $h = 10^{-8}$, central 1.1e-11 at $h = 10^{-5}$, float32 central 1.0e-05 at $h = 10^{-2}$. Runtime about 3 seconds.
- **Common problems:** a relative error near 1 from a sign error or a missing $1/n$; checking in float32; computing the loss as `log(sigmoid(z))`, which gives `-inf` for large negative $z$ (use `np.logaddexp`, session 10).

### Quiz

1. What is $\nabla_x (x^\top A x)$ when $A$ is not symmetric?
   - **Answer:** $(A + A^\top)x$. The form $2Ax$ holds only for symmetric $A$.
2. Why use central rather than forward differences for gradient checks?
   - **Answer:** truncation error is $O(h^2)$ instead of $O(h)$, so the best error in float64 is about $10^{-11}$ instead of $10^{-8}$.
3. Your gradient check gives a relative error of 0.6. What do you conclude?
   - **Answer:** the formula is wrong; in the lab an extra factor gave 0.612, while the correct gradient gave $9 \times 10^{-12}$.

**Watch out:** "The gradient is the direction to the minimum." The gradient gives the steepest increase near the current point, so $-\nabla f$ is the steepest local decrease, which is a different thing. For $f = x_1^2 + 10x_2^2$ at (10, 1), $-\nabla f = -(20, 20)$ points 39° away from the straight line to the minimum at (0, 0). This is why gradient descent zig-zags on stretched losses (session 8).

### Assignment 4 (due before session 5, 10 points)

1. By hand: the gradient of $\frac{1}{n}\|Xw - y\|^2 + \lambda\|w\|^2$, and the Jacobian of $g(x) = (x_1 x_2,\ x_1 + x_2^2)$ at (1, 2). Check both numerically. (3 points)
2. Complete the TODO. Then run the logistic gradient check on the digits 0 and 1 from `load_digits` with $\lambda$ = 0, 0.1 and 1, report the relative errors, and plant one bug of your own. (4 points)
3. Repeat the step-size plot for $f(x) = e^x$ at $x = 1$ and for $f(x) = 1/x$ at $x = 0.01$. Explain any change in the best $h$ with the truncation and rounding formulas. (3 points)

Hand in one PDF and your notebook.

### Sources

- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 5. https://mml-book.github.io/
- Parr & Howard 2018, The Matrix Calculus You Need for Deep Learning. https://arxiv.org/abs/1802.01528
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 4. https://www.deeplearningbook.org/
- 3Blue1Brown, Essence of Calculus. https://www.3blue1brown.com/topics/calculus
- Nocedal & Wright 2006, Numerical Optimization (Springer; book).

## Session 5: Automatic differentiation and backpropagation

**Goal:** students can explain computational graphs, forward and reverse mode, and why backpropagation is reverse-mode automatic differentiation, and can build a tiny autodiff engine.

### Talking pointers

- **Open with:** "PyTorch gets the gradient of a loss with millions of weights from a single backward pass. Today you see why that is possible: it is the chain rule, applied in the right order."
- **Segment 1, say:** draw the computational graph of $f = \ln x_1 + x_1 x_2 - \sin x_2$ with the seven trace values from the notebook.
- **Segment 2, say:** expand $(2 + \varepsilon)^3$ on the board, then show the operation-count plot: $n$ passes against one.
- **Segment 3, say:** show the two training curves lying on top of each other, then the times: 7.2 s against 4.0 ms.
- **Close with:** "Backpropagation is reverse-mode automatic differentiation: one backward pass, every gradient, paid for in memory." Then set assignment 5.

### Segment 1 (6 min): three ways to get derivatives

- Symbolic differentiation manipulates formulas. It is exact, but for long programs the expressions can grow very large (Baydin et al. 2018).
- Numerical differentiation uses finite differences (session 4). It is simple but approximate, and needs about two evaluations per input: a million weights would need two million passes.
- Automatic differentiation (AD) applies the chain rule to each elementary operation of the program as it runs. It is exact up to rounding.
- A program is an evaluation trace of elementary operations, which we draw as a computational graph. For $f(x_1, x_2) = \ln x_1 + x_1 x_2 - \sin x_2$ at (2, 5): $v_3 = \ln v_1$, $v_4 = v_1 v_2$, $v_5 = \sin v_2$, $v_6 = v_3 + v_4$, $v_7 = v_6 - v_5 = 11.6521$.
- **Pause and try:** compute $\partial f/\partial x_1$ and $\partial f/\partial x_2$ at (2, 5) by hand ($\cos 5 \approx 0.2837$).
  - **Answer:** $\partial f/\partial x_1 = 1/x_1 + x_2 = 5.5$ and $\partial f/\partial x_2 = x_1 - \cos x_2 \approx 1.7163$.

### Segment 2 (7 min): forward mode, reverse mode and their costs

- Forward mode carries a derivative next to each value. Dual numbers $a + b\varepsilon$ with $\varepsilon^2 = 0$ do this: $f(a + b\varepsilon) = f(a) + f'(a)\,b\,\varepsilon$, and $(a + b\varepsilon)(c + d\varepsilon) = ac + (ad + bc)\varepsilon$ is the product rule.
- One forward pass with tangent $v$ gives a Jacobian–vector product $Jv$: one column of $J$ when $v = e_j$. A gradient with $n$ inputs needs $n$ passes.
- Reverse mode records the trace, then sweeps it backwards and computes adjoints $\bar v = \partial f / \partial v$: each node adds its adjoint times its local derivative to the adjoints of its inputs. One sweep from a seed $u$ gives a vector–Jacobian product $u^\top J$, one row of $J$.
- For $f: \mathbb{R}^n \to \mathbb{R}^m$, forward mode needs $n$ passes and reverse mode $m$. A loss has $m = 1$, so one backward pass gives the whole gradient. In the lab, with $n = 300$ inputs, forward mode used 269,400 operations and reverse mode 1,796. For one input and many outputs, forward mode wins instead.
- **Pause and try:** expand $(2 + \varepsilon)^3$ using $\varepsilon^2 = 0$. What does the coefficient of $\varepsilon$ tell you?
  - **Answer:** $(2 + \varepsilon)^3 = 8 + 12\varepsilon$, because every term with $\varepsilon^2$ or $\varepsilon^3$ vanishes. The 12 is the derivative of $x^3$ at 2, namely $3 \times 2^2$.

### Segment 3 (7 min): backpropagation is reverse mode

- A network is a program made of layers, and backpropagation is reverse-mode AD applied to it (Deisenroth et al. 2020, chapter 5).
- Each layer only needs its VJP. For $Y = XW + b$: $\bar X = \bar Y W^\top$, $\bar W = X^\top \bar Y$, and $\bar b$ sums $\bar Y$ over the batch. For $H = \tanh(A)$: $\bar A = \bar H \odot (1 - H^2)$. No Jacobian is formed; for an elementwise layer of width $n$ it would have $n^2$ entries, almost all zero.
- The backward pass reuses forward values ($X$, $H$), so frameworks store activations, and memory grows with depth, width and batch size. Activation checkpointing trades memory for recomputation (Course 2 session 2).
- In the lab, a scalar engine (Karpathy, micrograd) and NumPy VJPs followed the same training path; only the speed differed. Course 1 session 5 builds the engine step by step, and Course 8 session 6 describes the same backward pass as composing lenses.
- **Pause and try:** a layer computes $y = Wx$ with $W$ of shape 3 × 4, and the backward pass receives $\bar y$ of shape (3,). Give $\bar x$ and $\bar W$ with their shapes.
  - **Answer:** $\bar x = W^\top \bar y$, shape (4,), and $\bar W = \bar y\, x^\top$, shape 3 × 4, the same as $W$.

### Lab guide (about 2.5 hours, notebook `s05_autodiff.ipynb`)

1. Section 1 (15 min): the trace and both partial derivatives by hand, then run.
2. Section 2 (20 min): $(2 + \varepsilon)^3$ by hand, then the dual numbers and PyTorch's forward mode.
3. Section 3 (25 min): the adjoints by hand for the trace and for $g = xy + x^2$ at (3, 2), then the engine.
4. Section 4 (20 min): predict the operation counts, then run; read the JVP and the VJP.
5. Section 5 (25 min): derive the three VJPs; compare the engine, NumPy and PyTorch.
6. Sections 6–7 (20 min): the two training runs and the Newton loop.
7. TODO (25 min): `relu` and the forward-mode Jacobian.

- **Expect:** $f$ = 11.6521, with $\partial f/\partial x_1$ = 5.5000000000 and $\partial f/\partial x_2$ = 1.7163378145 from every method (central differences off by 3.1e-11 and 8.7e-11); $(2 + \varepsilon)^3$ = Dual(8, 12); $g$ = 15.0 with gradient (8.0, 3.0). Operations for $n$ = 10, 30, 100, 300: forward mode 280, 2,640, 29,800, 269,400; reverse mode 56, 176, 596, 1,796. Network: the same loss, 0.694916983862, from all three implementations, with gradient differences 5.6e-17 (engine) and 8.3e-17 (PyTorch); 8,236 engine objects against 1,100 stored numbers. After 100 steps both reach 0.121774 (largest difference 2.2e-16), in 7.2 s against 4.0 ms (timings vary); after 3,000 steps, training accuracy 1.000 and test accuracy 0.996. The Newton loop gives 0.353553390593274 = $1/(2\sqrt 2)$. Runtime about 15 seconds.
- **Common problems:** writing `grad =` instead of `grad +=` in a backward function, so a value used twice keeps only one contribution; not resetting gradients to zero between steps; a recursive graph sort that hits Python's recursion limit on long programs (the notebook's sort uses a loop).

### Quiz

1. For $f: \mathbb{R}^{1000} \to \mathbb{R}$, how many passes does each mode need for the full gradient?
   - **Answer:** forward mode needs 1,000, one per input; reverse mode needs one forward and one backward pass.
2. What does one reverse-mode pass compute for a function with many outputs?
   - **Answer:** a vector–Jacobian product $u^\top J$, a weighted sum of the rows of $J$. The full Jacobian needs one pass per output.
3. Why does training memory grow with batch size and depth?
   - **Answer:** the backward pass needs every layer's forward activations, so they are kept for the whole batch until the backward pass has used them.

**Watch out:** "Backpropagation is a special trick only for neural networks." It is reverse-mode automatic differentiation, and it works for any program built from differentiable operations, loops and branches included. In the lab the same engine differentiated six steps of Newton's method for $\sqrt a$ and returned 0.353553390593274, equal to $1/(2\sqrt 2)$. Baydin et al. (2018) describe backpropagation as a special case of reverse-mode AD, a technique also used in other areas of scientific computing.

### Assignment 5 (due before session 6, 10 points)

1. By hand, the forward-mode pass (with tangents) and the reverse-mode pass (with adjoints) for $f(x, y) = x e^y + y^2$ at (1, 0). Check both with the notebook's classes and with PyTorch. (3 points)
2. Complete both TODOs. Then add `sigmoid` to `Value`, train a 2-16-1 network on two moons with the engine, and report its training and test accuracy and its time against the NumPy version. (4 points)
3. Repeat section 7 with 1, 2 and 3 Newton steps. Compare the derivative of the program with $1/(2\sqrt 2)$ and explain why they differ until the loop has converged. (3 points)

Hand in one PDF and your notebook.

### Sources

- Baydin, Pearlmutter, Radul & Siskind 2018, Automatic Differentiation in Machine Learning: a Survey. https://arxiv.org/abs/1502.05767
- Karpathy, micrograd. https://github.com/karpathy/micrograd
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 5. https://mml-book.github.io/

## Session 6: Probability for ML

**Goal:** students can use random variables, common distributions, expectation, variance, covariance, conditional probability and Bayes' rule, and can sample from a multivariate Gaussian.

### Talking pointers

- **Open with:** "A test that is right 99% of the time says you have a disease that 1 in 100 people have. The chance that you really have it is 50%. Today you will see why."
- **Segment 1, say:** roll a die ten times on camera and average the results, then show the running-mean plot settling at 3.5.
- **Segment 2, say:** draw 10,000 people as a tree and ask for P(sick | positive) before computing it.
- **Segment 3, say:** show the three ellipses over the samples, and explain how the Cholesky factor shapes round noise.
- **Close with:** "Before you trust a probability, ask: conditional on what, and at which base rate?" Then set assignment 6.

### Segment 1 (6 min): random variables, expectation and variance

- A random variable is a number decided by chance: Bernoulli($p$), which is 1 with probability $p$, like a binary label; categorical, like the output of a softmax; Gaussian $\mathcal{N}(\mu, \sigma^2)$, like measurement noise (Blitzstein & Hwang, Stat 110).
- The expectation $E[X] = \sum_x x\, P(X = x)$ is the long-run average, and the variance $\operatorname{Var}[X] = E[X^2] - E[X]^2$ measures spread. For a fair die, $E[X] = 7/2$ and $\operatorname{Var}[X] = 91/6 - 49/4 = 35/12 \approx 2.92$.
- Expectation is always linear, $E[aX + bY] = aE[X] + bE[Y]$, but variances add only when $X$ and $Y$ are uncorrelated, for example independent.
- Law of large numbers: the average of $n$ independent draws approaches $E[X]$, with standard deviation $\sigma/\sqrt n$. Minibatch gradients (session 9) and test accuracies (session 7) are such averages.
- **Pause and try:** a Bernoulli variable has $p = 0.3$. What are its mean and variance, and the standard deviation of the average of 100 independent draws?
  - **Answer:** mean 0.3 and variance $p(1 - p) = 0.21$; the average has standard deviation $\sqrt{0.21/100} \approx 0.046$.

### Segment 2 (7 min): conditional probability and Bayes' rule

- A joint distribution P(A, B) gives each pair of outcomes a probability. The marginal is $P(A) = \sum_b P(A, b)$, the conditional is $P(A \mid B) = P(A, B)/P(B)$, and A and B are independent when $P(A, B) = P(A)P(B)$ for all outcomes (Deisenroth et al. 2020, chapter 6).
- Example: P(rain) = 0.3 and P(umbrella | rain) = 0.9, but P(rain | umbrella) = 0.27/0.41 ≈ 0.66. The two conditionals answer different questions.
- Bayes' rule: $P(D \mid +) = P(+ \mid D)\,P(D) / P(+)$, with $P(+) = P(+ \mid D)P(D) + P(+ \mid \neg D)P(\neg D)$.
- The medical test: base rate 1%, 99% of sick people detected, 1% of healthy people wrongly flagged. Of 10,000 people, 100 are sick and 99 of them test positive; 9,900 are healthy and 99 of them test positive. So P(D | +) = 99/198 = 0.5.
- The base rate decides the answer: at 0.1% the same test gives 0.09. A second independent positive test starts from 0.5 as the prior and gives 0.99. A classifier for rare events has the same problem: few of its alarms may be real.
- **Pause and try:** the same test is used where 10% of people are sick. What is P(D | +)?
  - **Answer:** of 10,000 people, 1,000 sick give 990 true positives and 9,000 healthy give 90 false positives, so 990/1,080 ≈ 0.917.

### Segment 3 (7 min): covariance and the multivariate Gaussian

- $\operatorname{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$; the correlation divides it by both standard deviations and lies in [−1, 1] (Goodfellow et al. 2016, chapter 3). A covariance matrix $\Sigma$ is symmetric with nonnegative eigenvalues, so its eigenvectors are orthogonal (session 3).
- $\mathcal{N}(\mu, \Sigma)$ has density proportional to $\exp(-\tfrac12 (x - \mu)^\top \Sigma^{-1} (x - \mu))$. Its contours are ellipses along the eigenvectors of $\Sigma$, with half-axes proportional to $\sqrt{\lambda_i}$. In 2-D the ellipse of size $r$ holds $1 - e^{-r^2/2}$ of the probability: 39%, 86% and 99% for $r$ = 1, 2, 3 (Bishop 2006, chapter 2).
- Sampling: factor $\Sigma = LL^\top$ (Cholesky, $L$ lower triangular), draw $z \sim \mathcal{N}(0, I)$ and set $x = \mu + Lz$; then $\operatorname{Cov}(x) = LL^\top = \Sigma$.
- Correlation is not causation. Hot days raise both cold-drink sales and electricity use, so the two were correlated (0.50) in the simulation, yet setting sales at random dropped it to 0.001. A common cause, a confounder, creates correlation without any causal link.
- **Pause and try:** $\Sigma$ has rows (4, 2) and (2, 2). Check that $L$ with rows (2, 0) and (1, 1) is its Cholesky factor, and compute $x = \mu + Lz$ for $\mu = (1, -1)$ and $z = (1, -1)$.
  - **Answer:** $LL^\top$ has rows (4, 2) and (2, 1 + 1) = (2, 2), as required. $Lz = (2, 0)$, so $x = (3, -1)$.

### Lab guide (about 2 hours, notebook `s06_probability.ipynb`)

1. Section 1 (15 min): the die and Bernoulli values as fractions by hand, then the simulation.
2. Section 2 (20 min): $\sigma/\sqrt n$ by hand for $n$ = 100 and 10,000, then the plots.
3. Section 3 (15 min): the rain table's marginals and conditionals by hand.
4. Section 4 (25 min): the medical test with counts, then the formula, the simulation and the base-rate curve.
5. Section 5 (25 min): the Cholesky factor by hand, then sampling, ellipses and the covariance estimate.
6. Section 6 (10 min): the confounder.
7. TODO (15 min): two tests by simulation and a 3-D Gaussian.

- **Expect:** die mean and variance 7/2 and 35/12 = 2.9167, simulated 3.4980 and 2.9103. Spread of the mean 0.5309, 0.1703, 0.0540, 0.0169 for $n$ = 10 to 10,000 (formula 0.5401, 0.1708, 0.0540, 0.0171). Rain table 0.9000 and 0.6585. Medical test 0.5000 by formula and 0.5013 from 1,000,000 simulated people; 0.0902, 0.9167 and 0.9900 at base rates 0.001, 0.1 and 0.5. Gaussian: $x$ = (3, −1); sample covariance (3.9277, 2.0053; 2.0053, 2.0501); ellipse coverage 0.3864, 0.8658, 0.9878 against 0.3935, 0.8647, 0.9889; covariance error 0.8185 at 50 samples and 0.0318 at 50,000. Confounder 0.501, then 0.001 after the intervention, and 0.027 within the narrow band (noise about ±0.011; 20 repeats average 0.007). Runtime about 3 seconds.
- **Common problems:** `np.cov` without `rowvar=False` treats rows as variables; passing a variance where NumPy's `normal` expects a standard deviation; confusing P(A | B) with P(A, B).

### Quiz

1. $X$ and $Y$ are independent, with variances 4 and 9. What is $\operatorname{Var}[X - Y]$?
   - **Answer:** 13. Variances of independent variables add, and $\operatorname{Var}[-Y] = \operatorname{Var}[Y]$.
2. Why can a positive result from a 99%-accurate test mean only a 50% chance of disease?
   - **Answer:** when the disease is rare, the healthy people wrongly flagged are as many as the sick people detected: 99 of each per 10,000 people at a 1% base rate.
3. How do you sample from $\mathcal{N}(\mu, \Sigma)$ with only a standard normal generator?
   - **Answer:** compute the Cholesky factor $L$ with $LL^\top = \Sigma$, draw $z \sim \mathcal{N}(0, I)$ and return $\mu + Lz$.

**Watch out:** "P(A | B) = P(B | A)." In the lab, P(positive | disease) = 0.99 but P(disease | positive) = 0.50, and P(umbrella | rain) = 0.90 but P(rain | umbrella) = 0.66. Bayes' rule links the two through the base rates, $P(A \mid B) = P(B \mid A)\,P(A)/P(B)$, so they are equal only when P(A) = P(B). Ignoring the base rate is called the base-rate fallacy.

### Assignment 6 (due before session 7, 10 points)

1. By hand: the mean and variance of the sum of two fair dice, and P(D | +) for a test with 90% sensitivity and a 5% false-positive rate at a base rate of 2%. Check both by simulation. (3 points)
2. Complete both TODOs. Then estimate P(D | + +) when the two tests are not independent: given the disease status, the second test copies the first result with probability 0.5 and is a fresh test otherwise. Explain why the answer differs from 0.99. (4 points)
3. Repeat the confounder simulation with a weaker link, drink sales = 0.3 × temperature + noise. Report the correlation, the correlation after setting sales at random, and the average correlation within narrow temperature bands, and explain each in one sentence. (3 points)

Hand in one PDF and your notebook.

### Sources

- Blitzstein & Hwang, Introduction to Probability (Stat 110, free materials). https://projects.iq.harvard.edu/stat110/home
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 6. https://mml-book.github.io/
- Bishop 2006, Pattern Recognition and Machine Learning, chapter 2. https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 3. https://www.deeplearningbook.org/

## Session 7: Statistics and estimation: MLE, MAP and uncertainty

**Goal:** students can derive maximum likelihood and MAP estimates, connect priors to regularization and losses to likelihoods, and put uncertainty on an estimate.

### Talking pointers

- **Open with:** "Your classifier scores 96.7% on the test set. Is it really better than one that scores 96%? Today we see where losses come from, and how sure a number from data can be."
- **Segment 1, say:** write the likelihood $p^3$ for 3 heads in 3 flips and ask where it is largest. Then show that cross-entropy is a log-likelihood with a minus sign.
- **Segment 2, say:** add one imaginary head and one imaginary tail to the coin; then show the ridge plot, where the best λ lands at σ²/τ².
- **Segment 3, say:** show the bootstrap histogram, then the 50 intervals with the one red interval that misses.
- **Close with:** "Every loss is a likelihood, every regularizer is a prior, and every number from data needs an error bar." Then set assignment 7.

### Segment 1 (6 min): likelihood and maximum likelihood

- A model gives the probability of the data, $p(D \mid \theta)$. As a function of the parameter θ, with the data fixed, it is the **likelihood** $L(\theta)$, not a probability distribution over θ.
- For independent data the likelihood is a product, so we maximize its logarithm, a sum. The maximum likelihood estimate (MLE) maximizes $\log L$, or equivalently minimizes the negative log-likelihood (NLL).
- A coin with $k$ heads in $n$ flips: $\log L(p) = k \log p + (n-k)\log(1-p)$, and setting the derivative to zero gives $\hat p = k/n$ (Course 1 session 2).
- Gaussian data: $\hat\mu = \bar x$ and $\hat\sigma^2 = \frac{1}{n}\sum_i (x_i - \bar x)^2$, dividing by $n$, not $n - 1$.
- Losses are NLLs. If $y = f_\theta(x) + \varepsilon$ with noise $\varepsilon \sim N(0, \sigma^2)$, then $-\log p(y \mid x) = (y - f_\theta(x))^2/(2\sigma^2) + \text{const}$: squared error. For a classifier giving class $y$ probability $q_\theta(y \mid x)$, the NLL $-\log q_\theta(y \mid x)$ is the cross-entropy loss (Goodfellow et al. 2016, chapter 5).
- **Pause and try:** the data 2, 4, 6 come from a Gaussian. What are the MLEs of μ and σ²?
  - **Answer:** $\hat\mu = 4$ and $\hat\sigma^2 = (4 + 0 + 4)/3 = 8/3 \approx 2.67$, dividing by $n = 3$.

### Segment 2 (7 min): priors and MAP

- Bayes' rule (session 6): $p(\theta \mid D) \propto p(D \mid \theta)\,p(\theta)$. The maximum a posteriori (MAP) estimate maximizes the log-likelihood plus the log-prior. It keeps only the peak of the posterior.
- A coin with a Beta(2, 2) prior, $p(p) \propto p(1-p)$, has MAP estimate $(k+1)/(n+2)$: one imaginary head and one imaginary tail. After 3 heads in 3 flips the MLE is 1 ("tails is impossible"); MAP gives 0.8. After 300 heads in 400 flips they almost agree: 0.75 and 301/402 ≈ 0.749.
- A Gaussian prior gives ridge regression. With $y = Xw + \varepsilon$, $\varepsilon \sim N(0, \sigma^2 I)$ and $w \sim N(0, \tau^2 I)$, the negative log posterior is $\|y - Xw\|^2/(2\sigma^2) + \|w\|^2/(2\tau^2)$ plus a constant. Multiplying by $2\sigma^2$ gives $\|y - Xw\|^2 + \lambda\|w\|^2$ with $\lambda = \sigma^2/\tau^2$ (Bishop 2006, section 3.3). A Laplace prior gives the L1 penalty (the lasso) the same way.
- **Pause and try:** one feature, no intercept, $x = (1, 2)$, $y = (1, 2)$, σ² = 1 and τ² = 0.2. What are λ and the ridge estimate $w = \sum_i x_i y_i / (\sum_i x_i^2 + \lambda)$?
  - **Answer:** λ = 1/0.2 = 5 and $w = 5/(5 + 5) = 0.5$, half the least-squares value of 1: the prior pulls w towards 0.

### Segment 3 (7 min): uncertainty, the bootstrap, bias and variance

- An estimate is a random variable: new data would give a new value. Its standard deviation is the **standard error** (SE): σ/√n for a mean, $\sqrt{\hat p(1-\hat p)/n}$ for an accuracy $\hat p$ on $n$ test examples.
- The normal-approximation 95% confidence interval is estimate ± 1.96 SE. It can be poor for small $n$ or accuracies near 0 or 1.
- The bootstrap (Efron & Tibshirani 1993): resample the $n$ data points with replacement, recompute the estimate, repeat a few thousand times, and take the 2.5th and 97.5th percentiles. It needs no formula, so it also works for a median, an F1-score or an AUC. Course 1 session 9 suggests it for results over a few seeds.
- An estimator's mean squared error (MSE) is bias² + variance, with bias $E[\hat\theta] - \theta$. The $1/n$ variance estimate is biased (its average is $\frac{n-1}{n}\sigma^2$), yet for Gaussian data its MSE is lower than that of the unbiased $1/(n-1)$ version. MAP also trades a little bias for less variance.
- **Pause and try:** a classifier scores 0.9 on 400 test images. What is the 95% interval, and how many test images would halve its width?
  - **Answer:** SE = $\sqrt{0.9 \times 0.1/400}$ = 0.015, so 0.9 ± 0.029, about 0.871 to 0.929. The width shrinks like $1/\sqrt{n}$, so four times as many: 1,600.

### Lab guide (about 2 hours, notebook `s07_estimation.ipynb`)

1. Sections 1–2 (25 min): the coin and the Gaussian on paper, then in code; losses as NLLs.
2. Sections 3–4 (25 min): MLE against MAP for 3 to 1,000 flips; the two variance estimates.
3. Section 5 (25 min): ridge as MAP. Read the test-error curves and the shrinking weights.
4. Sections 6–7 (25 min): the bootstrap interval for a digit classifier; the coverage simulation.
5. TODO cells (20 min): MAP for a Gaussian mean; a paired bootstrap.

- **Expect:** 3 heads in 3 flips: MLE 1.000, MAP 0.800; data 2, 4, 6: μ̂ = 4.0000, σ̂² = 2.6667. MSE at n = 3: for p = 0.7, MLE 0.06984 and MAP 0.03138; for p = 0.95, MLE 0.01549 and MAP 0.03774; equal by n = 1,000. Variance estimates average 3.200 and 3.999, with MSE 5.76 and 8.00. Ridge: best λ 3.98 for n = 30 and n = 200 (σ²/τ² = 4); mean test MSE falls from 3.139 to 2.091 at n = 30, but only from 1.111 to 1.109 at n = 200. Digits: accuracy 0.9667 (348 of 360), normal interval 0.9481 to 0.9852, bootstrap 0.9472 to 0.9833. Coverage over 1,000 simulated test sets: 0.938 (normal), 0.956 (bootstrap). Runtime about 6 seconds.
- **Common problems:** `np.var` divides by n unless you pass `ddof=1`; resampling without replacement, which returns the same test set and an interval of width zero; comparing two classifiers by whether their intervals overlap instead of bootstrapping the paired difference.

### Quiz

1. Why is minimizing cross-entropy the same as maximum likelihood?
   - **Answer:** each example's cross-entropy loss, $-\log q_\theta(y \mid x)$, is its NLL; summed over independent examples, it is the NLL of the data set.
2. Which prior gives ridge regression, and what is λ?
   - **Answer:** a Gaussian prior $w \sim N(0, \tau^2 I)$; with noise variance σ², λ = σ²/τ².
3. How does the bootstrap build a 95% interval for a test accuracy?
   - **Answer:** resample the test results with replacement many times, compute each resample's accuracy, and take the 2.5th and 97.5th percentiles.

**Watch out:** "A 95% confidence interval means a 95% chance that the true value is inside this particular interval." The 95% belongs to the procedure: over many repeated experiments, about 95% of its intervals contain the true value. In the notebook, 49 of the first 50 simulated intervals contained the true accuracy 0.9; any one interval either contains it or not. A probability statement about the parameter itself needs a Bayesian credible interval, and so a prior.

### Assignment 7 (due before session 8, 10 points)

1. By hand, derive the MAP estimate for a coin with a Beta(a, b) prior, and show that the $1/n$ variance estimate averages $\frac{n-1}{n}\sigma^2$. Complete the first TODO cell. (3 points)
2. Repeat the ridge sweep with τ = 0.25 and τ = 1. Does the best λ move to σ²/τ² (16 and 1)? Plot the curves and explain the difference between n = 30 and n = 200. (4 points)
3. Complete the paired bootstrap of logistic regression against 3-nearest-neighbours. Report the difference in accuracy with its 95% interval, and say whether one is clearly better. (3 points)

Hand in one PDF and your notebook.

### Sources

- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 8–9. https://mml-book.github.io/
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 5. https://www.deeplearningbook.org/
- Bishop 2006, Pattern Recognition and Machine Learning, chapters 1–3. https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
- Efron & Tibshirani 1993, An Introduction to the Bootstrap (Chapman & Hall).
- Blitzstein & Hwang, Introduction to Probability (Stat 110). https://projects.iq.harvard.edu/stat110/home

## Session 8: Optimization I: gradient descent and convexity

**Goal:** students can run and analyse gradient descent, explain step-size limits, convexity and conditioning, and see why momentum helps.

### Talking pointers

- **Open with:** "Double the learning rate and training may get faster, get slower, or explode. Today the mathematics tells you which one, before you press run."
- **Segment 1, say:** on the board, iterate $x \leftarrow (1 - 4\eta)x$ for $f(x) = 2x^2$ with η = 0.4 and η = 0.6, then show the notebook's step-size plot.
- **Segment 2, say:** draw a bowl with a chord above it; then show the network's loss climbing from 0.017 to 1.78 between two equally good networks.
- **Segment 3, say:** show the three zig-zag paths, then the breast-cancer result: not converged after 20,000 iterations on raw features, 898 iterations after standardizing.
- **Close with:** "The steepest direction limits the step; the condition number sets the speed." Then set assignment 8.

### Segment 1 (6 min): gradient descent and the step-size limit

- Gradient descent (GD) repeats $x_{t+1} = x_t - \eta \nabla f(x_t)$ with step size (learning rate) η. Session 4 showed why a small step along $-\nabla f$ lowers f.
- Take a quadratic $f(x) = \frac12 x^\top A x - b^\top x$ with A symmetric positive definite. Then $\nabla f = Ax - b$, the minimizer solves $Ax^* = b$, and the error $e_t = x_t - x^*$ obeys $e_{t+1} = (I - \eta A)e_t$.
- In the eigenvector basis of A, each component is multiplied by $1 - \eta\lambda_i$ per step. GD converges exactly when $|1 - \eta\lambda_i| < 1$ for every eigenvalue, that is, when $0 < \eta < 2/\lambda_{\max}$.
- For any smooth function whose Hessian eigenvalues are at most L, a step $\eta < 2/L$ lowers f by at least $\eta(1 - L\eta/2)\|\nabla f\|^2$ (Bottou et al. 2018).
- **Pause and try:** $f(x) = 2x^2$, $x_0 = 1$ and η = 0.6. What are $x_1$ and $x_2$, and what is the largest step size that converges?
  - **Answer:** each step multiplies x by 1 − 4η = −1.4, so $x_1 = -1.4$ and $x_2 = 1.96$: it diverges. The limit is 2/4 = 0.5.

### Segment 2 (7 min): convexity

- A function is convex if every chord lies on or above its graph: $f(\theta a + (1-\theta)b) \le \theta f(a) + (1-\theta) f(b)$ for $0 \le \theta \le 1$. A twice-differentiable f is convex exactly when its Hessian is positive semidefinite everywhere (Boyd & Vandenberghe 2004, chapter 3).
- Equivalently, every tangent plane lies below the graph: $f(y) \ge f(x) + \nabla f(x)^\top (y - x)$. So where $\nabla f(x) = 0$, no point is lower: for a convex function every local minimum is global.
- Convex losses in ML: least squares, logistic regression, ridge, the lasso and the support vector machine. Sums of convex functions are convex, and so is a convex function of a linear map.
- Neural network losses are not convex. Swapping two hidden units gives different weights with exactly the same loss, and the points between them are usually worse: in the notebook, 0.0167 at both ends and 1.784 at the midpoint. Gradient methods still train such networks well, for reasons that are only partly understood (Course 2 session 3).
- **Pause and try:** is $f(x) = x^4 - 2x^2$ convex? Where are its minima?
  - **Answer:** no: $f''(x) = 12x^2 - 4 < 0$ for $|x| < 1/\sqrt3 \approx 0.58$. The minima are at x = ±1 (f = −1), with a local maximum at x = 0.

### Segment 3 (7 min): conditioning, feature scaling and momentum

- The condition number of the Hessian, $\kappa = \lambda_{\max}/\lambda_{\min}$, measures how stretched the valley is.
- With the best fixed step, $\eta = 2/(\lambda_{\min} + \lambda_{\max})$, the error shrinks by $(\kappa - 1)/(\kappa + 1)$ per step: 0.980 for κ = 100, so 691 steps to shrink it by 10⁶ (69 steps for κ = 10). The steep direction caps the step, so GD zig-zags across the valley while creeping along it (Goodfellow et al. 2016, chapter 4).
- Feature scaling changes κ. A linear model's Hessian is built from $X^\top X$, so a feature in the hundreds next to one near 0.1 makes κ huge. Standardizing each feature (mean 0, standard deviation 1) is a change of units: the minimum loss stays the same, but κ can shrink enormously.
- Heavy-ball momentum (Polyak 1964): $v \leftarrow \beta v - \eta\nabla f(x)$, then $x \leftarrow x + v$. On a quadratic with the best η and β, the error shrinks by about $(\sqrt\kappa - 1)/(\sqrt\kappa + 1)$ per step, 0.818 instead of 0.980 for κ = 100 (Goh 2017 shows why, interactively). Adam (Course 2 session 2) also uses momentum.
- **Pause and try:** a quadratic has Hessian eigenvalues 1 and 100. What is the largest stable step? At η = 0.01, by what factor does the flat direction shrink per step?
  - **Answer:** η < 2/100 = 0.02. At η = 0.01 the flat direction shrinks by 1 − 0.01 × 1 = 0.99 per step, so it needs about 460 steps to shrink by a factor of 100.

### Lab guide (about 2 hours, notebook `s08_gradient_descent.ipynb`)

1. Section 1 (15 min): the 1-D iterations on paper, then in code.
2. Sections 2–3 (30 min): paths for κ = 1, 10 and 100, then four step sizes around the limit.
3. Section 4 (20 min): convexity along a line, for logistic regression and a small network.
4. Sections 5–6 (35 min): raw against standardized features, then momentum.
5. TODO cells (20 min): Nesterov's method and a step-size sweep.

- **Expect:** for η = 0.6, $x_1, \dots, x_5$ = −1.4, 1.96, −2.744, 3.842, −5.378. Best-step GD takes 1, 69 and 691 steps for κ = 1, 10 and 100, as theory predicts. For κ = 10, after 100 steps f = 3.53e-08 (η = 0.1), 2.04e-16 (η = 0.182), 0.0879 (η = 0.198) and 262 (η = 0.202). Logistic loss: smallest Hessian eigenvalue 0.0017, midpoint 1.073 below the chord's 1.500; network: 0.0167 at both ends, 1.784 at the midpoint. Breast cancer: the same minimum, 0.09959138, in both units; raw features (Hessian condition number 4.16e11) are still 0.262 above it after 20,000 iterations, standardized ones (22.9) converge in 898 iterations, or 129 with momentum. Heavy ball on κ = 100: 85 steps against 691. Runtime about 5 seconds.
- **Common problems:** reading a flat loss curve as convergence (the raw run looks flat while 0.262 above the minimum); standardizing with statistics that include the test set; tuning momentum without retuning the step size.

### Quiz

1. Why must η be below $2/\lambda_{\max}$ on a quadratic?
   - **Answer:** each step multiplies the error along eigenvector i by $1 - \eta\lambda_i$, and the steepest direction has $|1 - \eta\lambda_{\max}| < 1$ only if $\eta < 2/\lambda_{\max}$.
2. Why is every local minimum of a convex function global?
   - **Answer:** the tangent plane lies below the graph, $f(y) \ge f(x) + \nabla f(x)^\top (y - x)$, so where the gradient is zero no point is lower.
3. Why does standardizing features speed up GD on logistic regression?
   - **Answer:** it lowers the Hessian's condition number, so one step size suits all directions. The minimum loss itself does not change.

**Watch out:** "A bigger learning rate is always faster." Below the limit $2/\lambda_{\max}$, a larger step speeds up the flat directions but slows the steep ones, whose factor $1 - \eta\lambda_{\max}$ approaches −1. In the notebook, η = 0.198 left f at 0.0879 after 100 steps, the smaller η = 0.182 reached 2.04e-16, and η = 0.202 diverged.

### Assignment 8 (due before session 9, 10 points)

1. For $f(x) = \frac12(x_1^2 + 25x_2^2)$, find by hand the stable range of η, the best fixed step, its rate per step and the number of steps to shrink the error by 10⁶. Check them in code. (3 points)
2. Complete both TODO cells. Report Nesterov's steps on the κ = 100 quadratic and the best step size from your sweep, and compare both with theory. (4 points)
3. Repeat the permutation test of section 4 with three seeds and two other permutations. Explain in one paragraph why a single line on which the loss rises above its chord proves that the loss is not convex. (3 points)

Hand in one PDF and your notebook.

### Sources

- Boyd & Vandenberghe 2004, Convex Optimization, chapters 3 and 9. https://web.stanford.edu/~boyd/cvxbook/
- Bottou, Curtis & Nocedal 2018, Optimization Methods for Large-Scale Machine Learning. https://arxiv.org/abs/1606.04838
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapter 7. https://mml-book.github.io/
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 4. https://www.deeplearningbook.org/
- Polyak 1964, Some methods of speeding up the convergence of iteration methods, USSR Computational Mathematics and Mathematical Physics 4(5). https://doi.org/10.1016/0041-5553(64)90137-5
- Goh 2017, Why Momentum Really Works, Distill. https://distill.pub/2017/momentum/

## Session 9: Optimization II: SGD, Newton's method and constraints

**Goal:** students can explain stochastic gradients, second-order methods and Lagrange multipliers, and choose between them.

### Talking pointers

- **Open with:** "Gradient descent reads all the data before each step, SGD steps after ten examples, and Newton's method takes five steps in total. Which would you use, and when?"
- **Segment 1, say:** show the passes plot: after one pass SGD is ten times closer to the minimum, then it stalls unless the step decays.
- **Segment 2, say:** run Newton for $e^x - 2x$ on the board for two steps, then show the errors 0.31, 0.043, 0.0009, 4e-7.
- **Segment 3, say:** draw the line x + 2y = 5 and the smallest circle about the origin that touches it; then show the die's log-probabilities on a straight line.
- **Close with:** "SGD for big data, Newton for small, well-behaved problems, L-BFGS in between, and Lagrange multipliers whenever there is a constraint." Then set assignment 9.

### Segment 1 (7 min): stochastic gradient descent

- A training loss is an average, $f(w) = \frac1n\sum_i f_i(w)$, so one exact gradient costs n example-gradients. Stochastic gradient descent (SGD) instead steps along the gradient of a random minibatch of B examples.
- This estimate is unbiased (its average is the full gradient), and with replacement its variance is the single-example variance divided by B.
- One pass over the data buys one GD step or n/B SGD steps; early on, many noisy steps beat one exact step (Bottou et al. 2018).
- With a constant step, SGD does not converge: it hovers in a noise ball around the minimum that grows with η and shrinks with B. Decaying steps fix this; the classical conditions are $\sum_t \eta_t = \infty$ and $\sum_t \eta_t^2 < \infty$, for example $\eta_t \propto 1/t$ (Bottou et al. 2018).
- Adaptive methods such as Adam (Kingma & Ba 2015) give each weight its own step size from running averages of past gradients and their squares; Course 2 session 2 covers them.
- **Pause and try:** single-example gradients have standard deviation 2 in every coordinate. What is it for the average over a minibatch of 16?
  - **Answer:** the variance falls from 4 to 4/16 = 0.25, so the standard deviation is 0.5. Each fourfold increase in batch size halves the noise.

### Segment 2 (7 min): Newton's method and quasi-Newton

- Newton's method minimizes the quadratic Taylor model $f(w + d) \approx f(w) + \nabla f^\top d + \frac12 d^\top H d$, where H is the Hessian, so the step is $d = -H^{-1}\nabla f$. On a quadratic it lands on the minimizer in one step, whatever the condition number.
- Near a minimizer with positive definite H, convergence is quadratic: the error is roughly squared each step, so the correct digits double (Nocedal & Wright 2006).
- The price: forming H costs about $nd^2$ operations, solving with it $d^3$, and storing it $d^2$ numbers. For $10^6$ weights, H has $10^{12}$ entries, 4 TB in float32.
- Newton looks for a zero of the gradient, not a minimum: where H is not positive definite it can step uphill or converge to a maximum or saddle point. Practical versions add a line search, damping or a trust region.
- Quasi-Newton methods approximate $H^{-1}$ from changes in the gradient. BFGS stores a dense d × d matrix; L-BFGS keeps only the last few changes (10 in SciPy), so its memory grows linearly in d. It is scikit-learn's default solver for logistic regression.
- **Pause and try:** Newton's method for $f(x) = e^x - 2x$ from $x_0 = 0$. What is $x_1$?
  - **Answer:** $x_1 = x_0 - f'(x_0)/f''(x_0) = 0 - (1 - 2)/1 = 1$. The next step gives 0.736, close to the minimizer ln 2 ≈ 0.693.

### Segment 3 (6 min): constraints and Lagrange multipliers

- To minimize f(x) subject to g(x) = c: at the solution ∇f is perpendicular to the constraint surface, so it is parallel to ∇g: $\nabla f = \lambda\nabla g$. The number λ is the Lagrange multiplier; it also equals the rate at which the best value changes as c changes (Deisenroth et al. 2020, chapter 7).
- With inequality constraints, the Karush–Kuhn–Tucker (KKT) conditions add that multipliers are nonnegative, and that a multiplier is zero unless its constraint is tight (Boyd & Vandenberghe 2004, chapter 5).
- Maximum entropy: among distributions on the faces 1 to 6 with a given mean, the one with the largest entropy $-\sum_i p_i \ln p_i$ satisfies $-\ln p_i - 1 + \alpha + \beta i = 0$, so $p_i \propto e^{\beta i}$. That is a softmax of the scores βi, the Boltzmann distribution of physics, with β as an inverse temperature (Cover & Thomas 2006, chapter 12). For mean 4.5, β = 0.371.
- In the support vector machine (SVM) dual, multipliers $\alpha_i \ge 0$ give $w = \sum_i \alpha_i y_i x_i$, with $\alpha_i > 0$ only for the support vectors; the data enter only through dot products, which allows kernels (Bishop 2006, chapter 7).
- **Pause and try:** minimize $x^2 + y^2$ subject to $x + 2y = 5$.
  - **Answer:** $(2x, 2y) = \lambda(1, 2)$ gives $x = \lambda/2$ and $y = \lambda$; then $5\lambda/2 = 5$, so λ = 2, the point (1, 2) and the value 5, the squared distance from the origin to the line.

### Lab guide (about 2.5 hours, notebook `s09_sgd_newton_constraints.ipynb`)

1. Section 1 (15 min): Newton for $e^x - 2x$ on paper, then in code.
2. Sections 2–3 (35 min): minibatch variance; GD against three SGD variants, per pass.
3. Sections 4–6 (40 min): Newton and L-BFGS, checked against scikit-learn; Newton on $x^4 - 2x^2$.
4. Sections 7–8 (30 min): the Lagrange example, the maximum-entropy die, the SVM dual.
5. TODO cells (30 min): Newton for β; iterate averaging.

- **Expect:** Newton errors 6.93e-01, 3.07e-01, 4.26e-02, 8.95e-04, 4.00e-07, 8.02e-14. Variance × B: 5.109, 5.220, 5.236. f − f* after 1 and 30 passes: GD 4.51e-02 and 9.18e-06; SGD with constant step, B = 10: 4.75e-03 and 4.15e-03; B = 100: 2.53e-02 and 1.93e-04; B = 10 with decaying step: 3.13e-03 and 8.98e-06. Newton: 5 iterations, within 1.2e-08 of scikit-learn; L-BFGS 17 iterations; GD 83 iterations to reach 1e-10. SLSQP: (1, 2) with multiplier 2.0000. Die with mean 4.5: 0.0544, 0.0788, 0.1142, 0.1654, 0.2398, 0.3475, β = 0.3710. SVM: 3 support vectors, $\sum_i \alpha_i y_i$ = −2.8e-17. Runtime about 6 seconds.
- **Common problems:** judging SGD from one noisy evaluation; forgetting to reshuffle the data every pass; dropping the L2 term, which leaves the Hessian singular here because two features are exact combinations of others.

### Quiz

1. Why does SGD with a constant step stop improving, and what fixes it?
   - **Answer:** gradient noise keeps it in a ball around the minimum, which grows with η and shrinks with B; a decaying step, iterate averaging or larger batches shrink it.
2. Why is Newton's method rarely used to train neural networks?
   - **Answer:** the Hessian has $d^2$ entries ($10^{12}$ for a million weights), solving with it costs about $d^3$, and on non-convex losses the step can head for saddle points or maxima.
3. What distribution maximizes entropy for a fixed mean?
   - **Answer:** $p_i \propto e^{\beta i}$, a softmax (Boltzmann) form whose multiplier β is set by the mean.

**Watch out:** "Newton's method is always better because it converges faster." It needs fewer iterations, but each one costs far more, and for large d it is impossible. It also treats every zero of the gradient alike: in the notebook it went from 0.1 to the maximum of $x^4 - 2x^2$, while gradient descent went to a minimum. L-BFGS or SGD is usually the better trade.

### Assignment 9 (due before session 10, 10 points)

1. By hand: two Newton steps for $e^x - 2x$ from $x_0 = 0$, and the minimum of $x^2 + y^2 + z^2$ subject to $x + y + z = 3$, with its multiplier. Check both in code. (3 points)
2. Rerun section 3 with B = 1, 10 and 100 at the same ratio η/B, and with two decay schedules. Plot f − f* against passes and against wall-clock time. Which method is best after 1 pass, and after 30? (4 points)
3. Complete both TODO cells. Also solve the die for means 2.0 and 5.5, and explain the sign and size of β. (3 points)

Hand in one PDF and your notebook.

### Sources

- Bottou, Curtis & Nocedal 2018, Optimization Methods for Large-Scale Machine Learning. https://arxiv.org/abs/1606.04838
- Nocedal & Wright 2006, Numerical Optimization (Springer), chapters 3, 6, 7 and 12.
- Boyd & Vandenberghe 2004, Convex Optimization, chapters 5 and 9. https://web.stanford.edu/~boyd/cvxbook/
- Deisenroth, Faisal & Ong 2020, Mathematics for Machine Learning, chapters 7 and 12. https://mml-book.github.io/
- Kingma & Ba 2015, Adam: A Method for Stochastic Optimization. https://arxiv.org/abs/1412.6980
- Cover & Thomas 2006, Elements of Information Theory (Wiley), chapter 12.
- Bishop 2006, Pattern Recognition and Machine Learning, chapter 7. https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/

## Session 10: Numerical methods for ML

**Goal:** students can explain floating-point formats and their failures, write numerically stable ML code, and pick a stable way to solve linear systems.

### Talking pointers

- **Open with:** "Your training run finishes with no error message. The loss may be nan, or worse, a normal-looking number that is wrong. Today we see where computer arithmetic goes wrong, and how to guard against it."
- **Segment 1, say:** work out 2048 + 1 in float16 on the board, then show the spacing plot.
- **Segment 2, say:** show softmax(1000, 1001) giving nan, subtract the maximum on the board, and get (0.269, 0.731).
- **Segment 3, say:** show the polynomial-fit plot: the normal equations follow κ², QR follows κ.
- **Close with:** "No error message does not mean no error: check numbers against a stable method or a higher precision." Then set assignment 10.

### Segment 1 (7 min): floating point

- A floating-point number stores a sign, an exponent and a fraction of t bits: $x = \pm(1.f)_2 \times 2^e$. Numbers between $2^e$ and $2^{e+1}$ are $2^{e-t}$ apart, so the gap grows with the size of the number (Goldberg 1991 explains the IEEE 754 standard).
- Machine epsilon $\varepsilon = 2^{-t}$ is the gap between 1 and the next number; rounding to the nearest number makes a relative error of at most ε/2.
- Bits (sign/exponent/fraction), ε and largest number: float64 1/11/52, 2.2 × 10⁻¹⁶, 1.8 × 10³⁰⁸; float32 1/8/23, 1.2 × 10⁻⁷, 3.4 × 10³⁸; float16 1/5/10, 9.8 × 10⁻⁴, 65,504; bfloat16 1/8/7, 7.8 × 10⁻³, 3.4 × 10³⁸.
- float16 overflows above 65,504, and its smallest positive number is about 6 × 10⁻⁸; smaller gradients become 0. bfloat16 keeps float32's exponent bits, so it has float32's range but only 2–3 significant decimal digits (Kalamkar et al. 2019).
- Mixed-precision training (Micikevicius et al. 2018) computes in float16 but keeps float32 master weights, because an update smaller than about $2^{-11}$ (≈ 4.9 × 10⁻⁴) of the weight is rounded away, and it scales the loss so that small gradients do not underflow. Course 2 session 2 counts its memory.
- **Pause and try:** in float16 (10 fraction bits), what is 2048 + 1?
  - **Answer:** 2048. Between $2^{11} = 2048$ and 4096 the spacing is $2^{11-10} = 2$, so 2049 lies exactly halfway between 2048 and 2050, and the tie rounds to the even neighbour, 2048.

### Segment 2 (7 min): cancellation and stable formulas

- Catastrophic cancellation: subtracting two nearly equal numbers cancels their leading digits but keeps their absolute rounding errors, so the relative error of the difference can be enormous (Higham 2002).
- The one-pass variance $E[x^2] - (E[x])^2$ is the classic case. For the float32 data 10001, 10002, 10003, $x^2 \approx 10^8$, where float32 numbers are 8 apart; the notebook got −8 instead of 0.667. The two-pass formula $E[(x - \bar x)^2]$ is safe.
- Softmax and log-sum-exp: subtract $m = \max_i x_i$ first, since $\text{softmax}(x) = \text{softmax}(x - m)$ and $\log\sum_i e^{x_i} = m + \log\sum_i e^{x_i - m}$ (Goodfellow et al. 2016, chapter 4). Otherwise $e^x$ overflows float64 above x ≈ 709.8 and float32 above x ≈ 88.7.
- Cross-entropy from logits z is $\text{logsumexp}(z) - z_y$, which never takes the log of a rounded probability; that is why PyTorch's `cross_entropy` takes logits.
- Softplus, $\log(1 + e^x)$, becomes $\max(x, 0) + \text{log1p}(e^{-|x|})$. Binary cross-entropy from a logit z is $\text{softplus}(z) - yz$, and $\log\sigma(x) = -\text{softplus}(-x)$.
- **Pause and try:** compute softmax(1000, 1001) without a computer.
  - **Answer:** it equals softmax(0, 1) = $(1, e)/(1 + e)$ ≈ (0.269, 0.731). Computing $e^{1000}$ directly overflows and gives nan.

### Segment 3 (6 min): conditioning, stability and iterative solvers

- Conditioning belongs to the problem: the condition number $\kappa(A) = \sigma_{\max}/\sigma_{\min}$ bounds how much relative errors in the data can grow in the answer. As a rule of thumb, you lose about $\log_{10}\kappa$ decimal digits.
- Stability belongs to the algorithm: a backward-stable algorithm returns the exact answer to a slightly perturbed problem, so its error is about κε (Trefethen & Bau 1997).
- Least squares: the normal equations form $A^\top A$, and $\kappa(A^\top A) = \kappa(A)^2$, so they lose twice as many digits. Householder QR works with A itself (session 2). In the notebook, at κ = 1.2 × 10⁸, QR's error was 5 × 10⁻¹⁰ and the normal equations' 0.25, with no warning.
- For large sparse symmetric positive definite systems, conjugate gradient (CG) needs only products Av. After k steps its error, measured in the A-norm, is at most $2\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^k$ times the first one: the same √κ as momentum in session 8 (Nocedal & Wright 2006, chapter 5).
- **Pause and try:** κ(A) = 10⁵ and the model fits the data well. Roughly how many correct digits does float64 give for the least-squares coefficients by QR, and by the normal equations?
  - **Answer:** about 16 − 5 = 11 with QR. The normal equations work with κ = 10¹⁰, leaving about 16 − 10 = 6.

### Lab guide (about 2 hours, notebook `s10_numerical_methods.ipynb`)

1. Section 1 (15 min): the spacing on paper, then the format table and plot.
2. Section 2 (15 min): overflow, underflow, loss scaling and lost updates.
3. Sections 3–4 (25 min): naive against stable softmax, log-sum-exp and softplus.
4. Section 5 (10 min): the variance formula and $(1 - \cos x)/x^2$.
5. Sections 6–7 (35 min): normal equations against QR; CG against a dense solve.
6. TODO cells (20 min): Welford's algorithm and Kahan summation.

- **Expect:** 2048 + 1 = 2048 (float16), 256 + 1 = 256 (bfloat16), $2^{24} + 1 = 2^{24}$ (float32). ε: 2.2204e-16, 1.1921e-07, 9.7656e-04, 7.8125e-03. 300 × 300: inf in float16, 90112 in bfloat16. A gradient of 1e-8: 0 unscaled, 1.0012e-08 with scale 1,024, 9.9972e-09 with 65,536. 10,000 updates of 1e-4: float16 1.0, float32 2.000166. Softmax(1000, 1001): naive nan, stable (0.2689, 0.7311); log-sum-exp 1001.3133. Softplus at −40: naive 0, stable 4.24835e-18. One-pass variance: −8.0000 (float32) and 0.0000 (float64); two-pass 0.6667. Polynomial fits, κ from 1.21e+02 to 1.31e+11: QR errors 6.78e-15 to 5.86e-06; normal equations 6.59e-13 to 3.72e+00 (1.11e+01 at degree 13). CG: 100 iterations (κ = 81) and 246 (κ = 7,993), agreeing with the dense solve to 6.3e-10; 158 kB of matrix against 50 MB. Runtime about 5 seconds.
- **Common problems:** checking only for errors, not for wrong numbers; `np.exp` on large logits in float32; testing a stable formula only on moderate inputs, where the naive one works too.

### Quiz

1. Why does bfloat16 rarely need loss scaling while float16 does?
   - **Answer:** bfloat16 has float32's 8 exponent bits, and so its range. float16's 5 exponent bits cannot hold numbers below about 6 × 10⁻⁸, so small gradients become 0.
2. Why subtract the maximum before a softmax?
   - **Answer:** softmax is unchanged by subtracting the same number from every input, and after the shift the largest exponential is $e^0 = 1$, so nothing overflows.
3. Why prefer QR to the normal equations for least squares?
   - **Answer:** forming $A^\top A$ squares the condition number, so the normal equations lose about twice as many digits; QR works with A itself and is backward stable.

**Watch out:** "If it runs without errors, the numbers are right." In the notebook, the normal equations returned degree-13 coefficients with a relative error of 11 and no warning, the one-pass variance came out negative, and a float16 weight silently ignored 10,000 updates. Compare with a stable method, a higher precision or a known answer before trusting a number.

### Assignment 10 (due before session 11, 10 points)

1. By hand: the largest N such that every integer from 0 to N is exact in float16, in bfloat16 and in float32, and the float16 spacing at 1,000 and at 50,000. Check in code. (3 points)
2. Complete both TODO cells: Welford's algorithm on the two variance examples, and Kahan summation of 0.1 one million times in float32. Report the errors. (3 points)
3. Redo the polynomial-fit experiment on [−1, 1] instead of [0, 1], then with Chebyshev points. Report κ and the three errors, and explain the change using conditioning and stability. (4 points)

Hand in one PDF and your notebook.

### Sources

- Goldberg 1991, What Every Computer Scientist Should Know About Floating-Point Arithmetic. https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
- Micikevicius et al. 2018, Mixed Precision Training. https://arxiv.org/abs/1710.03740
- Kalamkar et al. 2019, A Study of BFLOAT16 for Deep Learning Training. https://arxiv.org/abs/1905.12322
- Higham 2002, Accuracy and Stability of Numerical Algorithms, 2nd edition (SIAM).
- Trefethen & Bau 1997, Numerical Linear Algebra (SIAM).
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 4. https://www.deeplearningbook.org/
- Nocedal & Wright 2006, Numerical Optimization (Springer), chapter 5.

## Session 11: Information theory for ML

**Goal:** students can compute entropy, cross-entropy, KL divergence and mutual information, and explain where each appears in ML.

### Talking pointers

- **Open with:** "Every classifier you train minimizes a quantity invented in 1948 for sending messages over noisy channels. Today we see why that quantity, cross-entropy, is the right loss."
- **Segment 1, say:** encode a, b, c, d as 0, 10, 110, 111 on the board and show that the average length equals the entropy, 1.75 bits.
- **Segment 2, say:** write H(p, q) = H(p) + KL(p‖q), then show the two-bump plot: one fit covers both bumps, the other picks one.
- **Segment 3, say:** show the $X^2$ scatter, then the perplexities of the three character models.
- **Close with:** "Entropy is average surprise, cross-entropy is the surprise of a model, and KL is the price of the wrong model." Then set assignment 11.

### Segment 1 (6 min): information and entropy

- An outcome with probability p carries $-\log_2 p$ bits of information, or "surprise": rare events carry more, and for independent events the surprises add.
- Entropy is the average surprise, $H(p) = -\sum_i p_i \log_2 p_i$ (Shannon 1948). With natural logarithms the unit is the nat, and 1 nat ≈ 1.443 bits; ML code usually works in nats.
- For K outcomes, $0 \le H \le \log_2 K$: zero when one outcome is certain, largest for the uniform distribution. A fair coin has 1 bit; a coin with P(heads) = 0.9 has 0.469 bits.
- Shannon's source coding theorem: no code can average fewer than H bits per symbol, and good codes come within 1 bit of it (MacKay 2003, chapters 4–5). For (1/2, 1/4, 1/8, 1/8), the code 0, 10, 110, 111 reaches exactly 1.75 bits.
- **Pause and try:** what is the entropy of (1/2, 1/4, 1/8, 1/8) in bits?
  - **Answer:** ½ × 1 + ¼ × 2 + 2 × (⅛ × 3) = 0.5 + 0.5 + 0.75 = 1.75 bits.

### Segment 2 (7 min): cross-entropy and KL divergence

- Cross-entropy, $H(p, q) = -\sum_i p_i \log q_i$, is the average code length when the data come from p but the code was built for q. The Kullback–Leibler (KL) divergence, $\text{KL}(p\|q) = \sum_i p_i \log(p_i/q_i)$, is the extra cost: $H(p, q) = H(p) + \text{KL}(p\|q)$, with KL ≥ 0 and equal to 0 only when p = q (Cover & Thomas 2006, chapter 2).
- For p = (½, ½) and q = (¼, ¾), H(p, q) = 1.2075 bits = 1 + 0.2075, while KL(q‖p) = 0.1887 bits.
- Why cross-entropy is the loss: a model's average negative log-likelihood (NLL) on training data is $H(\hat p, q_\theta) = H(\hat p) + \text{KL}(\hat p\|q_\theta)$, where $\hat p$ is the data's distribution, and $H(\hat p)$ does not depend on θ. So minimizing it minimizes the KL from the data to the model: maximum likelihood (session 7).
- Forward KL(p‖q), which maximum likelihood minimizes, makes q cover everywhere p has mass; reverse KL(q‖p), used in variational inference, lets q sit inside one mode of p (Bishop 2006, section 10.1).
- KL also appears in the VAE loss (Course 2 session 7), in distillation (Course 3 session 12), and in RLHF and DPO, where it keeps the tuned model near its reference model (Course 3 session 6).
- **Pause and try:** p = (1, 0) and q = (½, ½). What are KL(p‖q) and KL(q‖p)?
  - **Answer:** KL(p‖q) = 1 × log₂(1/0.5) = 1 bit. KL(q‖p) is infinite: q gives probability ½ to an outcome that p says is impossible.

### Segment 3 (7 min): mutual information and perplexity

- Mutual information, $I(X; Y) = H(X) + H(Y) - H(X, Y) = \text{KL}(p(x, y)\|p(x)p(y))$, is how many bits knowing Y saves about X. It is never negative, and 0 exactly when X and Y are independent (MacKay 2003, chapter 8).
- It detects any dependence, not just linear trends: in the notebook, Y = X² + noise had correlation −0.01 but about 2 bits of mutual information. Contrastive learning is linked to a lower bound on it (Course 2 session 5).
- Perplexity: a language model's cross-entropy on held-out text, in bits per token, gives perplexity $2^{\text{bits}}$ (equal to $e^{\text{nats}}$). A perplexity of k means the model is as unsure as a uniform choice among k tokens. Course 4 session 7 uses it to evaluate a small Bangla model.
- A bigram model predicts each character from the previous one, from counts plus one (add-one smoothing: the posterior mean under a uniform prior, session 7). On the notebook's text it scored 3.61 bits per character, against 4.15 for single-character frequencies.
- **Pause and try:** a model gives the four tokens of a test text probabilities 1/2, 1/4, 1/8 and 1/4. What is its perplexity?
  - **Answer:** the surprises are 1, 2, 3 and 2 bits, averaging 2 bits per token, so the perplexity is 2² = 4.

### Lab guide (about 2 hours, notebook `s11_information_theory.ipynb`)

1. Section 1 (15 min): the two entropies on paper, then the coding experiment.
2. Sections 2–3 (25 min): the decomposition, KL's asymmetry, and fitting by cross-entropy.
3. Section 4 (20 min): forward against reverse KL.
4. Section 5 (20 min): mutual information from tables and from samples.
5. Section 6 (20 min): uniform, unigram and bigram perplexity.
6. TODO cells (25 min): a trigram model; pixel–label mutual information.

- **Expect:** H = 1.7500 bits (1.2130 nats) and 0.4690 bits; code length 1.7515. H(p, q) = 1.2075, KL(p‖q) = 0.2075, KL(q‖p) = 0.1887 bits; triangle inequality broken, 2.536 > 1.268 bits. Fitting: KL($\hat p$‖q) falls from 0.2028 to 0.000000 and the cross-entropy to H($\hat p$) = 2.1191 bits. Gaussians: 0.4431 and 1.3069 nats. Two bumps: forward fit μ = 0.0000, σ = 2.0881; reverse fit μ = 1.9971, σ = 0.6049, with KL(q‖p) = 0.6918. Mutual information: 1.0000, 0.0000 and 0.5310 bits; for Y = X² + noise, correlation −0.010 and 1.996 bits (binning) or 2.309 bits (nearest neighbours). On 492 test characters (V = 29): uniform perplexity 29.00, unigram 17.76 (4.1504 bits), bigram 12.17 (3.6055 bits); the bigram scores 3.3818 bits on its own training text. Runtime about 3 seconds.
- **Common problems:** mixing bits and nats (log₂ against ln) when comparing numbers; a zero probability in q, which makes the cross-entropy infinite (smooth the counts); reporting perplexity on the training text.

### Quiz

1. Show that minimizing cross-entropy on training data is maximum likelihood.
   - **Answer:** the average NLL under $q_\theta$ is $H(\hat p, q_\theta) = H(\hat p) + \text{KL}(\hat p\|q_\theta)$, and the first term does not depend on θ.
2. Which KL makes a single Gaussian cover both bumps of a two-bump distribution, and why?
   - **Answer:** forward KL(p‖q). It averages $\log(p/q)$ over p, so q is punished heavily wherever p has mass and q has almost none.
3. The correlation is 0 but the mutual information is 2 bits. How?
   - **Answer:** correlation measures only linear dependence. For Y = X² with X symmetric around 0 there is no linear trend, yet Y reveals |X|.

**Watch out:** "KL divergence is a distance." It is not symmetric: 0.2075 against 0.1887 bits in the coin example, and 1 bit against infinity for (1, 0) and (½, ½). It also breaks the triangle inequality: for coins with P(heads) 0.9, 0.5 and 0.1, KL(0.9‖0.1) = 2.536 bits, more than KL(0.9‖0.5) + KL(0.5‖0.1) = 1.268 bits. Always say which direction you use, and why.

### Assignment 11 (due before session 12, 10 points)

1. By hand, in bits: H(p), H(p, q), KL(p‖q) and KL(q‖p) for p = (0.7, 0.2, 0.1) and q = (1/3, 1/3, 1/3). Check them in code. (3 points)
2. Repeat the forward and reverse KL fits with the bumps at ±1 and at ±4. Report μ and σ for each fit, and explain when the two fits agree. (3 points)
3. Complete the trigram TODO: choose α on a validation split, then report bits per character and perplexity for all four models. Explain why more context can do worse on a small text. (4 points)

Hand in one PDF and your notebook.

### Sources

- Shannon 1948, A Mathematical Theory of Communication, Bell System Technical Journal 27.
- MacKay 2003, Information Theory, Inference, and Learning Algorithms, chapters 2, 4, 5 and 8. https://www.inference.org.uk/itila/book.html
- Cover & Thomas 2006, Elements of Information Theory, 2nd edition (Wiley), chapter 2.
- Bishop 2006, Pattern Recognition and Machine Learning, sections 1.6 and 10.1. https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/
- Goodfellow, Bengio & Courville 2016, Deep Learning, chapter 3. https://www.deeplearningbook.org/

## Session 12: Graphs and matrices: from PageRank to graph neural networks

**Goal:** students can represent graphs as adjacency and Laplacian matrices, compute PageRank and spectral clusters, and see message passing as matrix multiplication.

### Talking pointers

- **Open with:** "A search engine, a clustering method and a graph neural network look unrelated. Each is a few products with one matrix that describes a graph."
- **Segment 1, say:** draw the path 1 – 2 – 3, write A, D and L on the board, and multiply L by (1, 0, −1).
- **Segment 2, say:** solve the three-page PageRank by hand, then show the error of power iteration under the $0.85^t$ line.
- **Segment 3, say:** show the moons, where spectral clustering succeeds at noise 0.05 and partly fails at 0.07, then write one GCN layer as $\hat A X W$.
- **Close with:** "PageRank, spectral clustering and graph neural networks are linear algebra on one matrix." Then set assignment 12, which is due with the capstone.

### Segment 1 (6 min): graphs as matrices, and random walks

- A graph from discrete mathematics, with n nodes, becomes an adjacency matrix A: $A_{ij} = 1$ for an edge from i to j, symmetric for an undirected graph. The degrees $d_i = \sum_j A_{ij}$ form $D = \text{diag}(d)$. $(A^k)_{ij}$ counts walks of length k, so $\text{trace}(A^3)/6$ counts triangles.
- A random walk moves to a uniformly random neighbour: $P = D^{-1}A$, whose rows sum to 1, and a distribution (a row vector) evolves as $\pi_{t+1} = \pi_t P$, a Markov chain.
- A stationary distribution, $\pi = \pi P$, is a left eigenvector of P with eigenvalue 1; for a connected undirected graph, $\pi_i = d_i/\sum_j d_j$.
- From any start the walk reaches π if the graph is also not bipartite; otherwise it can alternate for ever, which a "lazy" walk that stays put half the time fixes (Spielman's book draft).
- **Pause and try:** a star has one centre joined to 3 leaves. What is the stationary distribution?
  - **Answer:** the degrees are 3, 1, 1, 1, summing to 6, so π = (1/2, 1/6, 1/6, 1/6). The walk itself alternates between centre and leaves, since the star is bipartite.

### Segment 2 (7 min): PageRank

- PageRank (Page et al. 1999): a page is important if important pages link to it. A random surfer follows a random out-link with probability α, the damping factor (usually 0.85), and otherwise jumps to a uniformly random page; a page with no out-links jumps anywhere.
- The ranks are the surfer's stationary distribution, $r = rG$, with the Google matrix $G = \alpha P + (1 - \alpha)\frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
- Power iteration, $r \leftarrow rG$, needs only products with the sparse link matrix, and since $r_{t+1} - r = \alpha(r_t - r)P$ its error shrinks at least by α per step: about 113 steps per factor of $10^8$ at α = 0.85.
- Why damp? With every entry of G positive, the ranks are unique and power iteration converges (the Perron–Frobenius theorem). Without damping, pages that link only to each other can trap the rank: in the notebook, two such pages held 0.500 of it at α = 0.85 and all of it at α = 1.
- **Pause and try:** three pages, each with an out-link, and α = 0.85. Page 3 has no incoming links. What is its PageRank?
  - **Answer:** only random jumps reach it, so $r_3 = (1 - 0.85)/3 = 0.05$. With links 1 → 2, 2 → 1 and 3 → 1, the other two get 0.4865 and 0.4635.

### Segment 3 (7 min): the Laplacian, spectral clustering and graph convolutions

- The graph Laplacian $L = D - A$ satisfies $x^\top L x = \sum_{\text{edges } (i,j)} (x_i - x_j)^2$, so it is positive semidefinite, $L\mathbf{1} = 0$, and its number of zero eigenvalues is the number of connected components (von Luxburg 2007).
- Spectral clustering (Ng, Jordan & Weiss 2001): build a similarity graph (here a k-nearest-neighbour graph), take the eigenvectors of $L_{\text{sym}} = I - D^{-1/2}AD^{-1/2}$ with the smallest eigenvalues, scale each row to length 1, and run k-means on the rows. It follows connections, not straight-line distance, so it can separate two moons; but it solves a relaxed graph-cut problem, so it can also miss (von Luxburg 2007).
- One graph convolutional network (GCN) layer is $H' = \text{ReLU}(\hat A H W)$ with $\hat A = \tilde D^{-1/2}(A + I)\tilde D^{-1/2}$ (Kipf & Welling 2017): each node sums its own and its neighbours' features with degree weights (message passing), and a shared weight matrix W mixes the channels.
- Many layers apply $\hat A$ many times, a power iteration: features approach the top eigenvector, proportional to $\sqrt{d_i + 1}$, and nodes become alike (oversmoothing; Course 6 sessions 2 and 4).
- **Pause and try:** the path 1 – 2 – 3 with self-loops. What weights does node 2 give to nodes 1, 2 and 3 in $\hat A$?
  - **Answer:** the degrees with self-loops are 2, 3 and 2, so the weights are $1/\sqrt{6} \approx 0.408$, 1/3 ≈ 0.333 and 0.408. They sum to 1.15: the symmetric normalization is not an average.

### Lab guide (about 2 hours, notebook `s12_graphs_and_matrices.ipynb`)

1. Sections 1–2 (25 min): the path's matrices by hand, then random walks on two triangles, a star and a lazy star.
2. Section 3 (30 min): the three-page PageRank by hand; eight pages; the damping sweep.
3. Section 4 (25 min): the Laplacian; spectral clustering against k-means at two noise levels.
4. Sections 5–6 (25 min): one GCN layer two ways; smoothing and oversmoothing.
5. TODO cells (20 min): personalized PageRank; random-walk normalization.

- **Expect:** the path's Laplacian eigenvalues 0, 1, 3. Two triangles: walk and eigenvector give (0.143, 0.143, 0.214, 0.214, 0.143, 0.143); the star's walk never settles. Three pages: (0.4865, 0.4635, 0.05). Eight pages: 153 iterations, within 2.0e-13 of the eigenvector; the trapping pair holds 0.322, 0.500, 0.916 and 1.000 of the rank at α = 0.5, 0.85, 0.99 and 1. Moons (ARI): k-means 0.241 and 0.234; spectral 1.000 at noise 0.05 but 0.650 at 0.07, although the true split's normalized cut (0.0080) is lower than the spectral one (0.0131). Sign-rule accuracy: 0.84 without propagation, 0.97 to 0.99 after 1 to 8 steps, 0.50 from 32 steps on. Runtime about 3 seconds.
- **Common problems:** writing $P = AD^{-1}$, whose columns rather than rows sum to 1; forgetting dangling pages, so G's rows do not sum to 1; reading meaning into the signs of eigenvectors, which are arbitrary.

### Quiz

1. Why is the stationary distribution of a random walk an eigenvector?
   - **Answer:** π = πP says π is a left eigenvector of P with eigenvalue 1, an eigenvector of $P^\top$.
2. What two problems does PageRank's damping factor solve?
   - **Answer:** pages with no way out that trap the rank, and walks that never settle. With all entries of G positive, the ranks are unique and power iteration converges at rate α.
3. Write one GCN layer and say what each part does.
   - **Answer:** $H' = \text{ReLU}(\hat A H W)$: $\hat A$ mixes each node's features with its neighbours', W mixes channels and is shared by all nodes, and ReLU adds the nonlinearity.

**Watch out:** "Graph neural networks need special mathematics." One GCN layer is a normalized adjacency matrix times a feature matrix times a weight matrix, then a ReLU; in the notebook, the matrix form and an explicit message-passing loop agreed to 2.2 × 10⁻¹⁶. Its key ideas (normalization, power iteration, Laplacian eigenvectors) are this course's linear algebra; Course 6 builds on them, and Course 8 adds sheaves on graphs.

### Assignment 12 (due with the capstone, 10 points)

1. By hand: the PageRank of the three-page example with α = 0.5, and the Laplacian eigenvalues of the 4-cycle (0, 2, 2, 4) with an eigenvector for each. Check both in code. (3 points)
2. Sweep the number of neighbours (5, 10, 20) and the noise (0.03, 0.05, 0.07, 0.1). Report the ARI of spectral clustering and k-means, the edges between the moons, and the normalized cuts of the true and spectral partitions. When does spectral clustering fail, and why? (4 points)
3. Complete both TODO cells: compare personalized PageRank from page 0 with ordinary PageRank, and repeat the smoothing experiment with the random-walk normalization. (3 points)

Hand in one PDF and your notebook.

### Sources

- Page, Brin, Motwani & Winograd 1999, The PageRank Citation Ranking: Bringing Order to the Web. http://ilpubs.stanford.edu:8090/422/
- Ng, Jordan & Weiss 2001, On Spectral Clustering: Analysis and an Algorithm, Advances in Neural Information Processing Systems 14. https://proceedings.nips.cc/paper_files/paper/2001/file/801272ee79cfde7fa5960571fee36b9b-Paper.pdf
- von Luxburg 2007, A Tutorial on Spectral Clustering. https://arxiv.org/abs/0711.0189
- Kipf & Welling 2017, Semi-Supervised Classification with Graph Convolutional Networks. https://arxiv.org/abs/1609.02907
- Spielman, Spectral and Algebraic Graph Theory (book draft). https://www.cs.yale.edu/homes/spielman/sagt/

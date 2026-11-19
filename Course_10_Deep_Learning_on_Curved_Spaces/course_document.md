# Course 10: Deep Learning on Curved Spaces

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on Riemannian geometry for machine learning, taught through code: manifolds, tangent spaces, geodesics, curvature and Riemannian optimization, then hyperbolic embeddings and networks, SPD matrices, rotation groups, generative models on manifolds and mixed-curvature spaces. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Much of the data machine learning meets does not live in flat space. Directions, places on Earth, rotations, covariance matrices and hierarchies all live on curved spaces, where averages, distances and gradient steps have to be redefined. This course builds that machinery from the circle and the sphere upward, checks every formula numerically, and then uses it in the models of current research: hyperbolic embeddings and networks, SPD networks for EEG, rotation regression, and flow matching on manifolds. It is the research-level companion to Course 7 (Geometric Deep Learning and Graphs), which gives one-session tours of several of these topics, and to Course 9 (Mathematics and AI), which covers symmetry and equivariance.

Prerequisites: Course 2 (Mathematics for Machine Learning) or equivalent linear algebra, calculus and optimization, and basic deep learning (Course 1). No differential geometry is assumed.

Capstone: choose a dataset whose geometry matters (a hierarchy, directions or locations on the sphere, rotations, or covariance matrices), build a model in the right geometry and a strong Euclidean baseline, compare them fairly over several seeds, and explain the result in a 10-minute video, including when the curved model did not help. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a correct description of the geometry and the formulas used, checked numerically (25); a working curved-space model (25); a fair comparison with a tuned Euclidean baseline across seeds (25); an analysis of why the geometry helped or not, for example with δ-hyperbolicity or distortion (10); clarity of the report and video (15).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English. Many sessions match parts of graduate courses in differential geometry and geometric deep learning, so they also work as reading-group material.

### Sessions

1. **Why curved spaces?.** Students can recognize data that lives on a curved space and show how Euclidean averages, distances and interpolation go wrong on it.
   - Read: Bronstein, Bruna, Cohen & Veličković 2021, Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges; Mardia & Jupp 2000, Directional Statistics (Wiley; book)
   - Lab: about 1.5 hours, notebook `s01_why_curved.ipynb`
2. **Manifolds, tangent spaces and metrics.** Students can describe a manifold with charts or constraints, compute tangent spaces and projections, and measure lengths with a Riemannian metric.
   - Read: Lee 2018, Introduction to Riemannian Manifolds, 2nd edition (Springer; book); do Carmo 1976, Differential Geometry of Curves and Surfaces (Prentice-Hall; book)
   - Lab: about 2 hours, notebook `s02_tangent_spaces.ipynb`
3. **Geodesics, exponential maps and the Fréchet mean.** Students can compute geodesics, exponential and logarithm maps and parallel transport on the sphere, and find a Fréchet mean by Riemannian gradient descent.
   - Read: Pennec 2006, Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements, Journal of Mathematical Imaging and Vision 25(1); Lee 2018, Introduction to Riemannian Manifolds, 2nd edition (Springer; book)
   - Lab: about 2 hours, notebook `s03_geodesics_mean.ipynb`
4. **Curvature and hyperbolic space.** Students can explain positive, zero and negative curvature through triangles and circles, compute hyperbolic distances, and measure why trees fit hyperbolic space.
   - Read: Sala, De Sa, Gu & Ré 2018, Representation Tradeoffs for Hyperbolic Embeddings, ICML; Sarkar 2011, Low Distortion Delaunay Embedding of Trees in Hyperbolic Plane, Graph Drawing 2011 (Lecture Notes in Computer Science 7034)
   - Lab: about 2 hours, notebook `s04_curvature_hyperbolic.ipynb`
5. **Riemannian optimization.** Students can turn constrained problems into optimization on manifolds, compute Riemannian gradients and retractions, and solve eigenvector and alignment problems with them.
   - Read: Bonnabel 2013, Stochastic Gradient Descent on Riemannian Manifolds, IEEE Transactions on Automatic Control; Bécigneul & Ganea 2019, Riemannian Adaptive Optimization Methods, ICLR
   - Lab: about 2.5 hours, notebook `s05_riemannian_optimization.ipynb`
6. **Computing in hyperbolic space: the Poincaré and Lorentz models.** Students can implement Möbius addition, distances and exp/log maps in the Poincaré ball and the Lorentz model, convert between them, and avoid numerical failures.
   - Read: Ganea, Bécigneul & Hofmann 2018, Hyperbolic Neural Networks, NeurIPS; Nickel & Kiela 2018, Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry, ICML
   - Lab: about 2.5 hours, notebook `s06_poincare_lorentz.ipynb`
7. **Hyperbolic embeddings of hierarchies.** Students can train Poincaré embeddings of a hierarchy with Riemannian SGD and evaluate them against Euclidean embeddings with distortion and mean average precision.
   - Read: Nickel & Kiela 2017, Poincaré Embeddings for Learning Hierarchical Representations; Sala, De Sa, Gu & Ré 2018, Representation Tradeoffs for Hyperbolic Embeddings, ICML
   - Lab: about 2.5 hours, notebook `s07_hyperbolic_embeddings.ipynb`
8. **Hyperbolic neural networks.** Students can build hyperbolic layers from exp/log maps and Möbius operations, test a graph for tree-likeness with δ-hyperbolicity, and judge when hyperbolic models help.
   - Read: Ganea, Bécigneul & Hofmann 2018, Hyperbolic Neural Networks, NeurIPS; Chami, Ying, Ré & Leskovec 2019, Hyperbolic Graph Convolutional Neural Networks, NeurIPS
   - Lab: about 2.5 hours, notebook `s08_hyperbolic_networks.ipynb`
9. **SPD matrices: the geometry of covariance.** Students can compute affine-invariant and log-Euclidean distances and means of SPD matrices and use them to classify covariance features.
   - Read: Pennec, Fillard & Ayache 2006, A Riemannian Framework for Tensor Computing, International Journal of Computer Vision 66(1); Barachant, Bonnet, Congedo & Jutten 2012, Multiclass Brain–Computer Interface Classification by Riemannian Geometry, IEEE Transactions on Biomedical Engineering 59(4)
   - Lab: about 2.5 hours, notebook `s09_spd_matrices.ipynb`
10. **Rotations and poses: the Lie groups SO(3) and SE(3).** Students can compute exp and log maps of SO(3), measure rotation errors by geodesic distance, average rotations, and choose a rotation representation for neural networks.
   - Read: Solà, Deray & Atchuthan 2018, A Micro Lie Theory for State Estimation in Robotics; Zhou, Barnes, Lu, Yang & Li 2019, On the Continuity of Rotation Representations in Neural Networks, CVPR
   - Lab: about 2.5 hours, notebook `s10_rotations_lie_groups.ipynb`
11. **Generative models on manifolds.** Students can sample from distributions on the sphere and train a Riemannian flow matching model whose samples stay on the manifold.
   - Read: Chen & Lipman 2024, Flow Matching on General Geometries, ICLR; De Bortoli, Mathieu, Hutchinson, Thornton, Teh & Doucet 2022, Riemannian Score-Based Generative Modelling, NeurIPS
   - Lab: about 2.5 hours, notebook `s11_manifold_generative.ipynb`
12. **Mixed curvature, choosing a geometry, and the capstone.** Students can embed data in product spaces of mixed curvature, diagnose the geometry a dataset needs, and plan a capstone that compares geometries fairly.
   - Read: Gu, Sala, Gunel & Ré 2019, Learning Mixed-Curvature Representations in Product Spaces, ICLR; Bachmann, Bécigneul & Ganea 2020, Constant Curvature Graph Convolutional Networks, ICML
   - Lab: about 2.5 hours, notebook `s12_mixed_curvature.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. In this course, draw each new idea on the sphere or the disk before showing the general formula.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. The notebooks implement the geometry by hand in NumPy and PyTorch; the NOT RUN cells show the same steps with libraries such as geoopt and pyRiemann.
- **Sources:** read the papers and book chapters cited for a session before recording it.
- **Dates:** written in November 2026.

## Session 1: Why curved spaces?

**Goal:** students can recognize data that lives on a curved space and show how Euclidean averages, distances and interpolation go wrong on it.

### Talking pointers

- **Open with:** "Two winds blow from 350° and 10°, both from the north. Average the numbers and you get 180°, a south wind. Today we find the same mistake hiding in rotations, covariance matrices and hierarchies."
- **Segment 1, say:** show an angle, a city, a drone, an EEG covariance matrix and a family tree, and ask which rule each obeys.
- **Segment 2, say:** work 350°/10° and the midpoint of $I$ and a 90° rotation on the board, then show the notebook's four failures with their numbers.
- **Segment 3, say:** draw the course map, from the circle and the sphere to hyperbolic space, SPD matrices and rotations.
- **Close with:** "Store curved data as numbers if you like, but average, measure and interpolate with the operations of its own space." Then set assignment 1.

### Segment 1 (6 min): data that lives on curved spaces

- A **manifold** is a space that looks like ordinary $\mathbb{R}^n$ near every point but may bend as a whole, like the Earth's surface, which looks flat from any one field.
- The circle: angles, wind directions, times of day. The sphere: directions in 3-D and places on Earth; unit-length embeddings compared by cosine similarity, as in CLIP (Course 4 session 9), live on a high-dimensional sphere.
- Rotations (the group SO(3), matrices with $R^\top R = I$ and $\det R = 1$): orientations of robots, cameras and molecules. Symmetric positive definite (SPD) matrices: covariances of EEG channels (electroencephalography: brain signals recorded on the scalp). Hierarchies: trees such as the ICD-10 codes, which fit hyperbolic space (Course 7 session 8).
- Here a constraint ($\|x\| = 1$, $R^\top R = I$) fixes the geometry, and the **dimension** is the number of coordinates minus the number of independent constraints. The **manifold hypothesis**, that data such as images lie near an unknown low-dimensional manifold, is different (Fefferman et al. 2016 made it testable); this course is mostly about known geometry.
- **Pause and try:** a rotation matrix has 9 entries. How many numbers does it take to describe a rotation?
  - **Answer:** 3. $R^\top R = I$ is a symmetric matrix equation, so it gives 6 independent equations, and 9 − 6 = 3 (for example, an axis and an angle).

### Segment 2 (7 min): four ways Euclidean operations fail

- **Means of angles.** The arithmetic mean of 350° and 10° is 180°. The circular mean averages the points $(\cos\theta_i, \sin\theta_i)$ and reads off the angle of the result with atan2; its length $\bar R$ measures agreement (Mardia & Jupp 2000). For synthetic winds around north: 178.2° against 0.8°.
- **Distances on Earth.** The great-circle (haversine) distance runs along the surface; the chord through the Earth is $2R\sin(d/2R)$. Dhaka–Chattogram is about 216 km either way (the chord is 10 m shorter), but Dhaka–London is 7,998 km along the surface, 7,483 km through the Earth, and 10,528 km if (latitude, longitude) is treated as a flat plane. Flat up close, curved far away: that is a manifold.
- **Interpolating rotations.** $\frac12(I + R_z(90°))$ has determinant 0.5, so it is not a rotation. Spherical linear interpolation (slerp) of unit quaternions stays on SO(3) (Shoemake 1985).
- **Averaging covariances.** diag(9, 1) and diag(1, 9) both have determinant 9, but their entrywise mean diag(5, 5) has determinant 25: the "swelling effect". The log-Euclidean mean $\exp(\frac1N\sum_i \log C_i)$ (Arsigny et al. 2007) is diag(3, 3). Since $\det e^M = e^{\operatorname{tr} M}$, its determinant is always the geometric mean of the determinants; by Minkowski's determinant inequality, the Euclidean mean's is never smaller.
- **Pause and try:** what is $\frac12(I + R_z(180°))$, and what does it do to a vector?
  - **Answer:** diag(0, 0, 1). It keeps only the z-component, flattening every vector onto the z-axis; its determinant is 0.

### Segment 3 (7 min): the course map and the tools

- The fix: replace "add", "average" and "straight line" by the space's own operations (geodesics, exponential and logarithm maps, means that minimize squared distances), built on the sphere in sessions 2–3 and used for optimization in session 5. Session 4 adds curvature; sessions 6–8 work in hyperbolic space, 9 on SPD matrices, 10 on rotations, 11 on generative models and 12 on mixed curvature.
- Libraries: geoopt (Riemannian stochastic gradient descent, or SGD, and Adam in PyTorch; Kochurov et al. 2020), geomstats (statistics on manifolds; Miolane et al. 2020) and pyRiemann (SPD matrices). Our notebooks implement everything by hand and show the libraries in NOT RUN cells.
- Course 7 sessions 8–9 toured hyperbolic networks, SPD manifolds and flow matching on curved spaces (geometric deep learning; Bronstein et al. 2021); here we build the machinery underneath. Course 9 sessions 1–3 cover groups and equivariance; Course 2 sessions 1, 3, 4 and 8 supply the linear algebra and optimization.
- **Pause and try:** which space fits each? (a) The hour when a shop is busiest. (b) A drone's orientation. (c) The covariance of 64 EEG channels. (d) The ICD-10 hierarchy.
  - **Answer:** (a) a circle; (b) SO(3); (c) 64 × 64 SPD matrices; (d) hyperbolic space, because it is a tree.

### Lab guide (about 1.5 hours, notebook `s01_why_curved.ipynb`)

1. Section 1 (15 min): 350° and 10° on paper, then the synthetic winds.
2. Section 2 (20 min): the city table; why does Chattogram–Sylhet have no flat-map error? Then float32 at 1 km.
3. Section 3 (20 min): both means of diag(9, 1) and diag(1, 9) by hand, then the swelling plot.
4. Section 4 (20 min): the rotation midpoints by hand, then slerp against SciPy.
5. TODO cells (15 min): average bedtime, and two midpoints of Dhaka and London.

- **Expect:** 350° and 10°: arithmetic mean 180.0, circular mean 0.0, $\bar R$ = 0.9848. Synthetic winds: 178.2° against 0.8°, $\bar R$ = 0.860. Chord gaps: 0.010 km for Dhaka–Chattogram (216.0 km), 514.973 km for Dhaka–London (7998.2 km); the flat distance is +4.1% to +5.8% off near Dhaka, +0.0% for Chattogram–Sylhet and +31.6% for Dhaka–London. At 1 km, $\arccos(u\cdot v)$ gives 0.0000 km in float32. Determinants of the means (Euclidean against log-Euclidean): 25.000 against 9.000; 3.6367 against 1.0000 for the turned pair; 1.671 against 1.000 for 50 matrices. Rotation midpoints: determinants 0.500 and 0.000; slerp matches SciPy to 4.4e-16; at $t$ = 0.25, slerp gives 22.50° and linear-then-project 18.43°. Runtime about 3 seconds.
- **Common problems:** passing degrees to `np.sin`; swapping the arguments of `atan2(y, x)`; SciPy quaternions put the scalar last, $(x, y, z, w)$, while many papers put it first; forgetting to flip $q_1$ to $-q_1$ in slerp, which then takes the long way round.

### Quiz

1. Why is the circular mean the right average for angles, and what does $\bar R$ tell you?
   - **Answer:** it averages points on the circle, so 350° and 10° give 0°, not 180°. $\bar R$ near 1 means the angles agree; near 0, they are spread out.
2. Why do the chord and the great-circle distance almost agree for Dhaka–Chattogram but not for Dhaka–London?
   - **Answer:** $2R\sin(d/2R) \approx d - d^3/(24R^2)$: the gap grows with the cube of the distance.
3. Why does the log-Euclidean mean not swell?
   - **Answer:** $\det e^M = e^{\operatorname{tr} M}$ and the trace is linear, so its determinant is $\exp(\frac1N\sum_i \log\det C_i)$, the geometric mean of the determinants.

**Watch out:** "Any data can be treated as a vector in $\mathbb{R}^n$ without loss." Storing curved data as a vector is fine; computing with vector operations is not. Adding, averaging and drawing straight lines can leave the space (the midpoint of two rotations had determinant 0) or ignore its shape (the mean of two north winds pointed south). Use operations defined by the space itself.

### Assignment 1 (due before session 2, 10 points)

1. For the angles 20°, 40° and 300°, compute the arithmetic mean, the circular mean and $\bar R$ by hand, showing the sums of cosines and sines. Check them in code. (3 points)
2. Complete both TODO cells. Report both bedtimes and each midpoint's distances to Dhaka and London, and say which midpoint is halfway along the shortest route. (4 points)
3. Prove that the log-Euclidean mean of $C_1, \dots, C_N$ has determinant $(\prod_i \det C_i)^{1/N}$. Check it on five random 3×3 SPD matrices and compare with the determinant of their Euclidean mean. (3 points)

Hand in one PDF and your notebook.

### Sources

- Bronstein, Bruna, Cohen & Veličković 2021, Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges. https://arxiv.org/abs/2104.13478
- Mardia & Jupp 2000, Directional Statistics (Wiley; book). https://doi.org/10.1002/9780470316979
- Fefferman, Mitter & Narayanan 2016, Testing the Manifold Hypothesis, Journal of the American Mathematical Society 29(4). https://arxiv.org/abs/1310.0425
- Arsigny, Fillard, Pennec & Ayache 2007, Geometric Means in a Novel Vector Space Structure on Symmetric Positive-Definite Matrices, SIAM Journal on Matrix Analysis and Applications 29(1). https://doi.org/10.1137/050637996
- Shoemake 1985, Animating Rotation with Quaternion Curves, SIGGRAPH (Computer Graphics 19(3)). https://doi.org/10.1145/325165.325242
- Kochurov, Karimov & Kozlukov 2020, Geoopt: Riemannian Optimization in PyTorch. https://arxiv.org/abs/2005.02819
- Miolane et al. 2020, Geomstats: A Python Package for Riemannian Geometry in Machine Learning. https://arxiv.org/abs/2004.04667
- pyRiemann documentation (version 0.12). https://pyriemann.readthedocs.io

## Session 2: Manifolds, tangent spaces and metrics

**Goal:** students can describe a manifold with charts or constraints, compute tangent spaces and projections, and measure lengths with a Riemannian metric.

### Talking pointers

- **Open with:** "Every flat map of the world is wrong somewhere. Today we see why no single map can cover the globe honestly, and how a metric lets us measure correctly in any map."
- **Segment 1, say:** hold up a globe and an atlas: each page is a chart. Show where spherical coordinates break, then the two stereographic charts.
- **Segment 2, say:** differentiate $\gamma\cdot\gamma = 1$ on the board, project $v = (1, 2, 3)$ at the north pole by hand, then show the tangent-plane picture.
- **Segment 3, say:** derive $G = \operatorname{diag}(1, \sin^2\theta)$ from the Jacobian, then show the wobbly loop measured four ways and the Mercator table.
- **Close with:** "A manifold is charts glued together; a metric tells you how long things are in every chart." Then set assignment 2.

### Segment 1 (6 min): charts, atlases and constraints

- An $n$-dimensional manifold has, around every point, a **chart**: a smooth, invertible map from a piece of the manifold to a piece of $\mathbb{R}^n$. An **atlas** is a set of charts that covers the manifold, with smooth changes of chart where they overlap (Lee 2018).
- Spherical coordinates, with $\theta$ the angle from the north pole and $\varphi$ the longitude, give $x = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$. At the poles $\partial x/\partial\varphi = 0$, the Jacobian drops to rank 1 and the chart fails.
- Stereographic projection $\sigma_N(x) = (x_1, x_2)/(1 - x_3)$ misses only the north pole, and $\sigma_S(x) = (x_1, x_2)/(1 + x_3)$ only the south pole. Together they form an atlas; the change of chart is $u \mapsto u/\|u\|^2$. No single chart covers the whole sphere, which is why every world map distorts something.
- In machine learning, manifolds usually come as **constraints** $g(x) = 0$: the sphere $\|x\|^2 = 1$, rotations $R^\top R = I$, orthonormal frames (session 5).
- **Pause and try:** where do $\sigma_N$ and $\sigma_S$ send $(0, 0.6, 0.8)$? Check the change of chart.
  - **Answer:** $\sigma_N = (0, 0.6)/0.2 = (0, 3)$ and $\sigma_S = (0, 0.6)/1.8 = (0, 1/3)$; indeed $(0, 3)/3^2 = (0, 1/3)$.

### Segment 2 (7 min): tangent vectors and the projection

- A **tangent vector** at $x$ is the velocity $\gamma'(0)$ of a curve on the manifold through $x$. On the sphere $\gamma\cdot\gamma = 1$, so $2\gamma\cdot\gamma' = 0$, and the **tangent space** is the plane $T_xS^2 = \{v : x\cdot v = 0\}$.
- The **tangent projection** $P_x = I - xx^\top$ sends $v$ to $v - (x\cdot v)x$. It is symmetric, $P_x^2 = P_x$, its eigenvalues are 0, 1, 1, and $P_x v$ is the tangent vector closest to $v$. At the north pole, $P(1, 2, 3) = (1, 2, 0)$.
- In a chart, the Jacobian columns span the tangent plane. For a general constraint, the tangent space is the null space of the constraint's Jacobian (Boumal 2023, chapter 3); for SO(3) at $I$ it is the skew-symmetric matrices.
- A **vector field** picks a tangent vector at every point. The gradient of the height $x_3$ along the sphere, $P_x e_3$, vanishes at both poles; by the hairy ball theorem every continuous tangent field on the sphere vanishes somewhere (Course 9 session 3).
- **Pause and try:** at $x = (0.6, 0, 0.8)$, project $v = (0, 0, 1)$ onto the tangent plane.
  - **Answer:** $x\cdot v = 0.8$, so $P_x v = (0, 0, 1) - 0.8(0.6, 0, 0.8) = (-0.48, 0, 0.36)$, and $x \cdot P_x v = -0.288 + 0.288 = 0$.

### Segment 3 (7 min): Riemannian metrics and lengths

- A **Riemannian metric** is an inner product on each tangent space that varies smoothly with the point. The sphere inherits the dot product of $\mathbb{R}^3$.
- In a chart, a coordinate velocity $\xi$ becomes the tangent vector $J\xi$ with $\|J\xi\|^2 = \xi^\top G\xi$, where $G = J^\top J$ is the **metric tensor** (the first fundamental form of do Carmo 1976). For spherical coordinates $G = \operatorname{diag}(1, \sin^2\theta)$: $ds^2 = d\theta^2 + \sin^2\theta\, d\varphi^2$.
- The length of a curve, $\int\sqrt{\xi^\top G\,\xi}\,dt$, is the same in every chart, but only if the metric is used: the notebook's loop measures 5.7988 in every chart and 6.8153 if $(\theta, \varphi)$ is treated as flat.
- A chart with $G = \lambda(u)^2 I$ is **conformal**: it keeps angles. Stereographic has $\lambda = 2/(1 + \|u\|^2)$; Mercator has $\lambda = \cos(\text{lat})$, so the map enlarges lengths by $\sec(\text{lat})$ and areas by $\sec^2(\text{lat})$ (Snyder 1987). The Poincaré disk of sessions 4 and 6 has $\lambda = 2/(1 - \|u\|^2)$.
- **Pause and try:** how long is the latitude circle through Dhaka (23.76° N, $R$ = 6,371 km)? How long does a Mercator map that is true at the equator draw it?
  - **Answer:** $2\pi R\cos 23.76° \approx$ 36,637 km. The map draws every latitude circle as long as the equator, 40,030 km: 1.093 times too long.

### Lab guide (about 2 hours, notebook `s02_tangent_spaces.ipynb`)

1. Section 1 (20 min): both projections by hand, then the checks.
2. Section 2 (25 min): charts; watch the Jacobian's rank fall at the pole.
3. Section 3 (20 min): derive $G = \operatorname{diag}(1, \sin^2\theta)$ by hand, then the three metric tensors.
4. Sections 4–5 (25 min): the loop four ways, then Mercator.
5. Section 6 and TODO cells (30 min): the pictures, SO(3)'s tangent space and a latitude band's area.

- **Expect:** $P(1, 2, 3) = (1, 2, 0)$ at the north pole and $(-0.48, 0, 0.36)$ at $(0.6, 0, 0.8)$; eigenvalues of $P$: 0, 1, 1; random curves tangent to 2.9e-10. Jacobian singular values $(1, \sin\theta)$, rank 1 at the pole. Stereographic: $(0, 3)$ and $(0, 0.3333)$; change of chart correct to 1.8e-14. Metric tensors correct to 3.3e-16 (spherical) and about 4e-10 (stereographic and Mercator, by finite differences). Loop: 5.79881822 as a polygon and with both metrics; 6.8153 (+17.5%) as flat $(\theta, \varphi)$; 7.0557 (+21.7%) on the map. Mercator scales 1.0926 (lengths) and 1.1938 (areas) at Dhaka, 1.6067 and 2.5816 at London. Runtime about 2 seconds.
- **Common problems:** confusing latitude with the angle from the north pole ($\theta = 90° -$ latitude); measuring a curve with coordinate derivatives but no metric; `np.arccos` of a value rounded just above 1 (clip first).

### Quiz

1. Why is $T_xS^2 = \{v : x\cdot v = 0\}$?
   - **Answer:** differentiating $\gamma\cdot\gamma = 1$ gives $\gamma\cdot\gamma' = 0$, so every velocity at $x$ is perpendicular to $x$; and every such $v$ is the velocity of the great circle through $x$ in direction $v$.
2. What does the $\sin^2\theta$ in $G = \operatorname{diag}(1, \sin^2\theta)$ mean geometrically?
   - **Answer:** a change $d\varphi$ in longitude moves you $\sin\theta\, d\varphi$, because the latitude circle at angle $\theta$ from the pole has radius $\sin\theta$.
3. Why does a Mercator map enlarge areas near London more than near Dhaka?
   - **Answer:** its area scale is $\sec^2(\text{lat})$, 1.19 at 23.76° N against 2.58 at 51.51° N, because every latitude circle is drawn as long as the equator.

**Watch out:** "The tangent space is part of the manifold." The tangent plane touches the sphere at a single point. It is a vector space of velocities attached at $x$, and the points $x + v$ are off the sphere: for tangent $v \ne 0$, $\|x + v\|^2 = 1 + \|v\|^2 > 1$. To get from a tangent vector back to the manifold you need a map, the exponential map or a retraction (sessions 3 and 5).

### Assignment 2 (due before session 3, 10 points)

1. By hand, compute the Jacobian of $\sigma_N^{-1}(u) = (2u_1, 2u_2, \|u\|^2 - 1)/(\|u\|^2 + 1)$ at $u = (1, 0)$ and the metric tensor there. Check it against $(2/(1 + \|u\|^2))^2 I$. (3 points)
2. Complete both TODO cells and report your numbers. (4 points)
3. A rhumb line (constant compass bearing) is a straight line on a Mercator map. Use the Mercator metric to compute the length of the rhumb line from Dhaka to London, and compare it with the great-circle distance from session 1 (7,998 km). (3 points)

Hand in one PDF and your notebook.

### Sources

- Lee 2018, Introduction to Riemannian Manifolds, 2nd edition (Springer; book).
- Boumal 2023, An Introduction to Optimization on Smooth Manifolds (Cambridge University Press), chapter 3. https://www.nicolasboumal.net/book/
- do Carmo 1976, Differential Geometry of Curves and Surfaces (Prentice-Hall; book).
- Snyder 1987, Map Projections: A Working Manual, U.S. Geological Survey Professional Paper 1395. https://doi.org/10.3133/pp1395

## Session 3: Geodesics, exponential maps and the Fréchet mean

**Goal:** students can compute geodesics, exponential and logarithm maps and parallel transport on the sphere, and find a Fréchet mean by Riemannian gradient descent.

### Talking pointers

- **Open with:** "How do you average points when you cannot add them? Today we replace 'add and divide' by 'walk along geodesics', and find that on a curved space a vector carried around a triangle comes back turned."
- **Segment 1, say:** stretch a string between two cities on a globe to show a great circle, then compute $\exp$ at the north pole by hand.
- **Segment 2, say:** show the circle example (30° against 26.57°) and the convergence plot, then the equator example with two answers.
- **Segment 3, say:** walk a pen around the octant triangle on a ball, keeping it parallel to itself, and show that it comes back turned by 90°.
- **Close with:** "Exp and log let us do statistics in tangent planes; parallel transport moves vectors between them, and curvature makes the result depend on the path." Then set assignment 3.

### Segment 1 (6 min): geodesics, exp and log

- A **geodesic** is a curve that locally minimizes length; on a surface in $\mathbb{R}^3$, its acceleration is perpendicular to the surface. On the sphere the geodesics are the great circles.
- The **exponential map** walks from $x$ for length $\|v\|$ in direction $v$: $\exp_x(v) = \cos\|v\|\,x + \sin\|v\|\,v/\|v\|$. The **logarithm map** inverts it: $\log_x(y) = d(x,y)\,\frac{y - (x\cdot y)x}{\|y - (x\cdot y)x\|}$, with $d(x, y) = \arccos(x\cdot y)$, computed stably with atan2.
- So $d(x, y) = \|\log_x(y)\|$, and the geodesic from $x$ to $y$ is $\exp_x(t\log_x y)$, which is slerp from session 1.
- $\log_x$ is undefined at the antipode $-x$, the **cut locus** of $x$; $\exp_x$ is one-to-one only for $\|v\| < \pi$. In the notebook, two points $2\times10^{-9}$ apart next to $-x$ have logs of length $\pi$ pointing in opposite directions.
- **Pause and try:** at the north pole $N$, what is $\exp_N(\frac\pi2, 0, 0)$? And $\exp_N(\frac{3\pi}{2}, 0, 0)$ and its log?
  - **Answer:** $(1, 0, 0)$; then $(-1, 0, 0)$, whose log is $(-\frac\pi2, 0, 0)$, of length $\pi/2$ rather than $3\pi/2$, because the walk passed the cut locus (the south pole).

### Segment 2 (7 min): the Fréchet mean

- The **Fréchet (Karcher) mean** minimizes $F(x) = \frac{1}{2N}\sum_i d(x, p_i)^2$; in $\mathbb{R}^n$ it is the ordinary average. On the circle, 0°, 0° and 90° give 30° (intrinsic), while the circular mean of session 1 (extrinsic, computed in the plane) gives 26.57°.
- Where log is defined, the gradient of $\frac12 d(x, p)^2$ is $-\log_x(p)$. Riemannian gradient descent is therefore $x \leftarrow \exp_x(\frac{\eta}{N}\sum_i \log_x p_i)$; with $\eta = 1$ it is the Karcher iteration: average in the tangent plane, then step along the geodesic (Pennec 2006).
- In the notebook, clustered directions converge in 5 iterations and their Karcher mean is 0.0241° from the normalized Euclidean mean; spread-out directions need 21 iterations and the two means are 1.4952° apart.
- On the sphere a minimizer always exists. It is unique when the points lie in an open hemisphere, that is, in a geodesic ball of radius less than $\pi/2$ (Afsari 2011), but not always otherwise. For six points evenly spaced on the equator, both poles minimize $F$, and the iteration returns whichever pole is nearer its start.
- **Pause and try:** for six points evenly spaced on the equator, compute $F$ at the north pole and at one of the points.
  - **Answer:** at the pole every distance is $\pi/2$, so $F = \frac12(\frac\pi2)^2 = \pi^2/8 \approx 1.2337$. At a data point the distances are 0, $\frac\pi3$, $\frac{2\pi}3$, $\pi$, $\frac{2\pi}3$, $\frac\pi3$, giving $F = 19\pi^2/108 \approx 1.7363$.

### Segment 3 (7 min): parallel transport and holonomy

- **Parallel transport** moves a tangent vector along a curve while keeping it as constant as possible: for a surface in $\mathbb{R}^3$, its derivative along the curve has no tangential part (Lee 2018). It keeps lengths and angles. Along a geodesic on the sphere, $\Gamma_{x\to y}(v) = v - \frac{y\cdot v}{1 + x\cdot y}(x + y)$.
- Carried around a closed loop, a vector comes back rotated: this is **holonomy**. On the unit sphere the rotation angle equals the enclosed area, and a geodesic triangle's angles add up to $\pi$ + area (Gauss–Bonnet; do Carmo 1976).
- The octant triangle with corners $e_3$, $e_1$, $e_2$ has three right angles, so its area is $3\cdot\frac\pi2 - \pi = \frac\pi2$, one eighth of $4\pi$, and a transported vector turns by 90°.
- Machine learning needs transport whenever it compares or adds tangent vectors at different points: momentum in Riemannian Adam (session 5) and features in gauge-equivariant networks (Course 9 session 3). On a curved space the answer depends on the path.
- **Pause and try:** transport $v = (0, 1, 0)$ from $x = (1, 0, 0)$ to $y = (0, 0.6, 0.8)$.
  - **Answer:** $y\cdot v = 0.6$, $1 + x\cdot y = 1$ and $x + y = (1, 0.6, 0.8)$, so $\Gamma(v) = (-0.6, 0.64, -0.48)$: still of length 1 and perpendicular to $y$.

### Lab guide (about 2 hours, notebook `s03_geodesics_mean.ipynb`)

1. Section 1 (15 min): the circle example by hand, then the plot of $F$.
2. Section 2 (25 min): exp and log, the hand examples, the checks and the cut locus.
3. Sections 3–4 (35 min): the gradient check, the Karcher iteration on two data sets, the hemisphere test and the equator example.
4. Sections 5–6 (30 min): transport by hand and in code, then the octant and random triangles.
5. TODO cells (15 min): step sizes for the Karcher iteration, and the holonomy of a lune.

- **Expect:** circle: Fréchet mean 30.00°, circular mean 26.57°. Exp/log checks to about 2e-14; geodesics match `geometric_slerp` to 1.7e-16; the log of $\exp_N(\frac{3\pi}2, 0, 0)$ has length 1.5708. Gradient check: −0.54644084 both ways. Clustered: 5 iterations, means 0.0241° apart. Spread out: 21 iterations, means 1.4952° apart, $F$ 0.685297 against 0.685538, in no open hemisphere, yet both starts reach the same point. Equator: north or south pole after 41 iterations, $F$ = 1.233701 (1.736319 at a data point). Octant: 90.0000° (closed form); 93.5399°, 90.3534°, 90.0353° and 90.0035° by projection with 10 to 10,000 steps per edge. Six triangles: excess, area and holonomy agree to 3.1e-14°. Runtime about 3 seconds.
- **Common problems:** distances by arccos (inaccurate for nearby points; use atan2); forgetting that log is undefined at the antipode; stepping by $x + v$ instead of $\exp_x(v)$; measuring the holonomy angle without a sign.

### Quiz

1. Why is $\|\log_x(y)\| = d(x, y)$?
   - **Answer:** $\log_x(y)$ is the initial velocity of the geodesic that reaches $y$ at time 1, and geodesics have constant speed, so the speed equals the length of this shortest path.
2. Why is the Karcher iteration "average the logs, then take exp"?
   - **Answer:** $\operatorname{grad} F(x) = -\frac1N\sum_i\log_x(p_i)$, so a gradient step of size 1 is $\exp_x$ of the mean of the logs.
3. A geodesic triangle on the unit sphere has angles 90°, 90° and 30°. By how much does a vector turn when transported around it?
   - **Answer:** by its area, $210° - 180° = 30°$, or $\pi/6$.

**Watch out:** "The Fréchet mean always exists and is unique." On a compact space such as the sphere it exists, but it need not be unique: six points on the equator have two means, the two poles. Uniqueness is guaranteed for concentrated data (inside an open hemisphere on the unit sphere), and gradient descent returns a local minimum near its start, so for spread-out data try several starts and compare $F$.

### Assignment 3 (due before session 4, 10 points)

1. By hand, for $x = (1, 0, 0)$ and $y = (0, 1, 0)$: compute $\log_x(y)$, the midpoint $\exp_x(\frac12\log_x y)$, and the parallel transports of $(0, 0, 1)$ and $(0, 1, 0)$ from $x$ to $y$. Check them in code. (3 points)
2. Complete both TODO cells. Explain the iteration counts with the rate per iteration that you read off the convergence plot. (4 points)
3. Draw 20 points from a wrapped normal with spread 1.2 rad, run the Karcher iteration from 10 random starts, and report how many different means you find and their values of $F$. (3 points)

Hand in one PDF and your notebook.

### Sources

- Pennec 2006, Intrinsic Statistics on Riemannian Manifolds: Basic Tools for Geometric Measurements, Journal of Mathematical Imaging and Vision 25(1). https://doi.org/10.1007/s10851-006-6228-4
- Lee 2018, Introduction to Riemannian Manifolds, 2nd edition (Springer; book).
- Afsari 2011, Riemannian $L^p$ Center of Mass: Existence, Uniqueness, and Convexity, Proceedings of the American Mathematical Society 139(2). https://doi.org/10.1090/S0002-9939-2010-10541-5
- do Carmo 1976, Differential Geometry of Curves and Surfaces (Prentice-Hall; book).

## Session 4: Curvature and hyperbolic space

**Goal:** students can explain positive, zero and negative curvature through triangles and circles, compute hyperbolic distances, and measure why trees fit hyperbolic space.

### Talking pointers

- **Open with:** "On a ball, a triangle's angles add up to more than 180°; on a saddle, to less. Today we meet the space where they add up to less everywhere, and see why every tree fits into it."
- **Segment 1, say:** draw a triangle on a ball and on a saddle, then show the three circle formulas and the curvature recovered from them.
- **Segment 2, say:** draw the Poincaré disk, compute $d(0, 0.5) = \ln 3$ by hand, and show a Möbius map moving a point to the centre.
- **Segment 3, say:** count tree nodes 1, 3, 9, 27, …, then show Sarkar's embedding, the distortion plot and the float32 table.
- **Close with:** "Hyperbolic space has room for every tree, but you pay in bits." Then set assignment 4.

### Segment 1 (6 min): three kinds of curvature

- The **Gaussian curvature** $K$ of a surface is the product of its two principal curvatures. Gauss proved that it depends only on lengths measured inside the surface (do Carmo 1976), so circles and triangles drawn on the surface reveal it. A sphere of radius $R$ has $K = 1/R^2$, a plane 0, a saddle point a negative value.
- Circles of radius $r$ have circumference $2\pi\sin r$ ($K = 1$), $2\pi r$ ($K = 0$) and $2\pi\sinh r$ ($K = -1$). For small $r$, $C(r) \approx 2\pi r - \frac\pi3 K r^3$; at $r = 0.01$ the notebook recovers $K$ = 0.999995 and −1.000005.
- For a geodesic triangle, angle sum $- \pi = \iint K\,dA$ (Gauss–Bonnet). With sides 1 the angle sums are 208.40° (sphere), 180° and 157.93° (hyperbolic), and the notebook checks the areas 0.4956 and 0.3852 independently.
- In the hyperbolic plane every triangle has area less than $\pi$, because its angle sum cannot be negative: triangles are "thin", however long their sides.
- **Pause and try:** on the unit sphere, the equilateral triangle with side 1 has angles of 69.465°. What is its area?
  - **Answer:** $3 \times 69.465° - 180° = 28.395°$, which is 0.4956 in radians, and with $K = 1$ that is the area.

### Segment 2 (7 min): the hyperbolic plane and its models

- The **hyperbolic plane** has $K = -1$ at every point. By Hilbert's theorem no complete surface in $\mathbb{R}^3$ has constant negative curvature (do Carmo 1976), so we work with **models**: flat pictures with a distance formula.
- The **Poincaré disk** is the unit disk with $ds = \frac{2\,|dz|}{1 - |z|^2}$, a conformal factor like the stereographic $2/(1 + |u|^2)$ of session 2. Its distance is $d(x, y) = \operatorname{arcosh}\big(1 + \frac{2\|x - y\|^2}{(1 - \|x\|^2)(1 - \|y\|^2)}\big)$, and $d(0, x) = 2\operatorname{artanh}\|x\|$. Geodesics are diameters and circular arcs that meet the boundary at right angles; the boundary is infinitely far away.
- The **upper half-plane** $\{w : \operatorname{Im} w > 0\}$ is another model; $w = i\frac{1 + z}{1 - z}$ carries the disk onto it and keeps every distance (to 4.4e-15 in the notebook). The hyperboloid model comes in session 6.
- **Möbius maps** $T_a(z) = \frac{z - a}{1 - \bar a z}$ move any point $a$ to the centre and keep all distances: every point of the hyperbolic plane looks the same.
- **Pause and try:** compute $d(0, (0.5, 0))$ with the distance formula.
  - **Answer:** $1 + \frac{2 \cdot 0.25}{1 \cdot 0.75} = \frac53$, and $\operatorname{arcosh}\frac53 = \ln(\frac53 + \frac43) = \ln 3 \approx 1.0986$, which equals $2\operatorname{artanh} 0.5$.

### Segment 3 (7 min): why trees fit, and what it costs

- A tree with branching $b$ has $b^k$ nodes at depth $k$. Euclidean circles grow only linearly, so the leaves crowd: in a radial layout of our tree (branching 3, depth 5), adjacent leaves are only 0.129 apart, even the pairs that are 10 edges apart in the tree (on either side of a boundary between the root's wedges), and the worst-case distortion is 107.6. Hyperbolic circles grow like $\pi e^r$, with room for exponentially many nodes.
- **Sarkar's construction** (Sarkar 2011) puts the root at the origin, moves each node to the centre with a Möbius map, places its children at equal angles at hyperbolic distance $\tau$, and maps back. With $\tau$ large enough, the distortion gets as close to 1 as we like, in two dimensions: 1.83 at $\tau$ = 2 and 1.11 at 6 in the notebook. Short edges fail: at $\tau$ = 0.5 branches overlap (worst case 658). Poincaré embeddings (Nickel & Kiela 2017; Course 7 session 8) learn such embeddings instead.
- The cost: leaves sit at distance $5\tau$ from the root, at Euclidean radius $\tanh(5\tau/2)$, and float32 can store points only up to distance 17.33 from the origin (float64: 37.43). Sala et al. 2018 analyse this trade-off between dimension, precision and distortion.
- **Pause and try:** with $\tau = 4$ a leaf is at hyperbolic distance 20 from the root. How far is it from the boundary in Euclidean terms, and can float32 store it?
  - **Answer:** $1 - \tanh 10 \approx 2e^{-20} \approx 4.1\times10^{-9}$, smaller than the gap of $6\times10^{-8}$ between 1 and the largest float32 below it, so it rounds onto the boundary.

### Lab guide (about 2 hours, notebook `s04_curvature_hyperbolic.ipynb`)

1. Section 1 (20 min): the circle formulas, curvature from circumferences, and the growth plot.
2. Section 2 (20 min): the triangle angles on a calculator, then the two area checks.
3. Section 3 (15 min): $\ln 3$ by hand, then the Möbius and half-plane checks.
4. Sections 4–5 (40 min): Sarkar's construction, the two pictures, and the distortion table and plot.
5. Section 6 and TODO cells (25 min): the float32 table, the curvature of a sphere of radius 2, and a binary tree.

- **Expect:** curvature from circles at $r = 0.01$: +0.999995, 0, −1.000005; chords around the circle of radius 2 sum to 22.788235 ($2\pi\sinh 2$ = 22.788236). Angle sums 208.3955°, 180° and 157.9297°; areas 0.495595 and 0.385199. $d(0, 0.5)$ = 1.0986122887; a gap of 0.01 is 0.9669 at radius 0.99 and 0.0200 at the centre. Radial layout: average distortion 0.2630, worst case 107.62. Sarkar, worst case: 657.8639 ($\tau$ = 0.5), 77.5194, 38.9239, 1.8268 ($\tau$ = 2), 1.2986 (3), 1.1133 (6); average 0.3085 falling to 0.0156. Largest storable distance 17.33 (float32) and 37.43 (float64); at $\tau$ = 4, 69 points on the boundary and 68.0% of pairs off by more than 1%; float64 edge lengths at $\tau$ = 6 between 5.999241 and 6.000427. Runtime about 3 seconds.
- **Common problems:** points with $|z| \ge 1$ (infinite distances); forgetting the complex conjugate in $T_a$; judging hyperbolic distances by eye in the disk.

### Quiz

1. How does the circumference of a circle reveal curvature?
   - **Answer:** $C(r) \approx 2\pi r - \frac\pi3 K r^3$ for small $r$: shorter than $2\pi r$ when $K > 0$, longer when $K < 0$. In the hyperbolic plane, $C(r) = 2\pi\sinh r$ grows exponentially.
2. Why does Sarkar's construction need long edges?
   - **Answer:** with short edges the space is nearly flat at the scale of the tree, so branches overlap (at $\tau$ = 0.5 two nodes were $0.0122\,\tau$ apart). Long edges use hyperbolic space's exponential room.
3. Why does float32 fail at $\tau$ = 4 for our tree?
   - **Answer:** the leaves are at distance 20 from the root, beyond float32's limit of 17.33: $1 - |z| \approx 4\times10^{-9}$ is smaller than the gap below 1.

**Watch out:** "Hyperbolic space is just a disk with a strange distance formula." The disk is one map of the hyperbolic plane, as Mercator is one map of the Earth. Every point looks the same (a Möbius map moved a point to the centre without changing any distance), the boundary is infinitely far away, and the upper half-plane and the hyperboloid give exactly the same distances. Negative curvature belongs to the space itself, visible from inside through fast-growing circles and thin triangles.

### Assignment 4 (due before session 5, 10 points)

1. By hand, compute the angles and area of the hyperbolic equilateral triangle with side 2 and the circumference of the hyperbolic circle of radius 2. Check them in code. (3 points)
2. Complete both TODO cells. (4 points)
3. Store the Sarkar embeddings in float16 (`np.float16`) and find the largest $\tau$ in the table for which the distances still work. Explain the answer with float16's largest storable distance from the origin. (3 points)

Hand in one PDF and your notebook.

### Sources

- Sala, De Sa, Gu & Ré 2018, Representation Tradeoffs for Hyperbolic Embeddings, ICML. https://arxiv.org/abs/1804.03329
- Sarkar 2011, Low Distortion Delaunay Embedding of Trees in Hyperbolic Plane, Graph Drawing 2011 (Lecture Notes in Computer Science 7034).
- do Carmo 1976, Differential Geometry of Curves and Surfaces (Prentice-Hall; book).
- Nickel & Kiela 2017, Poincaré Embeddings for Learning Hierarchical Representations, NeurIPS. https://arxiv.org/abs/1705.08039

## Session 5: Riemannian optimization

**Goal:** students can turn constrained problems into optimization on manifolds, compute Riemannian gradients and retractions, and solve eigenvector and alignment problems with them.

### Talking pointers

- **Open with:** "Unit vectors, orthonormal frames, rotations: many models carry constraints. You can punish violations with a penalty, or make every step stay on the constraint. Today we do the second and measure what it gains."
- **Segment 1, say:** compute the Riemannian gradient for $A = \operatorname{diag}(3, 1, 0)$ by hand, then show the QR-against-penalty table.
- **Segment 2, say:** show that power iteration is a Riemannian step, then the three convergence lines and the momentum and Adam plot.
- **Segment 3, say:** solve the 2-D Procrustes example by hand, then the dictionary-size table with its 10-pair surprise.
- **Close with:** "Project the gradient, step, retract, and give the optimizer's memory the same care." Then set assignment 5.

### Segment 1 (6 min): constraints as manifolds

- Many constraints define manifolds: unit vectors (the sphere), $n\times k$ matrices with orthonormal columns (the **Stiefel manifold**, $X^\top X = I$), rotations (the orthogonal group), SPD matrices (session 9). Optimizing on the manifold replaces constrained optimization (Absil et al. 2008; Boumal 2023).
- For a manifold inside a vector space, with the inherited metric, the **Riemannian gradient** is the tangent projection of the Euclidean gradient $G$: $G - (x\cdot G)\,x$ on the sphere, $G - X\operatorname{sym}(X^\top G)$ on the Stiefel manifold, $W\operatorname{skew}(W^\top G)$ on the orthogonal group.
- A **retraction** maps a tangent step back to the manifold and agrees with the exponential map to first order, but is cheaper: normalization on the sphere, the Q factor of a QR decomposition on the Stiefel manifold, the Cayley transform $W(I - \frac12\Omega)^{-1}(I + \frac12\Omega)$ on the orthogonal group.
- A penalty $\frac\mu4\|X^\top X - I\|^2$ never meets the constraint (one column settles at $\|x\|^2 = 1 + \lambda/\mu$), and larger $\mu$ needs smaller steps: 270 iterations for $\mu$ = 10, 20,439 for 1000.
- **Pause and try:** for $f(x) = \frac12 x^\top Ax$ with $A = \operatorname{diag}(3, 1, 0)$, find the Riemannian gradient at $x = (1, 1, 0)/\sqrt2$.
  - **Answer:** $Ax = (3, 1, 0)/\sqrt2$ and $x^\top Ax = 2$, so the gradient is $(3, 1, 0)/\sqrt2 - 2(1, 1, 0)/\sqrt2 = (1, -1, 0)/\sqrt2$, perpendicular to $x$.

### Segment 2 (7 min): gradient descent, SGD and Adam on manifolds

- **Riemannian gradient descent** repeats $x \leftarrow R_x(-\eta\operatorname{grad} f(x))$. Boumal 2023 (chapter 4) proves the same kind of guarantees as in flat space: with a small enough step, the gradient goes to zero.
- Power iteration is Riemannian ascent on the Rayleigh quotient with step $1/(x^\top Ax)$. A better fixed step can be faster: 89 iterations against 182 in the notebook, with the rates 0.8 and 0.9 that theory predicts.
- **Riemannian SGD** (Bonnabel 2013) uses minibatch gradients with decreasing steps and keeps convergence guarantees on manifolds.
- **Riemannian Adam** (Bécigneul & Ganea 2019) keeps the first moment as a tangent vector, transporting it to each new point, and uses one second-moment number per manifold factor, because coordinates have no intrinsic meaning on a manifold. geoopt implements it (Kochurov et al. 2020). Adam itself is in Course 3 session 2.
- In the notebook, momentum and Adam on Euclidean gradients failed at every learning rate, even with normalization after each step (0.86 and 1.3 rad from the answer). Projecting the gradient fixed both (about $10^{-7}$). Transporting the momentum made no measurable difference on the sphere.
- **Pause and try:** show that normalizing an ordinary ascent step $x + \eta Ax$ is a Riemannian step, and find its step size.
  - **Answer:** with $\rho = x^\top Ax$, $x + \eta Ax = (1 + \eta\rho)\,x + \eta\operatorname{grad} f(x)$, and dividing by $1 + \eta\rho$ does not change the normalized point: it is $R_x\big(\frac{\eta}{1 + \eta\rho}\operatorname{grad} f(x)\big)$.

### Segment 3 (7 min): PCA, orthogonal weights and Procrustes

- PCA's first direction maximizes the Rayleigh quotient on the sphere; the top-$k$ subspace maximizes $\frac12\operatorname{tr}(X^\top AX)$ on the Stiefel manifold (Course 2 session 3 found them by power iteration and the SVD).
- An orthogonal weight matrix preserves the length of its input; training it on the orthogonal group or Stiefel manifold keeps that property exactly.
- **Orthogonal Procrustes**: $\min_{W^\top W = I}\|WX - Y\|_F$ is solved by $W = UV^\top$ from the SVD $YX^\top = U\Sigma V^\top$ (Schönemann 1966). Conneau et al. 2018 aligned word vectors of two languages with an orthogonal map, starting adversarially and refining with Procrustes; the same method aligns Bangla and English vectors given a seed dictionary.
- On synthetic data in 20 dimensions, Procrustes reached P@1 0.968 (precision at 1: the fraction of test words whose nearest neighbour after mapping is the true translation) with 20 pairs, where least squares collapsed (0.148). With only 10 pairs, least squares did better (0.454 against 0.194): the rotation is undetermined in directions the dictionary misses. Gradient descent on the orthogonal group reached the SVD answer.
- **Pause and try:** with $X = I_2$ and $Y = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$, what is the Procrustes solution?
  - **Answer:** $YX^\top = Y$ is already a rotation by 90°, its SVD gives $UV^\top = Y$, so $W = Y$.

### Lab guide (about 2.5 hours, notebook `s05_riemannian_optimization.ipynb`)

1. Section 1 (20 min): the hand example, then the two identities.
2. Section 2 (20 min): three step rules for the leading eigenvector; compare measured and predicted rates.
3. Section 3 (25 min): QR retraction against the penalty; check $\|x\|^2 = 1 + \lambda/\mu$.
4. Section 4 (30 min): Procrustes by hand, the dictionary-size table, and gradient descent on O(20).
5. Section 5 (25 min): momentum and Adam; read the learning-rate plot.
6. TODO cells (30 min): three retractions, and Riemannian SGD.

- **Expect:** both identities hold to 5.6e-17. Leading eigenvector: 182 iterations (power), 185 ($\eta = 1/\lambda_1$), 89 (best $\eta$ = 0.200); rates 0.9000, 0.9000, 0.8000, as predicted. Stiefel: 67 iterations to 12.000000 with $\|X^\top X - I\|$ = 5.6e-16; penalty objectives 22.0000, 13.0000, 12.1000 and orthogonality errors 1.4142, 0.1414, 0.0141 for $\mu$ = 10, 100, 1000. P@1, least squares against Procrustes: 0.454 and 0.194 (10 pairs), 0.148 and 0.968 (20 pairs), 1.000 for both from 40 pairs. Gradient descent on O(20): 372 iterations, 8.7e-05 from the SVD answer. Best final angles: Riemannian GD 5.7e-02, Riemannian heavy ball 1.1e-07, without transport 7.0e-08, SGD momentum then normalize 8.6e-01, Riemannian Adam 2.9e-07, Adam on the projected gradient 7.2e-07, Adam then normalize 1.3. Runtime about 15 seconds.
- **Common problems:** using the Euclidean gradient without projecting it; QR without fixing the signs of R's diagonal, so the retraction jumps between sign choices; comparing optimizers at a single learning rate; fitting Procrustes with fewer pairs than dimensions.

### Quiz

1. Given the Euclidean gradient $G$ of $f$ at a point $x$ of the unit sphere, what is the Riemannian gradient?
   - **Answer:** its tangent projection, $G - (x\cdot G)\,x$.
2. Why does the penalty method never reach $X^\top X = I$?
   - **Answer:** at its optimum the penalty's pull balances the objective's push, leaving $\|x\|^2 = 1 + \lambda/\mu$ for a column; that is 1 only as $\mu \to \infty$, and large $\mu$ forces tiny steps.
3. Why did Adam followed by normalization fail while Adam on the projected gradient worked?
   - **Answer:** the Euclidean gradient has a large radial part that Adam's moments remember. Normalizing removes the radial part of each step but cannot repair the distorted moments; projecting first keeps only the tangent part.

**Watch out:** "Normalizing after each ordinary gradient step is the same as Riemannian optimization." For plain gradient descent it nearly is: normalizing is a retraction, and the radial part of the gradient only rescales the step. With momentum or Adam it is not: their memory accumulates the radial parts, and in the notebook both failed at every learning rate. Project the gradient first and keep the optimizer's state tangent, as Riemannian Adam and geoopt do.

### Assignment 5 (due before session 6, 10 points)

1. For $f(x) = x_1 + 2x_2$ on the unit circle, compute by hand the Riemannian gradient at $(1, 0)$ and at $(0, 1)$, take one step with $\eta = 0.5$ and the normalization retraction from $(1, 0)$, and find the maximizer. (3 points)
2. Complete both TODO cells. (4 points)
3. Repeat section 5 with a matrix whose top two eigenvalues are 10 and 9.99. Report each method's best final error, and say which conclusions change. (3 points)

Hand in one PDF and your notebook.

### Sources

- Boumal 2023, An Introduction to Optimization on Smooth Manifolds (Cambridge University Press), chapters 3–4. https://www.nicolasboumal.net/book/
- Absil, Mahony & Sepulchre 2008, Optimization Algorithms on Matrix Manifolds (Princeton University Press; book).
- Bonnabel 2013, Stochastic Gradient Descent on Riemannian Manifolds, IEEE Transactions on Automatic Control. https://arxiv.org/abs/1111.5280
- Bécigneul & Ganea 2019, Riemannian Adaptive Optimization Methods, ICLR. https://arxiv.org/abs/1810.00760
- Kochurov, Karimov & Kozlukov 2020, Geoopt: Riemannian Optimization in PyTorch. https://arxiv.org/abs/2005.02819
- Schönemann 1966, A Generalized Solution of the Orthogonal Procrustes Problem, Psychometrika 31(1).
- Conneau, Lample, Ranzato, Denoyer & Jégou 2018, Word Translation Without Parallel Data, ICLR. https://arxiv.org/abs/1710.04087

## Session 6: Computing in hyperbolic space: the Poincaré and Lorentz models

**Goal:** students can implement Möbius addition, distances and exp/log maps in the Poincaré ball and the Lorentz model, convert between them, and avoid numerical failures.

### Talking pointers

- **Open with:** "Hyperbolic models look fine on paper and print NaN in practice. Today we write the formulas ourselves, check every one, and find exactly where floating point breaks them."
- **Segment 1, say:** compute $0.5 \oplus 0.5$ and the 2-D example by hand, then show which gyrovector laws survive.
- **Segment 2, say:** draw the hyperboloid above the disk with the projection lines from $(-1, 0, 0)$, and convert $(0.5, 0)$ by hand.
- **Segment 3, say:** show the boundary table, the NaN gradients in PyTorch and the two-panel precision plot.
- **Close with:** "Pick the model for the job, keep points away from the edge, use float64 when you can, and test every formula you rely on." Then set assignment 6.

### Segment 1 (6 min): the Poincaré ball with curvature −c

- For $c > 0$, the Poincaré ball of curvature $-c$ is the ball of radius $1/\sqrt c$ with conformal factor $\lambda_x = 2/(1 - c\|x\|^2)$: a tangent vector $v$ at $x$ has length $\lambda_x\|v\|$.
- **Möbius addition** $x\oplus_c y$ replaces $+$, and gives the distance $d_c(x, y) = \frac{2}{\sqrt c}\operatorname{artanh}(\sqrt c\|(-x)\oplus_c y\|)$ and closed-form exponential and logarithm maps at every point (Ganea et al. 2018). Note $d(x, y) = \lambda_x\|\log_x y\|$, not $\|\log_x y\|$.
- Möbius addition makes a **gyrovector space** (Ungar 2008): left cancellation $(-x)\oplus(x\oplus y) = y$ holds; commutativity holds only up to a rotation (equal norms); associativity is replaced by a law with a rotation called a gyration; left translations $y \mapsto a\oplus y$ keep distances, right translations do not (changes up to 0.22 in the notebook).
- In one dimension $x \oplus y = \frac{x + y}{1 + xy}$, the rule for adding velocities in special relativity. As $c \to 0$, $\oplus_c$ tends to $+$ and $d_c(x, y)$ to $2\|x - y\|$.
- **Pause and try:** compute $0.5 \oplus 0.5$ for $c = 1$, and compare $d(0, 0.5 \oplus 0.5)$ with $d(0, 0.5)$.
  - **Answer:** $1/1.25 = 0.8$, and $d(0, 0.8) = \ln\frac{1.8}{0.2} = \ln 9 = 2\ln 3$, twice $d(0, 0.5) = \ln 3$: along a line through the origin, Möbius addition adds hyperbolic distances.

### Segment 2 (7 min): the Lorentz model and moving between models

- The **Lorentz model** uses the upper sheet of the hyperboloid $\langle x, x\rangle_L = -1/c$, with the Minkowski product $\langle x, y\rangle_L = -x_0y_0 + \sum_{i \ge 1} x_iy_i$ and distance $\frac{1}{\sqrt c}\operatorname{arcosh}(-c\langle x, y\rangle_L)$.
- Its exponential map, $\cosh(\sqrt c\|v\|_L)\,x + \sinh(\sqrt c\|v\|_L)\,\frac{v}{\sqrt c\|v\|_L}$, is the sphere's formula with cos and sin replaced by cosh and sinh. Nickel & Kiela 2018 reported that learning embeddings in this model was substantially more efficient than in the Poincaré ball.
- The maps between the models are $x = \frac{1}{\sqrt c}\frac{(1 + c\|p\|^2,\ 2\sqrt c\,p)}{1 - c\|p\|^2}$ and back $p = \frac{(x_1, \dots, x_n)}{1 + \sqrt c\,x_0}$: projection from the point $(-1/\sqrt c, 0, \dots, 0)$, like stereographic projection of the sphere. In the notebook, distances in the two models agree to about $10^{-14}$ for $c$ = 0.5, 1 and 2.
- **Pause and try:** for $c = 1$, send $p = (0.5, 0)$ to the hyperboloid and check that it lies on it.
  - **Answer:** $(1.25, 1)/0.75 = (5/3, 4/3)$, and $-\frac{25}{9} + \frac{16}{9} = -1$. Its distance from $(1, 0)$ is $\operatorname{arcosh}\frac53 = \ln 3$, as in the ball.

### Segment 3 (7 min): numerical stability and choosing a model

- **The boundary.** float32 cannot store a point closer to the edge than about $6\times10^{-8}$ (floating point is in Course 2 session 10), so $d(0, x)$ is infinite from $\|x\| = 1 - 10^{-8}$ on. Libraries clip: for $c = 1$, geoopt 0.5.1 (Kochurov et al. 2020) keeps $\|x\| \le 1 - \varepsilon$ ($\varepsilon = 4\times10^{-3}$ in float32, $10^{-5}$ in float64), allowing distances up to 6.21 or 12.21 from the origin.
- **arcosh near 1.** In float32, $1 + z$ rounds to 1 when $z < 6\times10^{-8}$, so distances below about $3\times10^{-4}$ become 0, and the infinite derivative of arcosh at 1 gives NaN gradients at coincident points. Remedies: the artanh form, $\operatorname{arcosh}(1 + z) = \operatorname{log1p}(z + \sqrt{z(z + 2)})$, or clamping, which here set a floor of $4.5\times10^{-4}$ on every distance.
- **Far from the origin** the Lorentz product subtracts two numbers of size about $e^{2D}/4$. For points 0.1 apart, the error stayed below 1% up to distance 14 (Lorentz) against 30 (Poincaré, arcosh form) in float64, and 4 against 10 in float32. Mishne et al. 2023 analyse these limits for both models and propose a Euclidean parametrization that eases them.
- **Choosing:** the Poincaré ball for pictures, angles, Möbius layers (session 8) and far-out points; the Lorentz model for simple formulas without a boundary (sessions 7–8). Use float64 when you can.
- **Pause and try:** in float32, why does $\operatorname{arcosh}(1 + z)$ return 0 for $z = 10^{-8}$, and what is the true value?
  - **Answer:** $1 + 10^{-8}$ rounds to exactly 1, whose arcosh is 0. The true value is about $\sqrt{2z} \approx 1.4\times10^{-4}$.

### Lab guide (about 2.5 hours, notebook `s06_poincare_lorentz.ipynb`)

1. Section 1 (15 min): both Möbius sums by hand, then in code.
2. Section 2 (25 min): three curvatures, and the $c \to 0$ limit.
3. Sections 3–4 (35 min): gyrovector laws, then geodesics.
4. Section 5 (25 min): $(0.5, 0)$ on the hyperboloid by hand, then the conversions.
5. Sections 6–7 (30 min): boundary, small distances, gradients, and the precision plot.
6. TODO cells (20 min).

- **Expect:** $0.5\oplus0.5$ = 0.8000; $(0.5, 0)\oplus(0, 0.5) = (0.5882, 0.3529)$, reversed $(0.3529, 0.5882)$, both of norm 0.6860. $d_1(0, (0.5, 0))$ = 1.0986122887, $d_2$ = 1.2465; formulas consistent to about 1e-14 for $c$ = 0.5, 1, 2; $|d_c - 2\|x - y\||$ = 6.5e-07 at $c$ = 1e-6. Geodesic 3.618936 against the straight segment's 3.728216. $(0.5, 0) \mapsto (1.666667, 1.333333, 0)$. Boundary: 16.6355 instead of 16.811243 in float32 at $1 - 10^{-7}$, infinite from $1 - 10^{-8}$. arcosh in float32 gives 0 from $\delta = 10^{-4}$. PyTorch: NaN gradients with arcosh, distance 4.472e-04 with clamping, gradient $(-2.2989, 0)$ 1e-9 apart with artanh. Largest distance with error below 1%: float32 6, 10, 10, 4 and float64 16, 30, 30, 14 (artanh, arcosh, log1p, Lorentz). Runtime about 6 seconds.
- **Common problems:** mixing up $c$ and the curvature $-c$ (geoopt's `Lorentz(k)` uses $\langle x, x\rangle_L = -k$); dividing by $\|v\| = 0$ at coincident points; PyTorch's default float32; computing Lorentz distances between nearby points far from the origin.

### Quiz

1. Why is $d(x, y) = \lambda_x\|\log_x y\|$ rather than $\|\log_x y\|$?
   - **Answer:** $\log_x y$ is a tangent vector at $x$, and the metric there is the Euclidean one scaled by $\lambda_x$, so its Riemannian length is $\lambda_x$ times its Euclidean length.
2. Which maps of the Poincaré ball are isometries: $y \mapsto a\oplus y$ or $y \mapsto y\oplus a$?
   - **Answer:** the left translations $y \mapsto a \oplus y$; right translations changed distances by up to 0.22 in the notebook.
3. Why did the Lorentz distance fail at about half the distance where the Poincaré one failed?
   - **Answer:** its rounding error grows like $e^{2D}$, because it subtracts numbers of size $e^{2D}/4$; the Poincaré formula's error grows like $e^{D}$, through $1 - \|x\|^2 \approx 4e^{-D}$.

**Watch out:** "Möbius addition is ordinary vector addition in disguise." In one dimension $0.5 \oplus 0.5 = 0.8$; in two dimensions $\oplus$ is neither commutative nor associative, and adding on the right does not preserve distances. $a \oplus y$ is the hyperbolic isometry that moves the origin to $a$, applied to $y$. It approaches ordinary addition only as $c \to 0$, or for vectors near the origin.

### Assignment 6 (due before session 7, 10 points)

1. For $c = 1$ and $v = (1, 0)$, compute by hand $\exp_0(v)$, its distance from the origin and its point on the hyperboloid. Explain why you get $(\cosh 2, \sinh 2, 0)$. (3 points)
2. Complete both TODO cells. (4 points)
3. Repeat section 7 for points 0.001 apart instead of 0.1. Report how the four formulas' limits change, and explain why. (3 points)

Hand in one PDF and your notebook.

### Sources

- Ganea, Bécigneul & Hofmann 2018, Hyperbolic Neural Networks, NeurIPS. https://arxiv.org/abs/1805.09112
- Nickel & Kiela 2018, Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry, ICML. https://arxiv.org/abs/1806.03417
- Ungar 2008, A Gyrovector Space Approach to Hyperbolic Geometry (Morgan & Claypool; book).
- Mishne, Wan, Wang & Yang 2023, The Numerical Stability of Hyperbolic Representation Learning, ICML. https://arxiv.org/abs/2211.00181
- Kochurov, Karimov & Kozlukov 2020, Geoopt: Riemannian Optimization in PyTorch. https://arxiv.org/abs/2005.02819

## Session 7: Hyperbolic embeddings of hierarchies

**Goal:** students can train Poincaré embeddings of a hierarchy with Riemannian SGD and evaluate them against Euclidean embeddings with distortion and mean average precision.

### Talking pointers

- **Open with:** "Draw a family tree of 297 people, five generations below one ancestor, so that cousins sit closer than strangers. Paper runs out of room; the Poincaré disk does not, if you can afford the digits."
- **Segment 1, say:** write the loss for one linked pair and two negatives on the board, then compute how much the Riemannian rescaling shrinks a gradient at radius 0.9.
- **Segment 2, say:** show the construction table: τ = 3 gives distortion 0.039 with leaves 6.8 × 10⁻⁷ from the boundary; τ = 4 breaks float32.
- **Segment 3, say:** compute one average precision by hand, then show the 12-run table: in 2-D every Poincaré run wins, but in 10-D the best Euclidean run reaches MAP 1.000.
- **Close with:** "Hyperbolic embeddings buy room when dimensions are scarce. Measure against a tuned Euclidean baseline before you assume they help." Then set assignment 7.

### Segment 1 (7 min): Poincaré embeddings and Riemannian SGD

- The task: place the nodes of a hierarchy so that linked nodes are close and unrelated nodes are far apart. Course 7 session 8 showed why hierarchies fit hyperbolic space; today we train the embeddings ourselves.
- Poincaré embeddings (Nickel & Kiela 2017): for each linked pair (u, v), sample nodes not linked to u (negatives) and minimize $-\log\big(e^{-d(u,v)} / \sum_{w} e^{-d(u,w)}\big)$, with w running over v and the negatives and d the Poincaré distance: a softmax whose "correct class" is the true neighbour.
- Nickel & Kiela trained on every (noun, ancestor) pair of WordNet, the transitive closure; our lab uses only the tree's edges.
- Riemannian SGD in the ball: the metric is $\lambda_x^2$ times the Euclidean one, with $\lambda_x = 2/(1 - \|x\|^2)$ (session 6), so the Riemannian gradient is the Euclidean gradient divided by $\lambda_x^2$: multiplied by $(1 - \|x\|^2)^2/4$. (Session 5's embedded manifolds needed only a projection; here the metric itself changes.) A retraction then pulls any point that left the ball back to radius $1 - 10^{-5}$. With step sizes that shrink over time, and under some further technical conditions, Riemannian SGD converges to a critical point (Bonnabel 2013).
- From the paper: start near the origin and use a 10 times smaller step for the first epochs ("burn-in").
- **Pause and try:** a point sits at Euclidean radius 0.9. By what factor does the rescaling shrink its Euclidean gradient?
  - **Answer:** $(1 - 0.81)^2/4 = 0.009$, about 1/111. Near the boundary a tiny Euclidean step is already a long hyperbolic step.

### Segment 2 (6 min): construction, the Lorentz model and precision

- Sarkar (2011) showed with a simple construction that any tree can be embedded in the hyperbolic plane with distortion below 1 + ε for any ε > 0: move a node to the origin with an isometry, put its children at hyperbolic distance τ at evenly spaced angles, and move back. Sala et al. (2018) extended it to higher dimensions. Session 4 did this for a balanced tree.
- The price is precision: a point at hyperbolic distance ρ from the origin has $1 - |z| \approx 2e^{-\rho}$, so the digits needed grow with depth × τ. Sala et al. prove upper and lower bounds on this precision–dimension trade-off. On WordNet their 2-D construction reached MAP 0.989, against 0.87 for Nickel & Kiela's 200-dimensional embedding.
- The Lorentz model (hyperboloid) gives closed-form geodesics and avoids the instabilities of the Poincaré distance; Nickel & Kiela (2018) found the largest gains in low dimensions. Mishne et al. (2023) found that in float64 the Poincaré ball represents points better, while the Lorentz model optimizes better. Course 2 session 10 explains the floating-point side.
- **Pause and try:** with τ = 3, a depth-5 leaf is at most 15 from the origin. How close to the boundary is it, and can float32 store it?
  - **Answer:** about $2e^{-15} \approx 6 \times 10^{-7}$ (measured: 6.8 × 10⁻⁷). float32 numbers just below 1 are about $6 \times 10^{-8}$ apart, so it just fits; at τ = 4 the gap, about $4 \times 10^{-9}$, rounds to zero.

### Segment 3 (7 min): evaluation, and when not to use hyperbolic embeddings

- Mean average precision (MAP) of reconstruction (Sala et al. 2018): for node a and each true neighbour b, the precision is the fraction of true neighbours in the smallest ball around a that contains b. Average over b, then over nodes. MAP is 1 when every node's neighbours come first; it checks order only.
- Distortion checks sizes: the average distortion is the mean of $|s\,d_E/d_G - 1|$ over all pairs, with the best global scale s, and the worst-case distortion is the largest ratio $d_E/d_G$ over the smallest. Report both: the Nickel–Kiela loss rewards ranking, so high MAP can come with large distortion.
- Use them for real hierarchies such as WordNet (the NOT RUN cell builds its mammal subtree) or ICD-10 codes (Course 7 session 8), not for graphs with many cycles (session 8 measures tree-likeness). With enough dimensions, Euclidean embeddings can match them.
- **Pause and try:** node a has two neighbours, ranked 1st and 3rd among all other nodes by distance. What is its average precision?
  - **Answer:** (1/1 + 2/3)/2 = 0.833. The second neighbour's ball also holds one non-neighbour.

### Lab guide (about 2.5 hours, notebook `s07_hyperbolic_embeddings.ipynb`)

1. Section 1 (15 min): build the 297-node tree; check the distance formulas, Möbius addition and the isometry.
2. Section 2 (15 min): MAP and distortion; the hand example.
3. Section 3 (30 min): train four models at three learning rates; read the whole table.
4. Section 4 (15 min): the best run of each model; depth against distance from the root.
5. Sections 5–6 (30 min): the construction, its float32 failures, and the pictures.
6. TODO cells (45 min): the Lorentz model; training on the transitive closure.

- **Expect:** helper checks within 1.2e-14. Best runs: Poincaré 2-D MAP 0.914 (average distortion 0.202, worst case 23.7); Euclidean 2-D 0.719 (0.343, 681.0); Poincaré 10-D 0.991 (0.196, 7.8); Euclidean 10-D 1.000 (0.224, 8.1). 2-D Poincaré runs 0.772–0.914 against Euclidean 0.697–0.719. Spearman correlation of depth with distance from the root: 0.752 and 0.289 in 2-D, 0.848 and 0.586 in 10-D. Construction: τ = 2 gives MAP 1.000, distortion 0.066, worst case 2.591 and 1 − radius 1.00e-04; τ = 3 gives 0.039, 1.429 and 6.76e-07; at τ = 4, 79 points round onto the boundary in float32; at τ = 8, float64 fails too. Runtime about 25 seconds.
- **Common problems:** forgetting the $(1 - \|x\|^2)^2/4$ factor, so points race to the boundary; computing MAP with "<" instead of "≤", which gives undefined (0/0) or wrong values when nodes tie in distance, as siblings do; tuning the learning rate for one geometry only.

### Quiz

1. Why is the Euclidean gradient multiplied by $(1 - \|x\|^2)^2/4$ in Riemannian SGD on the Poincaré ball?
   - **Answer:** it is $1/\lambda_x^2$, the inverse metric factor, which turns the Euclidean gradient into the Riemannian one; without it, steps near the boundary are far too long.
2. Why can the constructive embedding not simply use a very large τ?
   - **Answer:** leaves end up about $2e^{-\rho}$ from the boundary, with ρ near depth × τ; τ = 4 broke float32 and τ = 8 float64.
3. What do MAP and distortion each measure?
   - **Answer:** MAP: whether each node's true neighbours are its nearest points (order only). Distortion: whether the distances themselves match the graph distances.

**Watch out:** "Hyperbolic embeddings always beat Euclidean ones." They win when dimensions are scarce: in the notebook, 2-D Poincaré reached MAP 0.914 against 0.719. But in 10-D the best Euclidean run reached 1.000 against 0.991, and the ranking flipped with the learning rate. Real graphs are rarely perfect trees, so measure their tree-likeness (session 8) and tune the Euclidean baseline too (Course 1 session 9).

### Assignment 7 (due before session 8, 10 points)

1. By hand: the gradient factor at radius 0.5 and 0.99; the average precision of a node whose neighbours are ranked 1st, 2nd and 5th; $1 - |z|$ at hyperbolic distance 10 from the origin. Check each in code. (3 points)
2. Repeat section 3 for dimensions 2, 3, 5 and 10 with three seeds each. Plot MAP and average distortion against dimension, with error bars, for both geometries. Where does Euclidean catch up? (4 points)
3. Complete both TODO cells. Compare the Lorentz model's MAP and stability with the Poincaré ball's, and report whether training on the transitive closure raises the correlation between depth and distance from the root. (3 points)

Hand in one PDF and your notebook.

### Sources

- Nickel & Kiela 2017, Poincaré Embeddings for Learning Hierarchical Representations. https://arxiv.org/abs/1705.08039
- Sala, De Sa, Gu & Ré 2018, Representation Tradeoffs for Hyperbolic Embeddings, ICML. https://arxiv.org/abs/1804.03329
- Nickel & Kiela 2018, Learning Continuous Hierarchies in the Lorentz Model of Hyperbolic Geometry, ICML. https://arxiv.org/abs/1806.03417
- Sarkar 2011, Low Distortion Delaunay Embedding of Trees in Hyperbolic Plane, Graph Drawing (GD 2011), Lecture Notes in Computer Science (Springer).
- Bonnabel 2013, Stochastic Gradient Descent on Riemannian Manifolds, IEEE Transactions on Automatic Control 58(9). https://arxiv.org/abs/1111.5280
- Mishne, Wan, Wang & Yang 2023, The Numerical Stability of Hyperbolic Representation Learning, ICML. https://arxiv.org/abs/2211.00181

## Session 8: Hyperbolic neural networks

**Goal:** students can build hyperbolic layers from exp/log maps and Möbius operations, test a graph for tree-likeness with δ-hyperbolicity, and judge when hyperbolic models help.

### Talking pointers

- **Open with:** "Last session, hyperbolic embeddings won in two dimensions. Today we build a hyperbolic network for labels that form a tree, and the Euclidean network wins. Both results are true, and the reasons are today's lesson."
- **Segment 1, say:** write $M \otimes_c x = \exp_0(M \log_0 x)$ on the board, work the example with M = 2I, then draw a gyroplane through $p_k$.
- **Segment 2, say:** draw HGCN's three steps for one node: map to the tangent space, average the neighbours, map back.
- **Segment 3, say:** compute δ for four leaves of a star and four points of a cycle, then show the results table and the run that produced a non-finite loss.
- **Close with:** "A hyperbolic layer is an ordinary layer wrapped in exp and log maps. Whether it helps is an experimental question, so give the Euclidean baseline a fair chance." Then set assignment 8.

### Segment 1 (7 min): layers in the Poincaré ball

- Ganea et al. (2018) build each layer by moving to the tangent space at the origin, doing the Euclidean operation there, and moving back. The Möbius matrix–vector product is $M \otimes_c x = \exp_0(M \log_0 x)$, with the closed form $\frac{1}{\sqrt c}\tanh\big(\frac{\|Mx\|}{\|x\|}\operatorname{artanh}(\sqrt c\|x\|)\big)\frac{Mx}{\|Mx\|}$ in the ball of curvature −c. It satisfies $(MN) \otimes_c x = M \otimes_c (N \otimes_c x)$.
- A bias is added with Möbius addition (session 6), and a nonlinearity σ acts as $\exp_0(\sigma(\log_0 x))$. A layer is $\sigma^{\otimes}((M \otimes_c x) \oplus_c b)$. As c → 0, every operation becomes its Euclidean version; the notebook checks this with c = 10⁻⁸.
- Hyperbolic multinomial logistic regression (MLR): the logit of class k is $\lambda_{p_k}\|a_k\|$ times the signed distance from x to a "gyroplane", the set of geodesics through a point $p_k$ orthogonal to a normal $a_k$. In 2-D it is one geodesic. As c → 0 the logit becomes $4\langle x - p_k, a_k\rangle$, ordinary MLR.
- Training: keep parameters in the tangent space at 0 and use Adam, or keep points in the ball and use Riemannian optimizers (session 5).
- **Pause and try:** with c = 1, a point x lies at hyperbolic distance 1 from the origin. Where is $(2I) \otimes x$?
  - **Answer:** doubling $\log_0 x$ doubles the distance from the origin: the image lies in the same direction at distance 2, Euclidean radius tanh(1) = 0.76 instead of tanh(0.5) = 0.46.

### Segment 2 (6 min): hyperbolic graph networks

- HGCN (Chami et al. 2019) maps input features into hyperbolic space with the exp map, transforms them with Möbius products, and aggregates neighbours in a tangent space: log map at a node, weighted average, exp map back. Each layer learns its own curvature. Course 7 session 8 introduced it.
- Why not average the points in the ball directly? The Euclidean average does not respect hyperbolic isometries, as the pause-and-try shows. Tangent-space averaging, or a Fréchet mean (session 3), does better.
- Fully hyperbolic networks (Chen et al. 2022) work directly in the Lorentz model with Lorentz boosts and rotations. They argue that the tangent-space linear maps of earlier models are a relaxation of Lorentz rotation that leaves out boosts.
- Every exp and log map costs time and precision: in the notebook a hyperbolic run took about five times as long as a Euclidean one.
- **Pause and try:** the points 0.9 and −0.9 on a diameter of the disk have Euclidean average 0. Move them with the isometry $T(z) = (z - 0.9)/(1 - 0.9z)$. Is the average of the images the image of the average?
  - **Answer:** no. The images are 0 and −0.994, with average −0.497, but T(0) = −0.9. The hyperbolic midpoint, 0 before the move, does move to −0.9.

### Segment 3 (7 min): when do hyperbolic models help?

- Gromov's four-point condition (Gromov 1987): for four nodes, sum the distances of each of the three pairings and sort the sums, $S_1 \ge S_2 \ge S_3$; then $\delta = (S_1 - S_2)/2$, maximized over all quadruples. Trees have δ = 0, and the triangle inequality gives δ ≤ diameter/2, so $2\delta/\text{diameter}$ lies between 0 and 1. Sampling quadruples gives a lower bound.
- HGCN reported δ for each dataset, from 0 for the tree-shaped DISEASE graph to 11 for the Cora citation graph, and its largest improvements came on the most tree-like (low-δ) graphs.
- But Katsman & Gilbert (2025) found that properly trained Euclidean models with comparable parameter counts generally match or beat hyperbolic graph models, even on datasets called the most hyperbolic. They also argue that δ on its own is a flawed guide to whether a dataset suits hyperbolic models. Note that δ measures only the graph's distances, not the node features or labels.
- In our lab the class means were tree-like ($2\delta/\text{diameter}$ 0.278, against 0.411 for random points), yet the Euclidean multilayer perceptron (MLP) won at every dimension.
- **Pause and try:** compute δ for four leaves of a star, and for four equally spaced nodes of an 8-node cycle.
  - **Answer:** star: all six distances are 2, so the sums are 4, 4, 4 and δ = 0. Cycle: the sums are 4 + 4 = 8 for the opposite pairs and 2 + 2 = 4 twice, so δ = (8 − 4)/2 = 2 = diameter/2, the largest possible.

### Lab guide (about 2.5 hours, notebook `s08_hyperbolic_networks.ipynb`)

1. Section 1 (30 min): the Möbius operations and MLR, with every check, including the brute-force distance to a gyroplane.
2. Section 2 (20 min): δ for five graphs; do the pause-and-try by hand first.
3. Section 3 (15 min): the hierarchical data, its δ and the logistic-regression reference.
4. Section 4 (40 min): the two MLPs, three dimensions, three seeds, and the run without the cap.
5. TODO cells (45 min): trainable curvature; exact δ.

- **Expect:** checks within 2.9e-14 (gyroplane distance) and 3.3e-07 at c = 10⁻⁸. $2\delta/\text{diameter}$: tree 0.000, random graph 0.667, grid 0.800, small world 0.800, cycle 1.000. Raw logistic regression 0.829. Test accuracy, Euclidean against hyperbolic: 0.627 and 0.595 (d = 2), 0.781 and 0.759 (d = 5), 0.802 and 0.783 (d = 10); training accuracy at d = 2: 0.860 and 0.921. Without the cap: training accuracy 0.720, and one seed hit a non-finite loss at epoch 230. Runtime about 50 seconds.
- **Common problems:** applying $\exp_0$ to large tangent vectors, which puts points on the boundary where gradients vanish; computing in float32; comparing graphs by δ without dividing by the diameter.

### Quiz

1. Write the Möbius matrix–vector product using exp and log maps. What does it become as c → 0?
   - **Answer:** $M \otimes_c x = \exp_0(M\log_0 x)$; as c → 0 both maps become the identity, so it becomes Mx.
2. What does the hyperbolic MLR logit measure?
   - **Answer:** $\lambda_{p_k}\|a_k\|$ times the signed hyperbolic distance from x to the gyroplane through $p_k$ orthogonal to $a_k$.
3. Why is a small δ not enough to choose a hyperbolic model?
   - **Answer:** δ describes only the graph's distances, not the features or labels, and it is a worst case over quadruples. A tuned Euclidean baseline must still be beaten.

**Watch out:** "Hyperbolic layers are always better for graphs." They suit tree-like data in few dimensions, but they cost more, need care near the boundary, and often lose to a well-trained Euclidean model. In the notebook the Euclidean MLP won at every dimension on tree-shaped labels, and without the cap one hyperbolic run failed. Measure δ, tune both models with the same budget (Course 1 session 9), and report all runs.

### Assignment 8 (due before session 9, 10 points)

1. By hand: $(3I) \otimes x$ for x at hyperbolic distance 0.5 from the origin; δ for four nodes of a path 1–2–3–4; the MLR logit for c → 0 with x = (1, 0), p = (0, 0), a = (0.5, 0). Check each in code. (3 points)
2. Rerun section 4 with five seeds and learning rates 0.003, 0.01 and 0.03 for both models. Plot test accuracy against d with error bars. Is the gap at d = 2 larger than the seed-to-seed spread? (4 points)
3. Complete both TODO cells. Report the learned curvatures, and the exact and sampled δ of the 6 × 6 grid and the cycle. (3 points)

Hand in one PDF and your notebook.

### Sources

- Ganea, Bécigneul & Hofmann 2018, Hyperbolic Neural Networks, NeurIPS. https://arxiv.org/abs/1805.09112
- Chami, Ying, Ré & Leskovec 2019, Hyperbolic Graph Convolutional Neural Networks, NeurIPS. https://arxiv.org/abs/1910.12933
- Katsman & Gilbert 2025, Shedding Light on Problems with Hyperbolic Graph Learning, Transactions on Machine Learning Research. https://arxiv.org/abs/2411.06688
- Chen et al. 2022, Fully Hyperbolic Neural Networks, ACL. https://arxiv.org/abs/2105.14686
- Gromov 1987, Hyperbolic Groups, in Essays in Group Theory (MSRI Publications 8, Springer), pages 75–263.
- Kochurov, Karimov & Kozlukov 2020, Geoopt: Riemannian Optimization in PyTorch. https://arxiv.org/abs/2005.02819

## Session 9: SPD matrices: the geometry of covariance

**Goal:** students can compute affine-invariant and log-Euclidean distances and means of SPD matrices and use them to classify covariance features.

### Talking pointers

- **Open with:** "Average two thin ellipses, one lying flat and one tilted by 60 degrees, and you get a fat one: the area-like determinant jumps from 1 to 3.6. Covariance matrices need their own geometry."
- **Segment 1, say:** show the swelling plot, then the table where the Euclidean distance from I to a singular matrix stays below 1 while the curved distances grow without limit.
- **Segment 2, say:** work the mean of diag(1, 4) and diag(4, 1) on the board, then show the bar chart: recentring lifts every method across subjects.
- **Segment 3, say:** draw SPDNet as a pipeline of matrices: 22 × 22 in, BiMap to 8 × 8, ReEig, LogEig, then a classifier.
- **Close with:** "A covariance matrix is a point on a curved cone. Measure, average and classify it with that geometry, and recentre before you transfer across people." Then set assignment 9.

### Segment 1 (7 min): the SPD cone and its metrics

- A symmetric positive definite (SPD) matrix has only positive eigenvalues. Covariance matrices of EEG channels, diffusion tensors in MRI and image feature covariances are SPD. The n × n SPD matrices form an open cone of dimension n(n+1)/2: sums and positive multiples stay inside, differences may not.
- The Euclidean (Frobenius) metric treats them as vectors, with two failures. Averages swell: the determinant of the mean exceeds that of the matrices. And singular matrices are at a finite distance: in the notebook, the distance from I to diag(1, ε) never exceeded 1 as ε → 0.
- Functions of an SPD matrix act on its eigenvalues: $\log A = V \text{diag}(\log\lambda) V^\top$ (Course 2 session 3).
- Affine-invariant metric (Pennec et al. 2006): $d(A, B) = \|\log(A^{-1/2} B A^{-1/2})\|_F = \sqrt{\sum_i \log^2\lambda_i}$, with $\lambda_i$ the eigenvalues of $A^{-1}B$. It is unchanged by every congruence $A \mapsto WAW^\top$ and by inversion, and singular matrices are infinitely far away.
- Log-Euclidean metric (Arsigny et al. 2007): $\|\log A - \log B\|_F$, cheaper; it is unchanged by rotations, scaling and inversion, but not by general congruences. Bures–Wasserstein (Bhatia et al. 2019): $\sqrt{\operatorname{tr}A + \operatorname{tr}B - 2\operatorname{tr}(A^{1/2}BA^{1/2})^{1/2}}$, the optimal-transport (2-Wasserstein) distance between the Gaussians $N(0, A)$ and $N(0, B)$.
- **Pause and try:** for 2 × 2 matrices, what are the affine-invariant distances from I to 4I and from 2I to 8I?
  - **Answer:** both are $\sqrt{2}\ln 4 \approx 1.96$, since all eigenvalues of $A^{-1}B$ are 4. Scaling both matrices is a congruence. The Euclidean distances, 4.24 and 8.49, differ.

### Segment 2 (7 min): means, MDM and transfer across subjects

- The affine-invariant (Karcher) mean minimizes the sum of squared distances. Session 3's Riemannian gradient descent with step 1 gives the fixed-point iteration $M \leftarrow M^{1/2}\exp\big(\frac1N\sum_i \log(M^{-1/2}C_iM^{-1/2})\big)M^{1/2}$. The log-Euclidean mean $\exp(\frac1N\sum_i \log C_i)$ needs no iteration and has the same determinant, but is a different matrix in general (Arsigny et al. 2007).
- Minimum distance to mean (MDM) (Barachant et al. 2012): one mean per class, and each trial goes to the nearest. They also mapped matrices to the tangent space at the overall mean, $\log(M^{-1/2}CM^{-1/2})$, and used an ordinary linear classifier there. On the multiclass brain–computer interface (BCI) Competition IV dataset 2a, this tangent-space method with variable selection raised mean accuracy from the reference method's 65.1% to 70.2%.
- People differ: head shape, electrode contact and signal power change the covariances, so a classifier trained on some people fails on a new one. Recentring (Zanini et al. 2018) transforms each subject's trials by $M_s^{-1/2} C M_s^{-1/2}$, using that subject's mean $M_s$, so every subject's mean becomes the identity. It needs no labels.
- **Pause and try:** what are the affine-invariant and Euclidean means of diag(1, 4) and diag(4, 1)?
  - **Answer:** the matrices commute, so the curved mean takes geometric means of the eigenvalues: diag(2, 2), determinant 4 like both inputs. The Euclidean mean diag(2.5, 2.5) has determinant 6.25: swelling.

### Segment 3 (6 min): SPDNet

- SPDNet (Huang & Van Gool 2017) keeps SPD matrices as hidden values. BiMap: $X \mapsto W^\top X W$ with W of orthonormal columns (a point on the Stiefel manifold, session 5), like a fully connected layer that shrinks the matrix. ReEig: raise eigenvalues below a floor ε, like a ReLU, which also keeps matrices safely positive definite. LogEig: the matrix logarithm, after which ordinary layers follow.
- W is trained with Riemannian gradient steps on the Stiefel manifold; gradients flow through eigendecompositions, which become unstable when two eigenvalues are nearly equal.
- Uses: EEG and brain–computer interfaces, diffusion tensor imaging, and emotion, action and face recognition from feature covariances. Course 7 session 8 gave the overview; here we built every piece.
- **Pause and try:** a 22-channel EEG covariance goes through BiMap with W of size 22 × 8, then LogEig. What size comes out, and how many numbers reach the classifier?
  - **Answer:** an 8 × 8 matrix, symmetric, so 8 · 9/2 = 36 numbers.

### Lab guide (about 2.5 hours, notebook `s09_spd_matrices.ipynb`)

1. Section 1 (25 min): matrix functions, the four distances, invariances, and the walk towards a singular matrix.
2. Section 2 (25 min): Karcher and log-Euclidean means; the swelling plot.
3. Section 3 (15 min): the synthetic EEG-like trials of 8 subjects.
4. Sections 4–5 (40 min): MDM with three metrics and the tangent-space classifier, within and across subjects, with and without recentring.
5. Section 6 and TODO cells (45 min): SPDNet's layers; Bures–Wasserstein MDM; a one-layer SPDNet.

- **Expect:** under a congruence the affine-invariant distance changed by 2.75e-13, the log-Euclidean by 0.919. From I to diag(1, 10⁻⁹): Euclidean 1.0000, affine-invariant 20.723. Both curved means have determinant 0.2545562, the Euclidean mean 1.82; midpoint determinant 3.6367 against 1.0000. Within subject: Euclidean MDM 0.730, log-Euclidean 0.840, affine-invariant 0.839, tangent space 0.840. New subject without recentring: 0.649, 0.705, 0.676, 0.701; with recentring: 0.820, 0.826, 0.826, 0.824. Runtime about 15 seconds.
- **Common problems:** a covariance estimated from fewer samples than channels is singular, so its logarithm does not exist and `scipy.linalg.logm` returns complex numbers (use more samples, or shrinkage such as pyRiemann's `oas` estimator); forgetting the √2 on off-diagonal tangent coordinates; recentring with the Euclidean mean instead of the Riemannian one.

### Quiz

1. Which of the Euclidean, log-Euclidean, affine-invariant and Bures–Wasserstein distances are unchanged by every congruence $WAW^\top$?
   - **Answer:** only the affine-invariant one. In the notebook a random congruence changed the log-Euclidean distance by 0.919 and the Bures–Wasserstein one by 2.39; all three others are unchanged by rotations.
2. What does recentring do, and why may it use the test subject's trials?
   - **Answer:** it maps each subject's trials by $M_s^{-1/2} C M_s^{-1/2}$ so that the subject's mean becomes the identity. It uses no labels, so it is unsupervised adaptation.
3. What do ReEig and LogEig do in SPDNet?
   - **Answer:** ReEig raises eigenvalues below a floor, a nonlinearity that keeps matrices positive definite; LogEig takes the matrix logarithm, which flattens the cone so Euclidean layers can follow.

**Watch out:** "A covariance matrix is just a vector with d² numbers." It has only d(d+1)/2 free numbers and lives in an open cone: treated as a vector, averages swell and singular matrices look close. In the notebook the Euclidean classifier lost 11 points within subjects. But near a single point the cone is almost flat: after recentring, even Euclidean MDM reached 0.820. Use the tangent space at a well-chosen mean when you need vectors.

### Assignment 9 (due before session 10, 10 points)

1. By hand: the affine-invariant and log-Euclidean distances between diag(1, 9) and diag(9, 1); the affine-invariant mean of diag(1, 9) and diag(4, 4); the dimension of the manifold of 22 × 22 SPD matrices. Check each in code. (3 points)
2. Vary the desynchronization (power ratio 0.3, 0.5, 0.7) and the trial length (64, 128, 512 samples). Report within- and cross-subject accuracy of all four methods, with and without recentring. When does the choice of metric matter most? (4 points)
3. Complete both TODO cells, and compare Bures–Wasserstein MDM and the one-layer SPDNet with the methods of section 4. (3 points)

Hand in one PDF and your notebook.

### Sources

- Pennec, Fillard & Ayache 2006, A Riemannian Framework for Tensor Computing, International Journal of Computer Vision 66(1). https://hal.archives-ouvertes.fr/inria-00614990
- Barachant, Bonnet, Congedo & Jutten 2012, Multiclass Brain–Computer Interface Classification by Riemannian Geometry, IEEE Transactions on Biomedical Engineering 59(4). https://doi.org/10.1109/TBME.2011.2172210
- Arsigny, Fillard, Pennec & Ayache 2007, Geometric Means in a Novel Vector Space Structure on Symmetric Positive-Definite Matrices, SIAM Journal on Matrix Analysis and Applications 29(1). https://doi.org/10.1137/050637996
- Bhatia, Jain & Lim 2019, On the Bures–Wasserstein Distance between Positive Definite Matrices, Expositiones Mathematicae 37(2). https://arxiv.org/abs/1712.01504
- Zanini, Congedo, Jutten, Said & Berthoumieu 2018, Transfer Learning: A Riemannian Geometry Framework With Applications to Brain–Computer Interfaces, IEEE Transactions on Biomedical Engineering 65(5). https://doi.org/10.1109/TBME.2017.2742541
- Huang & Van Gool 2017, A Riemannian Network for SPD Matrix Learning, AAAI. https://arxiv.org/abs/1608.04233

## Session 10: Rotations and poses: the Lie groups SO(3) and SE(3)

**Goal:** students can compute exp and log maps of SO(3), measure rotation errors by geodesic distance, average rotations, and choose a rotation representation for neural networks.

### Talking pointers

- **Open with:** "A drone turns from 170 degrees to minus 170 degrees. Its heading changed by 20 degrees, but its Euler angle changed by 340. A network that predicts Euler angles has to learn that jump, and it cannot."
- **Segment 1, say:** write $[\omega]_\times$ for ω = (0, 0, θ), apply Rodrigues' formula with θ = 90°, and check the result rotates (1, 0, 0) to (0, 1, 0).
- **Segment 2, say:** show the three panels of section 2, where only the 6-D curve is smooth, then the error table: worst cases 177.2° and 178.7° against 5.8°.
- **Segment 3, say:** average 170° and −170° by hand, then show the averaging table, where the Euler average is 174.4° from the truth.
- **Close with:** "Rotations live on a group. Measure them with angles, average them on the group, and let networks output something continuous." Then set assignment 10.

### Segment 1 (7 min): SO(3), so(3) and the exp and log maps

- SO(3) is the set of 3 × 3 matrices with $R^\top R = I$ and det R = 1. It is a group (rotations compose) and a 3-dimensional manifold. Its tangent space at I, the Lie algebra so(3), holds the skew-symmetric matrices $[\omega]_\times$, with $[\omega]_\times v = \omega \times v$ (Solà et al. 2018).
- The exp map is Rodrigues' formula: with θ = ‖ω‖ and $K = [\omega]_\times$, $\exp(K) = I + \frac{\sin\theta}{\theta}K + \frac{1 - \cos\theta}{\theta^2}K^2$, a rotation by θ about ω/θ. The log map reverses it, with special care near θ = 0 and θ = π, where sin θ → 0.
- The geodesic distance is $d(R_1, R_2) = \|\log(R_1^\top R_2)\|$, the angle of the relative rotation, between 0 and π. Compute it with atan2: in the notebook, arccos returned 0 for a rotation by 10⁻⁸ rad.
- Poses combine a rotation and a translation: SE(3) for robots, cameras and molecules, and SE(2) for a robot on a floor (x, y and heading). SE(3) has its own exp map: a twist $(\omega, v)$, a tangent vector at the identity, goes to the rotation $\exp([\omega]_\times)$ and the translation $Vv$, where the matrix V depends on ω.
- **Pause and try:** what is the geodesic distance between rotations by 170° and by −170° about the same axis?
  - **Answer:** $R_1^\top R_2$ is a rotation by −340°, that is by 20° the other way, so the distance is 20°, though the angles differ by 340.

### Segment 2 (7 min): representations for neural networks

- Euler angles (3 numbers) wrap around at ±180° and suffer gimbal lock: at a pitch of ±90°, only the difference or the sum of the other two angles matters. Axis–angle (3 numbers) jumps at θ = π. Unit quaternions (4 numbers) have no gimbal lock, but q and −q are the same rotation. A 3 × 3 matrix (9 numbers) must be projected back onto SO(3).
- Zhou et al. (2019) proved that every representation of 3-D rotations in 4 or fewer real dimensions is discontinuous: some nearby rotations must get distant codes. A network is continuous, so near those places its errors are large.
- Continuous representations exist in 5 and 6 dimensions. The 6-D one keeps two columns of R; to decode any 6 outputs, apply Gram–Schmidt to get two orthonormal columns, and take their cross product as the third.
- Train with a loss on the decoded matrix or the geodesic angle, and report the worst case and a high percentile, not only the mean.
- **Pause and try:** which unit quaternions (w, x, y, z) represent a rotation by 180° about the z axis?
  - **Answer:** (0, 0, 0, 1) and (0, 0, 0, −1). A rule such as "w ≥ 0" cannot choose between them, so it must jump near this rotation, as the notebook's z component did (from +1 to −1).

### Segment 3 (6 min): averaging and interpolation

- The chordal $L_2$ mean minimizes $\sum_i \|R - R_i\|_F^2$: compute $S = \sum_i R_i = U\Sigma V^\top$ by SVD and take $R = U\,\text{diag}(1, 1, \det UV^\top)\,V^\top$ (Hartley et al. 2013; the SVD is from Course 2 session 3). The determinant fix avoids returning a reflection.
- The geodesic $L_2$ (Karcher) mean minimizes $\sum_i d(R, R_i)^2$, by session 3's iteration on the group: $R \leftarrow R\exp\big(\frac1N\sum_i \log(R^\top R_i)\big)$. For concentrated data the two means are close: 0.08° apart in the notebook.
- Interpolation: $R(t) = R_1\exp(t\log(R_1^\top R_2))$ moves at constant angular speed; with quaternions it is slerp (session 1).
- Equivariance, making a network's output rotate with its input, is a different question; Course 7 sessions 6–7 and Course 9 sessions 1–3 cover it.
- **Pause and try:** average rotations by 170° and −170° about z by averaging the angles. What do you get, and what is the correct average?
  - **Answer:** 0°, which is 170° from both. The correct mean is 180°, only 10° from each.

### Lab guide (about 2.5 hours, notebook `s10_rotations_lie_groups.ipynb`)

1. Section 1 (35 min): Rodrigues, the log map near 0 and π, distances, and SE(3), all checked against SciPy.
2. Section 2 (20 min): jumps along a smooth path; gimbal lock.
3. Section 3 (40 min): the three networks and the Procrustes optimum; read the percentiles.
4. Section 4 (20 min): five ways to average fifty noisy rotations.
5. TODO cells (35 min): a geodesic loss; the SE(3) log map.

- **Expect:** Rodrigues vs SciPy 8.9e-16; log(exp) 8.8e-14; near π the naive log is off by 1.3e-07, ours by 8.9e-16; SE(3) 4.4e-16. Jumps along the path: Euler 359.9°, quaternion 1.999, 6-D 0.0017. Test errors (mean, 99th percentile, worst, in degrees): Euler 9.29, 118.2, 177.2; quaternion 4.13, 26.5, 178.7; 6-D 1.81, 3.8, 5.8; Procrustes 1.20, 2.6, 3.4. Averages: naive Euler 174.4° off, random-sign quaternions 61.4°, sign-aligned 2.090°, chordal 2.036° (equal to SciPy's mean), Karcher 2.108°. Runtime about 25 seconds.
- **Common problems:** SciPy's quaternions are (x, y, z, w) unless `scalar_first=True`; "xyz" (fixed axes) and "XYZ" (moving axes) are different conventions; an SVD projection without the determinant fix can return a reflection.

### Quiz

1. How do you compute the geodesic distance between two rotations, and why not with arccos?
   - **Answer:** it is the angle of $R_1^\top R_2$. Use atan2 of the skew part's norm and (tr − 1)/2; arccos loses all accuracy for small angles.
2. Why does a network that outputs quaternions make some very large errors?
   - **Answer:** q and −q are the same rotation, so no continuous function picks one quaternion per rotation (Zhou et al. 2019). The network is continuous, so near the switching places its output is badly wrong.
3. How is the chordal mean of rotations computed?
   - **Answer:** take the SVD of the sum of the matrices, $U\Sigma V^\top$, and return $U\,\text{diag}(1, 1, \det UV^\top)\,V^\top$.

**Watch out:** "Quaternions solve every rotation problem for neural networks." They avoid gimbal lock and are compact, but the double cover (q and −q) makes them discontinuous as network outputs and dangerous to average. In the notebook the quaternion network's worst error was 178.7° against 5.8° for the 6-D output, and averaging quaternions with mixed signs landed 61.4° from the truth. Use a continuous output, and compute losses and averages on the group.

### Assignment 10 (due before session 11, 10 points)

1. By hand: exp of $[\omega]_\times$ for ω = (0, 0, π/2) and ω = (π, 0, 0); the distance between rotations by 10° about z and by 10° about x; the chordal mean of rotations by 10° and 50° about z. Check each in code. (3 points)
2. Rerun section 3 with noise 0.02, 0.05 and 0.1, and add a fourth network that outputs 9 numbers projected onto SO(3) by SVD. Report mean, 99th percentile and worst error for all four. (4 points)
3. Complete both TODO cells, and compare the geodesic-loss network's errors with the Frobenius-loss one. (3 points)

Hand in one PDF and your notebook.

### Sources

- Solà, Deray & Atchuthan 2018, A Micro Lie Theory for State Estimation in Robotics. https://arxiv.org/abs/1812.01537
- Zhou, Barnes, Lu, Yang & Li 2019, On the Continuity of Rotation Representations in Neural Networks, CVPR. https://arxiv.org/abs/1812.07035
- Hartley, Trumpf, Dai & Li 2013, Rotation Averaging, International Journal of Computer Vision 103(3). https://doi.org/10.1007/s11263-012-0601-0

## Session 11: Generative models on manifolds

**Goal:** students can sample from distributions on the sphere and train a Riemannian flow matching model whose samples stay on the manifold.

### Talking pointers

- **Open with:** "Earthquakes, cyclones and floods happen on the surface of a sphere. A generative model of where they happen should never put an event inside the Earth or above the sky."
- **Segment 1, say:** compare the area within 90° of a point on the sphere with πr², then show the vMF integral with and without sin θ.
- **Segment 2, say:** draw the north pole, a point on the equator and the meridian between them, and mark $x_t$ and $u_t$ at t = 0.5.
- **Segment 3, say:** show the two sample maps and the plot of MMD² against steps, then count the degrees of freedom of a 100-residue protein backbone.
- **Close with:** "Build the geometry into the paths, the velocities and the sampler, and the samples stay where the data live." Then set assignment 11.

### Segment 1 (6 min): distributions on the sphere

- The von Mises–Fisher (vMF) distribution (Fisher 1953) is the sphere's Gaussian: density proportional to $e^{\kappa\,\mu^\top x}$, with mean direction μ and concentration κ. On $S^2$ the constant is $\kappa/(4\pi\sinh\kappa)$, and on $S^2$ it can be sampled exactly by inverting a one-dimensional cumulative distribution function, or CDF (Mardia & Jupp 2000 treat directional statistics in depth).
- A density on a manifold is defined against the manifold's own volume. In spherical coordinates the area element is $\sin\theta\,d\theta\,d\varphi$: in the notebook the vMF density integrated to exactly 1 with it, and to 4.016 at κ = 10 without it.
- Wrapped distributions push a tangent-space density through $\exp_\mu$. The density on the sphere then gains the factor $r/\sin r$, the change of area of the exp map (a circle of radius r in the plane becomes one of length 2π sin r). Without it, the wrapped normal integrated to 0.920689 instead of 1.
- Mixtures of vMF distributions model clustered directions and locations.
- **Pause and try:** what fraction of the sphere lies within geodesic distance r = 90° of a point, and what does the flat formula πr² predict?
  - **Answer:** the cap has area 2π(1 − cos r) = 2π, half of 4π. The flat formula gives $\pi(\pi/2)^2 = 7.75$, 62% of the sphere: flat formulas overcount area on the sphere.

### Segment 2 (7 min): Riemannian flow matching

- Flow matching (Course 3 session 9) regresses a velocity field onto per-pair targets along chosen paths; Course 7 session 9 gave the overview for curved spaces. Riemannian flow matching (Chen & Lipman 2024) uses geodesics as the paths: $x_t = \exp_{x_0}(t\log_{x_0}x_1)$, with $x_0$ from a base distribution (here uniform on the sphere) and $x_1$ from the data.
- The target velocity is $u_t = \log_{x_t}(x_1)/(1 - t)$: it points from $x_t$ to $x_1$ along the geodesic and has length $d(x_0, x_1)$, so the point moves at constant speed. The notebook checks it against a finite difference (3.5e-10).
- The network outputs a vector in $\mathbb{R}^3$, projected onto the tangent plane, and the loss is $\|P_{x_t}v_\theta(x_t, t) - u_t\|^2$. No simulation is needed during training, and on simple geometries the targets are in closed form; for general geometries Chen & Lipman replace the geodesic distance by spectral distances.
- Sampling integrates the learned field with exp-map Euler steps, $x \leftarrow \exp_x(h\,v_\theta(x, t))$, so samples stay on the sphere up to rounding: 5.6e-15 after 100 steps.
- **Pause and try:** $x_0$ is the north pole and $x_1$ a point on the equator. At t = 0.5, where is $x_t$, and what is the target velocity?
  - **Answer:** at latitude 45° on the meridian through $x_1$; $u_t$ points along that meridian towards $x_1$ with length π/2 ≈ 1.571, the same at every t.

### Segment 3 (7 min): the Euclidean shortcut, diffusion on manifolds, and uses

- The shortcut, Euclidean flow matching in $\mathbb{R}^3$ followed by normalization, put 9.3% of samples more than 0.1 off the sphere before normalization, and its squared maximum mean discrepancy to held-out data (MMD², a kernel two-sample statistic; Gretton et al. 2012) was 4.5 times higher (0.00419 against 0.00093).
- Riemannian continuous normalizing flows (Mathieu & Nickel 2020) define flows as solutions of ordinary differential equations (ODEs) on the manifold and train them by likelihood, which needs the divergence on the manifold; flow matching avoids that cost.
- Riemannian score-based models (De Bortoli et al. 2022) run diffusion (Course 3 session 8) on compact manifolds with noise from Brownian motion on the manifold, with an emphasis on spherical earth and climate data. Course 13 session 7 covers machine-learning weather prediction.
- FrameDiff (Yim et al. 2023) treats each residue of a protein backbone as a rigid frame in SE(3) (session 10) and diffuses over frames; it generated designable monomers of up to 500 amino acids without a pretrained structure predictor.
- Robot and camera poses (SE(3)), molecular torsion angles (a torus) and directions (spheres) are other uses.
- **Pause and try:** a backbone of 100 residues is modelled as 100 frames in SE(3). How many degrees of freedom does a sample have?
  - **Answer:** each frame has 3 for rotation and 3 for translation, so 600.

### Lab guide (about 2.5 hours, notebook `s11_manifold_generative.ipynb`)

1. Section 1 (30 min): the vMF density and sampler, the volume-measure checks, the wrapped normal, and the synthetic event locations.
2. Section 2 (35 min): exp and log maps, the target checks, and Riemannian flow matching.
3. Section 3 (10 min): Euclidean flow matching in R³.
4. Section 4 (30 min): sampling with 5 to 100 steps, MMD² and the maps.
5. TODO cells (45 min): flow matching along chords; flow matching on the torus.

- **Expect:** vMF integrals 1.0000000000 with sin θ, 1.692, 4.016 and 12.549 without; wrapped normal 1.000000 with r/sin r, 0.920689 without. Target checks 3.5e-10, 4.2e-15 and 4.4e-15. MMD² (noise floor −0.00004, uniform 0.13770), Riemannian against Euclidean then normalized: 0.00639 and 0.02151 (5 steps), 0.00226 and 0.00975 (10), 0.00122 and 0.00558 (25), 0.00093 and 0.00419 (100). Euclidean samples off the sphere by 0.043 on average at 100 steps; Riemannian ones by at most 5.6e-15. Mass more than 45° from every centre: 1.47% (Riemannian), 1.03% (Euclidean), 0.13% (data). Runtime about 30 seconds.
- **Common problems:** evaluating the target at t = 1, where $\log_{x_t}(x_1)/(1 - t)$ is 0/0; forgetting to project the network output onto the tangent plane; using an MMD kernel that is not positive definite on the sphere; the safe choice here is $e^{\kappa x^\top y}$.

### Quiz

1. Write the path and the target velocity of Riemannian flow matching on the sphere.
   - **Answer:** $x_t = \exp_{x_0}(t\log_{x_0}x_1)$ and $u_t = \log_{x_t}(x_1)/(1 - t)$, a tangent vector of constant length $d(x_0, x_1)$.
2. Why does the vMF normalization need the factor sin θ?
   - **Answer:** densities on the sphere are per unit area, and the area element in spherical coordinates is $\sin\theta\,d\theta\,d\varphi$; without it the integral was 4.016 at κ = 10.
3. Name two problems with generating in $\mathbb{R}^3$ and normalizing at the end.
   - **Answer:** samples drift off the sphere, so model capacity and errors go into the radial direction, and normalization moves mass in ways the model never learned, which distorts the density (MMD² 4.5 times higher in the notebook).

**Watch out:** "You can generate in R³ and normalize at the end." You always get points on the sphere, and here the cluster masses were even fine, with less mass between clusters than the Riemannian model. But normalization hides the model's errors instead of fixing them: before it, 9.3% of samples were more than 0.1 off the sphere, and afterwards MMD² was 4.5 times worse. Likelihoods computed in R³ also do not transfer to the sphere.

### Assignment 11 (due before session 12, 10 points)

1. By hand: the fraction of the sphere within 60° of a point; the vMF constant $\kappa/(4\pi\sinh\kappa)$ at κ = 2; the target $u_t$ at t = 0.25 for the pause-and-try example. Check each in code. (3 points)
2. Train both models for 1,000, 3,000 and 10,000 steps with three seeds each. Plot MMD² against training steps with error bars. Does the gap between the geometries close as training grows? (4 points)
3. Complete both TODO cells, and explain where the chords of the first one pass and why that is hard for the network. (3 points)

Hand in one PDF and your notebook.

### Sources

- Chen & Lipman 2024, Flow Matching on General Geometries, ICLR. https://arxiv.org/abs/2302.03660
- De Bortoli, Mathieu, Hutchinson, Thornton, Teh & Doucet 2022, Riemannian Score-Based Generative Modelling, NeurIPS. https://arxiv.org/abs/2202.02763
- Mathieu & Nickel 2020, Riemannian Continuous Normalizing Flows, NeurIPS. https://arxiv.org/abs/2006.10605
- Yim et al. 2023, SE(3) Diffusion Model with Application to Protein Backbone Generation, ICML. https://arxiv.org/abs/2302.02277
- Fisher 1953, Dispersion on a Sphere, Proceedings of the Royal Society of London A 217.
- Mardia & Jupp 2000, Directional Statistics (Wiley).
- Gretton, Borgwardt, Rasch, Schölkopf & Smola 2012, A Kernel Two-Sample Test, Journal of Machine Learning Research 13. https://jmlr.org/papers/v13/gretton12a.html

## Session 12: Mixed curvature, choosing a geometry, and the capstone

**Goal:** students can embed data in product spaces of mixed curvature, diagnose the geometry a dataset needs, and plan a capstone that compares geometries fairly.

### Talking pointers

- **Open with:** "Real graphs are not pure trees or pure cycles. A road network has grids, a family has trees, a social network has both. Why choose one curvature when you can combine several?"
- **Segment 1, say:** write $d^2 = d_{\mathbb{H}}^2 + d_{\mathbb{E}}^2$ and do the 3–4–5 example, then show the plot of all 18 runs.
- **Segment 2, say:** run the triangle test by hand on a star and on a 6-cycle, then show the table of δ and the test for each part.
- **Segment 3, say:** put the six numbers of the two best products on the board and ask whether one is clearly better; then walk through the capstone checklist.
- **Close with:** "Diagnose first, match budgets, keep a strong Euclidean baseline, and report every run, including the ones where curvature did not help." Then set assignment 12, which is due with the capstone.

### Segment 1 (7 min): product manifolds and learnable curvature

- A product manifold $M_1 \times M_2 \times \dots$ gives each data point one coordinate block in every factor; each factor has constant curvature (spherical, flat or hyperbolic), but the product as a whole does not (Gu et al. 2019).
- Geodesics move in all factors at once, so distances add in squares: $d^2 = \sum_i d_i^2$. A tree-like part can use a hyperbolic factor while a cycle uses a spherical or flat one.
- Gu et al. learned the embedding and each factor's curvature together with Riemannian optimization. On a Facebook social network, product spaces reduced distortion by 32.55% compared with single spaces.
- Curvature can also be a parameter that passes smoothly through zero: the κ-stereographic model covers spheres, the plane and hyperbolic space in one formula. It is used in graph networks (Bachmann et al. 2020) and in variational autoencoders (VAEs) with product latent spaces (Skopek et al. 2020), and geoopt implements it (the notebook's NOT RUN cell).
- In the notebook, with a learned radius per factor, $\mathbb{H}^2 \times \mathbb{E}^1$ reached average distortion 0.0592, against 0.0929 for $\mathbb{E}^3$.
- **Pause and try:** two nodes are 3 apart in the $\mathbb{H}^2$ factor and 4 apart in the $\mathbb{E}^1$ factor. How far apart are they in the product?
  - **Answer:** $\sqrt{3^2 + 4^2} = 5$, not 7: the product geodesic moves in both factors at once.

### Segment 2 (7 min): diagnosing the geometry

- Trees have δ = 0; a cycle whose length is a multiple of 4 reaches the largest relative value, $2\delta/\text{diameter} = 1$ (session 8), and other long cycles come close.
- The triangle test, the idea behind Gu et al.'s curvature estimate: for a triangle a, b, c with m the midpoint of b and c, the parallelogram law gives the flat-space median $\sqrt{\tfrac12(d(a,b)^2 + d(a,c)^2) - \tfrac14 d(b,c)^2}$. A longer true median suggests positive curvature, a shorter one negative. Gu et al. used such estimates to choose the factors and their dimensions.
- In the notebook the test read +0.0252 on the sphere, 0 in the plane and −0.0182 in the hyperbolic plane; on the graph, −0.174 for the tree and +0.283 for the cycle.
- The tests are hints, not proofs: the 4 × 4 grid also gave $2\delta/\text{diameter} = 1$ and a positive mean (+0.126) with both signs, because grid distances count city blocks.
- Another diagnostic is a trial embedding: the distortion of pairs inside each part. $\mathbb{H}^2$ fitted the tree (0.087) but not the cycle (0.249).
- **Pause and try:** in a star, b and c are two leaves (distance 2), m is the centre and a is a third leaf. In a 6-cycle with nodes 0 to 5, take b = 0, c = 2, m = 1 and a = 4. What does the test say in each?
  - **Answer:** star: d(a, m) = 1 against a flat value of $\sqrt{(4 + 4)/2 - 1} = 1.73$, ratio − 1 = −0.42, negative. Cycle: d(a, m) = 3 against the same 1.73, ratio − 1 = +0.73, positive.

### Segment 3 (6 min): practical advice and the capstone

- Numerical precision: use float64 near the boundary of the ball, clip tangent vectors, and check constraints. Lorentz coordinates in the notebook grew to $3.3 \times 10^4$, with constraint errors of 3.0e-08.
- Optimization: the notebook uses Riemannian Adam, with momentum moved between tangent spaces (session 5). Even so, factors can collapse: the $S^1$ radius shrank to 0.65 and 0.45 in two of three seeds, and $S^2$ learned a radius of about 25, making it almost flat.
- Strong baselines: Katsman & Gilbert (2025) found that well-trained Euclidean models often match hyperbolic graph models. Give the Euclidean model the same dimension, tuning and steps (Course 1 session 9).
- Report every run with its spread. The capstone (see the syllabus) asks for this on data whose geometry matters, with a Euclidean baseline and several seeds.
- **Pause and try:** $\mathbb{H}^2 \times S^1$ gave 0.0618, 0.0678 and 0.0717; $\mathbb{H}^2 \times \mathbb{E}^1$ gave 0.0550, 0.0638 and 0.0587. Is one clearly better?
  - **Answer:** the means are 0.0671 and 0.0592, and the difference, 0.0079, is about two standard errors (0.004). The ranges overlap (0.0618 < 0.0638), so it is suggestive, not settled; run more seeds.

### Lab guide (about 2.5 hours, notebook `s12_mixed_curvature.ipynb`)

1. Section 1 (10 min): build and draw the graph.
2. Section 2 (35 min): δ and the triangle test, first on random triangles in the three model spaces, then on each part.
3. Section 3 (35 min): factor distances, Riemannian gradients, exp maps and Riemannian Adam, with the gradient checks.
4. Section 4 (30 min): 18 embeddings; read the per-part distortions and the radii.
5. TODO cells and section 7 (40 min): four dimensions; a real networkx graph; the capstone checklist.

- **Expect:** triangle test: sphere +0.0252, plane 0, hyperbolic −0.0182; tree −0.174 (66% negative), cycle +0.283 (27% positive), grid +0.126; $2\delta/\text{diameter}$ 0.000, 1.000 and 1.000. Riemannian gradients match finite differences to 8 digits. Mean average distortion (3 seeds): $\mathbb{E}^2$ 0.1253, $\mathbb{H}^2$ 0.0756, $S^2$ 0.1258, $\mathbb{E}^3$ 0.0929, $\mathbb{H}^2 \times S^1$ 0.0671, $\mathbb{H}^2 \times \mathbb{E}^1$ 0.0592; worst case 2.56 for $\mathbb{E}^3$ and 2.18 for $\mathbb{H}^2 \times \mathbb{E}^1$. Tree pairs: 0.149 in $\mathbb{E}^3$, 0.063 in $\mathbb{H}^2 \times \mathbb{E}^1$. Runtime about 35 seconds.
- **Common problems:** adding factor distances instead of their squares; a learning rate that lets a factor's radius collapse; judging a geometry from one seed.

### Quiz

1. How are distances combined in a product manifold, and why?
   - **Answer:** $d^2 = \sum_i d_i^2$, because a product geodesic moves along a geodesic in every factor at once.
2. A triangle test gives a median shorter than the flat-space value. What does that suggest?
   - **Answer:** negative curvature, as in trees and hyperbolic space; a longer median suggests positive curvature.
3. Why run every geometry with several seeds?
   - **Answer:** in the notebook the seed-to-seed spread was as large as the gap between the two best products, and a factor collapsed in some seeds but not others.

**Watch out:** "A more exotic geometry means a better model." In the notebook the sphere learned to be almost flat, the circle factor collapsed in two of three seeds, and a plain extra dimension ($\mathbb{H}^2 \times \mathbb{E}^1$) beat $\mathbb{H}^2 \times S^1$. The hyperbolic factor did help, because the graph contains a large tree, which the diagnostics showed. Let diagnostics and fair experiments choose the geometry, and report it when the simple one wins.

### Assignment 12 (due with the capstone, 10 points)

1. By hand: the product distance for factor distances 5 and 12; the triangle test on the path 1–2–3–4–5 with b = 1, c = 3, m = 2 and a = 5; the mean, standard deviation and standard error of 0.0550, 0.0638 and 0.0587. Check each in code. (3 points)
2. Complete both TODO cells: the four-dimensional comparison, and the diagnosis and embedding of a graph that ships with networkx. Did the diagnostics predict the winner? (4 points)
3. A one-page capstone plan: data, diagnostics, the curved model and its Euclidean baseline with matched budgets, metrics, seeds, and the result that would make you conclude the curved model did not help. (3 points)

Hand in one PDF and your notebook.

### Sources

- Gu, Sala, Gunel & Ré 2019, Learning Mixed-Curvature Representations in Product Spaces, ICLR. https://openreview.net/forum?id=HJxeWnCcF7
- Bachmann, Bécigneul & Ganea 2020, Constant Curvature Graph Convolutional Networks, ICML. https://arxiv.org/abs/1911.05076
- Skopek, Ganea & Bécigneul 2020, Mixed-curvature Variational Autoencoders, ICLR. https://arxiv.org/abs/1911.08411
- Bécigneul & Ganea 2019, Riemannian Adaptive Optimization Methods, ICLR. https://arxiv.org/abs/1810.00760
- Katsman & Gilbert 2025, Shedding Light on Problems with Hyperbolic Graph Learning, Transactions on Machine Learning Research. https://arxiv.org/abs/2411.06688

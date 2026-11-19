# Course 9 notebooks: Mathematics and AI

One notebook per session. Open them in Kaggle Notebooks or Google Colab.

- Every Python cell without a NOT RUN label was run once on a CPU on 17 November 2026 (Python 3, NumPy 2.5, scikit-learn 1.9, PyTorch 2.15).
- Sessions 1 to 8 and 12 are fully runnable: groups and actions, characters and projectors, steerable kernel bases, grokking with Fourier analysis, a category of layers, lenses as backprop, weight sharing derived from symmetry, sheaf diffusion, and an evolve-and-evaluate search for cap sets.
- **Lean code (sessions 9 and 11) was NOT compiled.** It follows Lean 4 and Mathlib conventions as of 2026, but Mathlib renames lemmas often. Compile every snippet before teaching it, and treat any error as part of the lab.
- Sessions 10 and 11 give runnable models of the ideas (proof search, pass@k, counterexample search for wrong formalizations). The parts that need a prover model, LeanDojo or a language model are labelled NOT RUN.
- Session 4 uses p = 47 and a small network so that grokking appears in about a minute on a CPU. The paper it follows uses p = 113 and a one-layer transformer.
- Session 12 searches in dimension 5 with random edits in place of a language model. In the run recorded here, random search with the same budget did as well as the evolutionary loop; the notebook says so.

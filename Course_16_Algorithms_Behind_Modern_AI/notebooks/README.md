# Course 16: Algorithms Behind Modern AI: notebooks

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, NumPy 2.5, SciPy 1.18, scikit-learn 1.9 and matplotlib 3.11, plus PyTorch 2.15 in sessions 4 and 6, where it only checks our own gradients and our own CTC loss), and the outputs are saved in the notebooks.
- Operation counts (multiply–adds, probes, table cells, distance computations, cache hits) are exact, and a second, independent run reproduced every printed number. Timings do not reproduce: they come from one run on a shared server CPU, so treat them as rough and expect different numbers on your machine.
- The data are synthetic or small: made-up words with a Zipf distribution, short English and Bangla texts written into the notebooks, random vectors with planted neighbours, simulated request traces, and scikit-learn's digits in session 12. Each notebook finishes in under a minute on a CPU. The numbers show how each algorithm behaves; they are not benchmark results.
- Nothing extra needs installing for the runnable cells on Google Colab or Kaggle.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a library, a model download or a GPU (the table below says what each needs). They were written from the libraries' documentation and have not been executed, so run each one before recording.
- The batching experiments in session 11 are a simulation, not measurements of a real server.
- Results that went against expectation are stated in each notebook's "What to notice" cell and in the course document. Examples: signed hashing helped the classifier only at the two smallest table sizes (session 2); the two tokenizer encoders differed on only 1.4% of word types (session 3); a wider beam did not always find the exact best string, and one sampling test gave a p-value of 0.047 (session 7); no LSH setting reached a recall of 0.9, and the pure-Python k-d tree was slower than NumPy brute force from 16 dimensions (session 9); HNSW's layers saved only a few dozen distance computations per query, and the simple "M nearest" link rule never reached a recall of 0.99 (session 10); first-in-first-out and random eviction were almost as good as LRU, and far behind the optimal rule (session 11); a shuffle buffer of 512 gave a slightly higher accuracy than a full shuffle, within the spread over seeds (session 12).

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_counting_cost.ipynb](s01_counting_cost.ipynb) | Counting cost: arrays, memory and Big-O for models | 11 | nothing (all cells run) |
| 2 | [s02_hashing.ipynb](s02_hashing.ipynb) | Hashing: dictionaries, the hashing trick and Bloom filters | 9 | nothing (all cells run) |
| 3 | [s03_tokenizer_algorithms.ipynb](s03_tokenizer_algorithms.ipynb) | Tokenizers: byte-pair encoding with heaps, linked lists and tries | 10 | the tokenizers and tiktoken libraries (pip install tokenizers tiktoken; tiktoken downloads its vocabulary on first use) |
| 4 | [s04_computation_graphs.ipynb](s04_computation_graphs.ipynb) | Computation graphs: topological sort and automatic differentiation | 8 | nothing (all cells run) |
| 5 | [s05_edit_distance.ipynb](s05_edit_distance.ipynb) | Dynamic programming I: edit distance and alignment | 9 | nothing (all cells run) |
| 6 | [s06_viterbi_ctc.ipynb](s06_viterbi_ctc.ipynb) | Dynamic programming II: Viterbi, the forward algorithm and CTC | 11 | the sentencepiece library and a corpus file (pip install sentencepiece; put your own text in corpus.txt) |
| 7 | [s07_decoding_search.ipynb](s07_decoding_search.ipynb) | Decoding: heaps, beam search and sampling | 10 | nothing (all cells run) |
| 8 | [s08_constrained_decoding.ipynb](s08_constrained_decoding.ipynb) | Automata and tries: constrained decoding and structured outputs | 11 | `pip install outlines transformers torch` and a model download (run on Kaggle or Colab; a GPU helps). |
| 9 | [s09_trees_and_lsh.ipynb](s09_trees_and_lsh.ipynb) | Nearest neighbours I: k-d trees, LSH and MinHash | 10 | `pip install datasketch` (a library that is not installed here). |
| 10 | [s10_vector_indexes.ipynb](s10_vector_indexes.ipynb) | Nearest neighbours II: HNSW, IVF and product quantization | 10 | `pip install faiss-cpu hnswlib` (two libraries that are not installed here). |
| 11 | [s11_caches_queues_batching.ipynb](s11_caches_queues_batching.ipynb) | Serving models: caches, queues and batching | 10 | vllm, a GPU and a model download (run it on Kaggle or Colab) |
| 12 | [s12_sampling_and_shuffling.ipynb](s12_sampling_and_shuffling.ipynb) | Randomized algorithms for data pipelines, and the capstone | 10 | tensorflow (a library that this course does not install) |

# Course 16: Algorithms Behind Modern AI

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on the data structures and algorithms inside modern AI systems: arrays and cost, hashing, tokenizers, computation graphs, dynamic programming, decoding, automata, nearest-neighbour search, caches and queues, and randomized algorithms. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Students who have taken a data structures course often ask where heaps, tries, hash tables and dynamic programming are used in AI. The answer is: everywhere. A tokenizer is a priority queue and a trie. Backpropagation is a topological sort. The loss that trains a speech recognizer is a dynamic program. A vector database is a graph search. A model server is a cache and a queue. This course takes one structure per session, starts from what a second-year student already knows, builds the real thing from scratch in a notebook, and counts what it costs. The other courses teach what these systems are for; this one teaches how they work inside, and it prepares students for the coding rounds of Course 15.

Prerequisites: a first course in data structures and algorithms (lists, stacks, queues, hash tables, trees, graphs, sorting and Big-O notation), and Python at the level of Course 1. No deep learning is needed to follow the algorithms. Course 1 sessions 5 and 6, or Course 4 session 1, help with the models that are mentioned.

Capstone: build a small search system over a collection of texts that you are allowed to use (your course notes, or a Bangla and English collection), using at least four structures from the course: for example a tokenizer (session 3), near-duplicate removal (session 9), a vector index (session 10), a cache (session 11), a constrained answer format (session 8) and an evaluation with edit distance or ROUGE-L (session 5). For each part, state its cost in Big-O notation and measure it, and present the system in a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a working system on real text (20); correct use of at least four structures (25); cost stated and measured for each part, with exact counts where possible (25); an honest evaluation of quality, including failures (15); clarity of the report and video (15).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English.

### Sessions

1. **Counting cost: arrays, memory and Big-O for models.** Students can count the operations and memory of array code and of model layers, explain contiguous storage, strides, views and amortized appends, and say when a sparse format wins.
   - Read: Harris et al. 2020, Array programming with NumPy. Nature 585(7825), 357–362; Drepper 2007, What Every Programmer Should Know About Memory
   - Lab: about 2 hours, notebook `s01_counting_cost.ipynb`
2. **Hashing: dictionaries, the hashing trick and Bloom filters.** Students can explain how hash tables give expected constant-time lookups, map a huge vocabulary into fixed memory with the hashing trick, and size a Bloom filter and a count–min sketch for a target error.
   - Read: Weinberger et al. 2009, Feature Hashing for Large Scale Multitask Learning (ICML 2009); Bloom 1970, Space/time trade-offs in hash coding with allowable errors. Communications of the ACM 13(7), 422–426
   - Lab: about 2 hours, notebook `s02_hashing.ipynb`
3. **Tokenizers: byte-pair encoding with heaps, linked lists and tries.** Students can implement BPE training two ways, explain with data structures why one is far faster, and encode text both by replaying merges and by longest match in a trie.
   - Read: Sennrich, Haddow & Birch 2016, Neural Machine Translation of Rare Words with Subword Units (ACL 2016); Zouhar et al. 2023, A Formal Perspective on Byte-Pair Encoding (Findings of ACL 2023)
   - Lab: about 2 hours, notebook `s03_tokenizer_algorithms.ipynb`
4. **Computation graphs: topological sort and automatic differentiation.** Students can represent a model as a directed acyclic graph, order it with Kahn's algorithm and with depth-first search, run reverse-mode differentiation as one backward sweep, and apply simple graph optimizations.
   - Read: Kahn 1962, Topological sorting of large networks. Communications of the ACM 5(11), 558–562; Baydin, Pearlmutter, Radul & Siskind 2018, Automatic Differentiation in Machine Learning: a Survey (JMLR)
   - Lab: about 2.5 hours, notebook `s04_computation_graphs.ipynb`
5. **Dynamic programming I: edit distance and alignment.** Students can set up a dynamic program (subproblems, recurrence, order, answer), compute edit distance in quadratic time with a backtrace or in linear memory, and use the same table for error rates and sequence alignment.
   - Read: Levenshtein 1966, Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady 10(8), 707–710; Wagner & Fischer 1974, The string-to-string correction problem. Journal of the ACM 21(1), 168–173
   - Lab: about 2.5 hours, notebook `s05_edit_distance.ipynb`
6. **Dynamic programming II: Viterbi, the forward algorithm and CTC.** Students can find the best path and the total probability over exponentially many paths with one table, implement Viterbi and the forward algorithm in log space, and compute the CTC loss from scratch.
   - Read: Viterbi 1967, Error bounds for convolutional codes and an asymptotically optimum decoding algorithm. IEEE Transactions on Information Theory 13(2), 260–269; Rabiner 1989, A tutorial on hidden Markov models and selected applications in speech recognition. Proceedings of the IEEE 77(2), 257–286
   - Lab: about 2 hours, notebook `s06_viterbi_ctc.ipynb`
7. **Decoding: heaps, beam search and sampling.** Students can implement greedy, beam and exact search for a language model, pick the top-k or top-p tokens with selection algorithms, and say what each decoding rule optimizes.
   - Read: Stahlberg & Byrne 2019, On NMT Search Errors and Model Errors: Cat Got Your Tongue? (EMNLP 2019); Meister, Cotterell & Vieira 2020, If Beam Search is the Answer, What was the Question? (EMNLP 2020)
   - Lab: about 2 hours, notebook `s07_decoding_search.ipynb`
8. **Automata and tries: constrained decoding and structured outputs.** Students can build a trie and a finite automaton, use them to mask a model's next-token choices so that the output always fits a list or a pattern, and explain the cost and the limits.
   - Read: Willard & Louf 2023, Efficient Guided Generation for Large Language Models; De Cao, Izacard, Riedel & Petroni 2021, Autoregressive Entity Retrieval (ICLR 2021)
   - Lab: about 2.5 hours, notebook `s08_constrained_decoding.ipynb`
9. **Nearest neighbours I: k-d trees, LSH and MinHash.** Students can explain why exact nearest-neighbour search fails in high dimensions, build locality-sensitive hash indexes for cosine and Jaccard similarity, and find near-duplicate documents in a corpus.
   - Read: Bentley 1975, Multidimensional binary search trees used for associative searching. Communications of the ACM 18(9), 509–517; Friedman, Bentley & Finkel 1977, An algorithm for finding best matches in logarithmic expected time. ACM Transactions on Mathematical Software 3(3), 209–226
   - Lab: about 2.5 hours, notebook `s09_trees_and_lsh.ipynb`
10. **Nearest neighbours II: HNSW, IVF and product quantization.** Students can build a graph index and a quantized index for vector search, measure recall against work and memory, and choose index settings for a retrieval system.
   - Read: Malkov & Yashunin 2020, Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (IEEE TPAMI); Kleinberg 2000, The small-world phenomenon: an algorithmic perspective (STOC 2000), 163–170
   - Lab: about 2.5 hours, notebook `s10_vector_indexes.ipynb`
11. **Serving models: caches, queues and batching.** Students can explain the KV cache as memoization, implement an LRU cache and a prefix tree that shares cached prompts, and simulate batching policies for a model server.
   - Read: Kwon et al. 2023, Efficient Memory Management for Large Language Model Serving with PagedAttention (SOSP 2023); Yu et al. 2022, Orca: A Distributed Serving System for Transformer-Based Generative Models (OSDI 2022), 521–538
   - Lab: about 2 hours, notebook `s11_caches_queues_batching.ipynb`
12. **Randomized algorithms for data pipelines, and the capstone.** Students can sample uniformly from a stream, shuffle correctly, draw from a large discrete distribution in constant time, and plan a capstone that combines the course's data structures.
   - Read: Vitter 1985, Random sampling with a reservoir. ACM Transactions on Mathematical Software 11(1), 37–57; Vose 1991, A linear algorithm for generating random numbers with a given distribution. IEEE Transactions on Software Engineering 17(9), 972–975
   - Lab: about 2 hours, notebook `s12_sampling_and_shuffling.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab. In this course, work the small example of each notebook's first section by hand on camera before showing the code.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. Operation counts are exact and reproduce on every run. Timings come from one run on a shared server CPU, so expect different numbers on your machine.
- **Sources:** read the papers cited for a session before recording it. Statements about current tools were checked in November 2026; check their documentation again before recording.
- **Dates:** written in November 2026.

## Session 1: Counting cost: arrays, memory and Big-O for models

**Goal:** students can count the operations and memory of array code and of model layers, explain contiguous storage, strides, views and amortized appends, and say when a sparse format wins.

### Talking pointers

- **Open with:** "You met Big-O on sorting and searching. Today we use it on models: you will say what an attention layer costs before you run it, and see why the same count can hide a factor of a thousand."
- **Segment 1, say:** count the multiply–adds of a 2 × 3 by 3 × 2 product on the board, then show the attention table.
- **Segment 2, say:** draw one buffer of 12 numbers and read it with two pairs of strides, then show the plot of copies per append.
- **Segment 3, say:** write the three CSR arrays of the 3 × 4 matrix on the board, then show bytes against density.
- **Close with:** "Count first, then measure: the count gives the growth, the measurement the constant." Then set assignment 1.

### Segment 1 (6 min): Big-O on tensors

- Our unit is one **multiply–add**, $s \leftarrow s + ab$. An $m \times n$ matrix times an $n \times p$ matrix costs $mnp$; a dense layer on a batch of $B$ inputs costs $B\,d_{in}d_{out}$.
- Self-attention on $n$ tokens of width $d$ (Course 4 session 1): $n^2$ scores of $d$ terms each, then $n$ weighted sums over $n$ values of width $d$, together $2n^2 d$; the four projections add $4nd^2$. Vaswani et al. (2017, Table 1) give $O(n^2 d)$ per layer.
- Doubling $n$ multiplies the score entries by 4. In the lab ($d = 64$) the $n^2$ part is 33.3% of the work at $n = 64$ and 97.0% at $n = 4{,}096$.
- Big-O describes growth and hides constants. Two 120 × 120 products both do 1,728,000 multiply–adds, yet Python loops took about 1,500 times as long as NumPy in the lab. Course 2 session 1 shows how to vectorize; Course 11 session 1 goes from counts to hardware limits.
- **Pause and try:** one attention head has $n = 1{,}000$ tokens and $d = 512$. How many multiply–adds do the scores and weighted sums need? What changes at $n = 2{,}000$?
  - **Answer:** $2 \times 1{,}000^2 \times 512 \approx 1.02 \times 10^9$. At $n = 2{,}000$ this is four times larger; the projections ($4nd^2 \approx 1.05 \times 10^9$) only double.

### Segment 2 (7 min): how arrays live in memory

- A NumPy array is one **contiguous buffer** plus a shape, a dtype and **strides**: the bytes to jump for one step along each axis (Harris et al. 2020). PyTorch tensors work the same way.
- A transpose swaps the strides; a slice changes the start and the strides. Both are **views**: $O(1)$, no data copied. A reshape of a transposed array, or indexing with a list, must **copy**, which is why `view` fails after `transpose` in PyTorch (Course 15 sessions 3 and 5).
- Processors load memory in cache lines, typically 64 bytes, so reading along the buffer is cheaper than jumping across it (Drepper 2007). In the lab, 64 million additions took about four times as long across a 256 MB array as along it.
- A Python list is a **dynamic array** of pointers with spare capacity. If the capacity grows by a constant factor, $n$ appends copy $O(n)$ elements in total: an append is $O(1)$ **amortized**, although a single one can cost $O(n)$ (Cormen et al. 2022). CPython grows by about one eighth: 100,000 appends copy at most 798,128 elements, under $9n$.
- `np.append` returns a new array every time, so $n$ appends copy $n(n-1)/2$ elements, $O(n^2)$. Append to a list and convert once.
- **Pause and try:** `a` is a 3 × 4 array of 8-byte integers. What are the strides of `a`, `a.T` and `a[:, ::2]`, and which of them copy data?
  - **Answer:** (32, 8), (8, 32) and (32, 16). None copies: all are views of the same 96 bytes.

### Segment 3 (7 min): sparse data

- Bag-of-words matrices, graph adjacency matrices and one-hot vectors are almost all zeros. **COO** (coordinate format) stores a (row, column, value) triple per non-zero. **CSR** (compressed sparse row) stores three arrays: `data`, `indices` (each value's column) and `indptr` (where each row starts).
- One counting sort turns COO into CSR in $O(\text{nnz} + \text{rows})$; nnz is the number of non-zeros. A sparse matrix–vector product costs nnz multiply–adds: 100,000 in the lab, against 10,000,000 dense.
- Sparse storage is not free: each non-zero carries a 4-byte column index, so CSR is smaller only below a density of about 2/3 with float64 values and 1/2 with float32. Course 11 session 5 times sparse products for pruned weights.
- An embedding layer multiplies a one-hot vector by a $V \times d$ matrix: $V \cdot d$ multiply–adds as a product, but **indexing** copies one row, $O(d)$. In the lab: 3,200,000 multiply–adds against 64 numbers copied.
- **Pause and try:** a float32 bag-of-words matrix has 10,000 documents, 50,000 words and 100 non-zeros per row. How many bytes in CSR with 32-bit indices, and how many dense?
  - **Answer:** nnz = 1,000,000, so CSR needs $8 \times 10^6 + 4 \times 10{,}001 \approx 8.04$ MB. Dense needs $10{,}000 \times 50{,}000 \times 4 = 2$ GB, about 250 times more.

### Lab guide (about 2 hours, notebook `s01_counting_cost.ipynb`)

1. Section 1 (10 min): $AB$ and $BA$ by hand, counting multiplications.
2. Sections 2–3 (30 min): the counter against $mnp$; attention's count and time.
3. Sections 4–5 (25 min): predict strides and "view or copy?"; traversal timings.
4. Section 6 (20 min): capacity jumps, three growth rules, `np.append`.
5. Sections 7–9 (25 min): CSR by hand; bytes against density; embedding lookup.
6. TODO cells (20 min): growth factors; CSR to CSC.

- **Expect:** $AB$ = [[5, 11], [14, 23]] with 12 multiply–adds, $BA$ with 18. Dense layer 3,211,264; the 120 × 120 product took 92.4 ms in loops and 0.063 ms in NumPy (timings from the saved run; they vary). Attention: 1,572,864 multiply–adds at $n = 64$, 2,214,592,512 at $n = 4096$; log–log slope 1.91 for the count, 1.99 for the time. Traversal across the buffer: about 2 times slower at 16 and 64 MB, 4.3 times at 256 MB. List capacities 4, 8, 16, 24, 32, 40, 52, … Copies for 100,000 appends: 131,071 (doubling), 798,128 (CPython rule), 4,999,950,000 (grow by one). Small matrix: data [5, 2, 3, 1, 4], indices [0, 3, 2, 0, 3], indptr [0, 2, 3, 5]. Large matrix: 1,208,004 bytes in CSR against 80,000,000 dense; equal at density 0.6666 (float64) and 0.4999 (float32). Runtime about 12 seconds.
- **Common problems:** importing NumPy before setting the thread variables; trusting a single timing; expecting `np.append` to work in place.

### Quiz

1. An attention layer takes 40 ms for 1,000 tokens, where the $n^2$ part dominates. About how long for 4,000 tokens?
   - **Answer:** about 640 ms: four times the tokens gives sixteen times the score entries.
2. Why is `list.append` $O(1)$ amortized but not $O(1)$ in the worst case?
   - **Answer:** an append that finds the list full may copy all $n$ elements. Because the capacity grows by a constant factor, $n$ appends copy $O(n)$ elements in total, so the average is constant.
3. A float32 matrix has 30% non-zeros. Is CSR with 32-bit indices smaller than dense storage?
   - **Answer:** yes: $0.3 \times 8 = 2.4$ bytes per entry against 4. CSR stops being smaller at about 50% density.

**Watch out:** "The algorithm with the better Big-O is the faster one." Big-O compares growth for large inputs; it ignores the constant, the memory layout and the sizes you really have. In the lab, two $O(n^3)$ products differed by a factor of about 1,500, and two loops with the same additions by a factor of four, because of the order in which they read memory. Count to choose an algorithm, then measure at your sizes.

### Assignment 1 (due before session 2, 10 points)

1. By hand, find the multiply–adds of one attention head for $n = 512$ and $n = 2{,}048$ with $d = 256$, and the $n$ at which the $n^2$ part equals the projections. Check with the notebook's counter. (3 points)
2. Complete both TODO cells. Report copies and unused slots for the four growth factors, explain the trade-off in three sentences, and check your CSC arrays against SciPy. (4 points)
3. Build the sentence-by-word count matrix of your own text (at least 200 sentences, Bangla or English) in COO and CSR with the notebook's functions. Report its density, the CSR and dense bytes, and the multiply–adds of one matrix–vector product in both formats. (3 points)

Hand in one PDF and your notebook.

### Sources

- Harris et al. 2020, Array programming with NumPy. Nature 585(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2
- Cormen, Leiserson, Rivest & Stein 2022, Introduction to Algorithms, 4th edition. MIT Press.
- Drepper 2007, What Every Programmer Should Know About Memory. https://www.akkadia.org/drepper/cpumemory.pdf
- Vaswani et al. 2017, Attention Is All You Need (NeurIPS 2017). https://arxiv.org/abs/1706.03762
- SciPy documentation, Sparse arrays (`scipy.sparse`; CSR format). https://docs.scipy.org/doc/scipy/reference/sparse.html

## Session 2: Hashing: dictionaries, the hashing trick and Bloom filters

**Goal:** students can explain how hash tables give expected constant-time lookups, map a huge vocabulary into fixed memory with the hashing trick, and size a Bloom filter and a count–min sketch for a target error.

### Talking pointers

- **Open with:** "A tokenizer finds a word among 50,000 entries without comparing it with 50,000 strings. Today we open the hash table that does this, then use hashing to remember a billion items in a few bits each."
- **Segment 1, say:** insert 10, 18, 3, 7 and 15 into eight slots on the board.
- **Segment 2, say:** show the plot of accuracy against the number of columns.
- **Segment 3, say:** draw 16 bits, add two entries with two hash functions each, and query a third.
- **Close with:** "Hashing gives up exactness in a controlled way: you choose the memory, and a formula tells you the error." Then set assignment 2.

### Segment 1 (6 min): hash tables

- A **hash table** keeps keys in an array of $M$ **slots**. A **hash function** $h$ turns a key into an integer; $h(\text{key}) \bmod M$ is its home slot. Two keys with the same home slot **collide**. A tokenizer's vocabulary is such a table, from token to id.
- **Chaining** keeps a list per slot. **Open addressing** keeps every key in the array and tries other slots after a collision; **linear probing** tries the next one. CPython's `dict` is a resizable hash table with open addressing, kept at most two-thirds full (CPython documentation and source code).
- With **load factor** $\alpha = n/M$, linear probing takes about $\frac12\big(1 + \frac{1}{1-\alpha}\big)$ probes for a successful search and $\frac12\big(1 + \frac{1}{(1-\alpha)^2}\big)$ for an unsuccessful one (Knuth 1998): 1.5 and 2.5 at $\alpha = 0.5$, but 5.5 and 50.5 at 0.9. Lookups are **expected** $O(1)$ while the table grows before it fills.
- The **worst case** is $O(n)$. In the lab, at load 0.1, a bad hash function (the sum of the bytes) needed 1,382.5 probes per successful lookup; FNV-1a needed 1.057.
- Python **salts** string hashes with a random secret per process, so an attacker cannot prepare keys that all collide (CPython documentation). `hash("a")` changes between runs: never store it; use `hashlib` or `zlib.crc32`.
- **Pause and try:** a linear-probing table has 1,000 slots. How many probes does an unsuccessful search need on average with 500 keys, and with 900?
  - **Answer:** 2.5 and 50.5. Less than twice the keys, twenty times the work.

### Segment 2 (7 min): the hashing trick

- A bag-of-words model needs a dictionary from word to column. The **hashing trick** drops it: the column is $h(\text{word}) \bmod m$ for a fixed $m$ (Weinberger et al. 2009). Memory stops growing with the vocabulary.
- The price is collisions: $n$ words in $m$ columns give about $n^2/(2m)$ colliding pairs. In the lab, 16,325 words in 16,384 columns left only 36.8% of the words alone in a column, yet accuracy was 0.932 against 0.939 with the full vocabulary. The signal is spread over many words, so one collision damages little.
- A second hash gives each word a **sign**, $+1$ or $-1$. Colliding words then cancel on average: the inner product of two hashed vectors is an **unbiased** estimate of the true one. Without signs it is too large by about $\big(\sum_i x_i \sum_j y_j - \langle x, y\rangle\big)/m$.
- fastText hashes character n-grams into 2 million buckets with FNV-1a (Bojanowski et al. 2017). **Hash embeddings** give each token several hashed vectors and learned weights to mix them (Svenstrup et al. 2017).
- **Pause and try:** you hash 1,000,000 different n-grams into 2,000,000 buckets. About how many pairs collide?
  - **Answer:** $n^2/(2m) = 10^{12}/(4 \times 10^6) = 250{,}000$ pairs.

### Segment 3 (7 min): Bloom filters and the count–min sketch

- A **Bloom filter** is $m$ bits and $k$ hash functions (Bloom 1970). Adding an entry sets its $k$ bits; a query reads them. Any 0 means **certainly never added**; all 1s mean **probably added**. So there are no false negatives.
- After $n$ entries the false-positive rate is about $(1 - e^{-kn/m})^k$, smallest at $k = (m/n)\ln 2$: about 9.6 bits per entry for 1%, whatever the entries' size. Two hash functions can produce all $k$ positions (Kirsch & Mitzenmacher 2008).
- Uses: skipping documents already seen while building a corpus (Course 5 session 3 does it exactly, with a set of MD5 hashes), and **MemFree decoding**, which checks each n-gram a model is about to write against a Bloom filter of the training set. The same paper shows that prompts asking for a change of style still bring out memorized text: a false sense of privacy (Ippolito et al. 2023; Course 8 session 1).
- A **count–min sketch** is $d$ rows of $w$ counters, one hash function per row (Cormode & Muthukrishnan 2005). Counting adds 1 in every row; a query takes the minimum, which is never too low. With $w = \lceil e/\varepsilon \rceil$ and $d = \lceil \ln(1/\delta) \rceil$ the overestimate is at most $\varepsilon N$ with probability $1 - \delta$, for a stream of length $N$.
- **Pause and try:** you must remember 1 billion n-grams with a 1% false-positive rate. How much memory, and how many hash functions?
  - **Answer:** $9.6 \times 10^9$ bits = 1.2 GB, and $k = 9.6 \ln 2 \approx 7$.

### Lab guide (about 2 hours, notebook `s02_hashing.ipynb`)

1. Section 1 (10 min): five insertions and three searches by hand.
2. Sections 2–3 (25 min): probes against load factor; the bad hash; the salt.
3. Sections 4–5 (35 min): accuracy and collisions against $m$; signed against unsigned.
4. Sections 6–7 (35 min): false positives against $k$ and bits per entry; the sketch's errors and heavy hitters.
5. TODO cells (15 min): size a Bloom filter; deletion with tombstones.

- **Expect:** by hand, probes 1, 2, 2, 1, 2. FNV-1a, successful and unsuccessful: 5.007 and 46.72 at load 0.90, 10.066 and 233.75 at 0.95 (Knuth: 10.5 and 200.5). `hash('a')` differs between two processes. Accuracy: full vocabulary 0.939; signed and unsigned 0.634 and 0.602 at $m = 64$, 0.932 and 0.931 at 16,384. Mean error of inner products at $m = 64$: −0.953 signed, 53.397 unsigned (predicted 55.624). Bloom filter at 9.6 bits per entry: no false negatives; false positives of 20,000: 1,980 at $k = 1$, 167 at $k = 6$, 200 at $k = 7$, 335 at $k = 12$; 24,000 bytes against 3,332,314 for a set. Count–min at ε = 0.001: overestimates from 24 to 102 (bound 200); 58 keys with count 100 or more, 145 reported, none missed. Runtime about 10 seconds.
- **Common problems:** using the built-in `hash()` for buckets, so results change on every run; reading a count–min estimate of a rare key as its count; expecting measured rates to equal the formulas exactly (167 against 202 at $k = 6$ is sampling noise).

### Quiz

1. A saved model chose its feature columns with Python's `hash(word) % m`. Why does it fail when loaded tomorrow?
   - **Answer:** string hashes are salted per process, so the same word now gets another column and the saved weights no longer match.
2. Why does the hashing trick use a second hash for a sign?
   - **Answer:** colliding words then add or subtract with equal probability, so hashed inner products are unbiased. Without signs every collision of two counts adds a positive amount.
3. A count–min sketch with $\varepsilon = 0.001$ has seen $N = 200{,}000$ items and reports 60 for a key. What do you know about its true count?
   - **Answer:** it is at most 60. The bound only puts it above $60 - \varepsilon N = -140$, so it may be 0: the sketch is useful for frequent keys only.

**Watch out:** "A Bloom filter tells you an item is in the set." It is the opposite: a "no" is always right, and a "yes" is only probable. In the lab, 200 of 20,000 3-grams that were never stored got a "yes". Skip work safely on a "no"; confirm a "yes" against exact storage when a mistake is costly.

### Assignment 2 (due before session 3, 10 points)

1. By hand, insert 5, 13, 21, 6, 14 and 7 into eight slots with linear probing and $h(k) = k$. Give the table and the probes of each insertion and of a search for 29. Compare with Knuth's formulas and explain the difference. (3 points)
2. Complete both TODO cells. Report $m$, $k$ and the gigabytes for 1 billion n-grams at a false-positive rate of 0.001. (4 points)
3. Store the word 3-grams of your own text (at least 2,000 words, Bangla or English) in a Bloom filter sized for 1%. Query the 3-grams of a second text and report the false-positive rate, with a Python set as ground truth. (3 points)

Hand in one PDF and your notebook.

### Sources

- Weinberger et al. 2009, Feature Hashing for Large Scale Multitask Learning (ICML 2009). https://arxiv.org/abs/0902.2206
- Bloom 1970, Space/time trade-offs in hash coding with allowable errors. Communications of the ACM 13(7), 422–426. https://doi.org/10.1145/362686.362692
- Knuth 1998, The Art of Computer Programming, Volume 3: Sorting and Searching, 2nd edition, section 6.4 (hashing).
- CPython documentation, "How are dictionaries implemented in CPython?" https://docs.python.org/3/faq/design.html
- CPython documentation, hash randomization (`PYTHONHASHSEED`, on by default since Python 3.3). https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED
- CPython source code, `Objects/dictobject.c` (open addressing; `USABLE_FRACTION`). https://github.com/python/cpython/blob/main/Objects/dictobject.c
- Bojanowski et al. 2017, Enriching Word Vectors with Subword Information (TACL). https://arxiv.org/abs/1607.04606
- Svenstrup, Hansen & Winther 2017, Hash Embeddings for Efficient Word Representations (NeurIPS 2017). https://arxiv.org/abs/1709.03933
- Kirsch & Mitzenmacher 2008, Less hashing, same performance: building a better Bloom filter. Random Structures & Algorithms 33(2), 187–218. https://doi.org/10.1002/rsa.20208
- Cormode & Muthukrishnan 2005, An improved data stream summary: the count-min sketch and its applications. Journal of Algorithms 55(1), 58–75. https://doi.org/10.1016/j.jalgor.2003.12.001
- Ippolito et al. 2023, Preventing Generation of Verbatim Memorization in Language Models Gives a False Sense of Privacy (INLG 2023). https://arxiv.org/abs/2210.17546

## Session 3: Tokenizers: byte-pair encoding with heaps, linked lists and tries

**Goal:** students can implement BPE training two ways, explain with data structures why one is far faster, and encode text both by replaying merges and by longest match in a trie.

### Talking pointers

- **Open with:** "Before a model reads a word, a tokenizer has cut the text into pieces. Learning the pieces is an algorithm problem: the simple trainer recounts the whole corpus for every merge, and the fast one touches only what changed. Today we build both."
- **Segment 1, say:** do three merges on `nana nani nan ana dana` on the board, including the tie.
- **Segment 2, say:** draw `x a b y` as a linked list, fuse `a b` and change the five counts; then show the plot of work per merge.
- **Segment 3, say:** encode `nana` twice on the board, by merge order and by longest match in a trie.
- **Close with:** "The fast trainer makes the same merges. It only stops looking where nothing changed." Then set assignment 3.

### Segment 1 (6 min): BPE and the naive trainer

- **Byte-pair encoding (BPE)** starts from single symbols, counts every pair of neighbours, merges the most frequent pair into a new symbol, and repeats (Sennrich et al. 2016; first described for compression by Gage 1994). Course 4 session 2 and Course 5 session 4 teach what tokenizers are for and how to choose one for Bangla.
- The **naive trainer** recounts all pairs after every merge: $O(N)$ per merge, $O(N \cdot M)$ for $M$ merges on $N$ symbols.
- First fix: count **word types** once, with their frequencies. In the lab 60,098 running words are 6,436 types, and $N$ shrinks from 436,762 symbols to 45,666.
- It is still wasteful: 1,000 merges looked at 15,043,777 pairs, although the last merged pair occurred only 18 times.
- **Pause and try:** a text has $10^9$ symbols and its word types have $5 \times 10^7$. About how many pairs does the naive trainer look at for 30,000 merges on each?
  - **Answer:** $N \cdot M$: $3 \times 10^{13}$ and $1.5 \times 10^{12}$. Twenty times fewer, and still far too many.

### Segment 2 (7 min): the fast trainer

- Merging `a b` in `… x a b y …` changes five counts: the occurrence of `(a, b)` goes, `(x, a)` and `(b, y)` lose one, `(x, ab)` and `(ab, y)` gain one. Nothing else changes.
- Three structures do exactly this work. Each word is a **doubly linked list** of symbols, so two neighbours fuse in $O(1)$. A **pair index** (hash tables, session 2) maps each pair to its count and to the places where it occurs. A **max-heap** gives the most frequent pair.
- **Lazy deletion:** when a count falls, its old heap entry stays. An entry that reaches the top is compared with the true count and pushed back if it is stale. This is safe because the count of an existing pair never rises.
- Each merged occurrence removes one symbol, so a whole run merges fewer than $N$ occurrences, with at most five updates each: $O(N)$ updates and $O(N)$ heap operations of $O(\log N)$, whatever $M$ is. Zouhar et al. (2023) analyse BPE formally and bring training from $O(N \cdot M)$ to $O(N \log M)$.
- In the lab the same 1,000 merges took 98,880 count updates, 152 times less work, and 4,000 merges took only 110,838.
- **Ties must be broken the same way everywhere:** 653 of the lab's 1,000 merges were chosen among pairs with equal counts. We take the smallest pair of ids; the reference tool `subword-nmt` takes the largest.
- **Pause and try:** the word `x a b y` occurs 7 times and we merge `(a, b)`. Which counts change?
  - **Answer:** `(a, b)`, `(x, a)` and `(b, y)` lose 7; `(x, ab)` and `(ab, y)` gain 7. Five updates, whatever the size of the corpus.

### Segment 3 (7 min): encoding

- **BPE replays its merges.** In each word, merge the pair of neighbours with the lowest **rank** (learned earliest) until no pair is in the list, and cache whole words in a hash table. GPT-2's encoder does both. In the lab the cache answered 89.4% of 60,000 words.
- **WordPiece** (BERT's tokenizer) takes the longest vocabulary piece that matches at each position. A **trie**, a tree with one edge per byte, finds it in one walk. Failure links, the idea of Aho & Corasick (1975), make this linear time (Song et al. 2021); session 8 returns to automata.
- **Unigram** tokenizers score whole segmentations and choose the best with the Viterbi algorithm (Kudo 2018; session 6).
- Byte-level vocabularies never fail on unknown text; they only get expensive. The lab's vocabulary spends 1.59 tokens per word on its own made-up text and 8.88 on a Bangla paragraph. A Bangla code point is three bytes, and merges must rebuild it: trained on Bangla alone, only 12 of the first 60 merges gave one whole code point, and 29 gave a token that cuts through one.
- **Pause and try:** the vocabulary is the letters plus `na`, `ana` and `nan`, learned in this order. Encode `nana` by both rules.
  - **Answer:** replaying merges gives `na na`, because `n + a` has the lowest rank. Longest match gives `nan a`.

### Lab guide (about 2 hours, notebook `s03_tokenizer_algorithms.ipynb`)

1. Section 1 (10 min): three merges by hand, with one tie.
2. Sections 2–3 (20 min): the corpus; the naive trainer on the stream and on the types.
3. Section 4 (35 min): read `train_indexed` line by line; counts, heap and plot.
4. Sections 5–6 (30 min): two encoders; the cache; unfamiliar text.
5. Section 7 (10 min): Bangla bytes and merges. Section 8 (NOT RUN) repeats the lab with the `tokenizers` and `tiktoken` libraries.
6. TODO cells (15 min): fewest tokens by dynamic programming; another tie rule.

- **Expect:** by hand 18 symbols, then 12, 10 and 8. Naive trainer: 3,400,374 pairs for 10 merges on the stream and 383,289 on the types; 15,043,777 for 1,000 merges, about 11.3 s. Indexed trainer: the same merges, 98,880 updates, 13,120 heap entries pushed and 1,804 stale ones met at the top, about 0.094 s (timings from the saved run; they vary). For 4,000 merges: 110,838 updates against 43,054,125 pairs. Encoders: 96,064 tokens by merges, 96,057 by longest match; 91 word types cut differently (1.4%), and 22 of 1,650 unseen words; 21.26 pair look-ups against 7.40 trie steps per word. Cache hits 48.2%, 73.8% and 89.4%; look-ups 1,399,240 without it, 134,307 with it. Tokens per word: 1.59 made-up, 4.29 English, 8.88 Bangla. The Bangla sentence: 26 code points, 70 bytes, 36 tokens; of 60 merges 12 give one whole code point and 29 cut through one. Runtime about 15 seconds.
- **Common problems:** merging right to left, so that the trainers disagree on words like `aaa`; leaving ties to dictionary order; decoding token by token (a token can be half a character: join the bytes first).

### Quiz

1. Why can the heap keep stale entries without giving a wrong answer?
   - **Answer:** once a pair exists its count only falls, so a stale entry is never too low. When it reaches the top we compare it with the true count and push it back corrected.
2. You train 4,000 merges where you trained 1,000 before. How does each trainer's work change?
   - **Answer:** the naive one's work grows with $M$, $O(N \cdot M)$: 43,054,125 against 15,043,777 pairs in the lab. The indexed one hardly grows: 110,838 against 98,880 updates.
3. A byte-level tokenizer has no merges for Bangla. How many tokens is `বাংলা`, and why can one token be invalid text?
   - **Answer:** 5 code points of 3 bytes: 15 tokens. A token is a run of bytes and may end inside a code point.

**Watch out:** "BPE encodes by taking the longest matching token." BPE replays its merges in the order learned; longest match is WordPiece's rule. With one vocabulary the two rules cut 91 of the lab's 6,436 word types differently (`_halo` became `_h alo` or `_ha lo`), although their token totals were almost equal. Always encode with the rule the model was trained with.

### Assignment 3 (due before session 4, 10 points)

1. By hand, train three merges on `tata tara rata tar ata` with the lab's tie rule. Then, with the merges of section 1, encode `nanan` and `nanana` by both rules and say which uses fewer tokens. (3 points)
2. Complete both TODO cells. Report for how many word types each encoder is above the minimum, the first merge at which the two tie rules differ, and how many tokens the two vocabularies share. (4 points)
3. Train 500 merges on your own text (at least 2,000 words, Bangla or English) with both trainers. Report $N$ for the stream and for the types, the work of both trainers, the tokens per word, and the first ten merges that give a whole word or a whole Bangla code point. (3 points)

Hand in one PDF and your notebook.

### Sources

- Sennrich, Haddow & Birch 2016, Neural Machine Translation of Rare Words with Subword Units (ACL 2016). https://arxiv.org/abs/1508.07909
- Zouhar et al. 2023, A Formal Perspective on Byte-Pair Encoding (Findings of ACL 2023). https://arxiv.org/abs/2306.16837
- Gage 1994, A New Algorithm for Data Compression. The C Users Journal 12(2).
- Song et al. 2021, Fast WordPiece Tokenization (EMNLP 2021). https://arxiv.org/abs/2012.15524
- Aho & Corasick 1975, Efficient string matching: an aid to bibliographic search. Communications of the ACM 18(6), 333–340. https://doi.org/10.1145/360825.360855
- Kudo 2018, Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates (ACL 2018). https://arxiv.org/abs/1804.10959
- OpenAI, GPT-2 source code, `src/encoder.py`. https://github.com/openai/gpt-2/blob/master/src/encoder.py
- Sennrich, subword-nmt (GitHub repository), `subword_nmt/learn_bpe.py`. https://github.com/rsennrich/subword-nmt
- OpenAI, tiktoken (GitHub). https://github.com/openai/tiktoken
- Hugging Face Tokenizers documentation. https://huggingface.co/docs/tokenizers

## Session 4: Computation graphs: topological sort and automatic differentiation

**Goal:** students can represent a model as a directed acyclic graph, order it with Kahn's algorithm and with depth-first search, run reverse-mode differentiation as one backward sweep, and apply simple graph optimizations.

### Talking pointers

- **Open with:** "A neural network is a graph. Training it uses two algorithms from your data structures course: a topological sort, and one sweep over the sorted nodes in reverse."
- **Segment 1, say:** draw the graph of $e = (a + b) \times (a \times b)$; run Kahn's algorithm, then depth-first search.
- **Segment 2, say:** write the gradients on the same graph (21 and 16), then show 33,554,431 visits against 48 steps.
- **Segment 3, say:** show the network shrinking from 88 to 40 operations, then the two memory curves.
- **Close with:** "Sorting, differentiating and shrinking a model are walks over one graph that use every edge once." Then set assignment 4.

### Segment 1 (6 min): a model is a graph, and graphs can be sorted

- A computation is a **directed acyclic graph** (DAG): an edge $u \to v$ means $v$ is computed from $u$. It is not a tree, because a value can feed several operations (**fan-out**): a shared weight, or the input of a skip connection.
- A **topological order** lists the nodes so that every edge points forward. It exists exactly when the graph has no cycle.
- **Kahn's algorithm** (Kahn 1962): count each node's incoming edges and put the nodes with none in a queue. Take a node, output it, and lower the count of every node it feeds; a node that reaches zero joins the queue.
- **Depth-first search** (DFS): a node is finished when everything it feeds is finished; the reversed finishing order is topological (Cormen et al. 2022).
- Both cost $O(V + E)$ for $V$ nodes and $E$ edges, in every case. With a cycle, Kahn's algorithm outputs fewer than $V$ nodes and DFS meets an unfinished node again.
- A program that records operations while it runs creates every value after its inputs, so the order of creation, a **tape**, is already topological. PyTorch records its graph during the forward pass (Paszke et al. 2019); its documentation calls it a DAG with the inputs as leaves.
- **Pause and try:** how many topological orders has $c = a + b$, $d = a \times b$, $e = c \times d$? Which does Kahn's algorithm give if the queue starts as `b, a`?
  - **Answer:** four: `a`, `b` in either order, then `c`, `d` in either order, then `e`. Kahn gives `b a c d e`.

### Segment 2 (7 min): the backward pass is one sweep

- Forward: compute the nodes in topological order, one operation per node.
- Backward (reverse-mode differentiation): each node gets a `grad`, the derivative of the output with respect to it. Set the output's `grad` to 1 and visit the nodes in **reverse** topological order. Each node sends `grad` × (local derivative) to its inputs; an input adds up what it receives.
- Every reader of a value comes earlier in this order, so a `grad` is complete before it is passed on. Cost: one multiply–add per edge, $E$ steps. Course 2 session 5 derives the calculus and builds an engine.
- By hand, with $a = 2$, $b = 3$: `c.grad` = $d$ = 6, `d.grad` = $c$ = 5, `a.grad` = 6 + 5 × 3 = 21, `b.grad` = 6 + 5 × 2 = 16.
- The trap: a recursion that follows every path to the inputs visits a shared node once per path. The **doubling chain** $x_k = x_{k-1} + x_{k-1}$ has $2^n$ paths: $2^{n+1} - 1$ visits, against $2n$ steps for the sweep. $n$ residual blocks also give $2^n$ paths.
- So a gradient costs a small constant multiple of the function itself, whatever the number of inputs: the cheap gradient principle (Griewank & Walther 2008; Baydin et al. 2018).
- **Pause and try:** ten blocks $h_{k+1} = h_k + \tanh(h_k)$ are chained. How many paths lead from the output to $h_0$, and how many steps does the sweep need?
  - **Answer:** $2^{10} = 1{,}024$ paths. Each block has three edges (one into `tanh`, two into the sum), so 30 steps.

### Segment 3 (7 min): what compilers and runtimes do to the graph

- A graph known before it runs, such as an ONNX file (Course 11 session 7), can be rewritten first.
- **Dead-code elimination:** search backwards from the outputs and drop what was not reached, $O(V + E)$.
- **Constant folding:** in topological order, compute now every operation whose inputs are all constants.
- **Common-subexpression elimination:** in topological order, look up the key (operation, input ids) in a hash table (session 2) and reuse the first node with that key: expected $O(1)$ per node.
- **Operator fusion** merges neighbours into one kernel, such as a multiplication and the addition after it; the product must have no other reader.
- ONNX Runtime's documentation (November 2026) lists constant folding, redundant-node elimination and node fusions among its basic graph optimizations.
- **Memory planning:** a value can be freed after its last reader has run (reference counts). Valid orders differ in peak memory: 9 live values against 3 in the lab. Course 11 session 8 measures this in bytes on a CNN.
- **Pause and try:** a program computes $p = x \times w$, $q = x \times w$, $r = 2 \times 3$, $s = p + q$, $t = s \times r$ and $u = q \times q$; only $t$ is an output. How many operations remain after the three passes?
  - **Answer:** three of six: $u$ is dead, $r$ folds to 6, and $q$ merges into $p$, leaving $p = x \times w$, $s = p + p$, $t = s \times 6$.

### Lab guide (about 2.5 hours, notebook `s04_computation_graphs.ipynb`)

1. Sections 1–2 (35 min): both orders by hand; the cycle; the `Node` class and the tape.
2. Section 3 (30 min): gradients by hand, the sweep, the check against PyTorch.
3. Section 4 (20 min): predict the visits at depth 5, then run.
4. Sections 5–6 (45 min): count the 40 operations by hand; read each pass; reference counts.
5. TODO cells (30 min): operator fusion; all valid orders of a small graph.

- **Expect:** Kahn `a b c d e`, DFS `b a d c e`, 11 steps each; with the cycle, Kahn outputs 1 of 5 nodes. Largest random graph: 53,594 nodes, 89,374 edges, 142,968 steps for both algorithms. Gradients 21.0 and 16.0, as in PyTorch; largest relative difference to `torch.autograd` 6.4e-16; the largest graph has 205 operations, 356 backward steps and 15,876,473,600,972 paths. Doubling chain: 63, 2,047, 65,535, 2,097,151 and 33,554,431 visits at depths 5, 10, 15, 20 and 24, against 10 to 48 sweep steps; about 7 s against 20 microseconds (timings from the saved run; they vary). Passes: 88 operations as written, then 68, 56 and 40 (158 to 63 nodes), the output unchanged; backward steps 172 to 77. Peak live values 9 (Kahn) against 3 (depth-first from the output). Runtime about 12 seconds.
- **Common problems:** a recursive DFS that hits Python's recursion limit on a long chain; sweeping forward instead of in reverse; building the CSE key from the original inputs instead of the merged ones.

### Quiz

1. Why must the backward sweep use reverse topological order?
   - **Answer:** a node's `grad` is the sum of what its readers send. In reverse topological order every reader comes first, so the sum is complete when the node passes it on.
2. Kahn's algorithm outputs 7 of a graph's 10 nodes. What do you know?
   - **Answer:** the graph has a cycle. The three missing nodes lie on a cycle or behind one.
3. A doubling chain has depth 30. How many visits does the path recursion make, and how many steps the sweep?
   - **Answer:** $2^{31} - 1 = 2{,}147{,}483{,}647$ visits against 60 steps.

**Watch out:** "A neural network's computation graph is a tree, so backpropagation is a simple recursion." Values are shared: a weight is used at many positions, and a skip connection uses a layer's input twice. The graph is a DAG, and a recursion along every path repeats each shared node once per path: 33,554,431 visits at depth 24 in the lab, where the sweep needs 48 steps. Sort once, then sweep once.

### Assignment 4 (due before session 5, 10 points)

1. By hand, for $p = a \times b$, $q = p + a$, $g = q \times p$ at $a = 3$, $b = 2$: the graph, the orders of Kahn's algorithm and DFS, all values and gradients. Check with the notebook and with PyTorch. (3 points)
2. Complete both TODO cells. Report the operations left after fusion, and for the small branch graph the number of valid orders and the smallest and largest peak. (4 points)
3. Build your own function with at least 30 operations and a shared weight or a skip connection. Report $V$, $E$, paths and backward steps; compare its gradients with PyTorch; run the three passes. (3 points)

Hand in one PDF and your notebook.

### Sources

- Kahn 1962, Topological sorting of large networks. Communications of the ACM 5(11), 558–562. https://doi.org/10.1145/368996.369025
- Cormen, Leiserson, Rivest & Stein 2022, Introduction to Algorithms, 4th edition. MIT Press (sections on depth-first search and topological sort).
- Baydin, Pearlmutter, Radul & Siskind 2018, Automatic Differentiation in Machine Learning: a Survey (JMLR). https://arxiv.org/abs/1502.05767
- Griewank & Walther 2008, Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation, 2nd edition. SIAM. https://doi.org/10.1137/1.9780898717761
- Paszke et al. 2019, PyTorch: An Imperative Style, High-Performance Deep Learning Library (NeurIPS 2019). https://arxiv.org/abs/1912.01703
- PyTorch documentation, Autograd mechanics. https://pytorch.org/docs/stable/notes/autograd.html
- ONNX Runtime documentation, Graph Optimizations (constant folding, redundant node elimination, node fusion). https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html
- Karpathy, micrograd (GitHub). https://github.com/karpathy/micrograd

## Session 5: Dynamic programming I: edit distance and alignment

**Goal:** students can set up a dynamic program (subproblems, recurrence, order, answer), compute edit distance in quadratic time with a backtrace or in linear memory, and use the same table for error rates and sequence alignment.

### Talking pointers

- **Open with:** "NEAR and EARN differ in every position, yet two edits turn one into the other. To find them you must try every way of lining the words up, and one small table does that."
- **Segment 1, say:** fill the 5 × 5 table for NEAR and EARN on the board, then show 2,193,844 calls against 81 cells.
- **Segment 2, say:** walk back through the table to read the alignment, score the Bangla pair (WER 0.571), then draw the band.
- **Segment 3, say:** change the recurrence to the longest common subsequence and score the three candidates (0.600, 0.500, 0.300).
- **Close with:** "Dynamic programming is a table, a recurrence and an order. Change the recurrence and the same table answers a new question." Then set assignment 5.

### Segment 1 (7 min): the recipe, and edit distance

- Dynamic programming solves each smaller subproblem once and stores the answer. Write four things first: the **subproblems**, the **recurrence**, the **order**, and where the **answer** is.
- **Edit distance** (Levenshtein 1966): the fewest insertions, deletions and substitutions that turn string $a$ into string $b$. Subproblem: $D[i][j]$, the distance between the first $i$ letters of $a$ and the first $j$ letters of $b$.
- Recurrence (Wagner & Fischer 1974): $D[i][j] = \min(D[i-1][j-1] + [a_i \ne b_j],\; D[i-1][j] + 1,\; D[i][j-1] + 1)$, with $D[i][0] = i$ and $D[0][j] = j$. Fill row by row; the answer is $D[m][n]$. Time and memory are $O(m \cdot n)$ in every case.
- Session 4's view: the cells are nodes of a grid graph with three edges into each cell, row by row is a topological order, and the distance is a shortest path from corner to corner.
- Plain recursion on the same recurrence solves the same cell again and again: 2,193,844 calls for two 9-letter strings in the lab, about 5.5 times more for each extra letter. **Memoization** (remember each solved cell) or the table solves each cell once: 81.
- **Pause and try:** in how many positions do SLOT and LOST differ, and what is their edit distance?
  - **Answer:** three positions (only the final T agrees), but the distance is 2: delete the S, then insert an S before the T.

### Segment 2 (7 min): alignments, error rates, memory and bands

- The **backtrace** walks from the corner to a neighbour that explains each value: diagonal is a match or a substitution, up a deletion, left an insertion. The path is an **alignment**; it need not be unique.
- With words as units, **word error rate** is WER = $(S + D + I)/N$ for $N$ reference words. Insertions are not among the $N$, so WER can exceed 1: 2.500 in the lab. Course 12 session 2 applies WER to Bangla speech and shows the normalization traps.
- Row $i$ needs only row $i - 1$: two rows give the distance in $O(\min(m, n))$ memory. Hirschberg's divide-and-conquer method (1975, given for the longest common subsequence) recovers the alignment in linear memory too.
- If the distance is at most $k$, a best path stays in the **band** $|i - j| \le k$, about $(2k + 1) \cdot n$ cells. Doubling $k$ until an answer appears costs $O(d \cdot n)$ cells for distance $d$ (Ukkonen 1985). In the lab: 189,709 cells instead of 2,259,000.
- No much faster exact algorithm is expected: time $O(n^{2 - \delta})$ would contradict the Strong Exponential Time Hypothesis, a well-known conjecture (Backurs & Indyk 2015).
- **Pause and try:** two strings have lengths 1,000 and 1,010. What is the smallest possible distance, and how many cells does a band with $k = 20$ fill at most?
  - **Answer:** at least 10, the difference in length. At most 41 cells in each of 1,000 rows: 41,000 of 1,010,000 cells, about 4%.

### Segment 3 (6 min): the same table, other scores

- **Longest common subsequence** (LCS): if the last items are equal, $L[i][j] = L[i-1][j-1] + 1$; otherwise the larger of $L[i-1][j]$ and $L[i][j-1]$. Without substitutions, edit distance is $m + n - 2 \cdot \text{LCS}$.
- **ROUGE-L** (Lin 2004) scores a summary by the LCS of its words with a reference: recall = LCS / reference length, precision = LCS / candidate length, and F combines them. In the lab the same nine words in three orders scored 0.600, 0.500 and 0.300.
- **Global alignment** (Needleman & Wunsch 1970) maximizes a score with rewards for matches and penalties for mismatches and gaps. **Local alignment** (Smith & Waterman 1981) finds the best-matching pieces: add 0 to the maximum and take the largest cell. Both compare DNA and proteins.
- Dynamic time warping uses the table for signals (Course 12 session 3).
- Replace "maximum" by "sum" and the table counts all alignments: 598,417 for 9 and 8 letters. Session 6 builds on this.
- **Pause and try:** reference "rice prices rose in Dhaka this week", candidate "this week rice prices in Dhaka rose sharply". Give the LCS and ROUGE-L precision, recall and F.
  - **Answer:** "rice prices in Dhaka", 4 words. Precision 4/8 = 0.500, recall 4/7 = 0.571, F = 0.533.

### Lab guide (about 2.5 hours, notebook `s05_edit_distance.ipynb`)

1. Sections 1–2 (35 min): the table by hand; three implementations and their counts.
2. Section 3 (30 min): backtrace and WER; add a sentence pair of your own.
3. Section 4 (30 min): two rows, the band, the table of cells.
4. Sections 5–7 (35 min): ROUGE-L; Needleman–Wunsch against brute force; timing.
5. TODO cells (30 min): swaps of neighbouring letters; Smith–Waterman.

- **Expect:** NEAR to EARN: distance 2. Plain recursion: 2,193,844 calls at length 9 against 81 cells; 390,815,720,696,161 calls predicted for length 20. WER 0.333 (English), 0.571 (Bangla), 2.500 for the over-long output; two outputs with WER 0.250 have 0.750 and 1.000 of the reference words correct. Lengths 1,500 and 1,506, distance 34: two rows hold 3,002 numbers; bands 1 to 4 fill no cell, bands 8 to 32 return `None`, band 64 gives 34 from 189,709 cells (0.084 of the table); doubling uses 302,907 cells, 7.5 times fewer than the full table. Needleman–Wunsch score 1 (7 matches, 3 gaps), as brute force. Time at length 1,600: 418.9 ms, slope 2.16 (timings from the saved run; they vary). Runtime about 4 seconds.
- **Common problems:** swapping reference and hypothesis, which exchanges insertions and deletions and changes $N$; forgetting the first row and column; reading the band's `None` as an error instead of "more than $k$".

### Quiz

1. Why is the plain recursion exponential when the table is $O(m \cdot n)$?
   - **Answer:** there are only $(m + 1)(n + 1)$ different subproblems, but the recursion reaches each one along many routes and solves it again every time.
2. A recognizer writes 12 words for a 10-word reference, with $S = 1$ and $D = 0$. What are $I$ and the WER?
   - **Answer:** the output has $N - D + I$ words, so $I = 2$ and WER = (1 + 0 + 2)/10 = 0.3.
3. What does a band of half-width $k$ return when the true distance is larger than $k$?
   - **Answer:** only "more than $k$", never a wrong distance. Widen the band and run again.

**Watch out:** "A word error rate of 0.25 means three quarters of the words are right." WER counts edits per reference word, and inserted words are edits too. In the lab two outputs had WER 0.250: one had 6 of 8 reference words right, the other all 8, with two extra words at the end. Report $S$, $D$ and $I$ next to the WER.

### Assignment 5 (due before session 6, 10 points)

1. By hand, fill the table for BANGLA and BENGAL, and give the distance and one best alignment. Check with the notebook. (3 points)
2. Complete both TODO cells. Report the distance with swaps for BANGLA and BENGAL and four pairs of your own, and the shared piece that your Smith–Waterman finds. (4 points)
3. Write `distance_by_doubling(a, b)` with `edit_banded`. For 1,500-letter strings with 5, 20 and 80 random edits, report distance and cells filled, and compare with $d \cdot n$ and with the full table. (3 points)

Hand in one PDF and your notebook.

### Sources

- Levenshtein 1966, Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady 10(8), 707–710.
- Wagner & Fischer 1974, The string-to-string correction problem. Journal of the ACM 21(1), 168–173. https://doi.org/10.1145/321796.321811
- Hirschberg 1975, A linear space algorithm for computing maximal common subsequences. Communications of the ACM 18(6), 341–343. https://doi.org/10.1145/360825.360861
- Ukkonen 1985, Algorithms for approximate string matching. Information and Control 64(1–3), 100–118. https://doi.org/10.1016/S0019-9958(85)80046-2
- Backurs & Indyk 2015, Edit Distance Cannot Be Computed in Strongly Subquadratic Time (unless SETH is false) (STOC 2015). https://arxiv.org/abs/1412.0348
- Lin 2004, ROUGE: A Package for Automatic Evaluation of Summaries. In Text Summarization Branches Out, 74–81. Association for Computational Linguistics. https://aclanthology.org/W04-1013/
- Needleman & Wunsch 1970, A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of Molecular Biology 48(3), 443–453. https://doi.org/10.1016/0022-2836(70)90057-4
- Smith & Waterman 1981, Identification of common molecular subsequences. Journal of Molecular Biology 147(1), 195–197. https://doi.org/10.1016/0022-2836(81)90087-5

## Session 6: Dynamic programming II: Viterbi, the forward algorithm and CTC

**Goal:** students can find the best path and the total probability over exponentially many paths with one table, implement Viterbi and the forward algorithm in log space, and compute the CTC loss from scratch.

### Talking pointers

- **Open with:** "A string of 16 letters can be cut into pieces in 32,768 ways. One small table finds the best way, and the same table can add up all of them."
- **Segment 1, say:** fill `best` and `back` for `nowhere` on the board.
- **Segment 2, say:** change max to sum, then show the plot where the probability line stops after day 714.
- **Segment 3, say:** fill the 3 × 5 counting table for `ab`, then show the check against PyTorch.
- **Close with:** "When paths share their beginnings, combine them in a table: max for the best, sum for all." Then set assignment 6.

### Segment 1 (7 min): the best path in a lattice

- A **lattice** is a directed acyclic graph with its nodes in layers, so left to right is a topological order (session 4). One path is one answer.
- The **Viterbi algorithm** (Viterbi 1967) keeps, for every node, the best score of any path into it and a **back-pointer** to the node before: session 5's recipe on a lattice.
- A **unigram tokenizer** gives every vocabulary piece a probability and encodes a string as the segmentation with the largest product (Kudo 2018). Positions are nodes, pieces are edges. $n$ letters can be cut in $2^{n-1}$ ways; the table needs at most $n \cdot L$ lookups for pieces of up to $L$ letters.
- In the lab, `nowhere` gives `no | where` (probability 1/16). Greedy longest match (session 3) gives `now | here` (1/64), and it was worse on 70 of 300 random strings.
- **Hidden Markov models** (HMMs) have $S$ hidden states and one observation per step: $S^T$ state paths for $T$ steps. Viterbi needs $O(T \cdot S^2)$ time and $O(T \cdot S)$ back-pointers (Rabiner 1989; Jurafsky & Martin 2026).
- **Pause and try:** piece costs in bits (minus log₂ of the probability): `a` 1, `not` 2, `her` 3, `an` 4, `other` 5, `n` 5. Find the cheapest segmentation of `another`. What does greedy longest match return?
  - **Answer:** `a | not | her`, cost 1 + 2 + 3 = 6, probability $2^{-6}$. Greedy takes `an`, then `other`: cost 9, eight times less probable.

### Segment 2 (6 min): from max to sum

- Change max to sum in the same loop and the table gives the **total probability of all paths**: the **forward algorithm**, at the same cost.
- Why both work: $\max(a + c, b + c) = \max(a, b) + c$ and $(a + b) \cdot c = a \cdot c + b \cdot c$, so paths that meet in a node can be combined before they are extended. Such a pair of operations is a **semiring**. One program serves all of them (Goodman 1999); with "count" it returns the number of paths.
- Long products **underflow**: float64 has nothing between 0 and about $4.9 \times 10^{-324}$. In the lab the forward value was exactly 0.0 from day 715 of 2,000, and Viterbi on probabilities returned a wrong path without warning.
- The cure is to store logarithms: products become sums, max stays max, and a sum becomes **log-sum-exp** (Course 2 session 10). Rabiner (1989) rescales every column instead; the lab gets −2075.9905 both ways.
- **Pause and try:** an HMM has 3 states and 20 time steps. How many state paths are there, and how many table steps, at 3 for the first column and 9 for each later one?
  - **Answer:** $3^{20} = 3{,}486{,}784{,}401$ paths, and $3 + 9 \times 19 = 174$ steps.

### Segment 3 (7 min): CTC, a loss made of a table

- Speech data give the text, but not which **frame** (a short slice of audio) belongs to which letter. **Connectionist temporal classification** (CTC; Graves et al. 2006; Hannun 2017) adds a **blank** symbol, reads a frame path by merging repeats and then deleting blanks, and sums the probabilities of all frame paths (**alignments**) that collapse to the text. Course 12 session 2 trains a small recognizer with `nn.CTCLoss`.
- The lattice is the target's $L$ letters with a blank before, between and after them: $2L + 1$ states. A path may stay, step to the next state, or skip a blank between two **different** letters.
- The forward table has $T \cdot (2L + 1)$ cells of at most three terms each: $O(T \cdot L)$. The loss is −log of the sum of the last two cells of the last row. In the lab, `more` has 257,575,523,205 alignments in 100 frames; the table has 900 cells.
- The gradient needs no new formula: reverse-mode differentiation through the table (session 4) is the backward algorithm (Eisner 2016). With max in place of sum, the table gives the best alignment of a known text (forced alignment, Course 12 session 3).
- **Decoding** (choosing a text from the frame probabilities) is harder: the best symbol of every frame gives the best *path*, not the best text. Prefix beam search (Course 12 session 6) approximates the most probable text.
- **Pause and try:** two frames; in each, the blank has probability 0.6 and `a` has 0.4. What does greedy decoding return, and what is the probability of the text `a`?
  - **Answer:** the best path is blank, blank (0.36), so greedy returns the empty text. The text `a` has three alignments: 0.24 + 0.24 + 0.16 = 0.64.

### Lab guide (about 2 hours, notebook `s06_viterbi_ctc.ipynb`)

1. Section 1 (10 min): `nowhere` on paper, then run.
2. Section 2 (20 min): Viterbi against brute force and greedy; three Bangla words.
3. Sections 3–4 (25 min): the HMM by hand and against brute force; underflow.
4. Section 5 (10 min): one function, four semirings.
5. Sections 6–7 (30 min): the counting table for `ab`; CTC against brute force and PyTorch.
6. Sections 8–10 (25 min): best path against best text; SentencePiece (Kudo & Richardson 2018; NOT RUN); TODO cells.

- **Expect:** `nowhere`: 64 ways to cut, 3 valid, `no | where` after 25 lookups. `বাংলাদেশ | ের` 0.039983 against greedy's 0.000200. HMM: best path 0.00504, forward sum 0.03273; in 80 random cases the best probability matched brute force 80 times, the path 75 times (ties). CTC: 5 alignments and loss 1.6864 for `ab` in 3 frames (every symbol 1/3); `moon` has 237,762,021,420 alignments in 100 frames and 0 in 4. Largest difference to PyTorch: 2.2e-16 for the loss, 1.0e-12 for the gradient with respect to the logits. Measured on PyTorch 2.15.0 only: with the log-probabilities as a leaf (no log-softmax in the graph), its gradient differs from ours by up to 0.7000; it equals ours plus the probabilities (within 1.0e-15). Greedy's text is not the most probable in 1,013, 437 and 135 of 2,000 random tables. Runtime: a few seconds (the saved run prints 2 s after section 8; it varies).
- **Common problems:** comparing paths instead of scores when two paths tie; giving CTC fewer frames than letters plus one for each double letter (the loss is `inf`); comparing with PyTorch's default `reduction="mean"`, which divides each loss by its target length.

### Quiz

1. Why does changing max to sum in the Viterbi table give the total probability of all paths?
   - **Answer:** multiplication distributes over addition, so the sum over all paths into a node is built from the sums of the nodes before it.
2. A CTC target has 5 letters, one of them doubled as in `hello`, and 50 frames. How many states, how many table cells, and how many frames at least?
   - **Answer:** $2 \times 5 + 1 = 11$ states, $50 \times 11 = 550$ cells, and 6 frames: five letters and one blank between the two equal letters.
3. The forward algorithm returns exactly 0.0 for a sequence of 2,000 steps. Is the sequence impossible under the model?
   - **Answer:** not necessarily: the product may have underflowed. In the lab the true value was about $10^{-902}$. Compute in log space.

**Watch out:** "Greedy decoding of a CTC model gives the most probable text." It gives the text of the single most probable frame path. A text's probability is the sum over all its alignments, so a text with many alignments can win: in the lab the best path was all blanks (0.120), but `a` had probability 0.4035. With confident frames the two agree more often, yet nothing guarantees it.

### Assignment 6 (due before session 7, 10 points)

1. By hand: `best` and `back` for `another` (pause-and-try vocabulary), and the counting table for the CTC target `aa` with 4 frames. Check both with the notebook. (3 points)
2. Complete both TODO cells. Report the best alignment of `moon`, its probability beside the total, and your sampled proportions for `nowhere`. (4 points)
3. Write 30 pieces with counts for your own text, segment 20 strings by Viterbi and by greedy longest match, and report how often they differ. (3 points)

Hand in one PDF and your notebook.

### Sources

- Viterbi 1967, Error bounds for convolutional codes and an asymptotically optimum decoding algorithm. IEEE Transactions on Information Theory 13(2), 260–269. https://doi.org/10.1109/TIT.1967.1054010
- Rabiner 1989, A tutorial on hidden Markov models and selected applications in speech recognition. Proceedings of the IEEE 77(2), 257–286. https://doi.org/10.1109/5.18626
- Jurafsky & Martin, Speech and Language Processing, 3rd edition draft, appendix "Hidden Markov Models" (release of 6 January 2026). https://web.stanford.edu/~jurafsky/slp3/
- Kudo 2018, Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates (ACL 2018). https://arxiv.org/abs/1804.10959
- Kudo & Richardson 2018, SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing (EMNLP 2018 demo). https://arxiv.org/abs/1808.06226
- Goodman 1999, Semiring Parsing. Computational Linguistics 25(4), 573–606. https://aclanthology.org/J99-4004/
- Graves, Fernández, Gomez & Schmidhuber 2006, Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks (ICML 2006), 369–376. https://doi.org/10.1145/1143844.1143891
- Hannun 2017, Sequence Modeling with CTC. Distill. https://distill.pub/2017/ctc/
- Eisner 2016, Inside-Outside and Forward-Backward Algorithms Are Just Backprop (tutorial paper). Proceedings of the Workshop on Structured Prediction for NLP, 1–17. https://aclanthology.org/W16-5901/

## Session 7: Decoding: heaps, beam search and sampling

**Goal:** students can implement greedy, beam and exact search for a language model, pick the top-k or top-p tokens with selection algorithms, and say what each decoding rule optimizes.

### Talking pointers

- **Open with:** "A language model does not write text. At every step it scores each of 50,000 tokens. Turning those scores into a sentence is a search problem and a selection problem, and you know the data structures for both."
- **Segment 1, say:** do greedy and width 2 by hand on the three-token tree, then show the table: greedy finds the best string for 54 prompts of 100.
- **Segment 2, say:** write three ways to find the top 50 of 50,000 scores, with their comparison counts.
- **Segment 3, say:** add Gumbel noise to three log-probabilities on the board and take the largest.
- **Close with:** "Search gives probable text and sampling gives varied text. Neither gives good text unless the model is good." Then set assignment 7.

### Segment 1 (7 min): decoding is search in a tree

- **Decoding** means choosing an output from a model that scores every next token (Course 4 session 1). The outputs form a tree of prefixes: $V$ tokens and $T$ steps give $V^T$ leaves.
- **Greedy** decoding keeps the best prefix. **Beam search** keeps the $b$ best: each kept prefix gets $V$ scores, and a heap selects the best $b$ of the $bV$ candidates. The cost is about $T \cdot b \cdot V$ scores, with no guarantee of finding the best string (Course 12 session 6 uses a variant for CTC models).
- A trigram model depends only on the last two characters, so the Viterbi algorithm of session 6 finds the exact optimum with $V^2$ states and about $T \cdot V^3$ scores. A transformer reads the whole prefix, so it has no such table.
- More probable is not better. In the lab the exact optimum is `the the the ...`, and the most probable sentence is `it.`: every extra character multiplies the probability by a number below 1. In machine translation, exact search found the empty translation to be the model's best output for 51.8% of the sentences (Stahlberg & Byrne 2019). Beam search works partly because it fails to find the maximum (Meister et al. 2020).
- Length normalization divides the log-probability by $lp(L) = ((5 + L)/6)^\alpha$ for an output of length $L$ (Wu et al. 2016).
- **Pause and try:** $V$ = 50,000, $T$ = 100 and $b$ = 4. How many scores do greedy and beam search compute?
  - **Answer:** greedy 100 × 50,000 = 5 million. Beam search expands 1 prefix at the first step and 4 at each of the other 99: 397 × 50,000 = 19.85 million.

### Segment 2 (7 min): sampling, and selecting the top k

- **Sampling** draws the next token from the model's distribution. **Temperature** τ divides the log-probabilities before the softmax; τ below 1 sharpens the distribution (Course 5 session 7 shows the effect on Bangla text).
- **Top-k** sampling keeps the $k$ most probable tokens and renormalizes (Fan et al. 2018). Finding them is the selection problem:
  - sort everything: $O(V \log V)$;
  - a min-heap of the $k$ largest seen so far: worst case $O(V \log k)$, but close to $V$ comparisons for scores in random order, because the root is rarely replaced;
  - quickselect (Hoare 1961): expected $O(V)$, worst case $O(V^2)$; the median-of-medians rule gives a linear worst case (Blum et al. 1973).
- **Top-p**, or nucleus, sampling keeps the smallest set of tokens whose probabilities add up to at least $p$ (Holtzman et al. 2020). The set adapts to the context: 4 characters after `th` and 15 after `e ` in the lab. It needs sorted order only until the sum passes $p$: select the largest $m$ tokens and sort only those.
- Why sample at all? Text found by maximization is repetitive, and human text is not the most probable text (Holtzman et al. 2020).
- **Pause and try:** the probabilities are 0.5, 0.2, 0.15, 0.1 and 0.05. What does top-k keep for $k = 2$, with which new probabilities? What does top-p keep for $p = 0.8$?
  - **Answer:** top-k keeps the first two, with 0.5/0.7 = 0.714 and 0.286. Top-p keeps three: 0.5 + 0.2 = 0.7 is below 0.8, and adding 0.15 gives 0.85.

### Segment 3 (6 min): randomness as argmax

- The **Gumbel-max trick**: draw $g_i = -\ln(-\ln u_i)$ with $u_i$ uniform on (0, 1). Then $\arg\max_i(\log p_i + g_i)$ is an exact sample from $p$. Sampling becomes a maximization.
- The $k$ largest perturbed scores give $k$ different items, distributed as if drawn one after another without replacement (Kool et al. 2019). Session 12 meets the idea again as weighted reservoir sampling.
- The chance that an item is among the $k$ is not $k \cdot p_i$: for $p_i = 0.3$ and $k = 3$ in the lab it is 0.7365, not 0.9.
- The same seed, model and decoding settings give the same text. Record all three with every result (Course 1 session 3).
- **Pause and try:** $p$ = (0.5, 0.3, 0.2), and we draw 2 items without replacement. What is the chance that the third item is drawn?
  - **Answer:** first draw 0.2; second draw 0.5 × 0.2/0.5 + 0.3 × 0.2/0.7 = 0.286. Together about 0.486, more than 2 × 0.2.

### Lab guide (about 2 hours, notebook `s07_decoding_search.ipynb`)

1. Section 1 (10 min): the three-token tree on paper, then in code.
2. Sections 2–3 (35 min): the trigram model; greedy, beam and exact search on 100 prompts.
3. Section 4 (20 min): the text each method returns; the most probable sentence.
4. Sections 5–6 (30 min): the top 50 of 50,000 with comparison counts; top-p.
5. Section 7 (15 min): Gumbel-max and Gumbel-top-k.
6. TODO cells (20 min): length normalization; your own heap.

- **Expect:** greedy returns AA (0.20), width 2 returns BA (0.36). Optimum found for 54, 71, 83, 94 and 100 of 100 prompts at widths 1, 2, 4, 8 and 16; width 16 computes 8,540 scores per prompt, exact search 395,948. All searches return `the the the ...` (0.08 distinct trigrams; the training text has 0.88). Comparisons: sort 715,841, heap 52,508 (335,937 for ascending input), quickselect 159,732. Nucleus for $p$ = 0.9: 15,996, 2,166 and 6 of 50,000 tokens. Gumbel-max p-value 0.486; the triple test gives 0.047, then 0.821, 0.373, 0.091, 0.252 and 0.313 with new seeds. `np.argpartition` took about 0.09 ms against 0.35 ms for `np.sort` (timing from the saved run; it varies). Runtime about 8 seconds.
- **Common problems:** comparing log-probabilities of outputs with different lengths; reading one p-value below 0.05 as proof of a bug (a correct sampler gives one in twenty runs, so repeat with new data).

### Quiz

1. Why can we search a trigram model exactly but not a transformer?
   - **Answer:** the trigram model's future depends only on the last two characters, so the best prefix for each of the $V^2$ states is enough. A transformer's score depends on the whole prefix.
2. The heap made 52,508 comparisons for scores in random order and 335,937 in ascending order. Why?
   - **Answer:** a score costs $O(\log k)$ extra comparisons only if it replaces the root. In random order that happens about $k \ln(V/k) \approx 345$ times; in ascending order, every time.
3. What do the $k$ largest values of $\log p_i$ plus Gumbel noise give?
   - **Answer:** $k$ different items, distributed exactly as sampling without replacement from $p$.

**Watch out:** "Beam search returns the most probable output, and a wider beam gives better text." Beam search is approximate: in the lab, width 1 missed the optimum for 46 prompts of 100. And the maximum itself is often poor text: the exact optimum was `the the the ...`, and in translation it is often the empty string (Stahlberg & Byrne 2019). Choose the width and the length penalty by measuring quality on held-out data.

### Assignment 7 (due before session 8, 10 points)

1. By hand: in the tree of section 1, change the first step to A 0.6, B 0.3, C 0.1. Give the outputs of greedy, beam search with width 2 and exhaustive search, and the number of scores each computes. (3 points)
2. Complete both TODO cells. Report the sentence for α = 0, 0.6 and 1.0, and your heap's comparison counts for the three input orders. (4 points)
3. Repeat section 3 with $T$ = 40 and widths up to 64. Plot optima found against scores computed, and explain in one paragraph what a wider beam does to the text. (3 points)

Hand in one PDF and your notebook.

### Sources

- Stahlberg & Byrne 2019, On NMT Search Errors and Model Errors: Cat Got Your Tongue? (EMNLP 2019). https://arxiv.org/abs/1908.10090
- Meister, Cotterell & Vieira 2020, If Beam Search is the Answer, What was the Question? (EMNLP 2020). https://arxiv.org/abs/2010.02650
- Wu et al. 2016, Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation. https://arxiv.org/abs/1609.08144
- Fan, Lewis & Dauphin 2018, Hierarchical Neural Story Generation (ACL 2018). https://arxiv.org/abs/1805.04833
- Holtzman et al. 2020, The Curious Case of Neural Text Degeneration (ICLR 2020). https://arxiv.org/abs/1904.09751
- Kool, van Hoof & Welling 2019, Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement (ICML 2019). https://arxiv.org/abs/1903.06059
- Hoare 1961, Algorithm 65: Find. Communications of the ACM 4(7), 321–322. https://doi.org/10.1145/366622.366647
- Blum, Floyd, Pratt, Rivest & Tarjan 1973, Time bounds for selection. Journal of Computer and System Sciences 7(4), 448–461. https://doi.org/10.1016/S0022-0000(73)80033-9

## Session 8: Automata and tries: constrained decoding and structured outputs

**Goal:** students can build a trie and a finite automaton, use them to mask a model's next-token choices so that the output always fits a list or a pattern, and explain the cost and the limits.

### Talking pointers

- **Open with:** "You ask a model for a date and it writes 'some time in March'. You ask for JSON and it forgets a bracket, and the program that reads the answer crashes. Today we make a wrong format impossible, with a trie and a finite automaton."
- **Segment 1, say:** draw the trie of the five district names and cover the letters that are not allowed after `ba`.
- **Segment 2, say:** draw the DFA for `(a|b)*abb`, then show the token `20` crossing two edges of the date automaton.
- **Segment 3, say:** do the two-letter example on the board: the mask gives `ab` with probability 0.5, the model's own conditional distribution gives 0.091.
- **Close with:** "The automaton guarantees the form. It knows nothing about the facts." Then set assignment 8.

### Segment 1 (6 min): masks and tries

- Programs read what models write: a tool call must be valid JSON (Course 4 session 8), a field must be a date, an answer must be one label of a list. A model that writes freely can leave the format at any step.
- **Constrained decoding:** at each step find the tokens that can still lead to a valid output, remove all others, renormalize, then sample or search as in session 7.
- For a list of strings, use a **trie**: one node per prefix. The allowed next characters are the edges that leave the current node, so each step costs one lookup. De Cao et al. (2021) retrieve entities this way: the model generates the entity's name under a beam search constrained by a trie of all valid names.
- In the lab a small model writes a valid district name in 3 of 2,000 samples without the trie and in 2,000 of 2,000 with it.
- **Pause and try:** a trie holds `cat`, `car`, `card` and `dog`. How many nodes does it have, with the root? What is allowed after `car`?
  - **Answer:** 9 nodes: the root, c, a, t, r, d, and d, o, g. After `car`: the letter `d`, or the end of the word.

### Segment 2 (7 min): patterns, automata and tokens

- A pattern such as a date describes too many strings for a trie. Write it as a regular expression and compile it. Thompson's construction (Thompson 1968) gives a nondeterministic finite automaton (NFA) whose size is linear in the pattern. The subset construction (Sipser 2012, chapter 1) makes it deterministic: a DFA reads a string with one table lookup per character.
- The price is a worst case of $2^n$ DFA states for $n$ NFA states. In the lab the date pattern needs only 19 states, but "the 12th character from the end is `a`" needs 4,097.
- Model tokens are several characters long, so one token can cross several edges. A token is allowed only if the automaton can read all of it. Checking every token at every step costs about $V \cdot \ell$ character steps for $V$ tokens of mean length $\ell$.
- Willard & Louf (2023) noticed that the allowed tokens depend only on the DFA state. So compute them once, for every state, with the state each token leads to. Each step is then one lookup. The index costs at most (states) × (total token length) to build; a trie over the vocabulary shares the common prefixes (8,519 against 1,867 character steps in the lab).
- **Pause and try:** a DFA has 19 states and the vocabulary has 50,000 tokens of mean length 4. Bound the cost of building the index token by token. What does each step cost without it?
  - **Answer:** at most 19 × 50,000 × 4 = 3.8 million character steps, once. Without the index, up to 200,000 character steps for every generated token.

### Segment 3 (7 min): limits

- **Nesting needs a stack.** JSON, code and arithmetic nest to any depth, and a finite automaton has finite memory. A stack fixes this: a pushdown automaton, the machine for context-free grammars (Sipser 2012, chapter 2). PICARD parses SQL incrementally and rejects invalid tokens (Scholak et al. 2021); Geng et al. (2023) apply grammar-constrained decoding to many structured tasks; XGrammar runs a pushdown automaton over bytes and precomputes the tokens whose validity does not depend on the stack (Dong et al. 2024).
- **The mask changes the distribution.** Masking step by step does not sample from the model's distribution restricted to valid outputs (Park et al. 2024). In the lab the two differ by a total variation distance of 0.678.
- **Tokens fight templates.** Forcing fixed text can split words into tokens that the model would not choose itself (Beurer-Kellner et al. 2024).
- **Contested:** Tam et al. (2024) report that strict format restrictions lowered reasoning performance. The .txt team, who build such tools, dispute the experiments in a published response. The question is not settled; measure on your own task.
- **Pause and try:** a model writes two letters: first `a` 0.5 or `b` 0.5; after `a`, `a` 0.9 or `b` 0.1; after `b`, 0.5 each. Every string except `aa` is valid. What is the probability of `ab` under the mask, and under the model's conditional distribution?
  - **Answer:** mask: 0.5 × 1 = 0.5. Conditional: 0.05 / (0.05 + 0.25 + 0.25) = 0.091.

### Lab guide (about 2.5 hours, notebook `s08_constrained_decoding.ipynb`)

1. Section 1 (10 min): the trie of five names on paper, then in code.
2. Section 2 (25 min): place names with and without the trie.
3. Section 3 (40 min): the compiler: parser, Thompson NFA, subset construction; the test against `re.fullmatch`; the exponential family.
4. Sections 4–5 (35 min): the (state, token) index; dates, numbers and clock times.
5. Sections 6–7 (25 min): the distortion, computed exactly; brackets and the stack mask.
6. Section 8 and TODO cells (25 min): read the Outlines cell; phone numbers; DFA minimization.

- **Expect:** 5 names, 38 letters, 31 trie nodes. Valid names: 3 of 2,000 without the trie (exact probability 0.0005), 2,000 of 2,000 with it. 0 disagreements with `re.fullmatch` on 4,000 strings for each of five patterns; DFA states 19, 7, 8, 3 and 5; the exponential family reaches 4,097 DFA states from 100 NFA states. Vocabulary 341 tokens; date index 419 allowed pairs of 6,479, built in 8,519 character steps, or 1,867 with the trie. 500 of 500 masked outputs match each pattern and 0 of 500 unmasked ones; 500 dates cost 1,185,632 character steps when scanning, 2,651 lookups with the index (about 0.22 s against 0.06 s, timing from the saved run; it varies). 3 of the 500 dates do not exist, for example 1965-02-30. Distortion: 0.409 for the toy example, 0.678 for the names (`dhaka` 0.397 against 0.042). Bracket DFAs: 5 to 509 states for depths 1 to 7; stack mask 1,000 of 1,000 balanced. Runtime about 5 seconds.
- **Common problems:** a token limit that cuts the output before the automaton accepts (the notebook keeps a token budget; with a library, check why generation stopped); a character of the pattern that is in no token; testing a compiler only on strings that match.

### Quiz

1. Why can the allowed tokens be computed before generation starts?
   - **Answer:** they depend only on the DFA state, not on the text so far. So one table with a row per state covers every possible output.
2. Why can a DFA not check balanced brackets of any depth?
   - **Answer:** it has a fixed number of states, and it needs a different state for every possible stack of open brackets. With two kinds of bracket that is $2^{d+1} - 1$ states for depth $d$.
3. The mask produced `sunamganj` about 1,570 times as often as the model's conditional distribution. Why?
   - **Answer:** the mask renormalizes at each step over the allowed letters only. After the first letters the rest of the name is forced with probability 1, although the model finds those letters unlikely.

**Watch out:** "Constrained decoding makes the model's answer correct." It guarantees the form only. In the lab all 500 generated dates matched the pattern, yet 3 of them do not exist and all of them were random. The mask also changes which valid answers are likely. Measure task accuracy with and without the constraint, and validate the content after parsing it.

### Assignment 8 (due before session 9, 10 points)

1. By hand: draw the trie for `dhaka`, `dinajpur`, `feni`, `faridpur` and `bhola`, and count its nodes. Then build an NFA for `ab*(c|d)` and convert it to a DFA with the subset construction. (3 points)
2. Complete both TODO cells. Report five generated phone numbers, and the number of DFA states before and after minimization for the five patterns. (4 points)
3. Add the 31 names to the story 0, 5 and 50 times and retrain the trigram model each time. Report the probability of a valid name and the total variation distance between the mask and the conditional distribution, and explain the trend. (3 points)

Hand in one PDF and your notebook.

### Sources

- Willard & Louf 2023, Efficient Guided Generation for Large Language Models. https://arxiv.org/abs/2307.09702
- De Cao, Izacard, Riedel & Petroni 2021, Autoregressive Entity Retrieval (ICLR 2021). https://arxiv.org/abs/2010.00904
- Thompson 1968, Programming techniques: Regular expression search algorithm. Communications of the ACM 11(6), 419–422. https://doi.org/10.1145/363347.363387
- Sipser 2012, Introduction to the Theory of Computation, 3rd edition. Cengage.
- Scholak, Schucher & Bahdanau 2021, PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models (EMNLP 2021). https://arxiv.org/abs/2109.05093
- Geng, Josifoski, Peyrard & West 2023, Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning (EMNLP 2023). https://arxiv.org/abs/2305.13971
- Dong et al. 2024, XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models. https://arxiv.org/abs/2411.15100
- Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni 2024, Grammar-Aligned Decoding (NeurIPS 2024). https://arxiv.org/abs/2405.21047
- Beurer-Kellner, Fischer & Vechev 2024, Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation (ICML 2024). https://arxiv.org/abs/2403.06988
- Tam et al. 2024, Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models (EMNLP 2024 Industry Track). https://arxiv.org/abs/2408.02442
- The .txt team's response to Tam et al. (blog post). https://blog.dottxt.ai/say-what-you-mean.html
- Outlines (GitHub repository and documentation). https://github.com/dottxt-ai/outlines

## Session 9: Nearest neighbours I: k-d trees, LSH and MinHash

**Goal:** students can explain why exact nearest-neighbour search fails in high dimensions, build locality-sensitive hash indexes for cosine and Jaccard similarity, and find near-duplicate documents in a corpus.

### Talking pointers

- **Open with:** "Find the stored vector closest to this one. Retrieval asks that for every question, and the search tree you know stops working at about ten dimensions. Today we see why, and what replaces it."
- **Segment 1, say:** draw one k-d tree split and the circle around the query, then show the table: 0.10% of the points examined in 2 dimensions, 99.30% in 16.
- **Segment 2, say:** draw two vectors and a random line through the origin: the bits differ only if the line passes between them.
- **Segment 3, say:** do the MinHash of {a, c, d} and {a, d, e, f} under three orders on the board.
- **Close with:** "Today's hash functions bring similar things together, and every candidate is then checked exactly." Then set assignment 9.

### Segment 1 (6 min): exact search and the curse of dimensionality

- The **nearest-neighbour problem**: given $n$ points and a query, return the closest point. Retrieval needs it (the notebook of Course 4 session 8 scores every note for each question), and so does duplicate detection.
- **Brute force** computes $n$ distances of $d$ operations each: $O(n \cdot d)$ per query, always exact.
- A **k-d tree** (Bentley 1975) splits the points at the median of one coordinate, level after level. A search skips every subtree whose splitting plane is farther away than the best point so far. For a fixed, small number of dimensions the expected cost is $O(\log n)$ (Friedman, Bentley & Finkel 1977).
- As $d$ grows, distances **concentrate**: the farthest point is hardly farther than the nearest (Beyer et al. 1999), and the skipping test fails. In the lab the tree examines 0.10% of 20,000 points in 2 dimensions, 6.43% in 8 and 99.30% in 16.
- For embeddings we accept **approximate** answers and report **recall**: the share of the true neighbours returned.
- **Pause and try:** an index holds 1 million vectors of 768 dimensions. How many multiplications does a brute-force query need, and how long is that at $10^9$ per second?
  - **Answer:** 1,000,000 × 768 = 768 million, about 0.8 seconds per query.

### Segment 2 (7 min): hash functions that keep neighbours together

- **Locality-sensitive hashing** (LSH; Indyk & Motwani 1998): hash so that near points collide more often than far points, and look only in the query's bucket.
- For cosine similarity, one bit says on which side of a **random hyperplane** the vector lies (Charikar 2002). Two vectors at angle $\theta$ get the same bit with probability $p = 1 - \theta/\pi$.
- One bit separates weakly, so **amplify**: $k$ bits form the key of a table (AND), and $L$ tables give $L$ chances (OR). A point becomes a **candidate** with probability $1 - (1 - p^k)^L$, an S-curve in the similarity.
- Compute the exact similarity for the candidates only: a query costs $k \cdot L$ dot products for hashing plus one per candidate. No single query has a guarantee: in the lab, $k = 12$ and $L = 64$ returned 0.896 of the true top 10 for 6.13% of the work of brute force.
- **Pause and try:** two vectors are at 60 degrees. What is the probability of the same bit? Of the same 8-bit key? Of sharing a bucket in at least one of 16 tables?
  - **Answer:** $1 - 60/180 = 0.667$; $0.667^8 = 0.039$; $1 - (1 - 0.039)^{16} = 0.471$.

### Segment 3 (7 min): MinHash and near-duplicate documents

- A document becomes the set of its **shingles** (every run of five characters). The **Jaccard similarity** of two sets is $|A \cap B| / |A \cup B|$.
- **MinHash** (Broder 1997): order all items at random; the min-hash of a set is its first item. Two sets share it with probability equal to their Jaccard similarity $J$. A hash function $(a x + b) \bmod p$ (session 2) replaces the random order, and $K$ of them give a **signature** that estimates $J$ with standard error $\sqrt{J(1 - J)/K}$.
- **Banding** (Leskovec et al. 2020, chapter 3): cut the signature into $b$ bands of $r$ rows. Two documents are candidates if they agree on a whole band: probability $1 - (1 - s^r)^b$. Check the candidates exactly, then join the pairs into groups with **union–find**, in almost linear time (Tarjan 1975).
- Web crawlers use SimHash, a fingerprint built on random hyperplanes (Manku et al. 2007). For language-model training data, Lee et al. (2022) use MinHash and then an edit-similarity check (session 5), and a suffix array for exact repeats of 50 tokens or more.
- Course 5 session 3 removes exact duplicates with a hash; Course 4 session 3 treats deduplication as a design decision; Course 6 session 4 measures how duplicates across folds inflate a score.
- **Pause and try:** signatures have 20 bands of 5 rows. With what probability is a pair with Jaccard similarity 0.8 a candidate? A pair with 0.3?
  - **Answer:** $1 - (1 - 0.8^5)^{20} = 1 - 0.672^{20} = 0.9996$, and $1 - (1 - 0.3^5)^{20} = 0.047$.

### Lab guide (about 2.5 hours, notebook `s09_trees_and_lsh.ipynb`)

1. Section 1 (10 min): MinHash of two small sets on paper, then all 720 orders in code.
2. Section 2 (30 min): the k-d tree; points examined against dimension.
3. Section 3 (40 min): random hyperplanes; the index on 20,000 vectors; recall against work.
4. Section 4 (25 min): MinHash with hash functions; banding.
5. Section 5 (35 min): the corpus: shingles, candidate pairs, exact check, union–find.
6. Section 6 and TODO cells (20 min): read the `datasketch` cell; SimHash; $k$ nearest neighbours in the tree.

- **Expect:** the min-hashes agree in 288 of 720 orders (0.40). The k-d tree examines 19.0, 76.9, 1,285.3, 19,859.9 and 20,000 points in 2, 4, 8, 16 and 32 dimensions, and 3,124.6 on the 4-dimensional sheet; the farthest-to-nearest ratio falls from 293.60 to 1.77. LSH with $k$ = 12, $L$ = 64: 457.7 candidates, recall 0.896. MinHash error at $J$ = 0.5: 0.1214 with 16 hash functions, 0.0163 with 1,024. Corpus: 7,591 candidate pairs of 1,999,000 (formula 8,801; 4,475 to 11,567 in ten more indexes); 559 of the 574 true pairs found (0.974); against the 666 planted pairs, recall 0.839 for pairs and 0.925 for the 197 groups, precision 1.000. The tree took about 0.02 ms per query in 2 dimensions and 13 to 15 ms from 16 on (timing from the saved run; it varies). Runtime about 25 seconds.
- **Common problems:** making shingle ids with Python's `hash()`, which changes from run to run; skipping the exact check (7,032 of the 7,591 candidates were false); judging an index by speed without its recall.

### Quiz

1. Why does a k-d tree examine almost every point in 64 dimensions?
   - **Answer:** it skips a subtree only if the splitting plane is farther away than the best point so far. In 64 dimensions the nearest point is almost as far as all the others (ratio 1.77 in the lab), so the test almost never succeeds.
2. An LSH index has too low a recall. Name two changes that raise it, and the cost of each.
   - **Answer:** fewer bits per table: larger buckets, so more candidates to check. More tables: more hashing per query and more memory.
3. Banding with 20 bands of 5 rows found 559 of the 574 pairs with similarity at least 0.6. Which pairs did it miss?
   - **Answer:** pairs with similarity from 0.60 to 0.70. There $1 - (1 - s^5)^{20}$ is between 0.80 and 0.97, so a true pair sometimes shares no band.

**Watch out:** "A k-d tree makes nearest-neighbour search logarithmic." The $O(\log n)$ is an expected cost for a fixed, small number of dimensions. In the lab the same tree examined 0.10% of the points in 2 dimensions and all of them in 32, and our Python version was then slower than brute force. For embeddings, use an approximate index and report its recall (session 10).

### Assignment 9 (due before session 10, 10 points)

1. By hand: for A = {1, 2, 4} and B = {2, 4, 5, 6}, give the Jaccard similarity, both signatures under $h(x)$ = (2x + 1) mod 7, (3x + 4) mod 7 and (5x + 2) mod 7, and the estimate. (3 points)
2. Complete both TODO cells. Report the Hamming distances of the SimHash fingerprints for planted and for random pairs, and the points examined for $k$ = 10 in 2 and in 16 dimensions. (4 points)
3. In section 5, change the banding to 25 bands of 4 rows and to 10 bands of 10 rows. Report candidate pairs, recall and group recall. Which setting would you choose for 10 million documents, and why? (3 points)

Hand in one PDF and your notebook.

### Sources

- Bentley 1975, Multidimensional binary search trees used for associative searching. Communications of the ACM 18(9), 509–517. https://doi.org/10.1145/361002.361007
- Friedman, Bentley & Finkel 1977, An algorithm for finding best matches in logarithmic expected time. ACM Transactions on Mathematical Software 3(3), 209–226.
- Beyer, Goldstein, Ramakrishnan & Shaft 1999, When is "nearest neighbor" meaningful? (ICDT 1999, LNCS 1540), 217–235. https://doi.org/10.1007/3-540-49257-7_15
- Indyk & Motwani 1998, Approximate nearest neighbors: towards removing the curse of dimensionality (STOC 1998), 604–613. https://doi.org/10.1145/276698.276876
- Charikar 2002, Similarity estimation techniques from rounding algorithms (STOC 2002), 380–388. https://doi.org/10.1145/509907.509965
- Broder 1997, On the resemblance and containment of documents. Proceedings of Compression and Complexity of Sequences 1997, 21–29. https://doi.org/10.1109/SEQUEN.1997.666900
- Leskovec, Rajaraman & Ullman 2020, Mining of Massive Datasets, 3rd edition, chapter 3 (Finding Similar Items). http://www.mmds.org/
- Manku, Jain & Das Sarma 2007, Detecting near-duplicates for web crawling (WWW 2007), 141–150. https://doi.org/10.1145/1242572.1242592
- Lee et al. 2022, Deduplicating Training Data Makes Language Models Better (ACL 2022). https://arxiv.org/abs/2107.06499
- Tarjan 1975, Efficiency of a good but not linear set union algorithm. Journal of the ACM 22(2), 215–225. https://doi.org/10.1145/321879.321884
- datasketch (GitHub repository and documentation). https://github.com/ekzhu/datasketch

## Session 10: Nearest neighbours II: HNSW, IVF and product quantization

**Goal:** students can build a graph index and a quantized index for vector search, measure recall against work and memory, and choose index settings for a retrieval system.

### Talking pointers

- **Open with:** "Session 9 ended badly: in high dimensions an exact index looks at every point. A vector database answers quickly anyway, with a graph, a partition and a compressed code, and without a guarantee. Today we build all three and measure what we lose."
- **Segment 1, say:** walk greedily on the six-node graph on the board, get stuck at D, then widen the search to `ef` = 3.
- **Segment 2, say:** cut a vector of 32 numbers into 8 parts and replace each part by one byte.
- **Segment 3, say:** show the summary table and ask which index the class would choose for 10 million vectors.
- **Close with:** "An index returns near neighbours, not the nearest ones. How near is a number that you must measure." Then set assignment 10.

### Segment 1 (7 min): search on a graph

- A **proximity graph** links every vector to some vectors near it. To search, start at an entry node and walk to the neighbour closest to the query, until no neighbour is closer. The walk can stop at a **local minimum**.
- **Best-first search** keeps the best `ef` nodes found, with the two heaps of session 7: a min-heap of candidates to expand, and a max-heap of at most `ef` results. It stops when the closest candidate is farther than the worst result. A larger `ef` costs more distance computations and gives higher recall.
- A graph built by inserting points one at a time keeps long links from its early days. They make it **navigable**: Kleinberg (2000) showed when greedy routing on such small-world graphs needs few steps.
- **HNSW** (Malkov & Yashunin 2020) adds layers, as in a skip list (Pugh 1990). Each point gets a random top layer; the upper layers are sparse; a search walks down greedily and uses `ef` only in layer 0. A node keeps at most $M$ links ($2M$ in layer 0), chosen to point in different directions. `efConstruction` is the `ef` used during the build.
- Nothing is guaranteed: recall is measured, not proved. In the lab HNSW reached recall 0.969 with 407 distance computations instead of 20,000. The layers alone saved only about 30 of them; the rule for choosing links mattered more.
- **Pause and try:** with $M$ = 8, each layer keeps about one point in 8 of the layer below. For 20,000 points, about how many are in layers 1, 2 and 3?
  - **Answer:** about 2,500, 312 and 39. The lab got 2,466, 294 and 33.

### Segment 2 (7 min): partition and compress

- **Inverted file (IVF):** k-means gives `nlist` centroids, and each vector goes into the list of its nearest centroid. A query scans only the `nprobe` nearest lists. In the lab, with 128 lists, `nprobe` = 1 gave recall 0.521 and `nprobe` = 4 gave 0.970 after scanning 3.19% of the vectors.
- **Product quantization** (PQ; Jégou et al. 2011) compresses the vectors themselves. Cut each vector into $m$ parts. For each part, train a codebook of 256 centroids with k-means, and store the number of the nearest centroid: one byte. A vector then costs $m$ bytes. A 768-dimensional float32 vector takes 3,072 bytes; with $m$ = 64 it takes 64.
- **Distances from tables:** for a query, compute the distance from each of its $m$ parts to the 256 centroids of that part. The approximate distance to any stored vector is the sum of $m$ table entries.
- The codes mix up close neighbours: with 8 bytes, recall from the codes alone was 0.526. So take a short list by code and **re-rank** it with the exact vectors: 0.994 for a list of 100.
- Course 11 session 3 quantizes each number of a tensor to 8 bits. PQ quantizes groups of numbers together, with learned codebooks.
- **Pause and try:** vectors have 32 dimensions and $m$ = 8. How many bytes are the codebooks? How many different points can the codes represent?
  - **Answer:** 8 × 256 centroids × 4 coordinates × 4 bytes = 32,768 bytes. $256^8 = 2^{64}$, about $1.8 \times 10^{19}$ points.

### Segment 3 (6 min): choosing an index

- Judge an index by recall@k, queries per second, memory and build time. ANN-Benchmarks compares libraries this way (Aumüller et al. 2019).
- FAISS combines the pieces of this session, for example IVF with PQ codes (Johnson et al. 2021; Douze et al. 2024). DiskANN keeps a graph and the full vectors on an SSD and only compressed vectors in memory (Subramanya et al. 2019). Guo et al. (2020) train the quantizer for inner-product search.
- Deletes, updates and filters are harder for graphs: the FAISS documentation says that its HNSW index does not support removing vectors, and a strict filter can remove the nodes a search would walk through.
- In retrieval-augmented generation (Lewis et al. 2020; Course 4 session 8) the model cannot use a passage that the index did not return. The recall of the index limits the whole system.
- Use one similarity (cosine, inner product or L2) from training to index to query. On unit vectors all three give the same order.
- **Pause and try:** 10 million vectors of 768 dimensions. How much memory as float32? As PQ codes with $m$ = 64?
  - **Answer:** $10^7$ × 3,072 bytes = 30.7 GB. With PQ, $10^7$ × 64 bytes = 640 MB, plus the codebooks.

### Lab guide (about 2.5 hours, notebook `s10_vector_indexes.ipynb`)

1. Section 1 (10 min): the greedy walk on the six-node graph, on paper and in code.
2. Section 2 (10 min): the data and the brute-force ground truth.
3. Section 3 (40 min): best-first search with two heaps; the flat graph; the `ef` sweep.
4. Section 4 (35 min): HNSW; two controlled comparisons; the table at equal recall.
5. Sections 5–6 (35 min): IVF and `nprobe`; product quantization and re-ranking.
6. Sections 7–8 and TODO cells (25 min): the summary table; the FAISS and hnswlib cell; IVF with PQ; deleting from a graph.

- **Expect:** the walk stops at D (5); `ef` = 3 finds F (1). Flat graph: 16.0 links per node, largest 298; recall 0.840 to 0.999 for 379.6 to 1,069.8 distance computations. HNSW: recall 0.702 to 0.997 for 179.5 to 806.5. Distance computations at recall 0.95: 516 (flat graph), 371 (HNSW), 399 (HNSW without the descent), 485 (nearest rule); at 0.99: 740, 568, 596, not reached. IVF: recall 0.521, 0.793, 0.970 and 0.991 for `nprobe` 1, 2, 4 and 8. PQ with 4, 8 and 16 bytes: 0.228, 0.526 and 0.857 from the codes alone; 0.795, 0.994 and 1.000 after re-ranking. Bytes per vector: 128 (brute force), 192.0 (flat graph), 172.4 (HNSW). A graph query at `ef` = 50 took about 0.6 ms and brute force 2.6 ms (timing from the saved run; it varies). Runtime about 50 seconds.
- **Common problems:** comparing indexes at equal `ef` instead of equal recall; computing recall against another index instead of brute force; building the index with one similarity and querying with another.

### Quiz

1. Why does best-first search use two heaps?
   - **Answer:** the min-heap gives the closest candidate to expand next. The max-heap gives the worst of the best `ef` results, the one to beat and to remove. The search stops when the first is farther than the second.
2. With `nprobe` = 1, IVF returned 0.521 of the true neighbours. Where were the others?
   - **Answer:** in neighbouring cells. A query near a cell border has true neighbours on the other side; scanning 4 cells raised recall to 0.970.
3. PQ with 8 bytes gave recall 0.526 from the codes alone and 0.994 after re-ranking 100. Why does re-ranking help so much?
   - **Answer:** the codes are too coarse to order close neighbours, but good enough to put the true top 10 among the best 100. Exact distances then order those 100 correctly.

**Watch out:** "A vector database returns the nearest neighbours." It returns near neighbours, and how near depends on the index and its settings: in the lab, the same data gave recall from 0.228 to 1.000. A neighbour that the index missed looks exactly like a neighbour that does not exist. Measure recall against brute force on a sample of your own queries.

### Assignment 10 (due before session 11, 10 points)

1. By hand, on the six-node graph: add the link D–F and repeat the greedy walk from A for the query (6, 4). Then, on the original graph, run best-first search with `ef` = 2 from A for the query (4, 0), and write both heaps after each step. (3 points)
2. Complete both TODO cells. Report recall@10 with the approximate and exact distance computations of IVF with PQ for `nprobe` = 1, 4 and 16, and the recall after each way of deleting. (4 points)
3. Build HNSW with $M$ = 4 and $M$ = 16. Plot recall against distance computations for the three values of $M$, give the bytes per vector, and say which $M$ you would choose for recall 0.95. (3 points)

Hand in one PDF and your notebook.

### Sources

- Malkov & Yashunin 2020, Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (IEEE TPAMI). https://arxiv.org/abs/1603.09320
- Kleinberg 2000, The small-world phenomenon: an algorithmic perspective (STOC 2000), 163–170. https://doi.org/10.1145/335305.335325
- Pugh 1990, Skip lists: a probabilistic alternative to balanced trees. Communications of the ACM 33(6), 668–676. https://doi.org/10.1145/78973.78977
- Jégou, Douze & Schmid 2011, Product quantization for nearest neighbor search. IEEE Transactions on Pattern Analysis and Machine Intelligence 33(1), 117–128. https://doi.org/10.1109/TPAMI.2010.57
- Aumüller, Bernhardsson & Faithfull 2019, ANN-Benchmarks: A benchmarking tool for approximate nearest neighbor algorithms. Information Systems. https://doi.org/10.1016/j.is.2019.02.006
- Johnson, Douze & Jégou 2021, Billion-scale similarity search with GPUs. IEEE Transactions on Big Data 7(3), 535–547. https://arxiv.org/abs/1702.08734
- Douze et al. 2024, The Faiss library. https://arxiv.org/abs/2401.08281
- Subramanya et al. 2019, DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node (NeurIPS 2019). https://papers.nips.cc/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html
- Guo et al. 2020, Accelerating Large-Scale Inference with Anisotropic Vector Quantization (ICML 2020). https://arxiv.org/abs/1908.10396
- Lewis et al. 2020, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS 2020). https://arxiv.org/abs/2005.11401
- Faiss wiki (documentation of the FAISS indexes). https://github.com/facebookresearch/faiss/wiki
- hnswlib (GitHub repository and documentation). https://github.com/nmslib/hnswlib

## Session 11: Serving models: caches, queues and batching

**Goal:** students can explain the KV cache as memoization, implement an LRU cache and a prefix tree that shares cached prompts, and simulate batching policies for a model server.

### Talking pointers

- **Open with:** "One user and one model is a function call. Ten thousand users and one model is a cache and a queue, and you know both from your data structures course."
- **Segment 1, say:** write the two sums on the board, then show the count for 512 tokens: 44,870,400 scores against 131,328.
- **Segment 2, say:** run LRU by hand on `A B A C A B` with two places, then draw two prompts with the same system prompt as one tree.
- **Segment 3, say:** draw 8 slots as rows and steps as columns; fill them as static batches, then continuously.
- **Close with:** "Keep what you have computed, and never let a free slot wait." Then set assignment 11.

### Segment 1 (6 min): the KV cache is memoization

- A decoder produces one token per step (session 7). Without a cache, step $t$ runs attention again over all $t$ tokens: a $t \times t$ table of scores in every layer. So $n$ tokens cost $1^2 + 2^2 + \dots + n^2 \approx n^3/3$ scores per layer.
- A decoder is causal: a token looks only backwards, so the key and the value of an earlier token never change. Store them (the KV cache), and step $t$ computes one row of $t$ scores: about $n^2/2$ in all.
- This is memoization (session 5): the same output for less work and more memory. Course 4 session 4 builds and times a KV cache; Course 11 session 8 computes its size in bytes.
- **Pause and try:** how many scores per layer does it cost to produce 100 tokens, without and with the cache?
  - **Answer:** without: 100 × 101 × 201 / 6 = 338,350. With: 100 × 101 / 2 = 5,050, which is 67 times fewer.

### Segment 2 (7 min): caches across requests, and what to evict

- Many prompts start with the same tokens: a system prompt, examples, a long document. A prefix's stored entries do not depend on what follows, so the next request can reuse them (Gim et al. 2024).
- Keep them in a prefix tree over token ids and reuse the longest stored prefix. SGLang's RadixAttention is a radix tree with least-recently-used (LRU) eviction of leaves (Zheng et al. 2024). One changed token invalidates everything after it, so put the parts that change at the end. Commercial APIs sell this as prompt caching (for example Anthropic's, as of November 2026).
- Limited memory means eviction. An LRU cache is a hash map (session 2) plus a doubly linked list: `get` and `put` in expected $O(1)$.
- Belady's rule evicts the item whose next use is furthest away: optimal, but it needs the future (Belady 1966). LRU has at most about $k$ times as many misses with the same $k$ places, and no deterministic rule without the future has a better guarantee (Sleator & Tarjan 1985). The lab measures 1.29–1.66 on a Zipf workload and 7.95 on the worst trace for $k = 8$.
- vLLM keeps each sequence's keys and values in fixed-size blocks found through a block table, like the pages of an operating system (Kwon et al. 2023).
- **Pause and try:** an LRU cache has 3 places. The trace is `A B C A D B`. Which requests are hits, and what does Belady's rule do differently?
  - **Answer:** only the fourth request (A) is a hit. When D arrives, LRU evicts B, the least recently used item, and the next request misses. Belady's rule evicts A or C, which are never requested again, and gets 2 hits.

### Segment 3 (7 min): queues and batching

- A graphics processor (GPU) handles a batch in much less time than the same sequences one after another. Shorter sequences are padded to the longest. If the lengths are known, sort by length first (Course 6 session 9): the lab's padding falls from 0.803 of the token places to 0.036.
- Output lengths are not known in advance. **Static batching** runs a batch until its longest sequence ends: finished slots compute padding, and new requests wait.
- **Continuous batching**: after every step, finished sequences leave and waiting requests join. Orca introduced this as iteration-level scheduling (Yu et al. 2022); the name came later, and servers such as vLLM use it.
- In our simulation (not a real server), static batches used 0.321 of the slot places for tokens and continuous batching 0.994. At load 0.5 static batching could not keep up with the arrivals.
- Fuller batches raise throughput but can make each request slower. Measure throughput, the wait for the first token and the 95th-percentile latency, not only the mean (Course 15 session 9). A priority queue serves interactive requests first; background requests can starve unless waiting raises their priority.
- **Pause and try:** a static batch holds four sequences that need 10, 20, 30 and 100 tokens. How many slot places are computed, and what share produces a token?
  - **Answer:** 4 × 100 = 400 slot places for 160 tokens: 40%. With continuous batching the first slot is free again after step 10.

### Lab guide (about 2 hours, notebook `s11_caches_queues_batching.ipynb`)

1. Section 1 (10 min): both traces on paper, then the code.
2. Section 2 (25 min): the count table; the changed token.
3. Sections 3–4 (30 min): the LRU class; four eviction rules; the worst trace.
4. Section 5 (20 min): the prefix tree, reuse against capacity.
5. Sections 6–7 (25 min): padding; the simulator.
6. Section 8 and the TODO cells (20 min): read the vLLM cell (not run); priorities; a paged allocator.

- **Expect:** for 512 tokens, 44,870,400 scores per layer without the cache and 131,328 with it; same tokens, logits within 1.8e-14. About 6 pointer writes per request for the LRU class; 14.2 to 382.6 items examined by the list. Hit rates at capacity 64: LRU 0.373, FIFO 0.324, Belady 0.572; on the cycle LRU misses 9,000 requests, Belady 1,132. Prefix tree: 0.166, 0.921 and 0.959 of prompt tokens reused with 500, 8,000 and 16,000 places. Backlog: 41,861 steps static, 13,532 continuous. Mean latency at loads 0.2, 0.5 and 0.8: 152.5, 6,588.7 and 11,898.7 steps static; 53.8, 54.3 and 64.1 continuous. Peak memory: 4,096 places reserved, 1,296 in blocks. Without the cache, 512 tokens took about 4.44 s against 0.02 s (timing from the saved run; it varies). Runtime about 10 seconds.
- **Common problems:** forgetting to move an item to the front on a hit (LRU becomes FIFO); reading the simulator's steps as seconds on a real server; quoting static latencies at loads that static batching cannot serve (they grow with the length of the run).

### Quiz

1. Why does a KV cache not change the output?
   - **Answer:** a token attends only to earlier tokens, so its key and value do not depend on later ones. The stored values are the ones the model would compute again.
2. Why does an LRU cache need both a hash map and a linked list?
   - **Answer:** the hash map finds an item in expected $O(1)$; the doubly linked list keeps the order of use and moves a node in $O(1)$. With only one of them, one operation costs $O(k)$.
3. In the simulation, why could static batching not serve load 0.5?
   - **Answer:** only 0.321 of its slot places produce tokens, so its capacity is about a third of the server's. A higher load makes the queue grow.

**Watch out:** "A cache hit can change the model's answer." A KV cache or a prefix cache stores exactly what the model would compute again, so the output is the same up to floating-point rounding ($1.8 \times 10^{-14}$ in the lab). A cache changes cost and waiting, not content. It is valid only for an identical prefix: after one different token, everything must be computed again.

### Assignment 11 (due before session 12, 10 points)

1. By hand: LRU, FIFO and Belady's rule with 3 places on the trace `A B C D A B E A B C D E`: the cache after each request and the hits. Then repeat FIFO and LRU with 4 places and say what is surprising. (3 points)
2. Complete both TODO cells. Report the mean latency and the longest wait of each class, with and without ageing, and check your allocator's peak against the 1,296 token places of section 7. (4 points)
3. In section 5, store only the system prompt and the example block of each request, not the question. Report the share reused at 4,000 and 8,000 places against the notebook's 0.708 and 0.921, and explain the difference. (3 points)

Hand in one PDF and your notebook.

### Sources

- Kwon et al. 2023, Efficient Memory Management for Large Language Model Serving with PagedAttention (SOSP 2023). https://arxiv.org/abs/2309.06180
- Yu et al. 2022, Orca: A Distributed Serving System for Transformer-Based Generative Models (OSDI 2022), 521–538. https://www.usenix.org/conference/osdi22/presentation/yu
- Zheng et al. 2024, SGLang: Efficient Execution of Structured Language Model Programs (NeurIPS 2024). https://arxiv.org/abs/2312.07104
- Gim et al. 2024, Prompt Cache: Modular Attention Reuse for Low-Latency Inference (MLSys 2024). https://arxiv.org/abs/2311.04934
- Sleator & Tarjan 1985, Amortized efficiency of list update and paging rules. Communications of the ACM 28(2), 202–208. https://doi.org/10.1145/2786.2793
- Belady 1966, A study of replacement algorithms for a virtual-storage computer. IBM Systems Journal 5(2), 78–101. https://doi.org/10.1147/sj.52.0078
- vLLM, README and documentation (PagedAttention, continuous batching, automatic prefix caching), read in November 2026. https://github.com/vllm-project/vllm
- Anthropic, Prompt caching (API documentation), read in November 2026. https://platform.claude.com/docs/en/build-with-claude/prompt-caching

## Session 12: Randomized algorithms for data pipelines, and the capstone

**Goal:** students can sample uniformly from a stream, shuffle correctly, draw from a large discrete distribution in constant time, and plan a capstone that combines the course's data structures.

### Talking pointers

- **Open with:** "A file has a billion lines and you have memory for a thousand. Choose a thousand lines so that every line has the same chance, in one pass."
- **Segment 1, say:** do the four-item stream on the board with fractions, then count the 27 outcomes of the wrong shuffle.
- **Segment 2, say:** draw an alias table for four items as four columns of equal width, then a sum tree with four leaves.
- **Segment 3, say:** read the map of the course row by row, then show the capstone rubric.
- **Close with:** "Every structure in this course has a cost you can state and a count you can measure. In the capstone, do both." Then set assignment 12.

### Segment 1 (7 min): streams and shuffles

- **Reservoir sampling** (Vitter 1985) keeps $k$ items from a stream of unknown length: keep the first $k$; item number $i$ enters with probability $k/i$ and replaces a random place. Every item ends in the sample with probability $k/n$, by induction: an older item has probability $k/(n-1)$ and survives item $n$ with probability $1 - 1/n$. One pass, $O(k)$ memory.
- The **Fisher–Yates shuffle** (Durstenfeld 1964) goes from the last position down and swaps position $i$ with a random position from 0 to $i$: $n!$ equally likely results in $O(n)$ time. The common bug swaps every position with any position. Its $n^n$ equally likely sequences of choices cannot spread evenly over $n!$ orders: 27 over 6 for three items.
- Data that does not fit in memory passes through a **shuffle buffer**, as in `tf.data`: output a random item of a buffer of $B$ items and refill it from the stream. An example moves at most $B - 1$ places earlier, so a small buffer leaves sorted data almost sorted. In the lab, a buffer of 128 on sorted digits gave 4.03 classes in a batch instead of 9.65, and an accuracy of 0.546 instead of 0.863.
- **Pause and try:** a reservoir of $k = 2$ reads a stream of 5 items. What is the probability that the third item is in the final sample?
  - **Answer:** it enters with probability 2/3, survives item 4 with 1 − (2/4)(1/2) = 3/4 and item 5 with 4/5. The product is 2/5, which is $k/n$.

### Segment 2 (7 min): sampling from a discrete distribution

- To draw one of $V$ items with given probabilities, a linear scan costs $O(V)$ per sample in the worst case and binary search on the cumulative sums $O(\log V)$. The **alias method** costs $O(1)$ after an $O(V)$ set-up (Walker 1977; Vose 1991): $V$ columns of equal width with at most two items each; choose a column, then toss a biased coin.
- Negative sampling in word2vec draws noise words in proportion to the word count to the power 3/4 (Mikolov et al. 2013).
- If the weights change after every draw, use a **sum tree**: every parent holds the sum of its children, so an update and a sample cost $O(\log n)$. Prioritized experience replay uses it (Schaul et al. 2016; Course 3 session 10 covers reinforcement learning).
- Weighted sampling without replacement from a stream: give each item the key $u^{1/w}$ and keep the $k$ largest keys with a heap (Efraimidis & Spirakis 2006). It is the Gumbel-top-k trick of session 7 in another form (Kool et al. 2019).
- Test a sampler with a chi-square test and fixed seeds. A correct sampler still gives a p-value below 0.05 once in twenty tests, as the lab's sum tree did (0.037; Course 1 session 9).
- **Pause and try:** a vocabulary has 100,000 words. How many probabilities does one sample look at with a linear scan in the worst case, with binary search, and with an alias table?
  - **Answer:** 100,000; about $\log_2 100{,}000 \approx 17$; and one table row, whatever the size of the vocabulary.

### Segment 3 (6 min): a map of the course, and the capstone

- Which structure for which problem, with the cost to remember:

| Session | Problem | Cost |
|---|---|---|
| 1. Counting cost: arrays, memory and Big-O for models | growing a list; sparse data | append amortized $O(1)$; sparse product $O(\text{nnz})$ |
| 2. Hashing: dictionaries, the hashing trick and Bloom filters | token to id; "seen before?" | expected $O(1)$, worst case $O(n)$ |
| 3. Tokenizers: byte-pair encoding with heaps, linked lists and tries | training a tokenizer | $O(N \log M)$, not $O(N \cdot M)$ |
| 4. Computation graphs: topological sort and automatic differentiation | gradients | $O(V + E)$ |
| 5. Dynamic programming I: edit distance and alignment | error rates | $O(m \cdot n)$ |
| 6. Dynamic programming II: Viterbi, the forward algorithm and CTC | best path; CTC loss | $O(T \cdot S^2)$; CTC $O(T \cdot L)$ |
| 7. Decoding: heaps, beam search and sampling | top $k$ of $V$ scores | heap: $O(V \log k)$ worst case |
| 8. Automata and tries: constrained decoding and structured outputs | valid formats | one table lookup per step |
| 9. Nearest neighbours I: k-d trees, LSH and MinHash | near-duplicates | candidates, not all $n(n-1)/2$ pairs |
| 10. Nearest neighbours II: HNSW, IVF and product quantization | vector search | no guarantee: measure recall |
| 11. Serving models: caches, queues and batching | repeated work | $n^2/2$ scores, not $n^3/3$; LRU expected $O(1)$ |

- The capstone (see the syllabus): a small search system over texts that you may use, with at least four of these structures. For each part, state the cost with its case and measure it with an exact count. Evaluate quality honestly, and present the system in a 10-minute video.
- **Pause and try:** your capstone searches 50,000 notes stored as vectors of dimension 384. What does one brute-force query cost, and what must you measure if an index of session 10 replaces it?
  - **Answer:** 50,000 × 384 = 19.2 million multiply–adds, which may be fast enough: measure first. An index is approximate, so report recall@10 against the brute-force answers.

### Lab guide (about 2 hours, notebook `s12_sampling_and_shuffling.ipynb`)

1. Section 1 (10 min): the four-item stream on paper.
2. Sections 2–3 (25 min): the reservoir test and its bug; the two shuffles.
3. Section 4 (25 min): the shuffle buffer on sorted digits.
4. Sections 5–6 (30 min): scan, binary search and alias; the sum tree.
5. Section 7 (10 min): weighted reservoir sampling against Gumbel-top-k.
6. Section 8 and the TODO cells (20 min): read the `tf.data` cell (not run); shards; the capstone plan table.

- **Expect:** reservoir: corrected chi-square 83.8 (p-value 0.864); with the bug 307.7 (3.08e-23). Shuffles: Fisher–Yates p-value 0.519, naive chi-square 808.75. Buffers of 1, 8, 32, 128, 512 and 1,300: 1.22, 1.32, 1.97, 4.03, 7.87 and 9.65 classes in a batch; accuracy 0.101, 0.149, 0.163, 0.546, 0.880 and 0.863. For $V$ = 100,000: 20,487.0 probabilities examined by the scan, 16.71 probes, 1 row. Alias test ($V$ = 1,000): p-value 0.532. Sum tree: 11 nodes per update; p-value 0.037, then 0.182 to 0.665 with five new seeds. Weighted reservoir: the same choice as Gumbel-top-k in 200,000 of 200,000 runs; p-value 0.844. A million draws for $V$ = 100,000 took about 20.5 ms with the alias table against 103.6 ms with `np.searchsorted` (timing from the saved run; it varies). Runtime about 14 seconds.
- **Common problems:** `randrange(i)` where `randrange(i + 1)` is needed; a plain chi-square test on the $k$ items of one run, which are not independent; reading one p-value below 0.05 as a bug.

### Quiz

1. Why can the naive shuffle of three items not be fair?
   - **Answer:** it has 27 equally likely sequences of choices and 6 orders, and 27 is not a multiple of 6.
2. Sorted data passes through a shuffle buffer of 128 examples. Why do the batches still hold few classes?
   - **Answer:** an example moves at most 127 places earlier, so a batch draws mostly from the buffer, which is about one class long in the lab.
3. When do you use an alias table, and when a sum tree?
   - **Answer:** an alias table for fixed weights: $O(1)$ per sample after $O(V)$ set-up. A sum tree when weights change between draws: $O(\log n)$ per update and per sample.

**Watch out:** "A shuffle buffer of 1,000 examples shuffles the dataset." A buffer mixes only examples that are near each other in the stream, because an example moves at most $B - 1$ places earlier. On a million examples sorted by class, a buffer of 1,000 changes almost nothing. Shuffle the order of the files first, and use a buffer several times longer than a run of similar examples: in the lab, 512 was enough for runs of 130.

### Assignment 12 (due with the capstone, 10 points)

1. The capstone plan table (the last TODO cell): at least four structures of the course. For each, give the session, the cost with its case (worst, expected or amortized), the exact count you will measure, and how you will judge quality. (4 points)
2. One page: the texts you will use and why you may use them, their size, 20 test queries with the answers you expect, and the brute-force baseline. (3 points)
3. Build one part on a sample of 1,000 documents and report its measured count next to its Big-O claim. (3 points)

Hand in one PDF and your notebook.

### Sources

- Vitter 1985, Random sampling with a reservoir. ACM Transactions on Mathematical Software 11(1), 37–57. https://doi.org/10.1145/3147.3165
- Vose 1991, A linear algorithm for generating random numbers with a given distribution. IEEE Transactions on Software Engineering 17(9), 972–975. https://doi.org/10.1109/32.92917
- Durstenfeld 1964, Algorithm 235: Random permutation. Communications of the ACM 7(7), 420. https://doi.org/10.1145/364520.364540
- Walker 1977, An efficient method for generating discrete random variables with general distributions. ACM Transactions on Mathematical Software 3(3), 253–256. https://doi.org/10.1145/355744.355749
- Efraimidis & Spirakis 2006, Weighted random sampling with a reservoir. Information Processing Letters 97(5), 181–185. https://doi.org/10.1016/j.ipl.2005.11.003
- Mikolov et al. 2013, Distributed Representations of Words and Phrases and their Compositionality (NeurIPS 2013). https://arxiv.org/abs/1310.4546
- Schaul, Quan, Antonoglou & Silver 2016, Prioritized Experience Replay (ICLR 2016). https://arxiv.org/abs/1511.05952
- Kool, van Hoof & Welling 2019, Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement (ICML 2019). https://arxiv.org/abs/1903.06059
- TensorFlow documentation, `tf.data.Dataset.shuffle` (buffer_size). https://www.tensorflow.org/api_docs/python/tf/data/Dataset#shuffle

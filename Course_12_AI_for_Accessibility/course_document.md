# Course 12: AI for Accessibility

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on how AI can help disabled people hear, see, read and communicate, and how it can fail them: speech recognition and captions, sign language and lip reading, image description and reading support, and augmentative and alternative communication, with evaluation, ethics and deployment in Bangladesh. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Speech recognition, computer vision and language models are already changing assistive technology: live captions, image descriptions, word prediction, and early systems for sign language and lip reading. This course teaches how these systems work by building small versions of each, and how to evaluate them with the people who use them. It gives special attention to Bangla and to the Deaf community in Bangladesh, where data are scarce and tools are few. Disabled people appear in this course as users, experts and partners: no session promises that AI replaces interpreters, captioners or teachers.

Prerequisites: Python and basic deep learning (Course 1); Course 3 helps for sessions 5–7. Course 11 (On-Device AI) is a useful companion for deployment.

Capstone: with a community partner where possible, build a small assistive tool, such as a sign or lip-reading recognizer for a small vocabulary, a caption segmenter, a photo-quality guide for blind users or a Bangla word predictor. Collect a small consented dataset, evaluate the tool for each group of users and with users themselves, and present it in a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a problem defined with users or a partner (20); a working baseline and model with honest metrics (25); evaluation per group, with uncertainty (20); a user test or expert review, and what it changed (20); clarity of the report and video, including limitations and consent (15).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English. Caption every video in the course, and where possible invite Deaf, blind or AAC-using guests: the course should practise what it teaches.

### Sessions

1. **Disability, accessibility and AI.** Students can explain models of disability and accessibility standards, compute WCAG contrast ratios, simulate colour vision deficiency, and say where AI helps or harms.
   - Read: WHO 2022, Global report on health equity for persons with disabilities; W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2
   - Lab: about 2 hours, notebook `s01_accessibility_basics.ipynb`
2. **Speech recognition for Bangla.** Students can compute log-mel features, explain CTC and encoder–decoder speech recognition, train a tiny CTC recognizer, and measure character and word error rates.
   - Read: Graves, Fernández, Gomez & Schmidhuber 2006, Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks, ICML; Hannun 2017, Sequence Modeling with CTC, Distill
   - Lab: about 2.5 hours, notebook `s02_speech_recognition.ipynb`
3. **Captions for deaf and hard-of-hearing viewers.** Students can align a transcript to time, split it into readable caption blocks under timing and length limits, and evaluate captions beyond word error rate.
   - Read: W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2: definition of captions; success criteria 1.2.2 and 1.2.4; Bain, Huh, Han & Zisserman 2023, WhisperX: Time-Accurate Speech Transcription of Long-Form Audio, Interspeech
   - Lab: about 2 hours, notebook `s03_captions.ipynb`
4. **Sign languages and hand pose.** Students can explain what sign languages are, represent a hand as 21 landmarks, normalize them, and classify handshapes across signers.
   - Read: Bragg et al. 2019, Sign Language Recognition, Generation, and Translation: An Interdisciplinary Perspective, ASSETS; Zhang, Bazarevsky, Vakunov, Tkachenka, Sung, Chang & Grundmann 2020, MediaPipe Hands: On-device Real-time Hand Tracking
   - Lab: about 2 hours, notebook `s04_hand_pose.ipynb`
5. **Recognizing isolated signs.** Students can train temporal and skeleton-graph models on landmark sequences and evaluate them on signers they have never seen.
   - Read: Yan, Xiong & Lin 2018, Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition, AAAI; Li, Rodriguez Opazo, Yu & Li 2020, Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison (WLASL), WACV
   - Lab: about 2.5 hours, notebook `s05_isolated_signs.ipynb`
6. **Continuous signing and sign language translation.** Students can train a CTC model on continuous signing, decode it, and evaluate recognition and translation with the right metrics.
   - Read: Camgoz, Koller, Hadfield & Bowden 2020, Sign Language Transformers: Joint End-to-end Sign Language Recognition and Translation, CVPR; Papineni, Roukos, Ward & Zhu 2002, BLEU: a Method for Automatic Evaluation of Machine Translation, ACL
   - Lab: about 2.5 hours, notebook `s06_continuous_signing.ipynb`
7. **Lip reading.** Students can explain visual speech recognition and its limits, build a lip-landmark graph model with attention, and show how audio-visual fusion helps in noise.
   - Read: Afouras, Chung, Senior, Vinyals & Zisserman 2018, Deep Audio-Visual Speech Recognition; Ma, Haliassos, Fernandez-Lopez, Chen, Petridis & Pantic 2023, Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels
   - Lab: about 2 hours, notebook `s07_lip_reading.ipynb`
8. **Describing images for blind and low-vision users.** Students can explain how image captioning and visual question answering serve blind users, detect unusable photos, and make a model abstain when it is unsure.
   - Read: Gurari et al. 2018, VizWiz Grand Challenge: Answering Visual Questions from Blind People; Radford et al. 2021, Learning Transferable Visual Models From Natural Language Supervision (CLIP)
   - Lab: about 2 hours, notebook `s08_image_description.ipynb`
9. **Reading support: OCR, text-to-speech and simplification.** Students can explain OCR and text-to-speech pipelines for Bangla, train a line recognizer with CTC, and normalize text for a speech synthesizer.
   - Read: Shi, Bai & Yao 2017, An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition (CRNN); Sproat, Black, Chen, Kumar, Ostendorf & Richards 2001, Normalization of non-standard words, Computer Speech and Language 15(3)
   - Lab: about 2 hours, notebook `s09_reading_support.ipynb`
10. **Augmentative and alternative communication.** Students can explain AAC and its users, measure keystroke savings from word prediction, and compare access methods such as switch scanning.
   - Read: Beukelman & Light 2020, Augmentative and Alternative Communication: Supporting Children and Adults with Complex Communication Needs, 5th edition (Paul H. Brookes); Ward, Blackwell & MacKay 2000, Dasher: a data entry interface using continuous gestures and language models (ACM Symposium on User Interface Software and Technology, UIST)
   - Lab: about 2 hours, notebook `s10_aac.ipynb`
11. **Evaluation, fairness and participatory design.** Students can design an evaluation with disabled users, report performance per group with uncertainty, and handle consent and privacy.
   - Read: Morris 2020, AI and Accessibility: A Discussion of Ethical Considerations, Communications of the ACM 63(6); Bennett & Keyes 2019, What is the Point of Fairness? Disability, AI and the Complexity of Justice
   - Lab: about 2 hours, notebook `s11_evaluation_fairness.ipynb`
12. **Deploying accessible AI in Bangladesh, and the capstone.** Students can plan an assistive tool that works offline on a low-cost phone, shrink a model to fit, and scope a capstone with a community partner.
   - Read: Nagel et al. 2021, A White Paper on Neural Network Quantization; Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference
   - Lab: about 2 hours, notebook `s12_deployment.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. The labs use synthetic data generated in the notebooks (hand and lip landmarks, tone-based speech, degraded images), so they run anywhere; the NOT RUN cells show how to use the real datasets and models.
- **Sources:** read the papers cited for a session before recording it.
- **Dates:** written in November 2026. Facts about datasets, tools and organizations in Bangladesh were checked then; recheck them before each run of the course.

## Session 1: Disability, accessibility and AI

**Goal:** students can explain models of disability and accessibility standards, compute WCAG contrast ratios, simulate colour vision deficiency, and say where AI helps or harms.

### Talking pointers

- **Open with:** "About one person in six lives with a significant disability. Whatever you build, some of your users are disabled: you either plan for them or shut them out."
- **Segment 1, say:** write two numbers from one Bangladesh survey, 2.8% and 7.07%, and ask why they differ before explaining definitions.
- **Segment 2, say:** work out the contrast of grey #777777 on white on the board (4.48:1, a fail), then show #767676 at 4.54:1.
- **Segment 3, say:** show the flower photo and the default chart colours under simulated protanopia (orange and green end up 4.6 apart), then the course map.
- **Close with:** "Accessibility is designed in, measured, and checked with the people who use it." Then set assignment 1.

### Segment 1 (6 min): disability is common, and who defines it

- The World Health Organization (WHO) estimates that about 1.3 billion people, 16% of the world's population, experience a significant disability (WHO 2022).
- The **medical model** treats disability as a problem in the body, to be cured. The **social model** separates impairment, a difference in body or mind, from disability, the barriers society builds: stairs without a ramp, a video without captions (Oliver 1983). The UN Convention on the Rights of Persons with Disabilities (CRPD) also describes disability as impairments meeting barriers (UN 2006), and engineers can remove many barriers.
- **Assistive technology**, such as a hearing aid or a screen reader (software that reads the screen aloud), helps people do what they want to do; most tools in this course are assistive technology.
- "Nothing about us without us", a slogan of the disability rights movement (Charlton 1998), means disabled people take part in decisions about technology made for them, as users, experts and partners. Some communities prefer "persons with disabilities" (person-first, as in the CRPD), others "disabled people" (identity-first): ask, and follow them.
- Bangladesh ratified the CRPD in 2007 (International Disability Alliance); its Rights and Protection of Persons with Disabilities Act 2013 defines 12 types of disability (The Daily Star 2023). The National Survey on Persons with Disabilities (NSPD 2021), by the Bangladesh Bureau of Statistics, found 2.8% of the population with a disability as the 2013 Act defines it (The Business Standard 2022; UNICEF Bangladesh 2023); 7.07% reported difficulty in at least one domain such as seeing or hearing, by the international Washington Group measure (UNICEF Bangladesh 2023).
- **Pause and try:** a Bangla news app has 1 million users in Bangladesh. How many have a disability at 2.8%, and how many some functional difficulty at 7.07%?
  - **Answer:** about 28,000 and 70,700. The definitions differ, and neither group is small.

### Segment 2 (7 min): accessibility standards and the contrast ratio

- The Web Content Accessibility Guidelines (WCAG) 2.2, a W3C Recommendation since October 2023, group their success criteria under four principles, **perceivable**, **operable**, **understandable** and **robust**, each criterion at level A, AA or AAA (W3C 2023). Examples: alt text for images (1.1.1), captions for recorded video (1.2.2), full keyboard access (2.1.1), and colour never the only cue (1.4.1).
- Relative luminance: scale each sRGB channel to 0–1, undo the gamma encoding ($c/12.92$ if $c \le 0.04045$, else $((c + 0.055)/1.055)^{2.4}$), then $L = 0.2126R + 0.7152G + 0.0722B$. Green counts most because the eye is most sensitive to it.
- The contrast ratio is $(L_1 + 0.05)/(L_2 + 0.05)$, where $L_1$ is the luminance of the lighter colour; it runs from 1:1 to 21:1. Level AA needs 4.5:1 for normal text and 3:1 for large text; chart lines and controls need 3:1 (1.4.11). Level AAA needs 7:1.
- Red–green colour vision deficiency affects about 1 in 12 males and 1 in 200 females of Northern European ancestry; blue–yellow deficiency, fewer than 1 in 10,000 people (MedlinePlus Genetics). Machado et al. (2009) simulate each type with one 3 × 3 matrix on linear RGB, so designers can preview their colours.
- **Pause and try:** #777777 has channels 119/255 = 0.4667, with linear value 0.1845. What is its contrast on white, and does it pass AA for body text?
  - **Answer:** $1.05 / (0.1845 + 0.05) = 4.48$:1, just below 4.5:1, so it fails.

### Segment 3 (7 min): where AI helps, where it harms, and this course

- AI can widen access: speech recognition and captions (sessions 2–3), sign language recognition and translation (sessions 4–6), lip reading (session 7), image descriptions (session 8), optical character recognition (OCR) and text-to-speech (session 9), and word prediction for augmentative and alternative communication (session 10).
- It can also harm (Morris 2020; Whittaker et al. 2019): **errors** a blind user cannot check, such as a wrong image description; **bias** against people whose speech, movement or appearance is atypical; **privacy** loss, since disability is sensitive and rare disabilities are easy to identify; **surveillance** through face and lip analysis; and **replacement** of interpreters, captioners or teachers by a cheaper automatic tool. Sessions 11 and 12 return to these risks.
- Our labs use synthetic data so that they run on a laptop; real systems must still be tested with the people who will use them. Likewise, colour simulation is a model of vision, not a person.
- **Pause and try:** an automatic captioner gets one word in 20 wrong. A 10-minute lecture runs at 150 words per minute. How many words are wrong?
  - **Answer:** 1,500 × 0.05 = 75, about one every 8 seconds. "95% accurate" can still be hard to follow.

### Lab guide (about 2 hours, notebook `s01_accessibility_basics.ipynb`)

1. Section 1 (15 min): both contrast ratios on paper, then run the cell.
2. Section 2 (15 min): predict pass or fail for each row of the contrast report.
3. Section 3 (15 min): the nearest passing shade by bisection.
4. Section 4 (20 min): the flower photo under three simulated dichromacies; compare the CIELAB spreads of $a^*$ (green–red) and $b^*$ (blue–yellow).
5. Section 5 (15 min): pairwise colour differences $\Delta E$ for matplotlib's `tab10` and the Okabe–Ito palette (Okabe & Ito 2008).
6. Sections 6–7 (20 min): the greedy palette search, and a chart with markers and direct labels.
7. TODO cells (20 min).

- **Expect:** #777777 4.478:1 (fails), #767676 4.542:1; pure red text 4.00:1. Orange #ff7f0e reaches 3:1 at #ea740d and 4.5:1 at #bb5d0a. Flower: $a^*$ spread 19.42 falls to 1.89 (protanopia) and 2.56 (deuteranopia); tritanopia cuts $b^*$ from 20.73 to 11.21. Smallest `tab10` difference: 27.7 normal, 4.6 protanopia (orange and green), 7.2 deuteranopia, 15.2 tritanopia. Okabe–Ito stays at 16.1 or more, but 3 of its 8 colours are below 3:1 on white. The greedy six-colour palette keeps every pair 30.0 or more apart, all at 3.18:1 or more. Runtime about 4 seconds.
- **Common problems:** applying the weights or matrices to gamma-encoded instead of linear values; rounding the ratio before comparing it with 4.5; reading hex channels in the wrong order.

### Quiz

1. What is the difference between the medical and the social model, and which tells an engineer what to fix?
   - **Answer:** the medical model places the problem in the body; the social model places disability in barriers, which an engineer can remove, such as missing captions.
2. Every line in a chart has its own colour. Which two WCAG criteria should you still check?
   - **Answer:** 1.4.1 (colour must not be the only cue, so add markers or labels) and 1.4.11 (3:1 contrast). In the lab, green and red were 119.8 apart for normal vision but 7.3 under simulated deuteranopia.
3. Why linearize sRGB values before computing luminance or applying the Machado matrices?
   - **Answer:** sRGB values are gamma-encoded, but light adds linearly, so weighting encoded values gives wrong answers, even for greys: #777777 would get 0.4667 instead of 0.1845.

**Watch out:** "Accessibility is a niche feature for a few users." About 1.3 billion people have a significant disability (WHO 2022), and 7.07% of people in Bangladesh reported some functional difficulty in the NSPD 2021. Accessible design also helps in passing situations, such as captions on a noisy bus. Treat accessibility as a quality requirement, like correctness, from the start.

### Assignment 1 (due before session 2, 10 points)

1. Audit ten text-and-background colour pairs on a website or app you use in Bangladesh. Report each ratio, pass or fail at 3:1, 4.5:1 and 7:1, and the nearest passing shade for each failure. (3 points)
2. Complete both TODO cells and report the nearest passing colour for #ff7f0e on #555555, and the smallest `tab10` $\Delta E$ at severity 0.5 and 1.0 for protan and deutan deficiency. (4 points)
3. Choose one AI tool that claims to help disabled people. In about 300 words: whom it helps, one way it can fail and who is harmed, and how you would test it with disabled users. (3 points)

Hand in one PDF and your notebook.

### Sources

- WHO 2022, Global report on health equity for persons with disabilities. https://www.who.int/publications/i/item/9789240063600
- W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/
- Machado, Oliveira & Fernandes 2009, A Physiologically-based Model for Simulation of Color Vision Deficiency, IEEE Transactions on Visualization and Computer Graphics 15(6), 1291–1298. https://doi.org/10.1109/TVCG.2009.113
- United Nations 2006, Convention on the Rights of Persons with Disabilities. https://social.desa.un.org/issues/disability/crpd/convention-on-the-rights-of-persons-with-disabilities-crpd
- Oliver 1983, Social Work with Disabled People. Macmillan.
- Charlton 1998, Nothing About Us Without Us: Disability Oppression and Empowerment. University of California Press. https://www.ucpress.edu/books/nothing-about-us-without-us/paper
- Morris 2020, AI and Accessibility: A Discussion of Ethical Considerations, Communications of the ACM 63(6). https://arxiv.org/abs/1908.08939
- Whittaker et al. 2019, Disability, Bias, and AI. AI Now Institute. https://ainowinstitute.org/publication/disability
- MedlinePlus Genetics (US National Library of Medicine), Color vision deficiency. https://medlineplus.gov/genetics/condition/color-vision-deficiency/
- Okabe & Ito 2008, Color Universal Design (CUD): How to make figures and presentations that are friendly to colorblind people. https://jfly.uni-koeln.de/color/
- International Disability Alliance, Bangladesh country page (CRPD signed 9 May 2007, ratified 30 November 2007). https://www.internationaldisabilityalliance.org/countries/BGD
- The Business Standard 2022, 2.8% of total population have disabilities: BBS (NSPD 2021, published 27 December 2022). https://www.tbsnews.net/bangladesh/28-total-population-have-disabilities-bbs-558590
- UNICEF Bangladesh 2023, UNICEF concerned that more than half of children with disabilities in Bangladesh do not go to school (NSPD 2021, Washington Group measure). https://www.unicef.org/bangladesh/en/press-releases/unicef-concerned-more-half-children-disabilities-bangladesh-do-not-go-school
- The Daily Star 2023, Majority not enrolled in formal education (NSPD 2021; the 12 types of disability in the 2013 Act). https://www.thedailystar.net/business/economy/news/majority-not-enrolled-formal-education-3229786

## Session 2: Speech recognition for Bangla

**Goal:** students can compute log-mel features, explain CTC and encoder–decoder speech recognition, train a tiny CTC recognizer, and measure character and word error rates.

### Talking pointers

- **Open with:** "Automatic captions, voice typing and voice search all start with a model that turns sound into text. Today we build a tiny one, and learn to check whether it works for the people who need it."
- **Segment 1, say:** show the chirp's spectrogram and log-mel picture, then work out 200 samples per window, an 80-sample hop and 98 frames per second.
- **Segment 2, say:** collapse `a a - a b b - b` on the board, count the five 3-frame paths for `ab`, then show the plot of blank and digit probabilities.
- **Segment 3, say:** score "আমি বাজারে যাব" against "আমি বাজার যাব" (WER 0.333, CER 0.071), then show the noise plot.
- **Close with:** "Measure a recognizer where its users live: their dialects, their phones, their markets." Then set assignment 2.

### Segment 1 (6 min): from sound to features

- A waveform is air pressure measured thousands of times per second; speech is usually stored at 8,000 or 16,000 samples per second.
- Speech sounds change every few tens of milliseconds, so we analyse short **frames**: windows of 25 ms that start every 10 ms (the **hop**). Each frame is multiplied by a smooth window and passed through the fast Fourier transform. The result, energy per frequency per frame, is the short-time Fourier transform (STFT), drawn as a spectrogram.
- A **mel filterbank** pools the energies with triangular filters spaced evenly on the mel scale, $m = 2595 \log_{10}(1 + f/700)$: narrow filters at low frequencies, wide ones at high frequencies, roughly as we hear pitch. Taking the logarithm compresses the range of loudness.
- Whisper's front end does exactly this: 16 kHz audio, 400-sample (25 ms) windows, a 160-sample (10 ms) hop, 80 or 128 mel bands, and 30-second chunks (Radford et al. 2022). wav2vec 2.0 instead learns its features from the raw waveform with a convolutional encoder (Baevski et al. 2020).
- **Pause and try:** Whisper's settings are 16,000 samples per second, a 400-sample window and a 160-sample hop. About how many frames does a 30-second chunk give?
  - **Answer:** about 3,000: 30 s / 10 ms = 3,000 hops (exactly 2,998 complete windows without padding: 1 + 479,600/160, rounded down).

### Segment 2 (7 min): CTC, encoder–decoders and self-supervised models

- The alignment problem: the training data say which words were spoken, but not which frames belong to which sound.
- **Connectionist temporal classification** (CTC; Graves et al. 2006) lets the network output one symbol per frame, plus a **blank** meaning "nothing new". A frame path is read by merging repeats and then deleting blanks, so `a a - a b b - b` gives `aabb`; the blank between the two a's is what allows a double letter.
- The probability of a transcript is the sum over all paths that collapse to it. A dynamic program, the forward algorithm, computes this sum in log space with log-sum-exp (Course 2 session 10), and the loss is its negative log-likelihood (Course 2 session 7). Hannun (2017) explains it with pictures.
- **Greedy decoding** takes the best symbol at each frame and collapses; beam search keeps several candidates (session 6). Because CTC treats frames as independent given the audio, a separate language model often helps (Hannun 2017).
- **Encoder–decoder** models write text token by token while attending to the encoded audio. Whisper was trained this way on 680,000 hours of labelled web audio in many languages and accepts Bangla (Radford et al. 2022); its decoder is also a language model, so it can write fluent words that were never spoken.
- **Self-supervised pretraining:** wav2vec 2.0 learns from unlabelled audio by masking parts of it and picking the true hidden features among distractors, then is fine-tuned with CTC on a little labelled data (Baevski et al. 2020). XLS-R does the same on 128 languages (Babu et al. 2021), which helps languages with few labels.
- **Pause and try:** how many 3-frame paths over {a, b, -} collapse to `ab`? If each symbol has probability 1/3 at each frame, what is the CTC loss?
  - **Answer:** 5 (`aab`, `abb`, `ab-`, `a-b`, `-ab`), so the loss is −ln(5/27) = 1.686, which the notebook confirms with PyTorch.

### Segment 3 (7 min): Bangla data, error rates and fair scoring

- Open Bangla speech data include OpenSLR 53, a crowd-sourced corpus of Bangladeshi Bengali read speech (Kjartansson et al. 2018), and the Bangla part of Mozilla Common Voice, recorded by volunteers (Ardila et al. 2020). Both are mostly read sentences; check each licence.
- Real use is harder: regional varieties such as Chittagonian and Sylheti, Bangla–English code-switching ("আমার একটা meeting আছে"), cheap microphones, background voices, and atypical speech.
- **Word error rate:** WER = (S + D + I)/N: substitutions, deletions and insertions that turn the reference into the output, over N reference words. **Character error rate** (CER) counts characters. Bangla words carry suffixes (বাজার, বাজারে), so one wrong letter makes a whole word wrong; CER shows partial correctness.
- Normalize both sides the same way before scoring: Unicode form, punctuation, Bangla and ASCII digits. য় can be one code point or two that look identical (Course 5 session 2).
- **Pause and try:** reference "আমি বাজারে যাব" (14 code points), output "আমি বাজার যাব". What are the WER and the CER?
  - **Answer:** one wrong word in three, WER = 0.333; one missing vowel sign, CER = 1/14 = 0.071.

### Lab guide (about 2.5 hours, notebook `s02_speech_recognition.ipynb`)

1. Section 1 (15 min): frames, mel and CTC on paper, then run the cell.
2. Section 2 (20 min): STFT and mel filterbank in NumPy, checked against SciPy.
3. Sections 3–4 (25 min): the synthetic corpus (tone patterns with Bangla number words as transcripts); edit distance, WER and CER.
4. Section 5 (20 min): train the convolution + bidirectional GRU recognizer with `nn.CTCLoss`.
5. Sections 6–7 (35 min): blank and digit probabilities over time; the য় scoring trap; error rate against noise.
6. TODO cells (30 min).

- **Expect:** 200-sample windows, 80-sample hop, 98 frames per second; CTC loss 1.6864 = −ln(5/27); STFT within 7.1e-15 of SciPy. A 64,203-parameter model: validation WER 1.000 after epoch 1 (only blanks), 0.047 after epoch 2, 0.000 after epoch 6. In the plotted utterance the blank has probability above 0.5 in 72% of frames. CER of a perfect transcript: 0.1032 without normalization, 0.0000 after NFC. WER with white noise: 0.000 at 20 dB, 0.004 at 10 dB, 0.059 at 5 dB, 0.379 at 0 dB, 0.836 at −5 dB; with background voices: 0.329 at 10 dB, 1.019 at 0 dB. Runtime about 30 seconds.
- **Common problems:** giving `nn.CTCLoss` (batch, time, symbols) instead of (time, batch, symbols); forgetting that the stride-2 convolution halves the input lengths; averaging per-sentence WER instead of dividing total edits by total reference words.

### Quiz

1. Why does CTC need a blank symbol?
   - **Answer:** to output nothing on frames between sounds, and to separate repeated letters: without a blank, `a a` would always collapse to a single a.
2. A Bangla recognizer has WER 0.40 but CER 0.12. How can both be true?
   - **Answer:** most wrong words are only partly wrong, for example a missing suffix or vowel sign. Each such word counts fully in WER but only a character or two in CER.
3. How can WER be larger than 1?
   - **Answer:** through insertions. In the lab, background voices at 0 dB gave WER 1.019 because the model wrote down the other speakers' digits.

**Watch out:** "A low WER on clean read speech means the system will work in a noisy market." In the lab, a model with validation WER 0.000 reached 0.329 when three other voices spoke at 10 dB SNR, where white noise at the same level gave 0.004. Real systems also meet dialects, code-switching and phone microphones. Test on recordings from the places and people the system is for.

### Assignment 2 (due before session 3, 10 points)

1. By hand, then in code: the number of frames for 5 seconds of 16 kHz audio with Whisper's window and hop; the mel values of 500, 2,000 and 4,000 Hz; and the number of 4-frame paths that collapse to `ab`, checked with `nn.CTCLoss`. (3 points)
2. Complete the babble-augmentation TODO. Report the two rows of the noise table for the new model and explain what training on background voices gained and cost. (4 points)
3. Write ten Bangla sentences that mix in English words, transcribe each with the English words in Latin and in Bangla script, and compute WER and CER between the versions. Explain in one paragraph why the scoring convention must be fixed before evaluation. (3 points)

Hand in one PDF and your notebook.

### Sources

- Graves, Fernández, Gomez & Schmidhuber 2006, Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks, ICML. https://www.cs.toronto.edu/~graves/icml_2006.pdf
- Hannun 2017, Sequence Modeling with CTC, Distill. https://distill.pub/2017/ctc/
- Radford, Kim, Xu, Brockman, McLeavey & Sutskever 2022, Robust Speech Recognition via Large-Scale Weak Supervision (Whisper). https://arxiv.org/abs/2212.04356
- Baevski, Zhou, Mohamed & Auli 2020, wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations. https://arxiv.org/abs/2006.11477
- Babu et al. 2021, XLS-R: Self-supervised Cross-lingual Speech Representation Learning at Scale. https://arxiv.org/abs/2111.09296
- Ardila et al. 2020, Common Voice: A Massively-Multilingual Speech Corpus, LREC. https://arxiv.org/abs/1912.06670
- Kjartansson, Sarin, Pipatsrisawat, Jansche & Ha 2018, Crowd-Sourced Speech Corpora for Javanese, Sundanese, Sinhala, Nepali, and Bangladeshi Bengali, SLTU; the Bangla data are OpenSLR SLR53. https://www.openslr.org/53/
- OpenAI Whisper source code (audio front end: 16 kHz, 400-sample window, 160-sample hop, 80 or 128 mel bands, 30-second chunks). https://github.com/openai/whisper

## Session 3: Captions for deaf and hard-of-hearing viewers

**Goal:** students can align a transcript to time, split it into readable caption blocks under timing and length limits, and evaluate captions beyond word error rate.

### Talking pointers

- **Open with:** "A transcript is not a caption. A caption must give the right words at the right moment, in pieces a person can read, and tell viewers about the sounds they cannot hear."
- **Segment 1, say:** show the notebook's SRT output with its `[music]` block (print the whole file to see the speaker labels), then work the reading-speed example: 43 characters in 2 seconds is 21.5 characters per second.
- **Segment 2, say:** fill the DTW table for `1 3 4 3` and `1 1 3 4 4 3` on the board, then show the forced-alignment plot.
- **Segment 3, say:** compare the greedy and dynamic-programming captions: 19 against 1 breaks after words like "the", and both too fast in the fast passage.
- **Close with:** "Good captions are a design problem that involves viewers, not a by-product of speech recognition." Then set assignment 3.

### Segment 1 (6 min): what makes a good caption

- Captions give the speech and the important non-speech sounds of a video as synchronized text, including speaker identification, music and sound effects. WCAG requires captions for recorded video (success criterion 1.2.2, level A) and live video (1.2.4, level AA); in some countries captions are called subtitles (W3C 2023). Elsewhere "subtitles" often means a translation of the dialogue only.
- Deaf and hard-of-hearing viewers rely on them, and many other people use them too, for example when watching without sound or in a second language.
- Four qualities: **accuracy** (the right words), **synchronization** (on screen while the words are spoken), **completeness** (speaker names, sound cues such as [music] or [door closing]), and **readability**.
- Readability is measured in reading speed (characters per second, cps), characters per line, lines per block, and how lines are broken. Broadcasters and streaming services publish their own limits; check the guideline you must follow. The lab uses example limits: 42 characters per line, 2 lines, 1 to 7 seconds per block, and 17 cps.
- For Bangla, count what the reader sees: one visible letter can be several code points (Course 5 session 2).
- **Pause and try:** the block "Second, they must appear at the right time," has 43 characters and is shown for 2.0 seconds. What is its reading speed, and how long must it stay up for 17 cps?
  - **Answer:** 43 / 2.0 = 21.5 cps, too fast; it needs 43 / 17 = 2.53 seconds.

### Segment 2 (7 min): putting words on the timeline

- **Dynamic time warping** (DTW; Sakoe & Chiba 1978) aligns two sequences that unfold at different speeds, such as two recordings of one sentence. It fills a table $D(i, j) = d(i, j) + \min(D(i-1, j), D(i, j-1), D(i-1, j-1))$ in $O(nm)$ time and walks back along the cheapest path.
- A **Sakoe–Chiba band** fills only cells near the diagonal: faster, and no extreme warps, but a band that is too narrow excludes the true path.
- **Forced alignment** uses a known transcript. Given a CTC model's frame probabilities (session 2), the Viterbi algorithm finds the best path through the states `- w1 - w2 - … -`: the CTC forward algorithm with a maximum in place of the sum (Graves et al. 2006).
- **WhisperX** gets word timestamps by running Whisper on speech segments and force-aligning the words with a wav2vec 2.0 CTC model (Bain et al. 2023). Its alignment models are language-specific, and version 3.8.6 has no default Bangla model, so a Bangla CTC model must be chosen and tested.
- **Live captions** come from stenographers, respeakers (people who repeat the speech clearly into a recognizer) or automatic recognition, and always lag behind the speech.
- **Pause and try:** in the DTW table for `x = 1 3 4 3` and `y = 1 1 3 4 4 3` with cost $|x_i - y_j|$, what is the total cost, and which frames of y does the first 1 in x match?
  - **Answer:** 0, since every value finds an equal partner; the first frame of x matches the first two frames of y.

### Segment 3 (7 min): segmentation and quality

- A **greedy** segmenter fills each line until the next word does not fit. A **dynamic-programming** segmenter gives every possible cut a cost (low at sentence ends, high right after "the", "of" or "to"), adds a penalty for reading speed over the limit, and finds the cheapest segmentation.
- In the lab the DP made 1 break right after such a word against greedy's 19. Both left blocks over 17 cps in the fast passage: greedy 2 (up to 21.9 cps), DP 3 (up to 20.2 cps). No segmentation shows fast speech word for word at 17 cps; the options are longer display into pauses, edited text, or faster captions.
- Word error rate treats every error alike, but "at 2" written as "at 3" changes the meaning while a missing "um" does not. The NER model scores live captions as $(N - E - R)/N$, where N is the number of words in the captions and E and R are edition and recognition errors, each weighted by how much it harms understanding (Romero-Fresco & Martínez Pérez 2015).
- Also measure delay, completeness and reading speed. Automatic captions are a draft for a trained human editor to correct, not a replacement for human captioners.
- **Pause and try:** caption A writes "the exam is at 3" for "at 2"; caption B writes "gonna" for "going to" (counted as one substituted word and one deleted word). Each line is part of a 20-word block. What is the WER of each, and which is worse?
  - **Answer:** A has 1/20 = 0.05 and B has 2/20 = 0.10, yet A is worse: it changes the meaning.

### Lab guide (about 2 hours, notebook `s03_captions.ipynb`)

1. Section 1 (10 min): reading speed and the toy DTW table by hand.
2. Section 2 (20 min): DTW with and without a band, against the true warp.
3. Section 3 (30 min): Viterbi forced alignment over a CTC trellis, against greedy recognition and naive spreading.
4. Section 4 (30 min): greedy and DP segmentation; read where each breaks lines.
5. Section 5 (10 min): write SubRip (.srt) text.
6. TODO cells (20 min).

- **Expect:** 21.5 cps, 2.53 s; toy DTW cost 0. DTW: cost 15.18 and mean error 0.53 frames for the full table and the 20-frame band (4,500 of 19,200 cells); 5-frame band 3.70; linear stretch 6.02. Greedy recognition WER 0.300; forced alignment median start error 15 ms (95th percentile 44 ms); proportional spreading 815 ms. Segmentation: greedy 19 blocks, 19 breaks after binding words, 2 blocks over 17 cps (20.8, 21.9); DP 21 blocks, 1 such break, 3 over 17 cps (17.3, 20.1, 20.2). Runtime about 2 seconds.
- **Common problems:** writing SRT times with a dot instead of a comma before the milliseconds; letting a block end after the next one starts; measuring Bangla line length in code points.

### Quiz

1. Why can forced alignment be accurate when free recognition from the same model is poor?
   - **Answer:** it only has to place known words, so it chooses among paths that spell the transcript; extra or missing bursts cannot change the words. In the lab: WER 0.300, median start error 15 ms.
2. What does a Sakoe–Chiba band trade?
   - **Answer:** less computation and no extreme warps, against the risk of excluding the true path: the 20-frame band matched the full table, the 5-frame band did not.
3. Why is WER not enough to judge captions?
   - **Answer:** it ignores timing, reading speed, speaker labels and sound cues, and it counts a meaning-changing error like a harmless one.

**Watch out:** "A verbatim transcript makes the best captions." A transcript has no timing, no readable blocks, no speaker names and no sound cues. And verbatim text of fast speech can be too fast to read: in the lab, no segmentation kept the fast passage under 17 cps. Editing makes captions readable but can remove content viewers want, so decide the style with deaf and hard-of-hearing viewers.

### Assignment 3 (due before session 4, 10 points)

1. Caption a 2-minute clip from a lecture by hand, or correct an automatic caption file, as SRT with speaker labels and sound cues. Report the reading speed of every block and how many exceed your limit. (3 points)
2. Complete both TODO cells and report the blocks over 17 cps without filler words, and the alignment errors with more noise. (4 points)
3. Adapt the segmenter to Bangla: list Bangla words after which a line should not break, with examples, propose how to measure a Bangla line's length, and test both on ten Bangla sentences. (3 points)

Hand in one PDF and your notebook.

### Sources

- W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2: definition of captions; success criteria 1.2.2 and 1.2.4. https://www.w3.org/TR/WCAG22/
- Bain, Huh, Han & Zisserman 2023, WhisperX: Time-Accurate Speech Transcription of Long-Form Audio, Interspeech. https://arxiv.org/abs/2303.00747
- Sakoe & Chiba 1978, Dynamic programming algorithm optimization for spoken word recognition, IEEE Transactions on Acoustics, Speech, and Signal Processing 26(1).
- Graves, Fernández, Gomez & Schmidhuber 2006, Connectionist Temporal Classification, ICML. https://www.cs.toronto.edu/~graves/icml_2006.pdf
- Romero-Fresco & Martínez Pérez 2015, Accuracy rate in live subtitling: the NER model, in Audiovisual Translation in a Global Context. Palgrave Macmillan.
- WhisperX source code, version 3.8.6 (default alignment models by language). https://github.com/m-bain/whisperX
- OpenAI Whisper source code (`word_timestamps` option). https://github.com/openai/whisper

## Session 4: Sign languages and hand pose

**Goal:** students can explain what sign languages are, represent a hand as 21 landmarks, normalize them, and classify handshapes across signers.

### Talking pointers

- **Open with:** "Sign languages are not gestures added to speech. They are complete languages, and a model that reads them must respect that."
- **Segment 1, say:** play a short clip of a Deaf signer from a source that allows reuse, and point out the handshape, location, movement and facial expression in one sign.
- **Segment 2, say:** show the ten synthetic handshapes, then 20 raw samples of V next to the same samples after normalization.
- **Segment 3, say:** show the accuracy bars: 0.973 on a random split against 0.944 on new signers, and 0.727 against 0.893 for the left-handed signer without and with mirroring.
- **Close with:** "A model is only as general as the people in its test set." Then set assignment 4.

### Segment 1 (6 min): sign languages are languages

- Sign languages are natural languages with their own vocabulary and grammar, used by Deaf communities around the world (Bragg et al. 2019). They are not spoken languages spelled with the hands, and they are not universal: British and American Sign Language are different languages, although English is spoken in both countries.
- Many deaf people who sign see themselves as a linguistic and cultural community and write Deaf with a capital D; this course does the same when it means that community.
- Bangla Sign Language (BdSL) is the sign language of the Deaf community in Bangladesh. It has a manual alphabet for Bangla letters, used mainly for names and for words without a sign, and lexical signs for whole words, with a grammar of their own.
- A sign is built from a few parameters. Stokoe (1960) showed that American Sign Language signs combine handshapes, locations and movements; later work added **palm orientation** and **non-manual markers**: facial expression, mouth, head and body movement, which carry grammar such as marking a question in many sign languages (Bragg et al. 2019).
- Recognition systems should support, not replace, qualified interpreters. Bragg et al. (2019) call for Deaf people to be on the teams that design and judge them.
- **Pause and try:** a one-handed alphabet classifier looks at a single photo of one hand. Of the five parameters (handshape, location, movement, palm orientation, non-manual markers), how many can it see?
  - **Answer:** about two, handshape and palm orientation. Location needs the body, movement needs time, and non-manual markers need the face.

### Segment 2 (7 min): from video to landmarks

- **Hand pose estimation** finds the hand and predicts the positions of its joints. MediaPipe Hands first detects the palm, then predicts 21 3-D landmarks per hand, fast enough for phones (Zhang et al. 2020): the wrist, then four points along the thumb and along each finger, from the knuckle to the tip.
- The x and y coordinates are fractions of the image width and height, and z is a depth relative to the wrist. In the current release (1.2.3) the model is used through MediaPipe's Tasks API (`HandLandmarker`). Body and face landmark models exist as well.
- Landmarks instead of pixels: the classifier never sees the background, clothing or face, which helps privacy and cuts computation. But detector errors on blurred frames, poor light or overlapping hands pass silently into everything downstream, and landmarks drop facial expression, mouthing and contact between hand and body unless you add face and body landmarks.
- Landmarks recorded from identifiable people are still personal data: collect them with consent.
- **Pause and try:** a signer is filmed at 30 frames per second. How many numbers per second do two hands of landmarks give, compared with 256 × 256 colour frames?
  - **Answer:** 30 × 2 × 21 × 3 = 3,780 against 30 × 256 × 256 × 3 = 5,898,240, about 1,560 times fewer.

### Segment 3 (7 min): normalization and new signers

- The same handshape gives different numbers when the hand moves, turns or comes closer. **Normalize:** move the wrist to the origin, divide by the palm size (wrist to middle-finger knuckle), and rotate into the hand's own frame (wrist to middle knuckle is "up", little-finger knuckle to index knuckle is "right").
- A rotation cannot turn a left hand into a right hand. **Mirror** left hands (flip x) before normalizing, using the detector's handedness.
- **Invariant features** such as pairwise distances or joint angles do not change under rotation or mirroring, but distances cannot tell mirror images apart; Course 7 session 7 makes the same choice for molecules.
- **Evaluate on new signers.** A random split puts every signer in both training and test sets, so the model learns personal style. Split by signer, report accuracy per signer and per handshape, and give uncertainty, since few signers make a noisy estimate (Course 1 session 9).
- In the lab, normalization lifted kNN from 0.391 to 0.900 on new signers, and the left-handed new signer scored 0.893 against 0.947–0.973 for the others.
- **Pause and try:** your dataset has 5 signers, and a random 80/20 split gives 0.97. What should you do instead, and how many models does leave-one-signer-out train?
  - **Answer:** split by signer so test signers are never seen in training; leave-one-signer-out trains 5 models, each tested on one person.

### Lab guide (about 2 hours, notebook `s04_hand_pose.ipynb`)

1. Section 1 (10 min): normalize three landmarks and compute a joint angle by hand.
2. Sections 2–3 (25 min): the kinematic hand model, ten handshapes and twenty synthetic signers with personal style.
3. Section 4 (20 min): normalization, mirroring and pairwise distances; compare raw and normalized samples of V.
4. Section 5 (25 min): kNN and an MLP on four feature sets, random against new-signer splits.
5. Section 6 (15 min): the confusion matrix and per-signer accuracy.
6. TODO cells (25 min).

- **Expect:** palm size 2.0, a 90° clockwise rotation, a 36.9° joint angle. New-signer accuracy (kNN / MLP): raw 0.391 / 0.817, normalized 0.900 / 0.915, normalized + mirroring 0.916 / 0.944, distances 0.903 / 0.925; random split with normalized + mirroring 0.940 / 0.973. MLP on the left-handed new signer: 0.727 without mirroring, 0.893 with. Largest confusions: V and U (13 each way), S taken for A (11). Runtime about 15 seconds.
- **Common problems:** using MediaPipe's x and y without multiplying by the image width and height, which distorts angles in non-square images; mirroring the wrong hand (check on a few photos what the detector calls "Left"); a random split that puts the same signer in training and test.

### Quiz

1. Why does a random split overestimate accuracy for sign recognition?
   - **Answer:** each signer's personal style appears in both training and test sets. In the lab the MLP scored 0.973 on a random split and 0.944 on new signers.
2. Give two ways to handle left-handed signers, and the cost of each.
   - **Answer:** mirror left hands before normalizing, which depends on correct handedness detection; or use mirror-invariant features such as distances, which can no longer tell a left hand from a right hand.
3. Name two things a hand-landmark model cannot see that matter in a sign language.
   - **Answer:** non-manual markers such as facial expression and mouthing, and where the hand is relative to the body, including contact.

**Watch out:** "Sign language is universal" or "BdSL is Bangla spelled with the hands." Sign languages are separate natural languages with their own vocabulary and grammar (Bragg et al. 2019); British and American Sign Language differ although both countries speak English. BdSL has a manual alphabet for Bangla letters, but everyday signing uses lexical signs, movement, space and facial grammar, so a fingerspelling classifier is not a BdSL recognizer.

### Assignment 4 (due before session 5, 10 points)

1. On paper, normalize a 2-D hand of five given landmarks (your choice of coordinates, rotated by 60°) and compute two joint angles; check both in code. (3 points)
2. Complete both TODO cells and report the new-signer accuracy with joint angles, and the mean, worst and best leave-one-signer-out accuracy. (4 points)
3. Write a one-page plan for collecting a small BdSL handshape dataset with a Deaf partner organization: consent, payment, which signers to include (handedness, age, region), what is recorded and stored, and how the test signers are chosen. (3 points)

Hand in one PDF and your notebook.

### Sources

- Bragg et al. 2019, Sign Language Recognition, Generation, and Translation: An Interdisciplinary Perspective, ASSETS. https://arxiv.org/abs/1908.08597
- Zhang, Bazarevsky, Vakunov, Tkachenka, Sung, Chang & Grundmann 2020, MediaPipe Hands: On-device Real-time Hand Tracking. https://arxiv.org/abs/2006.10214
- Stokoe 1960, Sign Language Structure: An Outline of the Visual Communication Systems of the American Deaf. Studies in Linguistics, Occasional Papers 8.
- MediaPipe source code, release 1.2.3 (Hand Landmarker in the Tasks API). https://github.com/google/mediapipe

## Session 5: Recognizing isolated signs

**Goal:** students can train temporal and skeleton-graph models on landmark sequences and evaluate them on signers they have never seen.

### Talking pointers

- **Open with:** "Last session a handshape was one frame. A sign is a movement in time, and every signer moves differently."
- **Segment 1, say:** show the wrist paths of one sign made by six synthetic signers, then work out padding and the masked mean on the board.
- **Segment 2, say:** draw the hand skeleton as a graph and trace which landmarks can affect the index fingertip after one, two and three spatial steps.
- **Segment 3, say:** show the bars: 0.988 on a random split, 0.870 on new signers. Then admit what did not work: the graph network and time warping.
- **Close with:** "Report the number your users will see: new signers, per sign, with error bars." Then set assignment 5.

### Segment 1 (6 min): isolated signs as sequences

- **Isolated sign recognition** labels a clip containing one sign, from start to rest. Continuous signing, with no pauses between signs, is session 6.
- A standard word-level dataset is WLASL, with about 2,000 American Sign Language words; accuracy on the full 2,000 words was far lower than on its 100-word subset, and in its authors' comparison a model reading raw video beat a pose-based graph model (Li et al. 2020). For any BdSL word dataset, check its vocabulary size, licence and number of signers before you use it.
- Each clip becomes a sequence of landmark frames (session 4), normalized for position and size. Signs vary in length because people sign at different speeds.
- A batch needs equal lengths, so we **pad** short sequences and keep a **mask** of the real frames. Averages and attention must ignore the padding; a recurrent network can skip it with packed sequences.
- Encoders over time: a 1-D convolution (local patterns, fast), a recurrent network such as a GRU (reads frames in order), or a Transformer encoder (attention between all frames; Course 4 session 1).
- **Pause and try:** sequence values 2, 4, 6 are padded to 2, 4, 6, 6, 6. What is the plain mean, and the masked mean?
  - **Answer:** 4.8 and 4.0. Without the mask, a short sign is pulled towards its last frame.

### Segment 2 (7 min): the skeleton as a graph

- The 21 landmarks are nodes and the bones are edges. A **spatial–temporal graph convolutional network** (ST-GCN; Yan et al. 2018) alternates two steps.
- The **spatial step** mixes each node's features with its neighbours', weighted by the normalized adjacency $D^{-1/2} A D^{-1/2}$, as in a graph convolutional network (Course 7 session 2). Yan et al. use separate weights for different groups of neighbours; our lab uses one weight for the node itself and one for its neighbours.
- The **temporal step** is a 1-D convolution over time for each node, so the network sees how every joint moves.
- Stacking blocks widens what each output sees in both space and time. Each node starts with its position and velocity.
- Graph models put the body's structure into the architecture and share weights across joints, so they can be small: in the lab the ST-GCN had 17,716 parameters against the GRU's 34,484.
- **Pause and try:** the index fingertip (landmark 8) is joined to 7, 7 to 6, 6 to the knuckle 5, and 5 to the wrist and the middle knuckle. Which landmarks can affect the fingertip's features after three spatial steps?
  - **Answer:** 8, 7, 6 and 5: one bone per step, so three steps reach the knuckle but not yet the wrist.

### Segment 3 (7 min): evaluation and augmentation

- **Split by signer.** A random split puts each person's style in both training and test sets. In the lab, the GRU scored 0.988 on a random split and 0.870 on four unseen signers.
- **Top-1 and top-5 accuracy:** top-5 counts a prediction as correct if the true sign is among the five best guesses, useful for a sign search interface with many classes; with 20 signs every lab model reached top-5 1.000. Report per-sign accuracy too, and watch class balance.
- **Error bars:** with 400 test sequences the standard error of an accuracy near 0.87 is 0.017, and more in practice because they come from only four signers (Course 1 session 9).
- **Augmentation** adds variation to training data: time warping (other speeds), small rotations, mirroring for left-handed signers, and landmark dropout (frames where the detector lost the hand). In the lab, time warping did not help: 0.853 with it, 0.870 without, probably because averaging over frames already made the GRU insensitive to speed.
- Lab recordings differ from everyday video: other cameras, light, clothing, backgrounds, partial views, signing styles and regional variants. Test there before you claim a result.
- **Pause and try:** model A scores 0.870 and model B 0.853 on the same 400 test sequences. Is A clearly better?
  - **Answer:** no. The gap, 0.017, is one standard error, and the four test signers make the real uncertainty larger.

### Lab guide (about 2.5 hours, notebook `s05_isolated_signs.ipynb`)

1. Section 1 (10 min): speed, padding and top-k by hand.
2. Section 2 (25 min): 20 synthetic signs from handshape, location, movement and orientation; minimal pairs; 16 signers with personal variants.
3. Section 3 (45 min): the GRU and the ST-GCN; random against new-signer splits; time-warp augmentation.
4. Section 4 (15 min): replaying new signers' signs faster and slower.
5. Section 5 (15 min): per-sign accuracy and confusions.
6. TODO cells (40 min).

- **Expect:** 32 frames; means 4.8 and 4.0. Top-1: GRU 0.988 (random split), GRU 0.870, ST-GCN 0.797 and GRU with time warp 0.853 (new signers); top-5 1.000 for all; standard error 0.017. Replayed at 0.6–1.6 times the speed: 0.865–0.882 without time warp, 0.853–0.865 with it. Worst signs: S10 0.30 (taken for S11 14 times), S01 0.55; per-signer accuracy 0.800–0.940. Runtime about 70 seconds.
- **Common problems:** a bidirectional GRU run over padding without packing; mean-pooling over padded frames; forgetting that a stride-2 layer halves the valid lengths; a random split that leaks signers.

### Quiz

1. Why does a random split overestimate accuracy for new users?
   - **Answer:** every test signer also appears in training, so the model can learn their personal variant of each sign. In the lab: 0.988 against 0.870.
2. What do the spatial and temporal steps of an ST-GCN each do?
   - **Answer:** the spatial step mixes each landmark with its skeleton neighbours (a graph convolution); the temporal step convolves each landmark's features over time.
3. Time-warp augmentation lowered accuracy from 0.870 to 0.853 in the lab. Should you conclude it is harmful?
   - **Answer:** no. The difference is about one standard error, and the GRU was already insensitive to speed; augmentation helps only against variation the model has not yet learned to ignore.

**Watch out:** "High accuracy on a random split means the model will work for new signers." A random split rewards remembering each person's way of signing: in the lab, accuracy fell from 0.988 to 0.870 on unseen signers, and their hardest sign scored only 0.30. Split by signer, report per signer and per sign, and test with the people who will use the system.

### Assignment 5 (due before session 6, 10 points)

1. By hand: the temporal receptive field, in frames, of three ST-GCN blocks with kernel 5 and stride 2 in the last block; and the landmarks that can reach the thumb tip (4) after two spatial steps. (3 points)
2. Complete both TODO cells and report a table: accuracy on clean and on frame-frozen new-signer tests, for the GRU with and without the frame-freezing augmentation and for your temporal CNN. (4 points)
3. Run four-fold cross-validation by signer (four signers per fold) for the GRU and report the mean, the range and a 95% interval. Compare it with the single split above. (3 points)

Hand in one PDF and your notebook.

### Sources

- Yan, Xiong & Lin 2018, Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition, AAAI. https://arxiv.org/abs/1801.07455
- Li, Rodriguez Opazo, Yu & Li 2020, Word-level Deep Sign Language Recognition from Video: A New Large-scale Dataset and Methods Comparison (WLASL), WACV. https://arxiv.org/abs/1910.11006
- Bragg et al. 2019, Sign Language Recognition, Generation, and Translation: An Interdisciplinary Perspective, ASSETS. https://arxiv.org/abs/1908.08597
- MediaPipe source code, release 1.2.3 (Hand Landmarker video mode in the Tasks API). https://github.com/google/mediapipe

## Session 6: Continuous signing and sign language translation

**Goal:** students can train a CTC model on continuous signing, decode it, and evaluate recognition and translation with the right metrics.

### Talking pointers

- **Open with:** "A signed sentence is not a list of signs with pauses between them. The signs flow into each other, and their order follows the sign language's grammar, not Bangla's."
- **Segment 1, say:** show the plot of one test sentence: the hand never rests between signs, and the wrist moves fastest in the transitions.
- **Segment 2, say:** write `TOMORROW I MARKET GO` and "আমি কাল বাজারে যাব" on the board, and mark every change: word order, the case ending, the verb form.
- **Segment 3, say:** show the BLEU and chrF bars, where the sentence that means the opposite wins.
- **Close with:** "Recognition finds the signs; translation must carry the meaning, and only people who know both languages can judge it." Then set assignment 6.

### Segment 1 (6 min): continuous recognition

- In continuous signing there are no pauses between signs. The hand travels from the end of one sign to the start of the next, and each sign is shaped by its neighbours (**co-articulation**), so there are no clean boundaries to cut at.
- **Glosses** are written labels for signs, usually spoken-language words in capitals, such as GO. They are not translations: a gloss sequence keeps the sign order and leaves out much of what space, movement and the face express. Gloss annotation needs trained annotators, and conventions differ between datasets.
- CTC (session 2) needs only the gloss sequence of each sentence, not the boundaries. A common benchmark is RWTH-PHOENIX-Weather 2014T: German Sign Language weather forecasts from television, with glosses and German translations (Camgoz et al. 2018).
- **Decoding:** greedy decoding takes the best symbol per frame; **prefix beam search** keeps several output prefixes and sums the frame paths that give each one (Hannun 2017). It can add a **gloss language model** with weight α and a per-gloss bonus β, tuned on held-out signers.
- **Pause and try:** the reference is `TOMORROW I MARKET GO` and the output is `TOMORROW I SCHOOL GO NOT`. What is the gloss WER?
  - **Answer:** one substitution and one insertion, 2 edits over 4 reference glosses: 0.50.

### Segment 2 (7 min): translation, not recognition

- **Sign language translation** produces a sentence in a spoken language. Grammar and word order differ, and meaning carried by space, movement and facial expression must become words. `TOMORROW I MARKET GO` becomes "আমি কাল বাজারে যাব": the subject moves first, বাজার takes the ending -এ, and the verb takes its future first-person form. In everyday Bangla you even "eat" water (পানি খাওয়া), so one gloss does not map to one word.
- Camgoz et al. (2018) treated this as neural machine translation from video with an attention-based encoder–decoder. They compared translating straight from video with going through glosses (recognize glosses, then translate them to text).
- Sign Language Transformers (Camgoz et al. 2020) train one transformer for both tasks at once: a CTC loss on glosses for recognition and a translation loss on the spoken-language sentence. **Gloss-free** methods skip gloss annotation, which is slow and expensive to produce.
- Data are the bottleneck. PHOENIX-2014T covers one narrow topic, weather. Before planning BdSL translation, check what sentence-level BdSL data exist; building such a corpus needs Deaf signers, interpreters and annotators, all paid.
- **Pause and try:** in "আমি কাল বাজারে যাব", how many of the four words are exactly the dictionary form of their gloss (I, TOMORROW, MARKET, GO)?
  - **Answer:** two, আমি and কাল. বাজারে has a case ending and যাব is an inflected verb, not the dictionary form যাওয়া.

### Segment 3 (7 min): metrics and people

- **Recognition** is scored with gloss WER: substitutions, deletions and insertions over the number of reference glosses.
- **BLEU** (Papineni et al. 2002) multiplies a brevity penalty by the geometric mean of clipped n-gram precisions for n = 1 to 4, summed over a whole test set. Report it with sacreBLEU and its signature, so that others can reproduce the number (Post 2018).
- **chrF** (Popović 2015) is an F-score over character n-grams, so বাজার and বাজারে get partial credit; this suits languages with many word endings, such as Bangla.
- Both count shared pieces of text and ignore meaning. In the lab, the sentence "আমি কাল বাজারে যাব না" ("I will **not** go ...") scored BLEU 66.9 and chrF 96.8, while a correct paraphrase scored 35.4 and 60.4.
- Translations for Deaf users need human evaluation by Deaf signers and bilingual experts: is the meaning right (adequacy), does it read well (fluency), does it work for the task? Deaf people should help build and judge these systems (Bragg et al. 2019), and an automatic translator must not replace qualified interpreters where errors cause harm, as in health, law or education.
- **Pause and try:** of the four candidates in the lab (word-for-word glosses, correct paraphrase, negated, wrong place), which gets the highest BLEU?
  - **Answer:** the negated sentence, 66.9: it shares every word of the reference and adds one.

### Lab guide (about 2.5 hours, notebook `s06_continuous_signing.ipynb`)

1. Section 1 (10 min): gloss WER and n-gram matches by hand.
2. Section 2 (20 min): continuous sentences built from session 5's signs, with transitions between them.
3. Section 3 (30 min): train the CTC gloss recognizer; watch the WER fall.
4. Section 4 (35 min): greedy decoding, prefix beam search, and beam search with a gloss bigram model tuned on a held-out signer.
5. Section 5 (25 min): BLEU and chrF from scratch on four candidate translations.
6. TODO cells (30 min).

- **Expect:** gloss WER 0.50 by hand; n-gram matches 4/5, 3/4, 2/3, 1/2. 800 sentences of 58 to 177 frames. Test gloss WER (greedy) 0.380, 0.081, 0.043 and 0.015 after 5, 10, 15 and 20 epochs. Final test gloss WER: greedy 0.015, prefix beam search 0.013, beam with the bigram model (α = 0.3, β = 1.0) 0.004; fully correct sentences 0.945, 0.950 and 0.985. BLEU / chrF: word-for-word 19.0 / 34.9, paraphrase 35.4 / 60.4, negated 66.9 / 96.8, wrong place 35.4 / 38.6. Runtime about 40 seconds.
- **Common problems:** tuning the language-model weights on the test signers; computing BLEU per sentence and averaging instead of over the corpus; comparing BLEU numbers computed with different tokenizers.

### Quiz

1. Why not cut a continuous sentence into signs and use session 5's isolated-sign classifier?
   - **Answer:** there are no clear boundaries, and co-articulation changes each sign's form. CTC learns the segmentation implicitly from gloss sequences.
2. What did the gloss language model fix, and what could it not fix?
   - **Answer:** it lowered gloss WER from 0.013 to 0.004 by preferring grammatical gloss orders, but `MOTHER HOME GO` read as `MOTHER SCHOOL GO` stayed wrong, because both are grammatical.
3. Why is a high BLEU not proof of a good translation?
   - **Answer:** BLEU counts shared word sequences, not meaning: the negated sentence scored 66.9 against 35.4 for a correct paraphrase.

**Watch out:** "Sign language translation is recognizing each sign in turn." Recognition gives glosses in signing order; translation must produce a grammatical sentence in another language, with its own order, endings and idioms, and put into words what space, movement and the face express. In the lab, replacing glosses word for word gave the lowest BLEU of all four candidates, 19.0.

### Assignment 6 (due before session 7, 10 points)

1. By hand, compute the four n-gram precisions, the smoothed values and the BLEU score of "আগামীকাল আমি বাজারে যাব" against "আমি কাল বাজারে যাব", and check that you get 35.4. (3 points)
2. Complete both TODO cells: a rule-based gloss-to-Bangla translator checked by a Bangla speaker, with the corpus BLEU of the greedy and beam outputs; and the gloss WER for faster signing. (4 points)
3. Write ten Bangla test pairs (paraphrases and meaning changes), score them with BLEU and chrF, and describe a human evaluation with Deaf signers: who rates, what they rate, and how they are paid. (3 points)

Hand in one PDF and your notebook.

### Sources

- Camgoz, Koller, Hadfield & Bowden 2020, Sign Language Transformers: Joint End-to-end Sign Language Recognition and Translation, CVPR. https://arxiv.org/abs/2003.13830
- Papineni, Roukos, Ward & Zhu 2002, BLEU: a Method for Automatic Evaluation of Machine Translation, ACL. https://aclanthology.org/P02-1040/
- Camgoz, Hadfield, Koller, Ney & Bowden 2018, Neural Sign Language Translation, CVPR (introduces RWTH-PHOENIX-Weather 2014T).
- Popović 2015, chrF: character n-gram F-score for automatic MT evaluation, WMT. https://aclanthology.org/W15-3049/
- Post 2018, A Call for Clarity in Reporting BLEU Scores, WMT. https://arxiv.org/abs/1804.08771
- Hannun 2017, Sequence Modeling with CTC (prefix beam search), Distill. https://distill.pub/2017/ctc/
- Bragg et al. 2019, Sign Language Recognition, Generation, and Translation: An Interdisciplinary Perspective, ASSETS. https://arxiv.org/abs/1908.08597

## Session 7: Lip reading

**Goal:** students can explain visual speech recognition and its limits, build a lip-landmark graph model with attention, and show how audio-visual fusion helps in noise.

### Talking pointers

- **Open with:** "Say 'pat', 'bat' and 'mat' to a mirror with the sound off: you cannot tell them apart, and neither can a camera. Today we find where a lip reader must fail, and where it helps most."
- **Segment 1, say:** mouth /p/, /b/ and /m/ silently on camera, then derive the lab vocabulary's 0.65 ceiling together.
- **Segment 2, say:** show the lip graph, compute one attention softmax by hand, then compare Auto-AVSR's 19.1% video-only error with 1.0% from audio.
- **Segment 3, say:** show where the audio and video curves cross and why late fusion won; end on consent.
- **Close with:** "Lip reading is a partial signal that matters most when the audio fails, and it reads faces, so it needs consent." Then set assignment 7.

### Segment 1 (6 min): what the lips show, and what they hide

- Lip reading (speechreading) is one strategy some deaf and hard-of-hearing people use, alongside sign language (sessions 4–6), captions (session 3) and hearing technology. Machine lip reading, or visual speech recognition (VSR), turns video of the mouth into text; it can also help in noisy places and with silent speech, where words are mouthed without sound.
- A phoneme is a unit of sound; a **viseme** is a lip shape shared by several phonemes (Fisher 1968). /p/, /b/ and /m/ all close the lips; voicing happens at the vocal folds and nasality behind the mouth, so neither can be seen.
- Words with the same viseme sequence are **homophenes**, such as *pat*, *bat* and *mat* (Course 4 session 9). Context helps; the video alone cannot decide.
- People lip-read only part of what is said. In the LipNet study, three lip readers with hearing loss made 47.7% word errors on new speakers from GRID, a corpus with a tiny fixed grammar (Assael et al. 2016).
- **Pause and try:** 20 equally common words contain homophene groups of sizes 3, 2, 3, 2 and 2, and 8 words with unique lip patterns. What is the best possible accuracy from video alone?
  - **Answer:** each group yields at most one right answer, so 5 + 8 = 13 patterns and 13/20 = 0.65.

### Segment 2 (7 min): datasets and models

- Datasets: GRID, 1,000 six-word sentences from each of 34 talkers (Cooke et al. 2006); LRW, 500 words from BBC television, up to 1,000 clips each (Chung & Zisserman 2016); LRS2 and LRS3, sentences from British television and over 400 hours of TED talks (Afouras et al. 2018; Afouras, Chung & Zisserman 2018).
- Pixel models crop the mouth, apply a 3-D convolution over time and space, a ResNet per frame and a temporal model (GRU, Transformer or Conformer), trained with CTC (session 2) or an attention decoder. LipNet made 4.8% word errors on GRID for speakers seen in training and 11.4% on new speakers (Assael et al. 2016).
- Auto-AVSR trained on 3,448 hours, including unlabelled video transcribed automatically, and reports word error rates (WER) on LRS3 of 19.1% from video, 1.0% from audio and 0.9% from both (Ma et al. 2023). AV-HuBERT learns from unlabelled video by self-supervision (Shi et al. 2022; Course 4 session 9).
- Landmark models are a light alternative: track the 20 mouth points of the common 68-point face markup as a graph. A **graph attention** (GAT) layer (Veličković et al. 2018; Course 7 session 2) scores each neighbour j of point i, $e_{ij} = \text{LeakyReLU}(a^\top[Wh_i \,\|\, Wh_j])$, turns the scores into weights $\alpha_{ij}$ with a softmax over the neighbours, and sums $\alpha_{ij} W h_j$. Landmarks are light but drop the teeth and tongue, which carry information.
- Bangla lip-reading data are scarce. Two public examples: LipBengal, 150 speakers and 73 classes of Bangla phonemes, letters and symbols (Sahed et al. 2025), and LRW-B, videos of isolated Bangla words (Uddin 2024).
- **Pause and try:** a landmark and its three neighbours get attention scores 2, 1, 1 and 0. What are the weights?
  - **Answer:** $e^2, e^1, e^1, e^0$ = 7.39, 2.72, 2.72 and 1.00, summing to 13.83, so 0.534, 0.197, 0.197 and 0.072.

### Segment 3 (7 min): audio-visual fusion, and consent

- The signal-to-noise ratio (SNR) is $10\log_{10}(P_\text{speech}/P_\text{noise})$ decibels (dB): 0 dB means equal power; −10 dB means ten times more noise than speech.
- Sound and lips fail differently. In a classic listening study, noise destroyed the place of articulation (where the sound is made: lips, teeth, gums or the back of the mouth) first, while voicing and nasality survived better (Miller & Nicely 1955); a repeat found voicing less robust (Lovitt & Allen 2006). Place is what the lips show.
- Fusion can be early (concatenate each frame's audio and video features), late (add the log-probabilities of two separate models), or in between, with cross-attention.
- In the lab, late fusion was best or tied at every SNR. The jointly trained early-fusion model leaned on the easier audio stream: with pure-noise audio it scored 0.160, against 0.618 for video alone. A jointly trained multimodal network can do worse than its best single stream, partly because the streams overfit and generalize at different rates (Wang, Tran & Feiszli 2020), so always compare with each stream alone.
- Faces identify people, and lip reading CCTV or phone video can expose private conversations: surveillance. Use consented data, process on the device, and let the deaf user decide when the system runs.
- **Pause and try:** speech power is 1 and noise power is 4. What is the SNR?
  - **Answer:** $10\log_{10}(1/4) = -6.0$ dB. In the lab, audio alone still beat the lips at −5 dB (0.728 against 0.618) but lost at −10 dB (0.420).

### Lab guide (about 2 hours, notebook `s07_lip_reading.ipynb`)

1. Section 1 (15 min): visemes, homophene groups and the ceiling.
2. Section 2 (25 min): 30 synthetic speakers; the *pat* and *mat* curves coincide. Follow the normalization.
3. Section 3 (20 min): the lip graph and GAT layer; check the attention weights.
4. Section 4 (25 min): the video-only reader and its confusion matrix.
5. Section 5 (20 min): audio and fusion models; where the curves cross.
6. TODO cells (15 min).

- **Expect:** 13 distinct viseme sequences for 20 words, so a ceiling of 0.650. The video-only model (34,964 parameters) scores 0.618 on six new speakers, with group accuracy 0.950, and 0.869 of its errors stay inside the true word's homophene group. At 20, 0, −10 and −20 dB: audio only 1.000, 0.902, 0.420 and 0.110; early fusion 1.000, 0.957, 0.635 and 0.313; late fusion 1.000, 0.993, 0.788 and 0.642. Early fusion with pure-noise audio: 0.160. Runtime about 65 seconds.
- **Common problems:** dividing each frame by its own mouth width, which erases the width changes that signal rounding; splitting clips at random instead of by speaker (session 5); forgetting the attention mask.

### Quiz

1. What is a viseme, and why can't a lip reader tell *pat* from *bat*?
   - **Answer:** a lip shape shared by several phonemes. /p/ and /b/ differ only in voicing, which happens at the vocal folds and cannot be seen.
2. In a GAT layer, what does the softmax normalize, and what does the graph mask do?
   - **Answer:** it turns each node's scores for its neighbours into weights that sum to 1; the mask keeps every non-neighbour's weight at zero.
3. Why does late fusion help most when the audio is noisy?
   - **Answer:** noisy audio gives flat word probabilities, so the video model's scores decide; clean audio gives confident scores that separate the homophenes.

**Watch out:** "Lip reading can recover everything that was said." Homophenes make some words impossible to tell apart from video: no model in the lab could beat 0.650, and ours reached 0.618. Even Auto-AVSR, trained on 3,448 hours, makes 19.1% word errors on LRS3 from video alone, against 1.0% from audio. Use lip reading to support noisy audio and captions, never as a transcript to trust alone or a replacement for interpreters and captioners.

### Assignment 7 (due before session 8, 10 points)

1. By hand: the video-only ceiling for 14 equally common words in homophene groups of sizes 4, 2 and 2 plus 6 unique words; the attention weights for scores 1, 0, 0 and −1; the SNR when noise power is 10 times speech power. Check the last two in code. (3 points)
2. Complete the first TODO cell: replace graph attention with a per-frame MLP and compare parameters, word accuracy and group accuracy, with and without 5 landmarks removed from every test frame. Is the graph worth it? (4 points)
3. Complete the second TODO cell: a fusion model whose lip branch starts from the trained video model, and one trained only down to −10 dB. Plot every fusion curve and explain the differences in a paragraph. (3 points)

Hand in one PDF and your notebook.

### Sources

- Afouras, Chung, Senior, Vinyals & Zisserman 2018, Deep Audio-Visual Speech Recognition. https://arxiv.org/abs/1809.02108
- Ma, Haliassos, Fernandez-Lopez, Chen, Petridis & Pantic 2023, Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels. https://arxiv.org/abs/2303.14307
- Assael, Shillingford, Whiteson & de Freitas 2016, LipNet: End-to-End Sentence-level Lipreading. https://arxiv.org/abs/1611.01599
- Veličković et al. 2018, Graph Attention Networks. https://arxiv.org/abs/1710.10903
- Cooke, Barker, Cunningham & Shao 2006, An audio-visual corpus for speech perception and automatic speech recognition, Journal of the Acoustical Society of America 120(5), 2421–2424. https://doi.org/10.1121/1.2229005
- Chung & Zisserman 2016, Lip Reading in the Wild (Asian Conference on Computer Vision).
- Afouras, Chung & Zisserman 2018, LRS3-TED: a large-scale dataset for visual speech recognition. https://arxiv.org/abs/1809.00496
- Shi, Hsu, Lakhotia & Mohamed 2022, Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction (AV-HuBERT). https://arxiv.org/abs/2201.02184
- Fisher 1968, Confusions among visually perceived consonants, Journal of Speech and Hearing Research 11(4), 796–804. https://doi.org/10.1044/jshr.1104.796
- Miller & Nicely 1955, An analysis of perceptual confusions among some English consonants, Journal of the Acoustical Society of America 27.
- Lovitt & Allen 2006, 50 years late: repeating Miller–Nicely 1955 (Interspeech). https://www.isca-archive.org/interspeech_2006/lovitt06_interspeech.html
- Wang, Tran & Feiszli 2020, What Makes Training Multi-Modal Classification Networks Hard? https://arxiv.org/abs/1905.12681
- Sahed et al. 2025, LipBengal: Pioneering Bengali lip-reading dataset for pronunciation mapping through lip gestures, Data in Brief 58, 111254. https://www.sciencedirect.com/science/article/pii/S2352340924012162
- Uddin 2024, Lip Reading Word-Bangla (LRW-B) Dataset, Mendeley Data. https://data.mendeley.com/datasets/k5d598277b
- Visual speech recognition models and code by the Auto-AVSR authors (repository). https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages

## Session 8: Describing images for blind and low-vision users

**Goal:** students can explain how image captioning and visual question answering serve blind users, detect unusable photos, and make a model abstain when it is unsure.

### Talking pointers

- **Open with:** "A blind student photographs a notice board and asks, 'What does it say?' The photo is blurred and cut off at the top. The most useful answer is not a guess: it is 'move the phone up and hold it still'."
- **Segment 1, say:** let a screen reader read a web page with and without alt text, then show the five damaged crops from the notebook.
- **Segment 2, say:** draw a 3 × 3 image–caption similarity matrix, then show how wording changed the tiny CLIP's accuracy.
- **Segment 3, say:** show the coverage–accuracy plot and read out the notebook's five messages.
- **Close with:** "Check the photo first, describe only what you can see, and say 'I am not sure' when you are not." Then set assignment 8.

### Segment 1 (6 min): what blind users need from a description

- A screen reader (TalkBack on Android, VoiceOver on iOS, NVDA on Windows) reads the screen aloud. For an image it can only read the **alternative text** (alt text) its author wrote. WCAG requires a text alternative for non-text content (success criterion 1.1.1), and purely decorative images should be hidden from screen readers (W3C 2023).
- Photos that blind people take themselves never come with alt text. In VizWiz, blind people took over 31,000 photos with a phone and recorded a spoken question about each, and every question received 10 answers from crowd workers. The photos are often poor in quality, the questions are conversational, and many cannot be answered from the photo at all (Gurari et al. 2018).
- So a useful system checks the photo and says how to fix it, answers only what the photo supports, and says what it could not do.
- Simple checks: blur removes edges, so the **variance of the Laplacian** (an edge filter), a classic focus measure, drops; darkness shows in the mean brightness, over-exposure in the share of pixels clipped at white.
- **Pause and try:** in the lab, the checks rejected 25% of good china crops and accepted 0.4% of damaged ones. If 30% of a user's photos are damaged, what share of all photos is rejected?
  - **Answer:** 0.7 × 0.25 + 0.3 × 0.996 = 0.175 + 0.299 ≈ 0.47: almost half, and over a third of those retakes (0.175 of 0.47) are unnecessary.

### Segment 2 (7 min): models that describe

- Image **captioning** generates a sentence from an image; **visual question answering** (VQA) answers a question about it.
- CLIP trains an image encoder and a text encoder on 400 million image–caption pairs with a contrastive loss, so that matching pairs get similar unit vectors (Radford et al. 2021). It describes by retrieval, picking the candidate description most similar to the image. Course 4 session 9 covers CLIP and vision-language models (VLMs), which connect an image encoder to a language model.
- BLIP adds a caption generator and cleans noisy web captions with a captioner and a filter (Li et al. 2022).
- Text in photos (medicine labels, notices, bus signs) needs reading, and VLMs are weak on Bangla script (Course 4 session 9); session 9 builds OCR (optical character recognition).
- In the lab's tiny CLIP, the wording mattered: 0.957 test accuracy with a training template, 0.904 with an unseen one.
- **Pause and try:** an image has cosine similarities 0.9, 0.2 and 0.1 with three captions. What probability does the softmax give its own caption at temperature τ = 1, and at τ = 0.1?
  - **Answer:** at τ = 1, $e^{0.9}/(e^{0.9} + e^{0.2} + e^{0.1})$ = 2.46/4.79 ≈ 0.51; at τ = 0.1 the scores become 9, 2 and 1, giving 0.999. A small temperature (0.089 in the lab) makes the choice sharp.

### Segment 3 (7 min): failure, evaluation and abstaining

- **Hallucination:** captioning models mention objects that are not in the image, and standard caption metrics do not always penalize it (Rohrbach et al. 2018). A fluent sentence hides the error from a user who cannot see the photo.
- Caption metrics such as BLEU (session 6) and CIDEr (Vedantam et al. 2015) measure overlap with captions written by sighted people, not usefulness. Test with blind users on real tasks: did they read the right dose?
- **Selective prediction** answers only when a confidence score passes a threshold chosen on validation data (Chow 1970; Geifman & El-Yaniv 2017). **Coverage** is the share of inputs answered; raising the threshold lowers coverage and usually raises accuracy. Course 3 session 12 covers calibration and conformal prediction.
- Confidence is not enough. In the lab, the threshold answered 0.912 of clean digits at 0.986 accuracy, but also 0.668 of cut-off digits (0.140 of those right) and 0.593 of photo patches with no digit. A framing check flagged 0.705 of cut-off digits, with no false alarms.
- Privacy: photos can show letters, bank cards and other people's faces that the user cannot see before sending. Prefer on-device processing, warn before uploading, and do not store photos.
- **Pause and try:** at a threshold, a model answers 800 of 1,000 test images and gets 784 right. What are its coverage and its accuracy on answered images?
  - **Answer:** coverage 800/1,000 = 0.80; accuracy 784/800 = 0.98.

### Lab guide (about 2 hours, notebook `s08_image_description.ipynb`)

1. Section 1 (20 min): five conditions, three measures, example crops.
2. Section 2 (25 min): thresholds from china crops, tested on new china crops and on the flower; the histograms.
3. Section 3 (25 min): the tiny CLIP and its templates.
4. Section 4 (25 min): the margin threshold, three damaged sets, coverage–accuracy curves.
5. Section 5 (15 min): the framing check and the user messages.
6. TODO cells (10 min).

- **Expect:** thresholds: dark below a mean of 0.205, bright above 0.223 clipped, blurry below a focus of −1.60. New china crops: correct verdict 0.947, good crops rejected 0.250, damaged accepted 0.004; flower crops: correct verdict 0.717, good rejected 0.817. Tiny CLIP test accuracy 0.950 to 0.957 with training templates, 0.904 with the unseen one. Margin threshold 0.122: clean digits answered 0.912 at accuracy 0.986 (0.957 if always answering); cut-off digits answered 0.668 at 0.140; blurred digits 0.657 at 0.322; no-digit patches answered 0.593. Framing check: 0.705 of cut-off digits, none of the clean or blurred ones. Runtime about 12 seconds.
- **Common problems:** choosing thresholds on the test crops; computing the focus measure on 0–255 values, so the thresholds no longer match; forgetting to normalize embeddings, so long vectors win.

### Quiz

1. Name two reasons a VizWiz question may be unanswerable.
   - **Answer:** the photo is too blurry or too dark, or it does not show what the question asks about, for example because the object is out of the frame.
2. How does a CLIP-style model describe an image by retrieval?
   - **Answer:** it embeds the image and every candidate description as unit vectors and picks the description with the highest cosine similarity.
3. Why did the margin threshold fail on photo patches with no digit?
   - **Answer:** the model only saw digits, so unfamiliar inputs can still get large margins; confidence tested on familiar data says nothing about foreign inputs.

**Watch out:** "A fluent caption is a correct caption." Fluency comes from the language side of the model; correctness must come from the image. In the lab, a blurred seven was confidently called "a handwritten eight", and 0.593 of patches with no digit got a digit description. Check the photo, measure accuracy for each kind of input, and prefer "I am not sure" to a smooth wrong answer.

### Assignment 8 (due before session 9, 10 points)

1. By hand: the softmax probability of the first caption for similarities 0.8, 0.5 and 0.1 at τ = 1 and τ = 0.1; and the share of photos rejected when 20% are damaged, using the flower rates (good rejected 0.817, damaged accepted 0.000). (3 points)
2. Complete the first TODO cell: a focus measure divided by the image variance. Choose its threshold on china crops only and report how it transfers to the flower photo. Explain why it helps or not. (4 points)
3. Complete the second TODO cell: an "unknown" description trained on photo patches. Report how many no-digit patches still get a digit description and whether clean accuracy changes, and write the message a blind user should hear in that case. (3 points)

Hand in one PDF and your notebook.

### Sources

- Gurari et al. 2018, VizWiz Grand Challenge: Answering Visual Questions from Blind People. https://arxiv.org/abs/1802.08218
- Radford et al. 2021, Learning Transferable Visual Models From Natural Language Supervision (CLIP). https://arxiv.org/abs/2103.00020
- Li, Li, Xiong & Hoi 2022, BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation. https://arxiv.org/abs/2201.12086
- Rohrbach, Hendricks, Burns, Darrell & Saenko 2018, Object Hallucination in Image Captioning. https://arxiv.org/abs/1809.02156
- Vedantam, Zitnick & Parikh 2015, CIDEr: Consensus-based Image Description Evaluation. https://arxiv.org/abs/1411.5726
- Geifman & El-Yaniv 2017, Selective Classification for Deep Neural Networks. https://arxiv.org/abs/1705.08500
- Chow 1970, On optimum recognition error and reject tradeoff, IEEE Transactions on Information Theory 16(1).
- W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/

## Session 9: Reading support: OCR, text-to-speech and simplification

**Goal:** students can explain OCR and text-to-speech pipelines for Bangla, train a line recognizer with CTC, and normalize text for a speech synthesizer.

### Talking pointers

- **Open with:** "A blind student receives a printed Bangla notice from the university office. One machine reads the print into text, another speaks the text aloud, and each can fail in ways the student will never see."
- **Segment 1, say:** write কি on the board and show that the sign drawn first is stored second; then show the joined line that segmentation read as 12 and the CTC reader as 1722.
- **Segment 2, say:** read "Tk 2,50,000" aloud in both number systems and ask which one a listener in Dhaka expects.
- **Segment 3, say:** put the original and the wrong simplified dosage side by side and do the arithmetic together.
- **Close with:** "Every step from paper to speech can change the meaning, so test each step on real documents with real readers." Then set assignment 9.

### Segment 1 (6 min): reading Bangla print

- Optical character recognition (OCR) turns an image of text into characters. Bangla print makes it hard in three ways: a vowel sign can be drawn on the left of a consonant but stored after it (কি); conjuncts join consonants with the hasanta (ক্ষ = ক + ্ + ষ); and the headline (মাত্রা) joins the letters of a word, so there is no white space between them.
- The same text can be stored as different code points (য় as one or two), so normalize the OCR output and the truth with NFC before scoring (Course 5 session 2; Unicode Standard Annex #15).
- An OCR pipeline first finds text lines (detection), then reads each line (recognition). A CRNN (Shi et al. 2017) turns the line image into a sequence of CNN features, reads them with a bidirectional recurrent network and trains with CTC (Graves et al. 2006; session 2), so it never cuts the line into letters. Tesseract's LSTM engine also reads whole lines and has a Bengali model, `ben` (Tesseract tessdata); Course 4 session 9 compares it with a vision-language model on Bangla text.
- Handwritten Bangla data include NumtaDB, a collection of handwritten digits (Alam et al. 2018), and BanglaLekha-Isolated, with basic letters, digits and common conjuncts (Biswas et al. 2017).
- **Pause and try:** how many code points does ক্ষি have, and in what order are they stored?
  - **Answer:** 4: ক, the hasanta, ষ and then the vowel sign ি, although ি is drawn first, on the left.

### Segment 2 (7 min): text-to-speech

- Text-to-speech (TTS) lets a screen reader speak (session 8) and can read documents aloud for anyone who finds print hard to read. A classic pipeline has four stages: text normalization, grapheme-to-phoneme conversion, an acoustic model and a vocoder.
- **Text normalization** rewrites non-standard words (numbers, currency, dates, times, abbreviations) as ordinary words (Sproat et al. 2001). The right reading depends on place and role: Bangladesh groups and reads large numbers in lakh (1,00,000) and crore (1,00,00,000); "2026" is a year in "in 2026" but a quantity in "2026 forms"; Bangla digits can appear inside English text.
- **Grapheme-to-phoneme** (G2P) conversion maps spelling to sounds. Bangla spelling does not show when a consonant's inherent vowel is spoken: কলম (pen) is spoken *kɔlom*, with a vowel after ক and ল but none after ম.
- The **acoustic model** maps phonemes or characters to a mel spectrogram (Tacotron 2, which reads characters; Shen et al. 2018), and the **vocoder** turns the spectrogram into a waveform (HiFi-GAN; Kong, Kim & Bae 2020).
- A screen reader reads Bangla only as well as its installed voice and its normalization rules allow, so test with blind users on real bills, forms and notices.
- **Pause and try:** how should "Tk 2,50,000" be read in the South Asian and the international number systems?
  - **Answer:** "two lakh fifty thousand taka" and "two hundred and fifty thousand taka": the same number, and a listener in Bangladesh expects the first.

### Segment 3 (7 min): simplification and easy-to-read text

- Easy-to-read text helps people with intellectual disabilities and people with low literacy. WCAG success criterion 3.1.5 (level AAA) asks for a simpler version when a text needs reading ability beyond lower secondary school (W3C 2023).
- Readability formulas count length. The Flesch Reading Ease, 206.835 − 1.015 × (words per sentence) − 84.6 × (syllables per word), was built for English (Flesch 1948) and does not transfer to Bangla, whose words are built differently. No formula measures meaning.
- Large language models simplify fluently, but they can drop or change facts. Check numbers, names and negations automatically, and have a person, ideally someone from the intended readers, review the meaning.
- In the lab, a careful version halved the sentence length (8.7 to 4.3 words) and kept every number; a wrong version dropped two numbers, and the check caught that, but not the dangerous change in its dosage.
- **Pause and try:** the original says "2 tablets every 8 hours, no more than 6 in 24 hours"; the simplified text says "2 tablets every 6 hours". How many tablets a day does it imply?
  - **Answer:** 24/6 × 2 = 8, above the limit of 6: a short, fluent and dangerous sentence.

### Lab guide (about 2 hours, notebook `s09_reading_support.ipynb`)

1. Section 1 (15 min): code points, NFC and Bangla digits.
2. Section 2 (10 min): the digit CNN.
3. Section 3 (25 min): spaced and joined lines; segment-then-classify.
4. Section 4 (30 min): the CTC line reader; read the probability plot.
5. Sections 5–6 (25 min): text normalization and its tests; the simplification check.
6. TODO cells (15 min).

- **Expect:** কি has 2 code points and ক্ষি 4; NFC makes the two forms of য় equal. The digit CNN: test accuracy 0.973 on 594 digits. Segment-then-classify: CER 0.071 (line accuracy 0.672) on spaced lines, 0.602 (0.048) on joined lines. The CTC reader (44,907 parameters, about a minute of training): CER 0.022 (0.890) on spaced lines, 0.036 (0.824) on joined lines. 20 of 20 number tests pass; "Tk 2,50,000" becomes "two lakh fifty thousand taka". Simplification: 8.7 words per sentence in the original, 4.3 in the careful version; the wrong version misses 8 and 24. Runtime about 70 seconds.
- **Common problems:** scoring OCR output without NFC on both sides; giving `nn.CTCLoss` (batch, steps, symbols) instead of (steps, batch, symbols); expanding plain numbers before currency and percentages, so "Tk 2,50,000" never matches the currency rule.

### Quiz

1. Why does segment-then-classify fail on printed Bangla words?
   - **Answer:** the headline joins the letters, and conjuncts and vowel signs touch their neighbours, so there are no blank columns to cut at; touching letters merge into one piece.
2. Name the four stages of a classic TTS pipeline and what each produces.
   - **Answer:** text normalization (ordinary words), grapheme-to-phoneme conversion (phonemes), the acoustic model (a mel spectrogram) and the vocoder (a waveform).
3. Why must the OCR output and the truth both be NFC-normalized before computing the CER?
   - **Answer:** identical-looking text can use different code points, such as the two forms of য়, and these would be counted as errors although the reader sees no difference.

**Watch out:** "OCR is a solved problem." Even on synthetic digits, the segmenting reader failed on joined lines (CER 0.602), and the better CTC reader still got 18% of joined lines wrong. A single wrong digit changes a phone number, a dose or a bank account. Real Bangla documents add conjuncts, old fonts, stamps, handwriting and phone photos: measure the CER on your users' own documents, and tell the user when the text may be wrong.

### Assignment 9 (due before session 10, 10 points)

1. By hand: the code points of কৌ (it can be stored two ways; what does NFC give?); 1,05,00,000 read in both number systems; and the CER of reading 1722 as 12. Check all three in code. (3 points)
2. Complete the first TODO cell: Bangla number words from 0 to 99 from a verified source, extended to শত, হাজার, লাখ and কোটি, with at least 10 tests. Name your source. (4 points)
3. Complete the second TODO cell: test both readers on longer lines and on noisier lines, and discuss which failures a blind reader would notice. (3 points)

Hand in one PDF and your notebook.

### Sources

- Shi, Bai & Yao 2017, An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition (CRNN). https://arxiv.org/abs/1507.05717
- Sproat, Black, Chen, Kumar, Ostendorf & Richards 2001, Normalization of non-standard words, Computer Speech and Language 15(3).
- Graves, Fernández, Gomez & Schmidhuber 2006, Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks (ICML). https://www.cs.toronto.edu/~graves/icml_2006.pdf
- Alam, Reasat, Doha & Humayun 2018, NumtaDB: Assembled Bengali Handwritten Digits. https://arxiv.org/abs/1806.02452
- Biswas et al. 2017, BanglaLekha-Isolated: A multi-purpose comprehensive dataset of Handwritten Bangla Isolated characters, Data in Brief 12.
- Tesseract OCR, trained LSTM models including Bengali (`ben`) (repository). https://github.com/tesseract-ocr/tessdata_fast
- Shen et al. 2018, Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions (Tacotron 2). https://arxiv.org/abs/1712.05884
- Kong, Kim & Bae 2020, HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis. https://arxiv.org/abs/2010.05646
- Unicode Standard Annex #15, Unicode Normalization Forms. https://unicode.org/reports/tr15/
- W3C 2023, Web Content Accessibility Guidelines (WCAG) 2.2. https://www.w3.org/TR/WCAG22/
- Flesch 1948, A new readability yardstick, Journal of Applied Psychology 32(3).

## Session 10: Augmentative and alternative communication

**Goal:** students can explain AAC and its users, measure keystroke savings from word prediction, and compare access methods such as switch scanning.

### Talking pointers

- **Open with:** "Imagine answering every question today by selecting letters one at a time while your friends wait. For some people who use AAC, every conversation works like that. Today we measure how prediction and good design give them back time."
- **Segment 1, say:** draw a letter board and a symbol board, then spell "hi" by row–column scanning on the board, counting the steps aloud.
- **Segment 2, say:** type a sentence with 1, 3 and 5 suggestions on screen, then show where the keystroke savings flatten.
- **Segment 3, say:** show the two grids and the bar chart, ending with predictive Huffman scanning at 0.99 bits per step.
- **Close with:** "Every step an AAC user saves is time in a conversation: design with them, not for them." Then set assignment 10.

### Segment 1 (6 min): who uses AAC, and why speed matters

- **Augmentative and alternative communication** (AAC) adds to speech (augmentative) or replaces it (alternative): gestures, symbol boards, letter boards and **speech-generating devices** that speak a selected message.
- AAC users include people with cerebral palsy, motor neurone disease (also called ALS), autism or aphasia after a stroke (Beukelman & Light 2020). Their needs differ: some spell, some use symbols; some point with a finger, some can press only one switch.
- Every selection costs time and effort. In the lab's model, alphabetical row–column scanning at one step per second gives 2.1 words per minute, so a ten-word reply takes almost five minutes. Speed decides how much a person can say while a conversation is still going on.
- Prediction must serve the user's own words. A suggestion is an offer, never a replacement for what the person means.
- **Pause and try:** in a row–column grid with a–f in row 1 and g–l in row 2, a cell in row i and column j costs i + j scan steps. How many steps does "hi" take?
  - **Answer:** h is in row 2, column 2 (4 steps) and i in row 2, column 3 (5 steps): 9 steps, 9 seconds at one step per second.

### Segment 2 (7 min): prediction and information

- **Word prediction** shows the k most likely words that start with the letters typed so far; one selection completes the word and adds the space. A unigram model ranks words by frequency; a bigram model uses the previous word; neural language models do better with enough text (Course 5 builds a small Bangla one).
- **Keystroke savings** (KS) = 1 − keystrokes with prediction / keystrokes without. In the lab, the bigram model saved 0.289, 0.386 and 0.421 of the keystrokes with 1, 3 and 5 suggestions.
- Information theory sets the limit (Course 2 session 11). One choice among 27 equally likely symbols carries $\log_2 27 = 4.75$ bits, but text is predictable: Shannon (1951) estimated about one bit per letter of English. The lab's character models needed 4.00 bits per character with no context and 2.63 with three letters of context.
- **Dasher** (Ward, Blackwell & MacKay 2000) turns a language model into an input method: each possible next letter gets screen space in proportion to its probability, and the user steers into the right one with a mouse, a head pointer or eye gaze.
- Personal words matter: 21% of the lab's test words never appeared in its training text. For Bangla, prediction also needs a tokenizer that handles conjuncts (Course 5 sessions 2 and 4).
- **Pause and try:** with 3 suggestions, KS = 0.386. How many keystrokes does a 100-character message (spaces included) need?
  - **Answer:** 100 × (1 − 0.386) ≈ 61.

### Segment 3 (7 min): access methods, scanning and personal data

- Direct selection uses a finger, a head pointer or **eye gaze**, where looking at a key for a set **dwell time** selects it. Eye gaze must tell looking from choosing (the "Midas touch" problem; Jacob 1991).
- **Switch scanning** lights up rows, then cells; the user presses a switch at the right moment. Putting frequent symbols in cheap cells cut the lab's cost from 6.07 to 4.16 steps per character.
- Each scan step has two outcomes, press or wait, so it carries at most 1 bit. A Huffman code (Huffman 1952) on letter frequencies needed 4.04 steps, near the 4.00-bit limit; with a fresh code from the character model before every letter, 2.67 steps, or 0.99 bits per step.
- **Brain–computer interfaces** go further: the P300 speller flashes rows and columns of a letter grid and detects the brain's response to the wanted letter (Farwell & Donchin 1988), row–column scanning without a muscle.
- A predictor that learns a user's phrases holds intimate data about health and family: keep it on the device, and let the user see and delete it. **Voice banking** records a person's voice while their speech is clear, so that a synthetic voice can sound like them later.
- **Pause and try:** with 5 suggestions KS = 0.421. If reading each suggestion costs 0.1 of a keystroke, how long does typing take compared with no prediction?
  - **Answer:** 0.579 × (1 + 0.1 × 5) = 0.868. With 10 suggestions, 0.537 × 2 ≈ 1.075: slower than no prediction.

### Lab guide (about 2 hours, notebook `s10_aac.ipynb`)

1. Section 1 (10 min): the text and the train/test split.
2. Section 2 (25 min): the two word predictors and the keystroke simulation.
3. Section 3 (20 min): the time model; try other values of r.
4. Section 4 (25 min): character n-grams and bits per character.
5. Sections 5–6 (30 min): the grids, Huffman and predictive scanning.
6. TODO cells (10 min).

- **Expect:** 2,259 words; 93 of the 452 test words unseen in training. Keystroke savings with 1, 3 and 5 suggestions: bigram 0.289, 0.386 and 0.421; unigram 0.245, 0.350 and 0.386. Time model: best k = 10 at r = 0 (0.537); k = 2 at r = 0.1 (0.778; 10 suggestions 1.075); k = 1 at r = 0.25 (0.889; 5 suggestions 1.303). Bits per character: 4.75 uniform, 4.00 (order 1) down to 2.63 (order 4), then 2.66 (order 5). Steps per character: alphabetical 6.07, frequency-ordered 4.16, Huffman 4.04, predictive one at a time 3.39, predictive Huffman 2.67 (0.99 bits per step, 4.7 words per minute at one step per second). Runtime about 4 seconds.
- **Common problems:** measuring savings on the training text; forgetting that selecting a suggestion also enters the space; building the frequency layout from the test text.

### Quiz

1. What does keystroke savings measure, and what does it ignore?
   - **Answer:** the share of keystrokes saved; it ignores the time and effort of reading the suggestions and of correcting wrong selections.
2. Why can one switch-scanning step carry at most 1 bit?
   - **Answer:** it has two outcomes, press or wait, and a choice between two outcomes carries at most $\log_2 2 = 1$ bit.
3. How does a frequency-ordered grid speed up row–column scanning?
   - **Answer:** it puts common symbols in cells reached in few steps; in the lab, 4.16 instead of 6.07 steps per character.

**Watch out:** "More suggestions always help." Keystroke savings keep rising slowly (0.421 with 5 suggestions, 0.463 with 10), but the user must read the list before every keystroke. In the lab's model, if reading one suggestion costs a tenth of a keystroke, 10 suggestions were slower than no prediction (1.075 of the time) and 2 were best. The right number depends on the person, the access method and their reading speed: measure it with them.

### Assignment 10 (due before session 11, 10 points)

1. By hand: the scan steps for "we" in both grids (read the positions from the figure); the time with 3 suggestions at r = 0.25 (KS 0.386); and the bits in one choice among 27 symbols. (3 points)
2. Complete the first TODO cell: add 20 personal sentences to the training text and report the keystroke savings with 1, 3 and 5 suggestions on the original test text and on new personal sentences. Discuss the privacy of storing such phrases. (4 points)
3. Complete the second TODO cell: add press time and missed presses to the scanning model and compare the two layouts. Does the frequency layout's advantage grow or shrink? (3 points)

Hand in one PDF and your notebook.

### Sources

- Beukelman & Light 2020, Augmentative and Alternative Communication: Supporting Children and Adults with Complex Communication Needs, 5th edition (Paul H. Brookes).
- Ward, Blackwell & MacKay 2000, Dasher: a data entry interface using continuous gestures and language models (ACM Symposium on User Interface Software and Technology, UIST).
- Shannon 1951, Prediction and Entropy of Printed English, Bell System Technical Journal 30(1).
- Huffman 1952, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE 40(9).
- Jacob 1991, The use of eye movements in human-computer interaction techniques: what you look at is what you get, ACM Transactions on Information Systems 9(2).
- Farwell & Donchin 1988, Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials, Electroencephalography and Clinical Neurophysiology 70(6).
- Dasher, a zooming predictive text entry system (repository). https://github.com/dasher-project/dasher

## Session 11: Evaluation, fairness and participatory design

**Goal:** students can design an evaluation with disabled users, report performance per group with uncertainty, and handle consent and privacy.

### Talking pointers

- **Open with:** "Our sign recognizer is 90.7% accurate. For whom? Today we find who that number leaves out, and how to evaluate with disabled people instead of on them."
- **Segment 1, say:** draw a line from "tested on" through "consulted" to "designing with", and ask where most student projects sit.
- **Segment 2, say:** show the per-group error bars, with the dim-light interval missing its true value, then the power curve.
- **Segment 3, say:** list on the board what one sign video reveals besides the signs: a face, a home, family members, perhaps a school uniform.
- **Close with:** "Report every group with its uncertainty, design with the people you build for, and protect their data as you would your own." Then set assignment 11.

### Segment 1 (6 min): designing with disabled people

- **Participatory design** (co-design) brings disabled people into every stage: choosing the problem, designing, testing and judging success. It puts "nothing about us without us" (session 1) into practice, and the people involved are experts in their own lives.
- Tools can look helpful to designers and still be unwanted. Morris (2020) discusses such risks in AI for accessibility, including systems that fail people whose speech, movement or appearance differs from the training data, and the privacy risk of systems that can infer disability. Bennett & Keyes (2019) argue that making a system statistically fair across groups does not settle whether it should exist or whom it serves.
- Treat participants as partners: pay them for their time and expertise, cover interpreters and travel, credit their contributions, and share results with them in an accessible form.
- Make consent accessible: in Bangla, in easy-to-read language, in sign language through an interpreter, and usable with a screen reader. Explain what is recorded, who will see it, how long it is kept and how to withdraw.
- **Pause and try:** a team tests its caption app with 20 hearing students and 2 deaf students. What share of the testers are the app's main users?
  - **Answer:** 2/22 ≈ 9%. Most of the feedback comes from people who do not need captions.

### Segment 2 (7 min): metrics, experience and groups

- Metrics are not experience. Word error rate treats all errors alike; the NER model weights caption errors by their effect on understanding (session 3). Measure what users need: comprehension, task success and time.
- The **System Usability Scale** (SUS; Brooke 1996) has ten statements answered from 1 to 5. Odd items are positive, even items negative: SUS = 2.5 × [Σ odd (answer − 1) + Σ even (5 − answer)], from 0 to 100, and it is not a percentage. In the lab, version B scored 63.1 against 51.9 for A (paired difference 11.2, interval 6.9 to 15.8), yet one person preferred A.
- Report results for each group: dialect, age, signing hand, skin tone, lighting, device. Gaps are real: five commercial speech recognizers made on average 0.35 word errors per word for Black speakers and 0.19 for white speakers of American English (Koenecke et al. 2020).
- Put a bootstrap interval on every group's accuracy (Course 2 session 7). Small groups give wide intervals: 0.031 wide for 1,000 test signs, 0.200 for 40. Comparing groups needs many examples: detecting 90% against 85% with 80% power takes about 683 per group.
- **Pause and try:** each 95% interval misses the true value 5% of the time. With five groups, what is the chance that at least one interval misses?
  - **Answer:** $1 - 0.95^5 \approx 0.23$. In the lab it happened: the dim-light group (true accuracy 0.74) measured 0.875, with an interval of 0.775 to 0.975.

### Segment 3 (7 min): privacy, consent and data

- Sign and lip videos show faces, which identify people, and often homes, family members and places. They can reveal that someone is disabled. Once published, a video cannot be withdrawn.
- Children need a parent's consent and their own agreement (assent) in a form they understand. People in institutions, such as residential schools, may feel unable to refuse: make clear that saying no has no cost.
- Licences shape what others can do: many lip and sign resources allow only non-commercial research, such as LRW and the lip-reading repository used in session 7. Document datasets with a datasheet (Gebru et al. 2021) and models with a model card that includes per-group results (Mitchell et al. 2019).
- Surveillance risk: a model that captions a Deaf student's lecture could read lips on CCTV (session 7). Limit the purpose in the consent form, keep only what you need, delete on request, and process on the device where possible (session 12). Course 8 covers privacy-preserving ML; its session 11 shows that privacy methods can widen group gaps.
- **Pause and try:** 60 children's videos were collected with their parents' consent, but 6 children said they did not want to be filmed. How many videos may you use?
  - **Answer:** 54. A child's own "no" counts even when a parent said yes.

### Lab guide (about 2 hours, notebook `s11_evaluation_fairness.ipynb`)

1. Section 1 (15 min): the synthetic test set and its groups.
2. Section 2 (25 min): bootstrap intervals per group; compare them with the true values.
3. Section 3 (25 min): power by simulation and by formula.
4. Section 4 (20 min): SUS by hand, then the paired comparison.
5. Section 5 (15 min): the per-group report.
6. TODO cells (20 min): planning a test set; intersections of groups.

- **Expect:** 1,370 test signs, overall accuracy 0.907 (interval 0.891 to 0.923). Measured accuracies: right-handed adults 0.930 (n = 1,000), left-handed adults 0.842, older adults 0.853, children 0.817, dim light 0.875 (true 0.74, outside its interval 0.775 to 0.975). Interval widths from 0.031 (n = 1,000) to 0.200 (n = 60 and 40). Power for a 90% against 85% gap: 0.119 with 50 per group, 0.575 with 400, 0.804 with 700, 0.920 with 1,000; formula 683. SUS: A 51.9, B 63.1, paired difference 11.2 (6.9 to 15.8). Runtime about 3 seconds.
- **Common problems:** reporting only the overall accuracy; bootstrapping the whole test set when the question is about one group; comparing two versions rated by the same people with an unpaired test.

### Quiz

1. Compute the SUS for the answers 4, 2, 4, 2, 4, 2, 4, 2, 4, 2.
   - **Answer:** odd items give 5 × 3 = 15, even items 5 × 3 = 15, so SUS = 2.5 × 30 = 75.
2. Why can a small group's measured accuracy rank it wrongly?
   - **Answer:** its interval is wide, so chance can move the estimate far: the dim-light group measured 0.875 although its true accuracy was 0.74.
3. What should a per-group error report contain?
   - **Answer:** for each group chosen with users: the number of test examples, the accuracy with an interval, the gap to the best-served group, and a warning when the interval is too wide to conclude anything.

**Watch out:** "If average accuracy is high, the system works for everyone." The average weights each group by its share of the test set, so the majority dominates. In the lab, the overall 0.907 hid lower accuracies for every other group, and the truly worst group looked fine on 40 examples. Report every group with an interval, collect enough examples per group, and ask users whether the system works for them.

### Assignment 11 (due before session 12, 10 points)

1. By hand: the SUS for answers 5, 2, 4, 1, 5, 2, 4, 2, 5, 1; the chance that at least one of ten 95% intervals misses; and the formula's sample size per group to detect 80% against 70%. Check each in code. (3 points)
2. Complete the first TODO cell: compare three ways to split 1,000 new test signs across the groups, and choose the plan with the narrowest interval for the worst group. (4 points)
3. Complete the second TODO cell on intersections, and write a one-page, easy-to-read consent form for a sign-video study, saying what is recorded, why, for how long, and how to withdraw. (3 points)

Hand in one PDF and your notebook.

### Sources

- Morris 2020, AI and Accessibility: A Discussion of Ethical Considerations, Communications of the ACM 63(6). https://arxiv.org/abs/1908.08939
- Bennett & Keyes 2019, What is the Point of Fairness? Disability, AI and the Complexity of Justice. https://arxiv.org/abs/1908.01024
- Brooke 1996, SUS: A "quick and dirty" usability scale, in Usability Evaluation in Industry (Taylor & Francis).
- Koenecke et al. 2020, Racial disparities in automated speech recognition, Proceedings of the National Academy of Sciences 117(14).
- Mitchell et al. 2019, Model Cards for Model Reporting. https://arxiv.org/abs/1810.03993
- Gebru et al. 2021, Datasheets for Datasets, Communications of the ACM 64(12). https://arxiv.org/abs/1803.09010
- Efron & Tibshirani 1993, An Introduction to the Bootstrap (Chapman & Hall).

## Session 12: Deploying accessible AI in Bangladesh, and the capstone

**Goal:** students can plan an assistive tool that works offline on a low-cost phone, shrink a model to fit, and scope a capstone with a community partner.

### Talking pointers

- **Open with:** "A model that works on your laptop has not helped anyone yet. Today we take one off the laptop: onto a cheap phone, into a community, and into your capstone."
- **Segment 1, say:** hold up an old phone and list what it lacks compared with a laptop (memory, speed, battery, a steady connection) and what it has (a camera and a microphone that are always with the user).
- **Segment 2, say:** draw a map of who must be involved: users, their organizations, interpreters or teachers, and whoever maintains the app after the course.
- **Segment 3, say:** walk through the capstone rubric on the course front page, then show the "ask once, then offer three choices" result.
- **Close with:** "Build with your partners, measure on their phones, and report what does not work." Then set assignment 12, which is due with the capstone.

### Segment 1 (6 min): designing for the phone people have

- Plan for low-cost Android phones with little memory and storage, slower processors and a battery that must last the day, and for patchy internet and mobile data that costs money. Treat these as assumptions to check with your partners, on their phones.
- Running the model **on the device** keeps a person's video and voice on their phone (session 11), works without a network and costs no data. Course 11 (On-Device AI) teaches the toolkit, from quantization (sessions 3 and 4) and runtimes (session 7) to honest benchmarking (session 11).
- **Dynamic int8 quantization** stores the weights of linear and recurrent layers as 8-bit integers with a scale and quantizes activations while the model runs, with no retraining (Course 5 session 10). Jacob et al. (2018) describe integer-only inference, and Krishnamoorthi (2018) and Nagel et al. (2021) survey the methods. In the lab it cut the sign model from 138,309 to 40,383 bytes, and accuracy on new signers went only from 0.943 to 0.941; but it was not meaningfully faster on this CPU.
- Language and people vary: regional varieties of Bangla such as Chittagonian and Sylheti and Bangla–English code-switching (session 2), and signers of different ages, hands and regions (sessions 4 and 5).
- Plan maintenance: phones, words and users change. Decide who fixes the app after the course ends.
- **Pause and try:** the lab's model has 33,708 parameters. How many bytes do its weights need at 4 bytes and at 1 byte each, and why is the saved int8 file (40,383 bytes) larger than that?
  - **Answer:** 134,832 and 33,708 bytes. The int8 file also keeps biases in float, a scale for each quantized weight tensor, and file metadata.

### Segment 2 (7 min): partners and sustainability

- Work with organizations of disabled people (Deaf associations, blind people's organizations), special schools, sign language interpreters, NGOs and government programs. Find the ones active in your area and confirm their current programs and contacts before you start; session 1 covers Bangladesh's 2013 disability act and the national survey.
- Partners own the problem. They help define it, collect data, judge success, share credit and are paid for their time (session 11).
- Share data and models only with consent and a clear licence, and check the licences of what you reuse: Bangla speech corpora (session 2); LRW and the lip-reading repository used in session 7 allow non-commercial use only. Document data with a datasheet and models with a model card (session 11).
- An offline app needs no server to pay for, but it still needs updates, testing on new phones and someone responsible: agree a handover with your partner.
- **Pause and try:** an app updates its model once a month. How much mobile data does one user spend in a year for a 40 KB model, and for a 400 MB speech model?
  - **Answer:** 12 × 40 KB = 480 KB, against 12 × 400 MB = 4.8 GB. Small models make updates affordable.

### Segment 3 (7 min): the capstone

- Choose a problem with a partner, such as a recognizer for a small sign or lip-reading vocabulary, a caption segmenter, a photo-quality guide for blind users or a Bangla word predictor (course front page).
- Collect a small consented dataset and write its datasheet; build a baseline from one of this course's notebooks; evaluate it per group with bootstrap intervals (session 11); test it with users, measuring task success and usability; report honestly, failures included.
- Design the interaction as well as the model. In the lab, asking the same signer to repeat an uncertain sign changed nothing (0.896 right before and after), because the errors came from the signer's personal way of signing. Offering the three most likely signs after an unsure repeat raised the final accuracy from 0.943 to 0.958. This is selective prediction (session 8) turned into a dialogue.
- Assessment follows the front page: a problem defined with users (20 points), a working baseline and model with honest metrics (25), evaluation per group with uncertainty (20), a user test or expert review and what it changed (20), and a clear report and video, including limitations and consent (15).
- **Pause and try:** your capstone recognizer is right on 45 of 50 test signs from your partners. What is the 95% interval for its accuracy?
  - **Answer:** 0.90 ± 1.96 × √(0.9 × 0.1/50) = 0.90 ± 0.083, about 0.82 to 0.98. Report the interval, not only 90%.

### Lab guide (about 2 hours, notebook `s12_deployment.ipynb`)

1. Section 1 (20 min): the synthetic signs and the signer split.
2. Section 2 (15 min): train the GRU.
3. Section 3 (30 min): quantize; size, latency and agreement; rerun the timing and watch it vary.
4. Section 4 (30 min): the threshold, three policies, per-signer results.
5. Section 5 and TODO cells (25 min).

- **Expect:** 576 training, 384 validation and 576 test sequences; 33,708 parameters; accuracy 0.883 on validation signers and 0.943 on new test signers (0.833 to 1.000 per signer). Float32 138,309 bytes, int8 40,383 bytes (3.42 times smaller); median single-thread latency 0.864 and 0.845 ms (1.02 times; it varies between runs); int8 accuracy 0.941, agreement 0.998. Threshold 0.995: first attempt answered 0.684 at accuracy 0.964; unsure signs right 0.896 of the time both at first and on the repeat. Final accuracy 0.943 when always answering, 0.943 when asking once (1.32 attempts per sign) and 0.958 when asking once and then offering three choices (a choice list on 0.276 of signs). Runtime about 12 seconds.
- **Common problems:** timing one run, or skipping the warm-up; expecting a laptop's multi-thread latency on a phone; choosing the threshold on the test signers.

### Quiz

1. What does dynamic quantization change, and what does it not need?
   - **Answer:** it stores the weights of linear and recurrent layers as 8-bit integers with a scale and quantizes activations while the model runs; it needs no retraining and no calibration data.
2. Why did asking the same signer to repeat a sign not help in the lab?
   - **Answer:** the errors came from that signer's personal way of making the sign, a systematic error that a repeat reproduces, not from random noise.
3. Name three things to agree with a community partner before collecting data.
   - **Answer:** any three of: the problem and how success will be judged; consent and who may use the data, under which licence; payment and credit; who maintains the tool afterwards.

**Watch out:** "If it works on my laptop, it will work on a user's phone." A laptop has more memory, faster cores and steady power, and the user's phone, lighting, signing and network all differ from yours. In the lab, quantization kept the accuracy but did not speed up this small model, and a threshold tuned on four validation signers missed its 98% target on new ones. Test on users' own phones, in their places, with them.

### Assignment 12 (due with the capstone, 10 points)

1. By hand: the float32 and int8 weight sizes of a 1-million-parameter model; a year of monthly updates for 1,000 users with a 40 KB and a 40 MB model; and the 95% interval for 0.90 accuracy on 50 test signs. (3 points)
2. Complete the first TODO cell: find the smallest model within 2 points of the best accuracy, with its int8 size and latency. (4 points)
3. Complete the second TODO cell, then write a one-page capstone plan agreed with your partner: the problem, the users, data and consent, the baseline, evaluation per group, the user test and who maintains the tool. (3 points)

Hand in one PDF and your notebook.

### Sources

- Nagel et al. 2021, A White Paper on Neural Network Quantization. https://arxiv.org/abs/2106.08295
- Jacob et al. 2018, Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. https://arxiv.org/abs/1712.05877
- Krishnamoorthi 2018, Quantizing Deep Convolutional Networks for Efficient Inference: A Whitepaper. https://arxiv.org/abs/1806.08342
- ONNX Runtime documentation. https://onnxruntime.ai/docs/

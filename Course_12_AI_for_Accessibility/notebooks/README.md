# Course 12 notebooks: AI for Accessibility

One notebook per session. Read them with their saved outputs on the course website or on GitHub, or open them in Google Colab or Kaggle Notebooks and run them from the top.

- Every cell without a NOT RUN label was run once, top to bottom, on a CPU in November 2026 (Python 3.13, NumPy 2.5, SciPy 1.18, pandas 3.0, scikit-learn 1.9 and matplotlib 3.11, plus PyTorch 2.15 in sessions 2, 5–9 and 12), and the outputs are saved in the notebooks. A second, independent run reproduced every printed number; only timings differ.
- The labs use synthetic data generated in the notebooks, so they run anywhere without downloads or recordings of real people: tone-based "speech", word timestamps, 21-point hand skeletons and sign sequences, lip-landmark sequences, degraded photos made from scikit-learn's sample images, digits from scikit-learn standing in for handwritten Bangla digits, and a short English text for word prediction. The numbers show how the methods behave; they are not results on real disabled users, and the course says so wherever it matters.
- Cells marked TODO are exercises for students. Cells marked NOT RUN need a download, a GPU or a library that is not installed here (Whisper, WhisperX, MediaPipe, an Auto-AVSR checkpoint, BLIP, Tesseract with Bengali data, NumtaDB, ONNX Runtime); they were written from the tools' documented interfaces and have not been executed, so run each one before recording (the table below says what each needs).
- Nothing extra needs installing for the runnable cells on Google Colab or Kaggle.
- Results that went against expectation are stated in each notebook's "What to notice" cell and in the course document. Examples: the colour palette designed for colour-blind readers has three colours below WCAG's 3:1 contrast on white (session 1); the dynamic-programming caption segmenter left more blocks over the reading-speed limit than the greedy one, although its line breaks were far better (session 3); the small skeleton graph network did worse than a GRU on new signers, and time-warp augmentation did not help (session 5); jointly trained audio-visual fusion fell below video alone in heavy noise, while late fusion was best or tied (session 7); a confidence margin still answered most damaged inputs (session 8); a group's accuracy measured on 40 examples missed its true value (session 11); int8 quantization shrank the sign model 3.4 times but barely changed its speed (session 12).

## Notebooks

| # | Notebook | Session | Code cells | NOT RUN cells need |
|---|---|---|---|---|
| 1 | [s01_accessibility_basics.ipynb](s01_accessibility_basics.ipynb) | Disability, accessibility and AI | 10 | the colour-science package (pip install colour-science), which is not installed here |
| 2 | [s02_speech_recognition.ipynb](s02_speech_recognition.ipynb) | Speech recognition for Bangla | 10 | the openai-whisper package (pip install openai-whisper), ffmpeg, a model download and a Common Voice clip |
| 3 | [s03_captions.ipynb](s03_captions.ipynb) | Captions for deaf and hard-of-hearing viewers | 8 | whisperx (pip install whisperx), ffmpeg, a GPU for reasonable speed, model downloads and a video file |
| 4 | [s04_hand_pose.ipynb](s04_hand_pose.ipynb) | Sign languages and hand pose | 9 | mediapipe (pip install mediapipe), the hand_landmarker.task model file and a folder of hand photos |
| 5 | [s05_isolated_signs.ipynb](s05_isolated_signs.ipynb) | Recognizing isolated signs | 8 | mediapipe and opencv-python (pip install mediapipe opencv-python), the hand_landmarker.task model file, |
| 6 | [s06_continuous_signing.ipynb](s06_continuous_signing.ipynb) | Continuous signing and sign language translation | 8 | the sacrebleu package (pip install sacrebleu), which is not installed here |
| 7 | [s07_lip_reading.ipynb](s07_lip_reading.ipynb) | Lip reading | 8 | the Auto-AVSR code, torchvision, torchaudio, ffmpeg, MediaPipe and an 891 MB model download (GPU recommended) |
| 8 | [s08_image_description.ipynb](s08_image_description.ipynb) | Describing images for blind and low-vision users | 9 | transformers, Pillow and a download of the BLIP models (about 1 GB each), ideally a GPU; the Tesseract program with Bengali data (apt-get install tesseract-ocr tesseract-ocr-ben) and pytesseract |
| 9 | [s09_reading_support.ipynb](s09_reading_support.ipynb) | Reading support: OCR, text-to-speech and simplification | 10 | the Tesseract program with Bengali data (apt-get install tesseract-ocr tesseract-ocr-ben), pytesseract and Pillow; the NumtaDB dataset of handwritten Bangla digits from Kaggle (Bengali.AI) and Pillow |
| 10 | [s10_aac.ipynb](s10_aac.ipynb) | Augmentative and alternative communication | 8 | nothing (all cells run) |
| 11 | [s11_evaluation_fairness.ipynb](s11_evaluation_fairness.ipynb) | Evaluation, fairness and participatory design | 7 | nothing (all cells run) |
| 12 | [s12_deployment.ipynb](s12_deployment.ipynb) | Deploying accessible AI in Bangladesh, and the capstone | 7 | onnx, onnxscript and onnxruntime (pip install onnx onnxscript onnxruntime); see Course 11 session 7 |

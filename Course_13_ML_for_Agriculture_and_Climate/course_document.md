# Course 13: Machine Learning for Agriculture and Climate

<p class="byline">November 2026 · Mohammad Motiur Rahman</p>

A 12-session course on machine learning for food and climate, with Bangladesh as the running example: plant disease detection, remote sensing of crops, crop mapping and yield prediction, weather and climate data, machine-learning weather prediction, floods, downscaling, extremes and decisions, farm sensors, and responsible deployment. Each session has talking pointers, three video segments ending in a pause-and-try question, a lab guide with a tested notebook, a three-question quiz, one common misconception and a graded assignment.

## Syllabus

Bangladesh feeds a large population from a low-lying delta exposed to floods, cyclones, salinity and heat. Satellites, weather models, sensors and phones produce data that can help, and machine learning can turn them into maps, forecasts and advice. But the field is full of traps: models that look accurate under random cross-validation fail in a new district or a new year, laboratory photos do not look like fields, and the extremes that matter most are rare. This course teaches the methods together with the validation that keeps them honest. The labs use synthetic data built to behave like the real thing, and the notebooks show how to load the real data.

Prerequisites: Python, pandas and basic machine learning (Course 1). Course 6's lessons on validation and Course 2's on probability and estimation help. A few labs use small neural networks at the level of Course 1.

Capstone: with a partner such as a district agriculture office, a research institute or an NGO where possible, pick one problem (a crop map, a yield or flood forecast, a disease detector, a downscaled climate indicator or an advisory service), use open data, validate across space and time, quantify uncertainty, and present the result and its limits in a 10-minute video. A suggested weighting is assignments 40%, capstone 40% and quizzes 20%. A suggested capstone rubric, out of 100: a problem that matters to a named user, and the decision it informs (15); data handled correctly, with sources (15); a model with a sensible baseline (20); validation that respects space and time, with uncertainty (30); clarity of the report and video, including limitations and who could be harmed (20).

Language: the channel is Bangla-first. Speak Bangla on camera and keep technical terms and code in English. Where you can, show the maps and forecasts for places your students know.

### Sessions

1. **Machine learning for agriculture and climate.** Students can map agriculture and climate problems to machine learning tasks and data sources, and show how random cross-validation misleads when data have places and years.
   - Read: Rolnick et al. 2022, Tackling Climate Change with Machine Learning, ACM Computing Surveys 55(2); Roberts et al. 2017, Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure, Ecography 40(8)
   - Lab: about 2 hours, notebook `s01_problems_and_data.ipynb`
2. **Plant disease detection from leaf images.** Students can train a leaf-disease classifier, show how it learns shortcuts from lab photos, and make it more robust and willing to abstain.
   - Read: Mohanty, Hughes & Salathé 2016, Using Deep Learning for Image-Based Plant Disease Detection, Frontiers in Plant Science 7:1419; Geirhos et al. 2020, Shortcut learning in deep neural networks, Nature Machine Intelligence 2:665–673
   - Lab: about 2 hours, notebook `s02_plant_disease.ipynb`
3. **Seeing crops from space.** Students can compute vegetation and water indices, mask clouds, build composites, and smooth a vegetation time series to read crop phenology.
   - Read: Drusch et al. 2012, Sentinel-2: ESA's Optical High-Resolution Mission for GMES Operational Services, Remote Sensing of Environment 120:25–36; Tucker 1979, Red and photographic infrared linear combinations for monitoring vegetation, Remote Sensing of Environment 8(2):127–150
   - Lab: about 2 hours, notebook `s03_remote_sensing.ipynb`
4. **Crop type mapping.** Students can classify crop types from satellite time series with a random forest and a 1-D CNN, and validate maps with spatial cross-validation.
   - Read: Pelletier, Webb & Petitjean 2019, Temporal Convolutional Neural Network for the Classification of Satellite Image Time Series, Remote Sensing 11(5):523; Roberts et al. 2017, Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure, Ecography 40(8):913–929
   - Lab: about 2 hours, notebook `s04_crop_mapping.ipynb`
5. **Predicting crop yield.** Students can build yield models from weather and satellite features, validate them on unseen years, and give prediction intervals.
   - Read: Lobell, Schlenker & Costa-Roberts 2011, Climate Trends and Global Crop Production Since 1980, Science 333(6042):616–620; You, Li, Low, Lobell & Ermon 2017, Deep Gaussian Process for Crop Yield Prediction Based on Remote Sensing Data (AAAI 2017)
   - Lab: about 2 hours, notebook `s05_yield_prediction.ipynb`
6. **Weather data, baselines and forecast skill.** Students can build persistence and climatology baselines, score forecasts with skill scores, and evaluate probabilistic forecasts with CRPS and the Brier score.
   - Read: Gneiting & Raftery 2007, Strictly Proper Scoring Rules, Prediction, and Estimation, Journal of the American Statistical Association 102(477):359–378; Hersbach et al. 2020, The ERA5 global reanalysis, Quarterly Journal of the Royal Meteorological Society 146(730):1999–2049
   - Lab: about 2 hours, notebook `s06_forecast_skill.ipynb`
7. **Machine learning weather prediction.** Students can explain how data-driven weather models work and are evaluated, and train and roll out a learned model of a chaotic toy atmosphere.
   - Read: Lam et al. 2023, Learning skillful medium-range global weather forecasting (GraphCast), Science 382; Rasp et al. 2024, WeatherBench 2: A benchmark for the next generation of data-driven global weather models, Journal of Advances in Modeling Earth Systems 16
   - Lab: about 2 hours, notebook `s07_ml_weather.ipynb`
8. **Floods: mapping and forecasting.** Students can map flood water from radar images, score maps with IoU, and compare an LSTM with a conceptual model for river flow.
   - Read: Kratzert et al. 2018, Rainfall–runoff modelling using Long Short-Term Memory (LSTM) networks, Hydrology and Earth System Sciences 22; Bonafilia et al. 2020, Sen1Floods11: a georeferenced dataset to train and test deep learning flood algorithms for Sentinel-1, CVPR Workshops
   - Lab: about 2 hours, notebook `s08_floods.ipynb`
9. **Downscaling and bias correction.** Students can bias-correct climate model output with quantile mapping, downscale coarse fields with a CNN, and evaluate the extremes, not just averages.
   - Read: Cannon, Sobie & Murdock 2015, Bias Correction of GCM Precipitation by Quantile Mapping: How Well Do Methods Preserve Changes in Quantiles and Extremes?, Journal of Climate 28; Vandal et al. 2017, DeepSD: Generating High Resolution Climate Change Projections through Single Image Super-Resolution
   - Lab: about 2 hours, notebook `s09_downscaling.ipynb`
10. **Extremes, uncertainty and decisions.** Students can fit an extreme-value distribution, compute return levels with uncertainty, and decide when to act on a probabilistic forecast.
   - Read: Coles 2001, An Introduction to Statistical Modeling of Extreme Values (Springer); Richardson 2000, Skill and relative economic value of the ECMWF ensemble prediction system, Quarterly Journal of the Royal Meteorological Society 126
   - Lab: about 2 hours, notebook `s10_extremes_decisions.ipynb`
11. **Sensors, soil and water on the farm.** Students can clean noisy farm sensor data with filtering and anomaly detection, and turn it into an irrigation decision.
   - Read: Kalman 1960, A New Approach to Linear Filtering and Prediction Problems, Journal of Basic Engineering 82(1); Allen, Pereira, Raes & Smith 1998, Crop evapotranspiration: guidelines for computing crop water requirements, FAO Irrigation and Drainage Paper 56
   - Lab: about 2 hours, notebook `s11_farm_sensors.ipynb`
12. **Responsible machine learning for farmers and the climate, and the capstone.** Students can turn a forecast into advice farmers can trust, estimate the carbon cost of their models, and plan a capstone with honest validation.
   - Read: Fabregas, Kremer & Schilbach 2019, Realizing the potential of digital development: The case of agricultural advice, Science 366; Strubell, Ganesh & McCallum 2019, Energy and Policy Considerations for Deep Learning in NLP
   - Lab: about 1.5 hours, notebook `s12_responsible_ml.ipynb`

## How to use this doc

Each session is a 20-minute video in three segments of 6–7 minutes. Under each session's goal come talking pointers for the camera, then the three segments with pause-and-try questions, a step-by-step lab guide, a quiz, one misconception to tackle head-on, and a graded assignment worth 10 points. Answers are included, so hide them before sharing with students.

- **Delivery:** the talking pointers are prompts, not a script. The general habits for recording are in the "Delivering the sessions on camera" section of Course 1: From Beginner to an AI Research Lab.
- **Notebooks:** each session has a notebook in the course's `notebooks` folder. Every cell not labelled NOT RUN was run once on a CPU in November 2026, and the saved outputs are the numbers quoted under **Expect**. The labs use synthetic data that mimic satellite images, weather series, radar images and sensor streams; the NOT RUN cells show how to load the real datasets.
- **Sources:** read the papers cited for a session before recording it.
- **Dates:** written in November 2026. Facts about Bangladesh and about machine-learning weather models were checked then; recheck them before each run of the course.

## Session 1: Machine learning for agriculture and climate

**Goal:** students can map agriculture and climate problems to machine learning tasks and data sources, and show how random cross-validation misleads when data have places and years.

### Talking pointers

- **Open with:** "Predicting last year's yield in a district the model has seen is easy. Farmers need next year's yield, in districts with no data. Today we learn to tell the two apart."
- **Segment 1, say:** show the three rice seasons and their shares, then one number for each hazard.
- **Segment 2, say:** go through the notebook's task table and ask of each row: who uses this prediction, and when?
- **Segment 3, say:** show the lab's bar chart: random 5-fold RMSE 0.209 t/ha against 0.418, 0.470 and 0.570 for honest splits.
- **Close with:** "Before you train anything, ask where and when the model will be used, and split your data the same way." Then set assignment 1.

### Segment 1 (6 min): why it matters for Bangladesh

- Agriculture is still the largest employer: about 45% of employed people worked in it in the Bangladesh Bureau of Statistics (BBS) Labour Force Survey 2022 (The Daily Star 2023).
- Rice grows in three seasons. Boro, the dry-season crop, is mainly irrigated and gives about 55% of output; Aman, the monsoon crop, about 35%; Aus about 10%. FAO's preliminary forecast for 2026/27 was 61.9 million tonnes of paddy (FAO GIEWS 2026).
- Hazards, with one verified example each:
  - **Floods:** the eastern flash floods of August 2024 affected more than 5 million people (UN OCHA 2024).
  - **Cyclones:** Cyclone Sidr killed 3,363 people in November 2007, by government count (ADRC 2007).
  - **Salinity:** a 2009 survey found about 1.06 million hectares of coastal land affected (FAO 2015).
  - **Heat:** April 2024 brought a heatwave of 30 days in a row, the longest since 1948, and 43.8 °C in Jashore (Down To Earth 2024; Prothom Alo 2024).
  - **Drought:** the High Barind Tract in the north-west is drought-prone (Riches 2008).
- These events are rare, local and changing: a model trained on ordinary years meets them when it matters most.
- **Pause and try:** Boro gives about 55% of rice output and Aus about 10%. A yield model is wrong by 5% for Boro and by 20% for Aus. Which error moves the national rice estimate more?
  - **Answer:** Boro: 0.05 × 55 = 2.75% of national output, against 0.20 × 10 = 2.0% for Aus. A small error on a big season can matter more than a big error on a small one.

### Segment 2 (7 min): tasks and data

- Four task types: **detect** (classify a leaf photo, session 2), **map** (label every pixel, such as crop types or flood water, sessions 4 and 8), **forecast** (yield, rainfall or river flow, sessions 5 to 8) and **decide** (when to irrigate or warn, sessions 10 and 11). Rolnick et al. (2022) survey where machine learning can help climate action, from farming to disaster response.
- Data: satellites such as Sentinel-2, Landsat and the Sentinel-1 radar (session 3); weather stations and reanalysis, a gridded reconstruction of past weather (session 6); official statistics such as the BBS Yearbook of Agricultural Statistics (FEWS NET); field sensors (session 11); and phones. The Krishi Call Centre (16123) took 92,094 calls from farmers from July 2025 to June 2026 (BSS 2026).
- Ground truth is scarce, late and noisy: a crop-type label needs a field visit, a district yield is an average with survey error, and disasters are rare. Label noise sets a floor on any model's error.
- For every problem, write down the inputs, where the labels come from, who uses the prediction, and when. The last two decide the validation split.
- **Pause and try:** name the task type of each: (a) estimating the area of Aman rice in a district from satellite images; (b) next week's rainfall in Rajshahi; (c) whether to send a flood warning by SMS tonight.
  - **Answer:** (a) map, (b) forecast, (c) decide: a decision is judged by costs and losses, not by error alone.

### Segment 3 (7 min): the course's warning: places and years leak

- Rows from one district share soil, irrigation and management; rows from one year share weather, pests and prices. Random K-fold cross-validation puts these "siblings" on both sides of the split, so it partly measures memory (Roberts et al. 2017; Course 6 sessions 3 and 4 treat validation and leakage in general).
- Choose the split from the use: for next year, leave one year out or train on past years only; for a new district, hold out whole regions (spatial blocks); for both, hold out a region and a block of years together (Course 1 session 4 introduces validation splits).
- In the lab, one boosted-tree model on the same 1,280 rows scores RMSE 0.209 t/ha under random 5-fold cross-validation, but 0.418 leaving one year out, 0.470 leaving a region out, and 0.570 for a new region in new years.
- The warning returns throughout the course: lab against field photos (session 2), new districts (sessions 4 and 5), new years and extremes (sessions 5 and 10).
- **Pause and try:** a district office wants yield estimates for a district with no past data. Random cross-validation says RMSE 0.21 t/ha and leave-region-out says 0.47 t/ha. Which do you report?
  - **Answer:** 0.47 t/ha. Leave-region-out copies the real use; random folds let the model see the same districts in training.

### Lab guide (about 2 hours, notebook `s01_problems_and_data.ipynb`)

1. Section 1 (10 min): add one row to the task table for a problem you know.
2. Section 2 (20 min): build the panel; list the effects the model can and cannot see.
3. Sections 3–4 (30 min): predict the order of the four scores before running.
4. Section 5 (15 min): find the worst regions on the error maps.
5. Section 6 (15 min): add fields from the same district-years.
6. TODO cells (30 min): drop coordinates and year; leave one district out.

- **Expect:** yield mean 3.97 t/ha (sd 0.69). RMSE ($R^2$): random 5-fold 0.209 (0.909), leave-one-year-out 0.418 (0.634), leave-region-out 0.470 (0.538), new region and new years 0.570 (0.321); mean baselines 0.694 to 0.766. Leave-one-year-out RMSE 0.274 in 2005, 0.360 in 2024, 0.372 in the median year. District mean absolute error 0.103 to 0.315 t/ha (random) and 0.133 to 1.103 (leave-region-out; worst regions R6 0.65, R7 0.44). One field per district-year: random 0.402, leave-region-out 0.601; four fields: 0.335 and 0.567 (noise floor 0.300). Runtime about 27 seconds.
- **Common problems:** passing `groups` to `KFold`, which silently ignores them; computing features such as district averages on all rows before splitting; reporting the random-CV score because it looks best.

### Quiz

1. Why does random K-fold give a lower error than leave-one-year-out on a district-by-year panel?
   - **Answer:** the test year's other districts are in training, so the model learns that year's shared shocks from them. In real use, that year is unseen.
2. Your model will estimate yields in districts that have no data. Which validation do you use?
   - **Answer:** leave-region-out (spatial blocks), or better, a region and a block of years held out together.
3. Give the four task types with one example each.
   - **Answer:** detect (a diseased leaf photo), map (crop types or flood water), forecast (yield or rainfall), decide (when to irrigate or warn).

**Watch out:** "More rows from the same places and years make a model more general." They make random cross-validation look better, not the model. In the lab, four fields per district-year instead of one lowered the random-CV RMSE from 0.402 to 0.335, near the noise floor of 0.300, while leave-region-out moved only from 0.601 to 0.567. Generality comes from new places and new years.

### Assignment 1 (due before session 2, 10 points)

1. For one agriculture or climate problem in Bangladesh, write its inputs, label source, user and moment of use, and the validation split that copies the use. Cite a source for every fact. (3 points)
2. Complete both TODO cells. Report RMSE for all schemes with and without `row`, `col` and `year`, and explain which scheme changed most and why. (4 points)
3. Set the hidden year shock to 0, 0.3 and 0.6 (the `0.30 * rng.normal()` term). Plot random-CV and leave-one-year-out RMSE against the shock size and explain the gap. (3 points)

Hand in one PDF and your notebook.

### Sources

- Rolnick et al. 2022, Tackling Climate Change with Machine Learning, ACM Computing Surveys 55(2). https://arxiv.org/abs/1906.05433
- Roberts et al. 2017, Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure, Ecography 40(8). https://doi.org/10.1111/ecog.02881
- FAO GIEWS 2026, Country Brief: Bangladesh (reference date 4 September 2026). https://www.fao.org/giews/countrybrief/country.jsp?code=BGD
- The Daily Star 2023, An overview of the Labour Force Survey 2022 (Bangladesh Bureau of Statistics). https://www.thedailystar.net/opinion/views/news/overview-the-labour-force-survey-2022-3346116
- UN OCHA 2024, Bangladesh: Eastern Flash Floods 2024, Situation Report No. 02 (30 August 2024). https://reliefweb.int/report/bangladesh/bangladesh-eastern-flash-floods-2024-situation-report-no-02-30-august-2024
- ADRC 2007, Bangladesh: Cyclone Sidr, disaster information (Government of Bangladesh figures). https://www.adrc.asia/view_disaster_en.php?KEY=1111
- FAO 2015, Bangladesh country report to the Global Soil Partnership (SRDI salinity survey of 2009). https://www.fao.org/fileadmin/user_upload/GSP/docs/asia_2015/Bangladesh.pdf
- Down To Earth 2024, Unusual heat scorches Bangladesh as April's consecutive heatwave breaks 76-year record. https://www.downtoearth.org.in/climate-change/unusual-heat-scorches-bangladesh-as-april-s-consecutive-heatwave-breaks-76-year-record-96034
- Prothom Alo 2024, Jashore records season's highest temperature at 43.8° Celsius. https://en.prothomalo.com/environment/41tx5th9wp
- Riches 2008, The High Barind Tract: a challenging drought-prone agricultural environment (IRRI). https://agris.fao.org/search/en/records/647248e4e17b74d2224f7676
- FEWS NET, Bangladesh data book (crop statistics and the BBS Yearbook of Agricultural Statistics). https://help.fews.net/fde/bangladesh-data-book
- BSS 2026, Farmers' trust in "Agriculture Call Centre" grows, calls top 92,000 annually. https://www.bssnews.net/special-stories/401845

## Session 2: Plant disease detection from leaf images

**Goal:** students can train a leaf-disease classifier, show how it learns shortcuts from lab photos, and make it more robust and willing to abstain.

### Talking pointers

- **Open with:** "A plant disease model scored over 99% on its own test set and 31% on photos taken elsewhere. Today we find out why, and what a farmer's app should do about it."
- **Segment 1, say:** show the notebook's lab photos above its field photos, then the two numbers from Mohanty et al. (2016): 99.35% and 31.4%.
- **Segment 2, say:** show the swap test, then the bar chart: field accuracy moves from 0.398 to 0.740.
- **Segment 3, say:** show the accuracy–coverage curve and read the Bangla "not sure" message aloud.
- **Close with:** "Test where the model will be used, change the training data to break the shortcut, and let the model say 'I am not sure'." Then set assignment 2.

### Segment 1 (6 min): the task and the datasets

- The task: classify a photo of one leaf as healthy or diseased (which disease), with an image classifier such as a convolutional neural network (CNN).
- PlantVillage released over 50,000 expert-curated photos of healthy and diseased leaves, taken one leaf at a time on plain backgrounds (Hughes & Salathé 2015).
- Mohanty et al. (2016) trained CNNs on 54,306 PlantVillage images of 14 crops and 26 diseases. They reached 99.35% accuracy on a held-out PlantVillage split, but 31.4% on images from other trusted online sources, taken in other conditions.
- Field datasets test the real use. PlantDoc has 2,598 internet photos of 13 plant species in 27 classes, and its authors report that training on it raised accuracy on real-world photos by up to 31% (Singh et al. 2020).
- Bangladesh has its own data. Rahman et al. (2020) took 1,426 photos of rice diseases and pests (9 classes) in the fields of the Bangladesh Rice Research Institute (BRRI); a small CNN reached 93.3%. Dhan-Shomadhan has 1,106 photos of five rice leaf diseases (brown spot, leaf scald, blast, tungro, sheath blight) from Dhaka Division, on field and white backgrounds (Hossain et al. 2023).
- **Pause and try:** Mohanty et al. compared their 31.4% with a random baseline of 2.6%. Where does 2.6% come from?
  - **Answer:** guessing one of 38 classes at random is right 1/38 ≈ 2.6% of the time. So 31.4% is far above chance, and still far from usable.

### Segment 2 (7 min): transfer learning, augmentation and shortcuts

- Transfer learning: start from a network pretrained on ImageNet, replace its last layer and fine-tune it on leaves; this needs far fewer labelled photos than training from scratch (Course 3 session 4 covers vision backbones and pre-training).
- Augmentation changes training images at random (crops, flips, brightness, colour, blur) to cover the variety the model will meet.
- Shortcut learning: a model finds an easier rule that works on the benchmark but not in the world (Geirhos et al. 2020). If each disease was photographed in its own session, background and brightness follow the class, and the model can read them instead of the lesions.
- Two tests: a **swap test** (the same leaves on another class's background) and a **field test**. In the lab, the baseline scored 0.978 on new lab photos, 0.848 on swapped backgrounds and 0.398 on field photos.
- Fixes that change the training images: background randomization (paste each leaf onto random soil, grass or colour) raised field accuracy to 0.537; adding colour jitter and blur raised it to 0.740, while lab accuracy fell to 0.900.
- A colour-based leaf mask, the excess green index (Woebbecke et al. 1995), did worse (0.480 in the field): it keeps green pixels only, so it cut away the yellow tissue that is the symptom of blight (overlap 0.485 with the true leaf).
- **Pause and try:** on swapped backgrounds the baseline drops from 0.978 to 0.848. Does it use the background? Is that the whole field problem?
  - **Answer:** yes, it uses the background: 13 points lost, and for 15% of leaves it predicted the background's class. But it is not the whole problem: field accuracy is 0.398, so light, blur and clutter matter too.

### Segment 3 (7 min): deployment for farmers

- A farmer's phone needs a small model that runs offline: Course 11 covers efficient architectures (session 2), quantization (session 3) and runtimes (session 7).
- New threats appear that no training set contains. Wheat blast was found in Bangladesh in February 2016, its first appearance in Asia; it hit about 15,000 hectares in eight districts (Islam et al. 2016).
- So the app must be allowed to say "not sure". Selective classification answers only when the top softmax probability passes a threshold (Geifman & El-Yaniv 2017). Report coverage (the fraction answered) with the accuracy on answered photos.
- In the lab, the best model answering its 60% most confident field photos (top probability at least 0.81) raised accuracy from 0.740 to 0.827. The baseline barely improved (0.398 to 0.450 at 40% coverage): a shortcut model is confidently wrong.
- Unanswered photos go to a person: Bangladesh's Krishi Call Centre (16123) took 92,094 calls from farmers between July 2025 and June 2026 (BSS 2026). The notebook's Bangla message says "I cannot be sure from this photo; call 16123."
- **Pause and try:** at 60% coverage and 0.827 accuracy, out of 1,000 farmer photos, how many get an answer, and about how many answers are wrong?
  - **Answer:** 600 answered and 400 sent to a person; about 0.173 × 600 ≈ 104 wrong answers.

### Lab guide (about 2 hours, notebook `s02_plant_disease.ipynb`)

1. Section 1 (15 min): generate both sets; compare class brightness.
2. Section 2 (25 min): the baseline, the swap test and the field test.
3. Section 3 (25 min): background randomization, then jitter and blur.
4. Section 4 (20 min): the leaf mask; its overlap and accuracy by class.
5. Section 5 (15 min): the accuracy–coverage curve.
6. TODO cells (20 min): remove the bias; choose the threshold on validation photos.

- **Expect:** mean brightness by class 0.714, 0.58, 0.618, 0.35 (lab) against 0.374 to 0.415 (field); 6,292 parameters. Lab / swapped / field accuracy: baseline 0.978 / 0.848 / 0.398; background randomization 0.980 / 0.965 / 0.537; plus jitter and blur 0.900 / 0.958 / 0.740. Excess-green mask IoU 0.801 (lab, 0.485 for blight) and 0.528 (field); mask model lab 0.915, field 0.480 (0.532 with the true mask). Best model at coverage 1.0, 0.8, 0.6, 0.4: accuracy 0.740, 0.792, 0.827, 0.875 (threshold 0.81 for 0.6); baseline 0.398 to 0.450. Runtime about 55 seconds.
- **Common problems:** choosing augmentation ranges or the abstention threshold on the field test set; a colour mask that deletes symptoms (check it class by class); reporting accuracy on answered photos without the coverage.

### Quiz

1. What is shortcut learning? Give the lab's example.
   - **Answer:** a rule that works on the benchmark but not in real use. The lab baseline partly read background colour and brightness, which followed the class in lab photos.
2. Why did background randomization leave lab accuracy unchanged but raise field accuracy?
   - **Answer:** lab test photos can be classified from the background or from the lesions, so both models score about 0.98 there. Randomization made the model use the leaf (the swap test rose from 0.848 to 0.965), and features of the leaf carry over to field photos.
3. An app reports 0.95 accuracy. What else must it report?
   - **Answer:** the coverage (what fraction of photos it answered) and where the test photos came from.

**Watch out:** "99% test accuracy means the app works for farmers." A test set made the same way as the training set measures the lab, not the field. Mohanty et al. measured 99.35% on PlantVillage and 31.4% on other photos; in our lab, 0.978 on lab photos and 0.398 in the field. Test on photos from farmers' own phones, from several districts and seasons.

### Assignment 2 (due before session 3, 10 points)

1. Complete TODO 1. Report lab, swapped and field accuracy without the background bias, and estimate how much of the field drop the shortcut caused. (3 points)
2. Complete TODO 2. Compare the coverage and accuracy promised by the validation photos with those on the field test photos. (3 points)
3. In one page, design a field test set for a rice disease app in Bangladesh: who takes the photos, in which seasons and districts, how labels are checked, and what the app does when it abstains. (4 points)

Hand in one PDF and your notebook.

### Sources

- Mohanty, Hughes & Salathé 2016, Using Deep Learning for Image-Based Plant Disease Detection, Frontiers in Plant Science 7:1419. https://arxiv.org/abs/1604.03169
- Geirhos et al. 2020, Shortcut learning in deep neural networks, Nature Machine Intelligence 2:665–673. https://arxiv.org/abs/2004.07780
- Hughes & Salathé 2015, An open access repository of images on plant health to enable the development of mobile disease diagnostics. https://arxiv.org/abs/1511.08060
- Singh et al. 2020, PlantDoc: A Dataset for Visual Plant Disease Detection (CoDS-COMAD 2020). https://arxiv.org/abs/1911.10317
- Rahman et al. 2020, Identification and recognition of rice diseases and pests using convolutional neural networks, Biosystems Engineering 194:112–120. https://arxiv.org/abs/1812.01043
- Hossain et al. 2023, Dhan-Shomadhan: A Dataset of Rice Leaf Disease Classification for Bangladeshi Local Rice. https://arxiv.org/abs/2309.07515
- Islam et al. 2016, Emergence of wheat blast in Bangladesh was caused by a South American lineage of Magnaporthe oryzae, BMC Biology 14:84. https://doi.org/10.1186/s12915-016-0309-7
- Geifman & El-Yaniv 2017, Selective Classification for Deep Neural Networks (NeurIPS 2017). https://arxiv.org/abs/1705.08500
- Woebbecke et al. 1995, Color indices for weed identification under various soil, residue, and lighting conditions, Transactions of the ASAE 38(1):259–269. https://doi.org/10.13031/2013.27838
- TensorFlow Datasets, plant_village catalog entry. https://www.tensorflow.org/datasets/catalog/plant_village
- BSS 2026, Farmers' trust in "Agriculture Call Centre" grows, calls top 92,000 annually. https://www.bssnews.net/special-stories/401845

## Session 3: Seeing crops from space

**Goal:** students can compute vegetation and water indices, mask clouds, build composites, and smooth a vegetation time series to read crop phenology.

### Talking pointers

- **Open with:** "A satellite photographs every rice field in Bangladesh every few days, for free. The hard part is the monsoon: the Aman crop grows under clouds."
- **Segment 1, say:** draw the spectral signatures from the notebook's first plot and point to the jump of vegetation from red to near-infrared.
- **Segment 2, say:** work out NDVI for a leaf and for water on the board, then show the cloudy monsoon date beside its blue-band mask.
- **Segment 3, say:** show one Aman pixel's NDVI series: raw points, masked points, and the smoothed curve against the truth.
- **Close with:** "Mask first, composite or smooth second, and always ask what NDVI can and cannot tell you." Then set assignment 3.

### Segment 1 (6 min): satellites and spectral signatures

- **Sentinel-2** (European Space Agency, ESA) measures 13 spectral bands at 10, 20 or 60 m, with a 290 km swath. Each satellite revisits a place every 10 days, two together every 5 days at the equator (Drusch et al. 2012). Sentinel-2C was launched in September 2024 to replace Sentinel-2A (ESA 2024).
- **Landsat 8 and 9** (NASA and USGS) give 30 m images; each repeats every 16 days, and together they give 8-day coverage (NASA 2021).
- **MODIS** on NASA's Terra and Aqua is coarse (250 m to 1 km) but views most places about daily. As of 2026, NASA expects MODIS to stop collecting science data in 2027 and points users to the VIIRS instrument (NASA Earthdata 2025; NASA LAADS DAAC).
- **Sentinel-1** carries a radar that sees through clouds (session 8). As of November 2026, Sentinel-1C and Sentinel-1D form the operating pair, after Sentinel-1A ended operations in June 2026 (ESA 2026).
- Surfaces have spectral signatures. Leaves absorb red light for photosynthesis and reflect near-infrared (NIR) strongly; water is dark in NIR; soil brightens towards the short-wave infrared; clouds are bright in every band, including blue.
- **Pause and try:** in a monsoon month, a pixel is cloudy on 80% of Sentinel-2 acquisitions. With a 5-day revisit, how many clear views do you expect in 30 days?
  - **Answer:** 30 / 5 = 6 acquisitions, and 6 × 0.2 = 1.2 clear views. Some months will give none at all.

### Segment 2 (7 min): indices, clouds and the monsoon problem

- The normalized difference vegetation index, NDVI = (NIR − Red)/(NIR + Red) (Tucker 1979), is near 0.7 to 0.8 for dense green crops, about 0.1 to 0.2 for soil and buildings, and negative for water.
- The normalized difference water index, NDWI = (Green − NIR)/(Green + NIR) (McFeeters 1996), is positive for open water. A rice field flooded for transplanting looks like water: in the lab, NDWI 0.04 and NDVI 0.01 on day 206.
- Clouds lower NDVI, because they reflect red and NIR almost equally. A missed cloud looks like a sudden crop failure.
- A simple cloud mask flags bright blue pixels, grows the mask to catch thin edges, and projects it along the sun's direction to flag shadows. In the lab: precision 0.878 and recall 0.902; thin haze slipped through. Operational masks use more bands and machine learning, such as the scene classification layer in Sentinel-2 Level-2A products.
- The monsoon problem: Aman, the monsoon rice, grows exactly when skies are cloudiest. In the synthetic year, cloud and haze covered 63% of the scene in July to September, against 9% in December to February.
- **Pause and try:** a leaf has red reflectance 0.04 and NIR 0.42; water has red 0.06 and NIR 0.03. Compute both NDVIs.
  - **Answer:** leaf (0.42 − 0.04)/(0.42 + 0.04) ≈ 0.83; water (0.03 − 0.06)/(0.03 + 0.06) ≈ −0.33.

### Segment 3 (7 min): composites, smoothing and phenology

- A **composite** combines several dates into one cloud-free image: the median of the unmasked dates, or the date with the maximum NDVI for each pixel. In the lab's monsoon window, the median composite still had no value for 41.6% of pixels; the maximum-NDVI composite filled every pixel but read 0.058 too high.
- **Phenology** is the timing of a crop's life: green-up, peak, senescence and harvest. A green-up date can be read where NDVI crosses halfway from its pre-season minimum to its peak.
- The Savitzky–Golay filter (Savitzky & Golay 1964) fits a low-order polynomial by least squares in a sliding window (Course 2 session 2 covers least squares). It keeps peaks sharper than a moving average. Chen et al. (2004) adapted it to NDVI by pulling the curve towards the upper envelope, since cloud noise is mostly downward.
- In the lab, smoothing the raw series put Aman green-up 17.4 days late on average; masking and interpolating cut the error to 5.0 days, and smoothing after masking added nothing (5.2 days).
- Data access (as of November 2026): the Copernicus Data Space Ecosystem, Google Earth Engine, Microsoft Planetary Computer and Element 84's Earth Search catalogue all serve Sentinel-2. Read each collection's scale and offset from its metadata: the integer values changed in 2022.
- **Pause and try:** why does a maximum-NDVI composite work without a cloud mask, and what does it cost?
  - **Answer:** clouds lower NDVI, so the maximum skips them. But it picks the greenest moment and any upward noise, so it is biased high (+0.058 in the lab).

### Lab guide (about 2 hours, notebook `s03_remote_sensing.ipynb`)

1. Section 1 (15 min): build the scene; read the spectral signatures.
2. Section 2 (20 min): add clouds and haze; compute NDVI and NDWI by class on two dates.
3. Section 3 (20 min): the blue-band mask, its precision and recall.
4. Section 4 (20 min): single date against median and maximum-NDVI composites.
5. Section 5 (30 min): four ways to clean a time series; green-up errors.
6. TODO cells (15 min): sweep the cloud threshold; Boro peak dates.

- **Expect:** pixels per class 720, 624, 288, 432, 240. Day 76: NDVI 0.74 (Boro), 0.19 (Aman); day 206: Aman NDWI 0.04 and NDVI 0.01, water NDWI 0.46. Cloudy fraction 0.26 overall, 0.63 in July–September, 0.09 in December–February. Mask precision 0.878, recall 0.902; missed pixel-dates 0.033 with NDVI error 0.040 (clear 0.018). Monsoon window: best single date (day 236) RMSE 0.083 with 0.780 of pixels empty; median composite 0.087 with 0.416 empty; maximum-NDVI 0.168, bias +0.058. Aman green-up (days 214 to 237): mean absolute error 17.4 days (raw + SG), 5.0 (masked + interpolated), 5.2 (plus SG), 10.1 (upper envelope). Runtime about 7 seconds.
- **Common problems:** computing NDVI on integer digital numbers without the scale and offset; interpolating across a whole season of missing dates; resampling the scene classification layer with anything but nearest neighbour.

### Quiz

1. Why is NDVI high for green leaves?
   - **Answer:** chlorophyll absorbs red light and the leaf structure reflects NIR strongly, so NIR − Red is large compared with NIR + Red.
2. A flooded field just after transplanting: what are its NDVI and NDWI roughly?
   - **Answer:** water-like: NDVI near or below 0, NDWI near or above 0 (0.01 and 0.04 in the lab).
3. Why did green-up dates from the unmasked series come out late?
   - **Answer:** clouds pull NDVI down during the monsoon green-up, so the smoothed curve crosses its halfway level later than the crop does.

**Watch out:** "NDVI measures yield directly." NDVI measures green canopy, not grain. Heat at flowering, pests and lodging late in the season can cut yield while the canopy stays green, and over dense canopies NDVI changes little as the crop grows more. NDVI is a useful input to yield models (session 5), calibrated against measured yields, never a yield measurement by itself.

### Assignment 3 (due before session 4, 10 points)

1. Complete TODO 1 and plot precision and recall against the threshold. Choose a threshold and justify it for time-series work. (3 points)
2. Complete TODO 2 and compare Boro and Aman: which season's dates are estimated better, and why? (3 points)
3. Change the cloud season so that the cloudiest period comes 30 days earlier, before Aman green-up. Re-run section 5 and explain how the four methods change. (4 points)

Hand in one PDF and your notebook.

### Sources

- Drusch et al. 2012, Sentinel-2: ESA's Optical High-Resolution Mission for GMES Operational Services, Remote Sensing of Environment 120:25–36. https://doi.org/10.1016/j.rse.2011.11.026
- Tucker 1979, Red and photographic infrared linear combinations for monitoring vegetation, Remote Sensing of Environment 8(2):127–150. https://doi.org/10.1016/0034-4257(79)90013-0
- McFeeters 1996, The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features, International Journal of Remote Sensing 17(7):1425–1432. https://doi.org/10.1080/01431169608948714
- Savitzky & Golay 1964, Smoothing and Differentiation of Data by Simplified Least Squares Procedures, Analytical Chemistry 36(8):1627–1639. https://doi.org/10.1021/ac60214a047
- Chen et al. 2004, A simple method for reconstructing a high-quality NDVI time-series data set based on the Savitzky–Golay filter, Remote Sensing of Environment 91(3–4):332–344. https://doi.org/10.1016/j.rse.2004.03.014
- ESA 2024, Sentinel-2C joins the Copernicus family in orbit. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2/Sentinel-2C_joins_the_Copernicus_family_in_orbit
- NASA 2021, Landsat 9 mission page. https://landsat.gsfc.nasa.gov/landsat-9
- NASA Earthdata 2025, Transition from MODIS to VIIRS (alert of 2 May 2025). https://www.earthdata.nasa.gov/data/alerts-outages/transition-from-modis-viirs
- NASA LAADS DAAC, MODIS to VIIRS transition (Terra and Aqua science data collection ends in 2027; checked November 2026). https://ladsweb.modaps.eosdis.nasa.gov/learn/modis-to-viirs-transition/
- ESA 2026, Time to say goodbye to Sentinel-1A. https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Time_to_say_goodbye_to_Sentinel-1A
- Element 84, Earth Search STAC catalogue. https://github.com/Element84/earth-search

## Session 4: Crop type mapping

**Goal:** students can classify crop types from satellite time series with a random forest and a 1-D CNN, and validate maps with spatial cross-validation.

### Talking pointers

- **Open with:** "A crop map that is 98% accurate in your notebook can be 88% accurate in the next district, and almost useless for the rare crop. Today we learn why, and how to measure it honestly."
- **Segment 1, say:** show the notebook's NDVI and radar curves by class and read the calendar from them: flooding, green-up, peak, harvest.
- **Segment 2, say:** draw a width-5 filter sliding along 36 dates, and explain why it finds a transplanting dip wherever it happens.
- **Segment 3, say:** show the two error maps side by side: scattered dots under random cross-validation, whole wrong fields under spatial blocks.
- **Close with:** "Split by field at least, by region when the map will be used somewhere new, and report the rare classes." Then set assignment 4.

### Segment 1 (6 min): crop types from time series

- A crop type map labels every pixel (or every field) with what grows there. One image is rarely enough: crops are told apart by their calendars, so the input is a time series of NDVI and radar values (session 3).
- Bangladesh's rice calendar gives a natural set of classes: Boro in the dry season (mainly irrigated), Aus harvested by about July, and Aman in the monsoon, with about 55%, 10% and 35% of rice output (FAO GIEWS 2026). The lab adds fields that grow Boro and then Aman in the same year, and trees.
- Labels come from field surveys: someone visits a field and records the crop. Surveys are expensive, so labels are few, clustered along roads and villages, and sometimes wrong.
- Classes are imbalanced. A rare class barely moves overall accuracy, so report per-class F1 and the macro F1, the average over classes.
- Real fields blur the classes: weeds in a fallow season, a short vegetable crop, planting dates that move by weeks between places and years.
- **Pause and try:** in the lab, Aus covers 319 of 9,216 pixels. If a model never predicts Aus but is perfect otherwise, what are its accuracy and its Aus F1?
  - **Answer:** accuracy 1 − 319/9,216 ≈ 0.965, and Aus F1 = 0. High accuracy, useless for Aus.

### Segment 2 (7 min): models for satellite time series

- **Random forest** on all dates and bands: a strong, fast baseline that copes with noise, but it treats each date as an unrelated column.
- **Temporal CNN** (TempCNN): 1-D convolutions along time. Pelletier et al. (2019) found it more accurate than random forests and recurrent networks on a large Formosat-2 time series.
- **Attention models:** the pixel-set encoder with temporal self-attention treats each field as a set of pixels and attends over dates (Garnot et al. 2020). Rußwurm & Körner (2020) found self-attention and recurrent models better than CNNs on raw, uncleaned time series, while preprocessing raised every model's accuracy and the choice of model mattered less. The ranking of model families is not settled.
- In the lab, the temporal CNN beat the random forest by 5 to 6 points of accuracy under field-level and block splits, probably because planting dates shifted by weeks across the region (−42 to +50 days) and a convolution recognizes a shape wherever it falls.
- **Pause and try:** a width-5 filter slides along 36 dates of 10-day composites. How many days does one filter see?
  - **Answer:** 5 × 10 = 50 days, enough to see a flooding dip followed by green-up.

### Segment 3 (7 min): validating a map

- Nearby pixels are alike (spatial autocorrelation), and pixels of one field are near copies. A random pixel split puts the same fields in training and test, so it measures memory (Roberts et al. 2017; Course 6 session 3).
- Ploton et al. (2020) mapped forest biomass in central Africa from 11.8 million trees: random validation suggested the model explained over half of the variation, while spatial validation showed almost no predictive power.
- Honest splits: by field (`GroupKFold` with field identifiers) at least; by spatial blocks larger than the range of autocorrelation when the map will be used in a new area; best of all, a separate survey in the new district.
- In the lab, accuracy fell from 0.983 (random pixels) to 0.906 (fields) and 0.885 (blocks) for the random forest, and Aus F1 from 0.78 to 0.25.
- The area of applicability (Meyer & Pebesma 2021) flags pixels whose features are unlike any training pixel. In the lab, 5.8% of block-CV test pixels fell outside it, and only 24% of those were right, against 91% inside.
- **Pause and try:** the lab map has 9,216 pixels but 260 fields, and errors come as whole fields. Why does that matter for an error bar on accuracy?
  - **Answer:** the independent test cases are closer to 260 fields than 9,216 pixels, so an interval computed on pixels is far too narrow (Course 1 session 9 covers error bars).

### Lab guide (about 2 hours, notebook `s04_crop_mapping.ipynb`)

1. Section 1 (15 min): build the region; count fields and pixels per class.
2. Section 2 (20 min): read the NDVI and radar curves of each class.
3. Section 3 (15 min): the random forest and the temporal CNN.
4. Section 4 (30 min): three splits; overall accuracy, macro F1 and per-class F1.
5. Sections 5–6 (25 min): error maps and the area of applicability.
6. TODO cells (15 min): class weights; NDVI only.

- **Expect:** fields per class 67, 71, 101, 8, 13 (pixels 2,236, 2,483, 3,644, 319, 534); regional planting shift −42 to +50 days. Accuracy (macro F1), random forest: random pixels 0.983 (0.950), fields 0.906 (0.809), blocks 0.885 (0.784); temporal CNN: 0.995 (0.987), 0.955 (0.839), 0.944 (0.831). Aus F1: 0.78 and 0.95 under random pixels, 0.25 to 0.30 under fields and blocks. Fields with more than half their pixels wrong: 0.115 (blocks) against 0.019 (random); fields with no error 0.792 against 0.915. Area of applicability: 0.058 of pixels outside; accuracy 0.913 inside, 0.242 outside. Runtime about 1 minute.
- **Common problems:** passing field or block identifiers to `KFold`, which ignores groups; assigning blocks pixel by pixel, which cuts fields across blocks and leaks them; forgetting `model.eval()`, so dropout and batch normalization stay in training mode at prediction time.

### Quiz

1. Why does a random pixel split overestimate map accuracy?
   - **Answer:** pixels of the same field are in both training and test, and they are near copies, so the model is tested on fields it has seen.
2. What does macro F1 show that overall accuracy hides?
   - **Answer:** performance on rare classes, because every class counts equally in the average.
3. What is the area of applicability?
   - **Answer:** the part of feature space close enough to the training data for the model's cross-validated error to apply; pixels outside it get a warning.

**Watch out:** "Random cross-validation tells you how a map will do in a new district." It tells you how well the model recognizes fields it has already seen. In the lab, random pixel cross-validation gave 0.983 and spatial blocks 0.885, and the rare Aus class fell from F1 0.78 to 0.25. For a new district, hold out whole regions, check the area of applicability, and if possible collect a small survey there.

### Assignment 4 (due before session 5, 10 points)

1. Complete TODO 1 and compare per-class F1 with and without class weights. (3 points)
2. Complete TODO 2. Which classes lose most without radar, and why? (3 points)
3. Repeat the block split with blocks of 12, 24 and 48 pixels. Plot accuracy and macro F1 against block size and explain the trend in terms of spatial autocorrelation. (4 points)

Hand in one PDF and your notebook.

### Sources

- Pelletier, Webb & Petitjean 2019, Temporal Convolutional Neural Network for the Classification of Satellite Image Time Series, Remote Sensing 11(5):523. https://arxiv.org/abs/1811.10166
- Roberts et al. 2017, Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure, Ecography 40(8):913–929. https://doi.org/10.1111/ecog.02881
- Garnot et al. 2020, Satellite Image Time Series Classification with Pixel-Set Encoders and Temporal Self-Attention (CVPR 2020). https://arxiv.org/abs/1911.07757
- Rußwurm & Körner 2020, Self-attention for raw optical Satellite Time Series Classification, ISPRS Journal of Photogrammetry and Remote Sensing 169:421–435. https://arxiv.org/abs/1910.10536
- Ploton et al. 2020, Spatial validation reveals poor predictive performance of large-scale ecological mapping models, Nature Communications 11:4540. https://doi.org/10.1038/s41467-020-18321-y
- Meyer & Pebesma 2021, Predicting into unknown space? Estimating the area of applicability of spatial prediction models, Methods in Ecology and Evolution 12(9). https://arxiv.org/abs/2005.07939
- FAO GIEWS 2026, Country Brief: Bangladesh (reference date 4 September 2026). https://www.fao.org/giews/countrybrief/country.jsp?code=BGD

## Session 5: Predicting crop yield

**Goal:** students can build yield models from weather and satellite features, validate them on unseen years, and give prediction intervals.

### Talking pointers

- **Open with:** "Two yield models score the same in random cross-validation. In a hot year, one is off by 0.02 tonnes per hectare and the other by 0.9. Which, and why?"
- **Segment 1, say:** list the features on the board, then show yield against heat days, with 2025 far to the right.
- **Segment 2, say:** show the partial dependence plot: the linear line keeps falling past 8 heat days, the boosting curve goes flat.
- **Segment 3, say:** show the interval plot for 2025: the boosting intervals float above the true yields.
- **Close with:** "Validate on years the model has not seen, check whether the new year lies inside your data, and give every forecast an interval that you have tested." Then set assignment 5.

### Segment 1 (6 min): yield data and features

- Official yields come from surveys: the Bangladesh Bureau of Statistics publishes yearly crop estimates in its Yearbook of Agricultural Statistics, with yields from measured sample plots, known as crop cuts (FEWS NET). Such data are noisy, yearly and short.
- Common features are seasonal summaries: **growing degree days** (GDD, the sum of daily mean temperature above a base temperature); **heat days** (days above a high threshold around flowering, when heat can make rice florets sterile); **seasonal rainfall** (too little and too much both hurt); and **peak NDVI** from satellites (session 3).
- Yields also trend: new varieties and practices raise them year after year, and climate trends push the other way. Lobell et al. (2011) estimated that climate trends since 1980 measurably reduced global maize and wheat production compared with a world without those trends.
- Heat is not hypothetical: the April 2024 heatwave, the longest since 1948, came while Boro rice, harvested from April to June, was still in the fields (Down To Earth 2024; FAO GIEWS 2026).
- **Pause and try:** a model loses 0.12 t/ha per heat day. A district usually has 3 heat days; a hot year brings 14. What loss does the model predict?
  - **Answer:** (14 − 3) × 0.12 = 1.32 t/ha, a large share of a yield of about 3 to 4 t/ha.

### Segment 2 (7 min): models, and validation on unseen years

- **Linear regression** on engineered features (rainfall and rainfall squared, heat days, GDD, NDVI, year) is easy to read: in the lab it recovered −0.109 t/ha per heat day (true −0.12) and +0.029 t/ha per year (true 0.035). Standardize features first; rainfall squared is about $10^6$, and badly scaled columns can make a least-squares solver drop real coefficients (Course 2 session 10).
- **Gradient boosting** finds bends and interactions by itself (Course 6 session 5).
- **Remote-sensing models** learn features from images: You et al. (2017) summarized satellite image time series as histograms of pixel values per county, trained deep networks on them, and added a Gaussian process to share information between neighbouring counties.
- Validate as the model will be used: leave one year out (or train on past years only). In the lab, random 5-fold cross-validation scored both models at RMSE 0.323 t/ha; leaving one year out, the linear model stayed at 0.334 but boosting rose to 0.437, because it had learned each year's shared shock from that year's other districts.
- **Pause and try:** in training, heat days ranged from 0 to 8. A new district has 15. What heat effect will a tree ensemble apply?
  - **Answer:** about the effect at 8 heat days, the edge of its training range, because every tree predicts a constant beyond its last split. It misses about 7 × 0.12 = 0.84 t/ha of loss.

### Segment 3 (7 min): extreme years and prediction intervals

- In the lab's hot year, all districts had 10 to 17 heat days. Boosting overpredicted by 0.919 t/ha on average (RMSE 0.989); the linear model was almost unbiased (−0.016, RMSE 0.269), because its slope continues and the true effect really was linear.
- Peak NDVI gave no warning: 0.700 in the hot year against 0.683 on average, because in the lab heat sterility does not change greenness.
- **Quantile regression** fits a quantile directly with the pinball loss: for residual $r = y - \hat y_q$, the loss is $q\,r$ when $r \ge 0$ and $(q - 1)\,r$ when $r < 0$. Quantiles 0.05 and 0.95 give a 90% interval (Course 2 session 7 covers intervals for estimates; Course 3 session 12 covers conformal prediction).
- Test coverage honestly. Linear quantile intervals covered 0.876 of held-out-year yields (0.69 to 0.97 in single years, since a year shock moves all districts together) and 0.938 in the hot year. Boosting's narrower intervals covered only 0.671 and 0.266.
- **Pause and try:** for $q = 0.95$, what is the pinball loss when the true yield is 0.2 t/ha above the predicted quantile, and when it is 0.2 below?
  - **Answer:** 0.95 × 0.2 = 0.19 above, and 0.05 × 0.2 = 0.01 below. Misses above cost 19 times more, so the fitted line sits high enough that only about 5% of yields lie above it.

### Lab guide (about 2 hours, notebook `s05_yield_prediction.ipynb`)

1. Section 1 (20 min): build the panel and the hot year; compare their heat days, yields and NDVI.
2. Section 2 (25 min): two models under random and leave-one-year-out cross-validation; read the coefficients.
3. Section 3 (25 min): predict the hot year; read the partial dependence plot.
4. Section 4 (30 min): quantile intervals, their coverage and width.
5. TODO cells (20 min): drop features; conformal intervals.

- **Expect:** heat days mean 2.8 (maximum 8); 2025 mean 13.5 (10 to 17). Yield mean 3.38 t/ha (sd 0.71); 2025 mean 2.91. Peak NDVI 0.683 and 0.700. RMSE: random 5-fold 0.323 (both models); leave-one-year-out 0.334 (linear) and 0.437 (boosting). Linear coefficients 0.0290 t/ha per year, −0.1088 per heat day, 5.90 per unit NDVI. Hot year: linear RMSE 0.269 (mean error −0.016), boosting 0.989 (+0.919). 90% intervals: linear coverage 0.876 (0.69 to 0.97 by year), width 1.07 t/ha, hot year 0.938 (width 0.89); boosting 0.671 (0.44 to 0.88), width 0.74, hot year 0.266 (width 1.10). Runtime about 46 seconds.
- **Common problems:** random cross-validation for a yield model; unscaled features in linear and quantile regression; lower and upper quantile models that cross, so check that the lower bound is below the upper one.

### Quiz

1. Why did boosting's error rise from 0.323 to 0.437 t/ha when whole years were held out, while the linear model's hardly changed?
   - **Answer:** with random folds, boosting learned each year's hidden shock from other districts of the same year through the year feature. A straight line in year cannot do that, so it had less to lose.
2. What does a tree ensemble predict for feature values beyond its training range?
   - **Answer:** the same as at the edge of the range: each tree's last leaf is a constant, so the prediction goes flat.
3. A 90% interval covers 0.876 of yields over all years but 0.69 in one year. Why can one year be so much worse?
   - **Answer:** a shared year shock shifts all districts together, so errors within a year are not independent; coverage must be judged over many years.

**Watch out:** "Tree ensembles extrapolate to conditions they have never seen." They cannot: beyond the training range, every tree predicts a constant. In the lab's hot year, boosting overpredicted yield by 0.919 t/ha while a linear model with a heat-day feature was off by 0.016. Check whether a new season lies inside the training data, use terms that can extrapolate where agronomy supports them, and treat any forecast outside the data with suspicion.

### Assignment 5 (due before session 6, 10 points)

1. Complete TODO 1. Report the hot-year error of the linear model without heat days, and without NDVI. Which feature carries the hot-year signal? (3 points)
2. Complete TODO 2 and compare conformal intervals with quantile regression intervals for coverage and width, in normal years and the hot year. (4 points)
3. Build a hybrid model: a linear term in heat days plus boosting on the remaining residual. Compare it with both models in the hot year. (3 points)

Hand in one PDF and your notebook.

### Sources

- Lobell, Schlenker & Costa-Roberts 2011, Climate Trends and Global Crop Production Since 1980, Science 333(6042):616–620. https://doi.org/10.1126/science.1204531
- You, Li, Low, Lobell & Ermon 2017, Deep Gaussian Process for Crop Yield Prediction Based on Remote Sensing Data (AAAI 2017). https://ojs.aaai.org/index.php/AAAI/article/view/11172
- FEWS NET, Bangladesh data book (crop statistics and the BBS Yearbook of Agricultural Statistics). https://help.fews.net/fde/bangladesh-data-book
- FAO GIEWS 2026, Country Brief: Bangladesh (reference date 4 September 2026). https://www.fao.org/giews/countrybrief/country.jsp?code=BGD
- Down To Earth 2024, Unusual heat scorches Bangladesh as April's consecutive heatwave breaks 76-year record. https://www.downtoearth.org.in/climate-change/unusual-heat-scorches-bangladesh-as-april-s-consecutive-heatwave-breaks-76-year-record-96034

## Session 6: Weather data, baselines and forecast skill

**Goal:** students can build persistence and climatology baselines, score forecasts with skill scores, and evaluate probabilistic forecasts with CRPS and the Brier score.

### Talking pointers

- **Open with:** "'Tomorrow will be like today' is a forecast, and a hard one to beat. Before anyone believes your weather model, it must beat that, and the calendar average, at every lead time."
- **Segment 1, say:** show one synthetic year: the seasonal cycle, the wiggles around it (anomalies), and the rainy monsoon.
- **Segment 2, say:** show the two skill curves: persistence crossing below zero at day 5, the AR model sliding towards climatology.
- **Segment 3, say:** show the CRPS bars, then the reliability diagram with the overconfident forecast bending away from the diagonal.
- **Close with:** "Always report a baseline, score anomalies, and judge probabilities with proper scores and a reliability diagram." Then set assignment 6.

### Segment 1 (6 min): weather data

- Weather is the state of the atmosphere on a day; climate is the statistics of weather over many years. An **anomaly** is the departure from the climatological value for that date. Anomalies persist: the April 2024 heatwave in Bangladesh lasted 30 days in a row (Down To Earth 2024).
- **Stations** measure one point, often with gaps and changes of instrument. National services such as the Bangladesh Meteorological Department run station networks.
- **Reanalysis** combines past observations with a weather model to reconstruct the atmosphere everywhere, consistently. ERA5 from the European Centre for Medium-Range Weather Forecasts (ECMWF) gives hourly fields on a grid of about 31 km (Hersbach et al. 2020); it is the usual training data for machine-learning weather models (session 7).
- Gridded data come as **NetCDF** files (labelled arrays such as temperature by time, latitude and longitude) or **Zarr** stores (the same, split into chunks so cloud storage can serve only what you need). `xarray` reads both.
- **Pause and try:** the climatology for a date is 27.0 °C, today's anomaly is +2.0 °C, and the lag-1 autocorrelation of anomalies is 0.92. What do persistence, climatology and damped persistence predict for tomorrow?
  - **Answer:** persistence 29.0 °C; climatology about 27.0 °C; damped persistence 27.0 + 0.92 × 2.0 ≈ 28.8 °C.

### Segment 2 (7 min): baselines and skill

- **Persistence** repeats today; **climatology** predicts the long-term average for the date. Persistence wins at short leads, climatology at long leads.
- The **skill score** compares a forecast with a reference: SS = 1 − MSE/MSE(reference). 1 is perfect, 0 is no better than the reference, and negative is worse.
- In the lab, persistence had RMSE 0.80 °C at day 1 against 2.04 for climatology (skill 0.84), but negative skill from day 5. The autoregressive (AR) model's skill against climatology fell from 0.86 at day 1 to 0.26 at day 5 and 0.06 at day 10.
- The **anomaly correlation coefficient** (ACC) correlates forecast and observed anomalies. Never correlate raw temperatures: in the lab, climatology alone correlated 0.89 with observed temperature at day 5, purely through the seasonal cycle, while its anomaly correlation is zero.
- Estimate the climatology from training years only; using test years leaks the answer.
- **Pause and try:** at day 5, the AR model's RMSE is 1.75 °C and climatology's is 2.03 °C. What is the AR model's skill score against climatology?
  - **Answer:** 1 − 1.75²/2.03² = 1 − 3.06/4.12 ≈ 0.26, matching the lab.

### Segment 3 (7 min): probabilistic forecasts

- An **ensemble** runs a model from slightly different starting states; its spread expresses uncertainty. A good ensemble's spread matches its typical error.
- The **continuous ranked probability score** (CRPS) compares the forecast distribution with the observation; for draws $X, X'$ from the forecast, CRPS = $E|X - y| - \tfrac12 E|X - X'|$, and it has a closed form for a Gaussian (Gneiting & Raftery 2007). For a single-number forecast it equals the absolute error, so the two can be compared.
- In the lab at 3 days: the well-spread ensemble scored 0.800, half the spread 0.849, double the spread 0.945, climatology 1.133, and the single number 1.109. Small ensembles overstate the CRPS: 0.958 from 5 members, 0.805 from 200.
- The **Brier score** is the mean of $(p - o)^2$ for a probability $p$ and an outcome $o$ of 1 or 0. Both CRPS and the Brier score are **proper**: a forecaster gets the best expected score by stating true beliefs. The logarithmic score, the cross-entropy of Course 2 session 11, is another.
- A **reliability diagram** checks that events forecast at 70% happen about 70% of the time (Course 3 session 12). In the lab, doubling the log-odds of a rain forecast made 76% of forecasts extreme and erased its Brier skill (0.085 to −0.003).
- **Pause and try:** you forecast a 70% chance of rain. What is the Brier score if it rains, and if it does not?
  - **Answer:** (0.7 − 1)² = 0.09 if it rains, and (0.7 − 0)² = 0.49 if it stays dry.

### Lab guide (about 2 hours, notebook `s06_forecast_skill.ipynb`)

1. Section 1 (15 min): generate 30 years of temperature and rain; read one year.
2. Section 2 (35 min): persistence, climatology and the AR model at leads 1 to 10; RMSE, skill and ACC.
3. Section 3 (30 min): Gaussian ensembles and the CRPS, closed form and from members.
4. Section 4 (25 min): rain probabilities, Brier score and reliability.
5. TODO cells (15 min): damped persistence; the Brier decomposition.

- **Expect:** 10,958 days (7,305 training, 3,653 test); temperature mean 26.0 °C, anomaly sd 2.08 °C; wet days 0.23 (July 0.71, January 0.06). RMSE at days 1, 5, 10: persistence 0.80, 2.07, 2.62; climatology 2.04, 2.03, 2.03; AR 0.75, 1.75, 1.98. Skill against climatology: persistence 0.84, −0.03, −0.66; AR 0.86, 0.26, 0.06; AR against persistence at day 1, 0.12. ACC (AR) 0.93, 0.50, 0.22; climatology's plain correlation at day 5 0.89. CRPS at day 3: 0.800, 0.849, 0.945, 1.133 and 1.109 (MAE); CRPS skill 0.29; members 0.958 (5) to 0.805 (200). Brier scores 0.1310 (climatology), 0.1199 (logistic, skill +0.085), 0.1314 (overconfident, −0.003). Runtime about 4 seconds.
- **Common problems:** correlating raw values instead of anomalies; fitting the climatology on the test years; comparing the CRPS of ensembles of different sizes; mixing UTC and local days (Bangladesh is UTC+6) when making daily values from ERA5.

### Quiz

1. Why is persistence a strong baseline at 1 day and a weak one at 10 days?
   - **Answer:** anomalies last a few days, so today predicts tomorrow well; after a week the anomaly has decayed, and today's value adds error compared with the climatological average.
2. Why compute the anomaly correlation and not the correlation of raw temperatures?
   - **Answer:** both forecast and observation follow the seasonal cycle, so raw correlation is high even for climatology (0.89 in the lab); anomalies measure what the forecast adds.
3. An ensemble's spread is half its typical error. What happens to its CRPS?
   - **Answer:** it gets worse (0.849 against 0.800 in the lab): the CRPS penalizes overconfidence.

**Watch out:** "Beating persistence at one day ahead means the model is skilful." At day 1 persistence is strong (skill 0.84 against climatology in the lab), and beating it by 12%, as the AR model did, is a modest result. At day 5 and beyond persistence is worse than climatology, so beating it means nothing. Report skill against both persistence and climatology, at every lead, with probabilistic scores where uncertainty matters.

### Assignment 6 (due before session 7, 10 points)

1. Complete TODO 1 and plot damped persistence beside persistence and the AR model. (3 points)
2. Complete TODO 2 and explain which term of the Brier decomposition makes the overconfident forecast worse. (3 points)
3. Compute RMSE, skill and CRPS separately for June to September and for December to February in the test years. Which season is harder, and why? (4 points)

Hand in one PDF and your notebook.

### Sources

- Gneiting & Raftery 2007, Strictly Proper Scoring Rules, Prediction, and Estimation, Journal of the American Statistical Association 102(477):359–378. https://doi.org/10.1198/016214506000001437
- Hersbach et al. 2020, The ERA5 global reanalysis, Quarterly Journal of the Royal Meteorological Society 146(730):1999–2049. https://doi.org/10.1002/qj.3803
- Down To Earth 2024, Unusual heat scorches Bangladesh as April's consecutive heatwave breaks 76-year record. https://www.downtoearth.org.in/climate-change/unusual-heat-scorches-bangladesh-as-april-s-consecutive-heatwave-breaks-76-year-record-96034

## Session 7: Machine learning weather prediction

**Goal:** students can explain how data-driven weather models work and are evaluated, and train and roll out a learned model of a chaotic toy atmosphere.

### Talking pointers

- **Open with:** "In 2023 a neural network that runs in under a minute beat the world's best physics-based 10-day forecast on 90% of its authors' scores. Is forecasting now a machine learning problem? Today we build a tiny version and see where it breaks."
- **Segment 1, say:** draw the pipeline: observations, data assimilation, analysis, model, forecast. Circle the one box machine learning replaced.
- **Segment 2, say:** show the lab's truth and forecast panels, then the activity table: a sharp rollout against a blurred forecast trained with mean squared error.
- **Segment 3, say:** show the error-growth plot and the spread-against-error plot; ask why the network's ensemble is overconfident.
- **Close with:** "Machine learning changed how forecasts are made, but not the limits of predictability or the need for observations and honest evaluation." Then set assignment 7.

### Segment 1 (6 min): from numerical weather prediction to learned models

- Numerical weather prediction (NWP) solves the equations of fluid flow and heat on a global grid, step by step. Its starting state, the **analysis**, comes from **data assimilation**, which combines observations with a short forecast.
- A reanalysis such as ERA5 (session 6) re-runs one fixed assimilation system over past decades; data-driven models learn from it.
- The main models: FourCastNet, a Fourier neural operator (Pathak et al. 2022); Pangu-Weather, a 3D transformer (Bi et al. 2023); GraphCast, a graph neural network that beat ECMWF's high-resolution forecast on 90% of 1,380 targets (Lam et al. 2023); GenCast, a diffusion model that beat ECMWF's ensemble on 97.2% of 1,320 targets (Price et al. 2025); and Aurora, a 1.3-billion-parameter foundation model (Bodnar et al. 2025).
- Some now run operationally (as of November 2026). ECMWF's Artificial Intelligence Forecasting System (AIFS; Lang et al. 2024) went live on 25 February 2025 (ECMWF 2025a) and its ensemble, AIFS ENS, on 1 July 2025, beside the physics-based system (ECMWF 2025b). In December 2025 the US agency NOAA made operational AIGFS, a GraphCast-based model fine-tuned on NOAA's own analyses (WMO 2025).
- **Pause and try:** GraphCast takes 6-hour steps. How many steps make a 10-day forecast, and why does it matter?
  - **Answer:** 40. Each step works on the model's own output, so small errors compound.

### Segment 2 (7 min): how the models work, and why they blur

- The core is a learned step: from the current state (GraphCast also uses the state 6 hours earlier), predict the state 6 hours later, then apply the step to its own output again: an **autoregressive rollout**.
- GraphCast maps the latitude–longitude grid onto a multi-scale mesh and passes messages on it (Course 7 session 11). AIFS uses a graph encoder and decoder around a transformer.
- Training minimizes the mean squared error (MSE) against reanalysis. GraphCast is fine-tuned on rollouts of up to 12 steps (3 days), so the loss sees compounding errors (Lam et al. 2023).
- The catch: under uncertainty, the forecast with the smallest expected squared error is the **average of the possible futures**, which is smooth and weak. Small intense systems lose strength: NOAA reported better cyclone tracks but worse intensities in AIGFS version 1.0 (WMO 2025).
- Probabilistic models avoid one blurred answer. GenCast, a conditional diffusion model (Course 3 session 8), generates each ensemble member by denoising (Price et al. 2025). AIFS ENS is trained with a loss based on the continuous ranked probability score, CRPS (Lang et al. 2024b).
- **Pause and try:** tomorrow's value is equally likely to be +4 or −4. Which single forecast minimizes the expected squared error, and what is its RMSE? What is the RMSE of forecasting +4?
  - **Answer:** 0, with RMSE 4. Forecasting +4 gives $\sqrt{0.5 \times 0 + 0.5 \times 64} \approx 5.66$. The blurred forecast wins on RMSE although it is never right.

### Segment 3 (7 min): evaluation, limits and Bangladesh

- WeatherBench 2 (Rasp et al. 2024) is the common test: ERA5 as truth, fixed test years, headline scores (RMSE, anomaly correlation, and CRPS and spread–skill for ensembles) and a live website.
- Scores depend on the reference. Checked against surface stations, ECMWF found its physics-based ensemble still more skilful than AIFS ENS for 10-metre wind speed (ECMWF 2025c).
- The models still start from analyses made by physics-based data assimilation (ECMWF 2025b). AIFS ENS runs at 31 km against 9 km for the physics-based ensemble, too coarse for one thunderstorm.
- One study checked GraphCast's 1- to 3-day rainfall forecasts at 43 Bangladesh Meteorological Department stations in 2023–2024: higher correlation (0.57–0.65) and lower RMSE than the ECMWF and GFS forecasts compared, but too many extreme-rain false alarms, and better skill in central and northern Bangladesh than on the coast and in the south-eastern hills (Hasan et al. 2026). One model, two years: promising, not settled.
- AIFS forecasts are open data under a CC BY 4.0 licence (ECMWF, AIFS open data); the lab's last cell downloads one for Dhaka.
- **Pause and try:** roughly how many 9 km grid boxes fit in one 31 km box?
  - **Answer:** $(31/9)^2 \approx 11.9$, about 12, so a storm filling one 9 km box is averaged over 12.

### Lab guide (about 2 hours, notebook `s07_ml_weather.ipynb`)

1. Sections 1–2 (25 min): the Lorenz-96 toy atmosphere (40 variables on a circle; a step of 0.05 time units stands for 6 hours) and a perfect model started from analyses with errors of 1 to 0.001.
2. Sections 3–4 (35 min): train the periodic CNN on the 6-hour change and roll it out to 25 days; read the panels and RMSE curves.
3. Section 5 (20 min): the direct MSE model; compare RMSE and activity (the spread of a forecast's departures from climatology).
4. Section 6 (20 min): 20-member ensembles, spread against error, and CRPS.
5. Sections 7–8 (20 min): the NOT RUN cells (WeatherBench 2, the open AIFS forecast) and the TODO cells.

- **Expect:** the perfect model became worse than climatology (RMSE 3.64) from day 5.00, 13.50 and 20.25 for initial errors 1, 0.1 and 0.01, and never within 25 days for 0.001; small errors doubled every 1.50 days. The step CNN (3,329 parameters) had a 6-hour RMSE of 0.0493 (persistence 0.9312). Rollout RMSE was 0.220, 1.332 and 3.380 at days 1, 5 and 10; worse than climatology from day 11.00 (perfect model 13.50, persistence 1.25); anomaly correlation below 0.6 from day 9.75 (perfect model 12.00). The direct MSE CNN's activity fell from 3.54 at day 1 to 0.84 at day 15 (truth about 3.64); its RMSE lost to the rollout at day 5 (2.967 against 1.332) but won at day 15 (3.558 against 4.504). Spread/error ratio 0.55–0.74 for the CNN ensemble, 0.98–1.05 for the perfect model. Day-5 CRPS: single CNN 0.859, CNN ensemble 0.648, perfect-model ensemble 0.296. Runtime about 45 seconds.
- **Common problems:** starting forecasts from the exact truth instead of an analysis with errors, which flatters every model; forgetting circular padding, so the ends of the circle go wrong first; judging a blurred forecast by RMSE without checking its activity.

### Quiz

1. Why do data-driven weather models still depend on physics-based systems?
   - **Answer:** they learn from a reanalysis made by data assimilation, and each forecast starts from such an analysis.
2. Why does training with MSE blur long-range forecasts?
   - **Answer:** under uncertainty the MSE-optimal forecast is the average of the possible futures, and averaging different weather patterns smooths them.
3. In the lab the CNN ensemble's spread was only 0.55–0.74 of its error, while the perfect model's matched. Why?
   - **Answer:** the perturbations sampled only the initial-condition error; the CNN's model error was shared by every member, so the spread could not show it.

**Watch out:** "Machine-learning weather models have learned physics, so they can replace numerical weather prediction everywhere." They learned the statistics of a reanalysis made by physics-based assimilation, and they still start from physics-based analyses. They are judged mostly on large-scale fields at 25–30 km, weaken small intense systems such as cyclones, and have seen few record-breaking events. ECMWF runs AIFS beside its physics-based system, not instead of it.

### Assignment 7 (due before session 8, 10 points)

1. From the doubling time in section 2 (1.50 days), estimate by hand the days of useful forecast gained by halving the initial error and by cutting it tenfold. Compare with the notebook's crossing days. (3 points)
2. Complete the rollout-training TODO. Report the day-5 RMSE and day-10 activity before and after fine-tuning with a 4-step loss, and explain the change. (4 points)
3. In half a page: which scores, against which reference data, would you want before trusting a machine-learning rainfall forecast for a district in Bangladesh? Use WeatherBench 2 and Hasan et al. 2026. (3 points)

Hand in one PDF and your notebook.

### Sources

- Lam et al. 2023, Learning skillful medium-range global weather forecasting (GraphCast), Science 382. https://arxiv.org/abs/2212.12794
- Rasp et al. 2024, WeatherBench 2: A benchmark for the next generation of data-driven global weather models, Journal of Advances in Modeling Earth Systems 16. https://arxiv.org/abs/2308.15560
- Price et al. 2025, Probabilistic weather forecasting with machine learning (GenCast), Nature 637. https://arxiv.org/abs/2312.15796
- Lang et al. 2024, AIFS – ECMWF's data-driven forecasting system. https://arxiv.org/abs/2406.01465
- Lang et al. 2024b, AIFS-CRPS: Ensemble forecasting using a model trained with a loss function based on the Continuous Ranked Probability Score. https://arxiv.org/abs/2412.15832
- Pathak et al. 2022, FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators. https://arxiv.org/abs/2202.11214
- Bi et al. 2023, Accurate medium-range global weather forecasting with 3D neural networks (Pangu-Weather), Nature 619. https://arxiv.org/abs/2211.02556
- Bodnar et al. 2025, A foundation model for the Earth system (Aurora), Nature 641. https://arxiv.org/abs/2405.13063
- Lorenz 1996, Predictability: a problem partly solved, ECMWF Seminar on Predictability (4–8 September 1995), volume 1, pages 1–18; reprinted in Palmer & Hagedorn (eds.) 2006, Predictability of Weather and Climate (Cambridge University Press). https://www.cambridge.org/core/books/predictability-of-weather-and-climate/predictability-a-problem-partly-solved/3221BDE379DEB669BA52C66263AF3206
- Hasan, Yildiz & Kamruzzaman 2026, Assessment of the GraphCast AI model for precipitation forecasting and its potential in extreme event prediction over Bangladesh, PLOS Climate 5(6). https://doi.org/10.1371/journal.pclm.0000791
- ECMWF 2025a, Operational release of AIFS Single 1.0, ECMWF Newsletter 183. https://www.ecmwf.int/en/newsletter/183/news/operational-release-aifs-single-10
- ECMWF 2025b, ECMWF's ensemble AI forecasts become operational. https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational
- ECMWF 2025c, Lang & Magnusson, AIFS ENS becomes operational, ECMWF Newsletter 185 (autumn 2025). https://www.ecmwf.int/sites/default/files/elibrary/102025/81687-aifs-ens-becomes-operational.pdf
- ECMWF, AIFS machine learning data (open data, CC BY 4.0 licence). https://www.ecmwf.int/en/forecasts/datasets/aifs-machine-learning-data
- WMO 2025, NOAA deploys new generation of AI-driven global weather models. https://wmo.int/media/news/noaa-deploys-new-generation-of-ai-driven-global-weather-models

## Session 8: Floods: mapping and forecasting

**Goal:** students can map flood water from radar images, score maps with IoU, and compare an LSTM with a conceptual model for river flow.

### Talking pointers

- **Open with:** "During a monsoon flood an ordinary satellite photo shows only cloud, but radar sees through it. Today we map the water under the clouds, then forecast the river before it rises."
- **Segment 1, say:** draw a river with an upstream gauge and a village downstream; ask how much warning the gauge gives. Show a current river flood bulletin from Bangladesh's official forecasters.
- **Segment 2, say:** show the raw and filtered radar scenes and the histograms, then the scene with 3% water, where Otsu's map is full of false water.
- **Segment 3, say:** show the two hydrographs: the LSTM following a normal season, then both models missing the record peak.
- **Close with:** "A flood map is judged by the water it finds, not the dry land it gets right, and a flood model is judged by the floods it has never seen." Then set assignment 8.

### Segment 1 (6 min): floods and flood warnings

- Floods differ in their warning time. Big rivers rise over days, so upstream gauges and rainfall give time to warn. Flash floods follow intense rain on hilly ground within hours. Storm surges come with cyclones; session 10 returns to cyclone warnings. Session 1 introduced Bangladesh's main climate hazards, with the eastern flash floods of August 2024 as an example.
- Machine learning helps with two tasks: **mapping** where the water is now, for relief and damage estimates, and **forecasting** river levels days ahead, for evacuation and for moving animals and stored grain.
- In Bangladesh, the Flood Forecasting and Warning Centre (FFWC) of the Bangladesh Water Development Board issues river flood forecasts in the flood season, April to October, with deterministic lead times extended from 3 to 5 days (WMO 2018).
- Machine learning already runs in operational warnings. Google's flood forecasting system combines learned models of river stage with inundation maps and sends alerts; in the 2021 monsoon it covered flood-prone areas of India and Bangladesh home to more than 350 million people and sent more than 100 million alerts (Nevo et al. 2022). An LSTM trained across many gauged basins later forecast extreme floods in ungauged basins up to five days ahead, with reliability similar to or better than the same-day estimates of a leading global system (Nearing et al. 2024).
- **Pause and try:** a flood wave moves down a big river at about 1.5 m/s. How much warning does a gauge 300 km upstream give?
  - **Answer:** 300,000 m ÷ 1.5 m/s = 200,000 s, about 56 hours or 2.3 days. Warning time depends on data from far upstream.

### Segment 2 (7 min): mapping water with radar

- Synthetic aperture radar (SAR), such as Sentinel-1 (session 3), sends microwave pulses and records the echo, the **backscatter**, through cloud and at night. Calm water reflects the pulse away like a mirror and looks dark; buildings bounce it back and look bright.
- Traps: wind roughens water and brightens it; smooth sand, roads and radar shadows look dark like water; flooded crops can look bright.
- **Speckle** is grainy noise from interfering echoes. It multiplies the signal, and an image averaged over $L$ looks follows a gamma distribution. Filters reduce it but blur edges.
- Otsu's method (Otsu 1979) picks the threshold that best separates a histogram's two peaks. It needs no labels but fails when an image has almost no water, because then there is only one peak.
- A U-Net (Ronneberger et al. 2015) learns from labelled images; Course 6 session 7 covers such segmentation models. Sen1Floods11 (Bonafilia et al. 2020) provides hand-labelled Sentinel-1 chips from 11 flood events.
- Score maps with **intersection over union** (IoU): the overlap of predicted and true water divided by their union. Pixel accuracy is dominated by easy dry pixels.
- **Pause and try:** a tile has 1,000 pixels, 50 of them water. Map A says "no water". Map B marks 60 pixels as water, 45 correctly. Give the accuracy and IoU of each.
  - **Answer:** A: accuracy 0.95, IoU 0. B: 15 false and 5 missed pixels, so accuracy 0.98 and IoU = 45/65 ≈ 0.69.

### Segment 3 (7 min): forecasting river flow

- Rainfall–runoff models turn rain and evaporation into river flow. **Conceptual models** treat a catchment as connected buckets with a few parameters calibrated per basin; the simplest is a **linear reservoir**, flow = storage ÷ k.
- A long short-term memory (LSTM) network reads the weather day by day and keeps a memory, its cell state, much as a catchment keeps water in storage. On hundreds of US basins, LSTMs matched a well-established conceptual model (Kratzert et al. 2018).
- The **Nash–Sutcliffe efficiency** (Nash & Sutcliffe 1970) is NSE = $1 - \sum (Q_{sim} - Q_{obs})^2 / \sum (Q_{obs} - \bar Q_{obs})^2$: 1 is perfect, 0 is no better than the mean observed flow. It depends on the period: a quiet season has little variance, so the same errors give a lower NSE.
- **Ungauged basins** have no flow record to calibrate a conceptual model. A network trained on many gauged basins with their attributes (area, slope, soil) can transfer, as in Nearing et al. 2024.
- **Pause and try:** observed flows are 2, 4 and 6; a model predicts 3, 4 and 5. What is its NSE?
  - **Answer:** squared errors sum to 2; squared deviations from the mean 4 sum to 8; NSE = 1 − 2/8 = 0.75.

### Lab guide (about 2 hours, notebook `s08_floods.ipynb`)

1. Section 1 (15 min): 250 synthetic 64 × 64 radar scenes with rivers, flooded fields, sandbars and buildings.
2. Section 2 (25 min): Otsu's threshold with and without filters; accuracy against IoU; scenes with little water.
3. Section 3 (25 min): train the small U-Net, compare it with Otsu, then make every test scene 3 dB darker.
4. Sections 4–5 (35 min): ten years of a synthetic catchment; fit the linear reservoir, train the LSTM, compare NSE and the record-storm peak.
5. Sections 6–7 (20 min): read the NOT RUN cells (Sen1Floods11, neuralhydrology) and do the TODO cells.

- **Expect:** water was a fraction 0.145 of test pixels, so "no water anywhere" scored accuracy 0.855 and IoU 0.000. Otsu's IoU was 0.645 on raw images (accuracy 0.921), 0.598 with a 3 × 3 mean filter, 0.890 with a 3 × 3 median filter and 0.734 with a 5 × 5 median; on the 7 scenes with under 5% water it fell to 0.609, and with 3% water Otsu chose −9.9 dB, inside the land peak. A fixed −15 dB threshold scored 0.947 and the U-Net (13,033 weights) 0.971. With scenes 3 dB darker: Otsu 0.890 (unchanged), fixed threshold 0.751, U-Net 0.871. NSE on the held-out wet season: LSTM 0.838, linear reservoir 0.372 (training years 0.974 and 0.720). Record storm: observed peak 99.9 mm/day against a training maximum of 45.4; LSTM 41.9, linear reservoir 24.5; the LSTM's output was capped at 49.3. Runtime about 20 seconds.
- **Common problems:** a mean filter, which lets bright land swallow water edges, or a large window, which erases narrow rivers; reporting pooled IoU only, which hides failures on scenes with little water; scoring the LSTM on its warm-up days, or normalizing with statistics from the test years.

### Quiz

1. Why does calm water look dark in a radar image?
   - **Answer:** it reflects the pulse away from the satellite like a mirror, so little energy returns.
2. Why is IoU better than pixel accuracy for flood maps?
   - **Answer:** water is a small fraction of the pixels, so a map can be accurate while missing most of the water; IoU counts only predicted and true water.
3. In the lab, why did the LSTM forecast only 41.9 mm/day for a peak of 99.9?
   - **Answer:** it had never seen a flow above 45.4, and its output, a weighted sum of hidden values between −1 and 1, could not exceed 49.3.

**Watch out:** "A flood map with 95% pixel accuracy is a good map." If 5% of a scene is water, a map with no water at all scores 95%. In the lab, 0.921 accuracy came with only 0.645 IoU. Report IoU (or precision and recall for water), check scenes with little water separately, and test on images from other places, dates and calibrations.

### Assignment 8 (due before session 9, 10 points)

1. By hand, compute the accuracy and IoU of three maps for a 400-pixel tile with 20 water pixels: no water; 30 pixels marked, 18 correct; 10 pixels marked, all correct. Which would you send to a relief team, and why? (3 points)
2. Complete the augmentation TODO: retrain the U-Net with random offsets of up to ±4 dB and report its IoU on the normal and darker test scenes, next to Otsu's. (4 points)
3. Complete the ungauged-catchment TODO. Report both models' NSE on the new catchment and explain what training data would help the LSTM transfer. (3 points)

Hand in one PDF and your notebook.

### Sources

- Kratzert et al. 2018, Rainfall–runoff modelling using Long Short-Term Memory (LSTM) networks, Hydrology and Earth System Sciences 22. https://arxiv.org/abs/1803.08458
- Bonafilia et al. 2020, Sen1Floods11: a georeferenced dataset to train and test deep learning flood algorithms for Sentinel-1, CVPR Workshops. https://github.com/cloudtostreet/Sen1Floods11
- Otsu 1979, A Threshold Selection Method from Gray-Level Histograms, IEEE Transactions on Systems, Man, and Cybernetics 9(1). https://doi.org/10.1109/TSMC.1979.4310076
- Ronneberger, Fischer & Brox 2015, U-Net: Convolutional Networks for Biomedical Image Segmentation. https://arxiv.org/abs/1505.04597
- WMO 2018, Flood Forecasting and Warning in Bangladesh (article by Md. Sazzad Hossain of FFWC, 22 March 2018). https://wmo.int/node/25420
- Nevo et al. 2022, Flood forecasting with machine learning models in an operational framework, Hydrology and Earth System Sciences 26, 4013–4032. https://hess.copernicus.org/articles/26/4013/2022/
- Nearing et al. 2024, Global prediction of extreme floods in ungauged watersheds, Nature 627. https://doi.org/10.1038/s41586-024-07145-1
- Nash & Sutcliffe 1970, River flow forecasting through conceptual models part I — A discussion of principles, Journal of Hydrology 10(3). https://doi.org/10.1016/0022-1694(70)90255-6

## Session 9: Downscaling and bias correction

**Goal:** students can bias-correct climate model output with quantile mapping, downscale coarse fields with a CNN, and evaluate the extremes, not just averages.

### Talking pointers

- **Open with:** "A district officer asks how hot the hottest days will be in 2080. The climate model's grid box is bigger than the district, and the model is 1.5 degrees too cool even for the past. Today we turn its output into numbers a district can use, and find where that goes wrong."
- **Segment 1, say:** draw one coarse grid box over hills, river plain and coast, and ask what single number could describe its rain.
- **Segment 2, say:** show the temperature quantile plot: QM's curve above the others and flat at the top. Then the rain plot, where only QDM follows the model's own change.
- **Segment 3, say:** show the five downscaling panels and the exceedance curve: the CNN wins on RMSE and still misses heavy rain.
- **Close with:** "Correcting a climate model makes its past look right; whether its future is right depends on the method's assumptions, so always check the change and the extremes." Then set assignment 9.

### Segment 1 (6 min): why climate model output needs work

- Global climate models simulate the whole Earth system for centuries. CMIP6, the sixth Coupled Model Intercomparison Project, coordinates common experiments across modelling centres, including future scenarios of emissions and land use (Eyring et al. 2016).
- Scenarios are named by Shared Socioeconomic Pathways, for example SSP2-4.5 (middle of the road) and SSP5-8.5 (very high emissions). A projection is conditional on its scenario.
- Grid boxes are often about 100 km across. One box can hold hills, river plains and coast, whose rain and heat differ a lot.
- Models are also **biased**: too cool or too warm, too little day-to-day spread, and often too many light-rain "drizzle" days and too few heavy falls.
- So two steps come before district use: **bias correction**, which adjusts the statistics at a place to match observations in a past period, and **downscaling**, which adds spatial detail.
- **Pause and try:** a grid box gets 10 mm on a day. Hills cover a quarter of the box and get three times as much rain as the flat part. How much falls on each?
  - **Answer:** flat land gets $x$ and hills $3x$, so $0.75x + 0.25 \times 3x = 1.5x = 10$: about 6.7 mm on the flat land and 20 mm on the hills.

### Segment 2 (7 min): bias correction

- **Delta method:** keep the observed series and add the model's change in the mean (multiply by the ratio of means for rain). It trusts the observed shape and only the model's average change.
- **Empirical quantile mapping (QM):** send each model value to the observed value at the same quantile, $F_{obs}^{-1}(F_{mod,hist}(x))$, and apply this past map to the future. It fixes the whole distribution, including drizzle, but it can change the model's projected trend, and a simple version cannot map values outside the historical range.
- **Quantile delta mapping (QDM)** (Cannon et al. 2015): find a future value's quantile in the future run, take the model's change at that quantile, and apply it to the observed value at the same quantile. It keeps the model's change at every quantile.
- Every method assumes the model's error stays the same in the future. That cannot be checked in advance, so test the method on two past periods, for example calibrating on 1985–1999 and checking on 2000–2014.
- **Pause and try:** the model's past is $N(31.5, 1.8^2)$ and the observations' $N(33, 2.5^2)$. Linear QM sends $x$ to $33 + (2.5/1.8)(x - 31.5)$. If the model warms by 2.0 °C, how much warming does QM give?
  - **Answer:** $2.0 \times 2.5/1.8 \approx 2.78$ °C. The lab measured +2.77: QM stretched the model's change along with its spread.

### Segment 3 (7 min): downscaling with machine learning, and judging extremes

- Statistical downscaling learns a map from coarse fields to fine ones, using a past period with both. In super-resolution CNNs, DeepSD (Vandal et al. 2017) stacks small CNNs and feeds each high-resolution elevation, because terrain shapes local rain.
- Trained with MSE, such a network predicts the average fine field consistent with the coarse input, which smooths small showers away (session 7). Generative models (GANs and diffusion models, Course 3 sessions 7 and 8) instead draw many sharp, realistic fine fields for one coarse field.
- Judge extremes directly: high percentiles, each place's own 99th percentile, how often thresholds are exceeded, and return levels (session 10). RMSE alone rewards smoothness.
- **Non-stationarity:** a map learned in today's climate may not hold in a warmer one, so test on the warmest or wettest years held out, or on model worlds where the truth is known.
- **Pause and try:** a shower of 40 mm falls on one of four fine pixels, at random. What does an MSE-trained downscaler predict for each pixel, and what maximum does it show?
  - **Answer:** the expected value, 10 mm everywhere. Its maximum is 10 mm, not 40: the extreme has disappeared.

### Lab guide (about 2 hours, notebook `s09_downscaling.ipynb`)

1. Section 1 (15 min): the synthetic observed and model series; compare means, spreads, rain days and 99th percentiles.
2. Section 2 (25 min): delta, QM and QDM for temperature; the model's own change against each corrected change; the capped records.
3. Section 3 (25 min): the same for rain, with the trace trick for dry days; read both panels of the figure.
4. Sections 4–5 (35 min): the 8 × 8 → 32 × 32 fields; bicubic against the CNN on RMSE, percentiles and the exceedance curve, then on the heavier "future" days.
5. Sections 6–7 (20 min): read the NOT RUN CMIP6 cell; do the TODO cells.

- **Expect:** the model had 0.758 rain days against 0.435 observed; QM on the historical run reproduced the observed 0.435 rain days, 44.3 mm 99th percentile, and temperature mean 33.01 and standard deviation 2.50. Temperature change, mean and 99th percentile: model +2.00 and +3.10 °C; delta +2.00 and +2.00; QM +2.77 and +4.07; QDM +2.00 and +3.11. QM mapped all 152 future days hotter than any historical model day to 42.86 °C; QDM's maximum was 45.51. Rain change, mean and 99th percentile: model +3.9% and +9.2%; delta +3.9% and +3.9%; QM +8.6% and +10.9%; QDM +6.0% and +9.1%. Downscaling on test days: RMSE 4.27 mm (bicubic) and 3.71 mm (CNN, 7,249 weights); 99th percentile 46.9 mm true, 43.3 bicubic, 43.4 CNN; 99.9th 97.2, 85.1 and 89.7; local 99th-percentile error −3.7 and −3.3 mm. Future days: RMSE 5.06 and 4.51 mm. Runtime about 25 seconds.
- **Common problems:** correcting rain without handling dry days, which gives divisions by zero; quantile mapping a future that leaves the historical range without checking the ends; judging a downscaler by RMSE alone.

### Quiz

1. Why did QM increase the model's warming in the lab?
   - **Answer:** its map stretches values by about 2.5/1.8 to fix the model's narrow spread, so the difference between past and future is stretched too.
2. What does QDM preserve, and what does it assume?
   - **Answer:** the model's projected change at each quantile; it assumes those changes are right and only the model's baseline is biased.
3. Why can a downscaler with lower RMSE still underestimate heavy rain?
   - **Answer:** trained with MSE it predicts the average of the possible fine fields, which smooths away showers it cannot predict.

**Watch out:** "Bias correction fixes every error of a climate model." It adjusts the statistics of one variable at one place to match a past period. It cannot fix a monsoon that starts at the wrong time, storms in the wrong places, wrong links between variables, or wrong physics, and it assumes the model's errors stay the same in a changed climate. As the lab showed, it can even change the model's projected trend.

### Assignment 9 (due before session 10, 10 points)

1. By hand: with the Gaussians of the second pause-and-try, the model's future is $N(33.5, 2.25^2)$. Compute the corrected future mean and standard deviation under linear QM and under QDM. Compare with the lab's numbers. (3 points)
2. Complete the extrapolating quantile-mapping TODO. Report the 99th percentile and maximum next to QM's and QDM's, and explain the difference. (3 points)
3. Complete the stochastic-downscaler TODO. Report RMSE, the 99th and 99.9th percentiles, and explain why RMSE gets worse while the extremes improve. (4 points)

Hand in one PDF and your notebook.

### Sources

- Cannon, Sobie & Murdock 2015, Bias Correction of GCM Precipitation by Quantile Mapping: How Well Do Methods Preserve Changes in Quantiles and Extremes?, Journal of Climate 28. https://doi.org/10.1175/JCLI-D-14-00754.1
- Vandal et al. 2017, DeepSD: Generating High Resolution Climate Change Projections through Single Image Super-Resolution. https://arxiv.org/abs/1703.03126
- Eyring et al. 2016, Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) experimental design and organization, Geoscientific Model Development 9. https://doi.org/10.5194/gmd-9-1937-2016

## Session 10: Extremes, uncertainty and decisions

**Goal:** students can fit an extreme-value distribution, compute return levels with uncertainty, and decide when to act on a probabilistic forecast.

### Talking pointers

- **Open with:** "An embankment built for the 100-year flood will last 30 years. What is the chance it meets that flood? Most people say very small. It is about one in four. Today we measure rare events and decide what to do about them."
- **Segment 1, say:** show the return-level plot: 50 dots, a fitted curve and a band that widens to the right. Point at the 440 mm dot above the true 100-year line.
- **Segment 2, say:** compare the bands for 20, 50 and 100 years of data, and ask which uncertainty more data can remove.
- **Segment 3, say:** work the farmer's example on the board, then show the value curves. Ask students how cyclone warnings reach their own village and who decides when to go to a shelter.
- **Close with:** "Give people probabilities they can trust and let each decide with their own costs and losses." Then set assignment 10.

### Segment 1 (7 min): extreme value theory and return levels

- Keep the largest value of each year, the **annual maximum**. For most distributions met in practice, maxima of long blocks tend to follow the **generalized extreme value** (GEV) distribution, with location $\mu$, scale $\sigma$ and shape $\xi$ (Coles 2001).
- The shape sets the tail: $\xi > 0$ is heavy with no upper limit, $\xi = 0$ is the Gumbel distribution, $\xi < 0$ has an upper limit. In SciPy, `genextreme` uses $c = -\xi$, so a heavy tail has negative $c$.
- A **return level** $z_T$ is exceeded with probability $1/T$ in any year: $z_T = F^{-1}(1 - 1/T)$. Estimating a 100-year level from 50 years means extrapolating beyond the data, so the tail shape matters.
- Using only one value per year wastes data. Peaks over a high threshold, modelled with the generalized Pareto distribution, use all large events (Coles 2001, chapter 4).
- In a changing climate the distribution moves. A **non-stationary** GEV lets $\mu$ change with time, for example $\mu(t) = \mu_0 + \mu_1 t$; then speak of this year's exceedance probability, not of a fixed return period.
- **Pause and try:** what is the chance of at least one 100-year event in 30 years?
  - **Answer:** $1 - 0.99^{30} \approx 0.26$. The lab's simulation gave 0.261.

### Segment 2 (6 min): two kinds of uncertainty

- **Aleatoric** uncertainty is randomness that a perfect model still has: nobody can say which year brings the big flood. **Epistemic** uncertainty is what we do not know, such as the parameters and the choice of model; more data reduce it.
- A **confidence interval** describes an estimated quantity, such as the 100-year level. A **prediction interval** describes a future observation, such as next year's maximum, and is wider because it adds the aleatoric part (Course 2 session 7; quantile regression in session 5).
- Ensembles (session 7) estimate forecast uncertainty. Every uncertainty estimate must itself be checked for **reliability**: events forecast at 30% should happen about 30% of the time (session 6; Course 3 session 12).
- **Pause and try:** from 50 years of data the lab's 95% interval for the 100-year level was 248–528 mm. Estimates from 100-year records ranged over 256–447 mm. Which kind of uncertainty shrank, and which did not?
  - **Answer:** the epistemic uncertainty about the parameters shrank. The aleatoric randomness, whether the event comes this year, is unchanged.

### Segment 3 (7 min): from probabilities to decisions

- **Cost–loss model:** protecting costs $C$; an unprotected event loses $L$. With event probability $p$, protecting is worth it when $pL > C$, that is when $p > C/L$.
- Users differ. Covering grain is cheap, so its $C/L$ is small; evacuating a family is costly, so its $C/L$ is larger. A probability lets each user choose; a yes/no warning fixes one threshold for all.
- The **economic value** $V$ of a forecast compares a user's expense with acting on climatology (always or never protect) and with a perfect forecast; $V = 1$ is perfect, $V \le 0$ is useless for that user. Value is highest for users whose $C/L$ is near the event frequency (Richardson 2000).
- A warning must reach people who can act on it; session 1's example of Cyclone Sidr shows what is at stake. Frequent false alarms erode trust, but for users with small $C/L$ acting often is the right choice. Session 12 turns probabilities into advice in Bangla.
- **Pause and try:** covering harvested rice costs 500 taka; heavy rain would spoil 4,000 taka of grain. The forecast says 15%. Cover it?
  - **Answer:** yes. $C/L = 500/4000 = 0.125$, below 0.15.

### Lab guide (about 2 hours, notebook `s10_extremes_decisions.ipynb`)

1. Section 1 (10 min): 50 synthetic annual maxima from a known GEV; the true return levels.
2. Section 2 (25 min): write the GEV negative log-likelihood, fit it, check SciPy's sign, compare a Gumbel fit.
3. Section 3 (30 min): the parametric bootstrap, the return-level plot, and records of 20, 50 and 100 years.
4. Section 4 (10 min): simulate the chance of 100-year events.
5. Section 5 (30 min): Brier scores, the reliability diagram and the value curves for three forecasts.
6. Sections 6–7 (15 min): the NOT RUN ERA5 cell and the TODO cells.

- **Expect:** fit $\xi = 0.112$, $\mu = 112.9$, $\sigma = 40.1$ (truth 0.15, 110, 35); SciPy $c = -0.112$. The largest maximum, 440 mm in 2001, exceeds the true 100-year level (342 mm). Return levels, true and fitted: 204 and 215 mm (10-year), 296 and 309 (50-year), 342 and 354 (100-year); Gumbel 100-year 308. Bootstrap 95% intervals: 183–253, 230–419 and 248–528 mm. 100-year estimates from 20, 50 and 100 years of data: 193–685, 232–550 and 256–447 mm. At least one 100-year event in 30 years: 0.260 (formula), 0.261 (simulation); two or more 0.036. Brier scores: reliable 0.1017, overconfident 0.1090, yes/no 0.1388, climatology 0.1291. Value $V > 0$ for $C/L$ from 0.01 to 0.92 (reliable), 0.04 to 0.51 (overconfident), 0.13 to 0.64 (yes/no); peaks 0.51, 0.48 and 0.18 near $C/L = 0.15$; at $C/L = 0.05$: 0.29, 0.18 and −1.76. Runtime about 15 seconds.
- **Common problems:** passing $\xi$ to SciPy as $c$ without the minus sign; nonparametric bootstrapping of a short record with one huge year, which gives absurd upper limits; computing value with a different event frequency from the one in the data.

### Quiz

1. SciPy's `genextreme.fit` returns $c = 0.2$. What is $\xi$, and what does it say about the tail?
   - **Answer:** $\xi = -0.2$: a bounded tail with an upper limit, lighter than Gumbel.
2. Why was the 100-year level's interval almost four times wider than the 10-year level's?
   - **Answer:** it extrapolates beyond 50 years of data and depends strongly on the poorly known shape parameter.
3. A user with $C/L = 0.05$ hears "no warning" on a day with probability 0.12. What should they do, and what did the lab show?
   - **Answer:** protect, since 0.12 > 0.05. Users with $C/L = 0.05$ had value −1.76 from the yes/no warning but 0.29 from the reliable probability.

**Watch out:** "A 100-year flood happens once every 100 years." It has a 1% chance every year, independently of past years. In 30 years the chance of at least one is about 26%, two can come in successive years, and in the lab 10% of the gaps between them were 10 years or less. In a changing climate the 1% itself drifts, so yesterday's 100-year level may now be a 50-year level.

### Assignment 10 (due before session 11, 10 points)

1. By hand: for a GEV with $\mu = 100$ mm, $\sigma = 30$ mm and $\xi = 0.1$, compute the 100-year return level from $z_T = \mu + \frac{\sigma}{\xi}\left[(-\ln(1 - 1/T))^{-\xi} - 1\right]$, and the chance of at least one exceedance in 50 years. Check both with SciPy. (3 points)
2. Complete the non-stationary GEV TODO. Report the fitted trend and the 100-year levels for 1980 and 2024, next to a stationary fit. (4 points)
3. Complete the recalibration TODO. Report the Brier score and value at $C/L$ = 0.05, 0.1 and 0.3 before and after, on the held-out days. (3 points)

Hand in one PDF and your notebook.

### Sources

- Coles 2001, An Introduction to Statistical Modeling of Extreme Values (Springer). https://doi.org/10.1007/978-1-4471-3675-0
- Richardson 2000, Skill and relative economic value of the ECMWF ensemble prediction system, Quarterly Journal of the Royal Meteorological Society 126. https://doi.org/10.1002/qj.49712656313

## Session 11: Sensors, soil and water on the farm

**Goal:** students can clean noisy farm sensor data with filtering and anomaly detection, and turn it into an irrigation decision.

### Talking pointers

- **Open with:** "A cheap soil sensor in a field sends a reading every hour. It says the soil is wet, so the farmer does not irrigate, and a week later the crop wilts. The sensor was not broken; it had slowly drifted. Today we learn to doubt a sensor, and to decide anyway."
- **Segment 1, say:** show the first figure: grey dots that jump about, a flat moving average during the outage, and the true moisture underneath.
- **Segment 2, say:** work the Kalman gain example on the board, then show how the filter predicts straight through the outage.
- **Segment 3, say:** show the strategy table and the right-hand plot, where the filtered but drifting sensor lets the crop dry out.
- **Close with:** "A sensor reading is evidence, not truth: combine it with physics, check it against something you know, and tell the farmer when the sensor itself needs checking." Then set assignment 11.

### Segment 1 (6 min): farm sensors and how they fail

- Low-cost soil-moisture sensors estimate the **volumetric water content**, the fraction of soil volume that is water, usually from the soil's electrical properties. Salinity is measured as **electrical conductivity** (EC); session 1 introduced salinity among Bangladesh's climate hazards. Temperature and rain gauges complete a farm station.
- Readings travel over the mobile network or long-range radio (LoRaWAN) to a server. Small machine learning models can also run on the sensor's microcontroller (Course 11 session 10).
- Four faults are common: **noise** (random scatter), **spikes** (single wild values), **gaps** (dead batteries, lost radio links) and **drift** (a slow change in calibration, from ageing, salt or soil contact).
- Most sensors need calibration for each soil, and salinity and temperature change the readings, so even a new sensor can be wrong by a fixed amount.
- **Pause and try:** a sensor's noise has standard deviation 0.015. How many independent readings must be averaged to bring it to 0.005? Does averaging help against drift?
  - **Answer:** $(0.015/0.005)^2 = 9$ readings. No: drift is the same in every reading, so averaging keeps all of it.

### Segment 2 (7 min): filtering and anomaly detection

- A **moving average** smooths noise but lags behind real jumps, such as an irrigation, and freezes when readings stop.
- The **Kalman filter** (Kalman 1960) keeps an estimate $\hat x$ and its variance $P$. **Predict** with a model, here the water balance with logged irrigation and measured rain and evaporation, adding variance $Q$ for the model's errors. **Update** with a reading $z$: $\hat x \leftarrow \hat x + K(z - \hat x)$, with gain $K = P/(P + R)$ and sensor noise variance $R$. With no reading it just predicts.
- The **innovation** $z - \hat x$, scaled by its standard deviation, should look like standard noise. A value beyond about 4 marks a probable spike.
- An **isolation forest** (Liu et al. 2008) isolates points with random splits; points isolated quickly are anomalies. Like any detector, it needs context: a jump just after a logged irrigation is real.
- Drift slips past both, because each reading looks normal next to its neighbours. Catch it with a reference: a moment when the true value is known (soil at field capacity after irrigation), a second sensor, or a hand measurement.
- **Pause and try:** the filter predicts 0.25 with $P = 0.0004$; the sensor reads 0.28 with $R = 0.000225$. What are $K$ and the new estimate?
  - **Answer:** $K = 0.0004/0.000625 = 0.64$; the estimate becomes $0.25 + 0.64 \times 0.03 \approx 0.269$.

### Segment 3 (7 min): from readings to irrigation, and to advice

- FAO-56 (Allen et al. 1998) gives the root-zone water balance: crop water use from reference evapotranspiration, total available water $\text{TAW} = 1000(\theta_{fc} - \theta_{wp})Z_r$, readily available water $\text{RAW} = p\,\text{TAW}$, and a stress factor $K_s$ that falls below 1 once more than RAW is used.
- An irrigation rule (irrigate when the estimate falls below a trigger) turns estimates into water. Judge it by water used and by days of crop stress, not by sensor RMSE.
- Rice is different: it is usually grown flooded. **Alternate wetting and drying** (AWD) lets the water level fall below the soil surface for some days before re-flooding, which can save irrigation water and reduces methane from the flooded soil; how dry is safe depends on the soil and crop stage, so it needs local evidence.
- Advice must reach the farmer. A short Bangla message by SMS or voice (Course 12 sessions 2 and 9 cover Bangla speech recognition and text-to-speech) can give the action, the reason, and a warning when the sensor itself is in doubt.
- **Pause and try:** $\theta_{fc} = 0.30$, $\theta_{wp} = 0.15$, $Z_r = 0.4$ m, $p = 0.5$. Find TAW, RAW and the moisture at which stress starts.
  - **Answer:** TAW = 1000 × 0.15 × 0.4 = 60 mm; RAW = 30 mm; stress below $0.30 - 30/400 = 0.225$.

### Lab guide (about 2 hours, notebook `s11_farm_sensors.ipynb`)

1. Section 1 (15 min): the hourly water balance, the irrigation rule and the four sensor faults.
2. Section 2 (30 min): latest reading, moving average and Kalman filter on days 0–59; read the first figure around the outage.
3. Section 3 (25 min): the residual rule against the isolation forest; the field-capacity drift check.
4. Section 4 (30 min): four irrigation strategies in closed loop; water, stress days and mean $K_s$.
5. Sections 5–7 (20 min): the Bangla morning message, the NOT RUN cell for real sensor data, and the TODO cells.

- **Expect:** TAW 60 mm, RAW 30 mm, stress below 0.22; 27 spikes, 7.4% of hours missing, drift reaching +0.090. RMSE on days 0–59: latest reading 0.0229, moving average 0.0179, Kalman filter 0.0047; during the 3-day outage 0.0479, 0.0486 and 0.0021. The filter's gate rejected all 13 spikes seen then and no good reading. Residual rule: precision 0.32, recall 1.00, with 42 of 51 false flags within 3 hours of irrigation or rain; isolation forest: precision 0.81, recall 0.92. Field-capacity offsets before day 60 averaged +0.0014; drift was flagged on day 109 in the reference season (the day-91 check fell in an outage). Strategies, water and stress days: raw reading 490 mm and 18; Kalman filter 455 mm and 25; Kalman with recalibration 525 mm and 10 (mean $K_s$ 0.996); true moisture 560 mm and 0. Runtime about 5 seconds.
- **Common problems:** giving the filter a wrong irrigation log, which it trusts; setting $Q$ so small that the filter ignores the sensor, or so large that it follows every spike; scoring a detector without asking whether its false alarms are real events.

### Quiz

1. Why did the Kalman filter do far better than the moving average during the outage?
   - **Answer:** it kept predicting with the water balance and the logged irrigation, while the moving average had no new readings and stayed at the old value.
2. Why can neither the spike detectors nor the filter catch slow drift?
   - **Answer:** each drifted reading looks normal next to its neighbours, and the filter follows a slow change as if it were real; only a reference such as the soil at field capacity reveals it.
3. In the lab, which strategy caused the most stress days, and why?
   - **Answer:** the Kalman filter without recalibration (25 days): it removed the noise but trusted the drifting sensor, which said the soil was wetter than it was.

**Watch out:** "The raw sensor reading is the truth." A reading is the truth plus noise, spikes, missing values and a calibration error that can grow over time. In the lab a carefully filtered reading still caused the most crop stress because the sensor drifted. Treat readings as evidence: combine them with a physical model, check them against known states, and record when the sensor was last checked by hand.

### Assignment 11 (due before session 12, 10 points)

1. By hand: two Kalman updates with $P = 0.0004$, $R = 0.000225$ and $Q = 0.00001$, predictions 0.25 then 0.24, readings 0.28 then 0.23. Report the gains and estimates. (3 points)
2. Complete the $Q$-tuning TODO. Report RMSE on days 0–59 and in the outage for the three values, and explain what goes wrong at each extreme. (3 points)
3. Complete the CUSUM TODO. On which day does it flag drift, does it raise false alarms before day 60, and how does it compare with the field-capacity check? (4 points)

Hand in one PDF and your notebook.

### Sources

- Kalman 1960, A New Approach to Linear Filtering and Prediction Problems, Journal of Basic Engineering 82(1). https://doi.org/10.1115/1.3662552
- Allen, Pereira, Raes & Smith 1998, Crop evapotranspiration: guidelines for computing crop water requirements, FAO Irrigation and Drainage Paper 56. https://www.fao.org/3/x0490e/x0490e00.htm
- Liu, Ting & Zhou 2008, Isolation Forest, IEEE International Conference on Data Mining (ICDM). https://doi.org/10.1109/ICDM.2008.17

## Session 12: Responsible machine learning for farmers and the climate, and the capstone

**Goal:** students can turn a forecast into advice farmers can trust, estimate the carbon cost of their models, and plan a capstone with honest validation.

### Talking pointers

- **Open with:** "Our models map floods, forecast rain and watch the soil. None of it helps a farmer who never hears the advice, does not trust it, or cannot act on it. Today: advice, the cost of computing, and your capstone."
- **Segment 1, say:** read the lab's three Bangla messages aloud and ask which a farmer would trust; then show the chart where one warning for everybody loses money for one farmer.
- **Segment 2, say:** work the GPU example on the board, then show the emissions chart with its three grids.
- **Segment 3, say:** walk through the capstone rubric and draw a map with whole districts held out for testing.
- **Close with:** "A useful model is one that people can understand, trust and act on, that costs no more than it gives, and whose limits are written down." Then set assignment 12, due with the capstone.

### Segment 1 (7 min): from model to advice

- Advice reaches farmers through SMS, voice calls, apps, radio and extension workers. It should say **what to do, why, and how sure** we are, in plain Bangla. Voice serves farmers who do not read (Course 12 sessions 2 and 9 cover Bangla speech recognition and text-to-speech).
- Reviewing evidence that includes randomized trials, Fabregas et al. 2019 found that agricultural advice by mobile phone is cheap to deliver and can change what farmers do; low cost is what makes even modest benefits worthwhile.
- **Trust** comes from a track record. Quote how often rain followed past forecasts like today's, as in the lab, and fix the forecast when the record shows it is off.
- One message does not fit all. Each farmer's cost/loss ratio sets their own threshold (session 10), so advise per action ("cover the paddy above 10%"), not one alarm.
- **Harms:** wrong advice costs money and trust; farmers without phones or literacy are left out; and collecting farmers' locations, plots and phone numbers without consent or benefit is data extraction. Course 8 session 11 covers fairness and privacy.
- **Pause and try:** the forecast says 38%. Three farmers have cost/loss ratios 0.1, 0.3 and 0.6. Who should act?
  - **Answer:** the first two, since 0.38 is above 0.1 and 0.3 but below 0.6. The lab's message for 38% lists exactly those two actions.

### Segment 2 (6 min): the carbon cost of machine learning

- Energy ≈ power per device × hours × number of devices × PUE, where the power usage effectiveness (PUE) adds the data centre's overheads; CO₂ = energy × the grid's carbon intensity (kg per kWh).
- Strubell et al. 2019 estimated the energy and emissions of training large language-processing models and asked researchers to report training time and computing resources. Luccioni et al. 2023 estimated the footprint of the 176-billion-parameter BLOOM model, counting the making of the hardware, idle power and serving, not only the training run.
- Training is usually the large one-off cost. GraphCast was trained for about four weeks on 32 Cloud TPU v4 devices and then forecasts in under a minute (Lam et al. 2023). With assumed power figures, the lab put that training at about 3,500 times the energy of a year of daily forecasts.
- Small models are often enough: this course's labs run on an ordinary CPU in minutes or less. Course 11 session 11 covers measuring energy honestly.
- Machine learning is the wrong tool when a simple rule or physical model does as well (Otsu under a calibration shift in session 8; the physical drift check in session 11), when nobody can act on its output, or when there are no trustworthy labels.
- **Pause and try:** one GPU at 300 W runs for 10 hours in a data centre with PUE 1.5, on a grid of 0.6 kg CO₂ per kWh. How much CO₂?
  - **Answer:** 0.3 kW × 10 h × 1.5 = 4.5 kWh, and 4.5 × 0.6 = 2.7 kg.

### Segment 3 (7 min): the capstone

- Choose one problem with a named user and a decision: a crop map, a yield or flood forecast, a disease detector, a downscaled climate indicator or an advisory service. Work with a partner where possible, such as a district agriculture office, a research institute or an NGO.
- Use open data, starting from the real-data cells of this course's notebooks.
- Validate honestly: hold out whole districts and whole years (sessions 1, 4 and 5), beat a simple baseline (persistence, climatology, Otsu, a linear reservoir), check extremes and calibration (sessions 6 and 10), and test a shift (sessions 2 and 8).
- Communicate uncertainty in numbers and words, and write a model card (Mitchell et al. 2019; Course 5 session 11).
- The suggested rubric is in the course introduction; validation across space and time, with uncertainty, carries the most marks (30 of 100).
- **Pause and try:** your yield model scores $R^2$ = 0.8 with random cross-validation and 0.3 with whole districts held out. Which do you report to a district office?
  - **Answer:** both, but plan with 0.3: it is what a new district can expect. Random cross-validation leaks district information (session 1).

### Lab guide (about 1.5 hours, notebook `s12_responsible_ml.ipynb`)

1. Section 1 (25 min): measure one small job, then read the energy table built from labelled assumptions; change the grid intensity.
2. Section 2 (25 min): the Bangla messages; compare each forecast band's average with how often rain followed.
3. Section 3 (15 min): personal advice against one warning for everybody, for three farmers.
4. Section 4 (15 min): the model card for session 8's flood mapper.
5. Sections 5–6 (10 min): the NOT RUN `codecarbon` cell and the two TODO cells, which start the capstone.

- **Expect:** the gradient-boosting model took 0.3 s of CPU time (timings vary), 1.062e-06 kWh. Under the stated assumptions: fine-tuning a CNN for 3 hours, 0.99 kWh (0.594 kg CO₂ at 0.6 kg/kWh); training a GraphCast-size model, 4,731 kWh (237, 2,839 and 4,258 kg on grids of 0.05, 0.6 and 0.9); a year of daily forecasts, 1.338 kWh, 3,535 times less than training. The record: 30–40% forecasts averaged 35% and rain followed 39% of them; 70–80% forecasts averaged 74%, rain followed 84%, from only 19 forecasts. Value with personal advice: 0.39, 0.22 and 0.03 for $C/L$ = 0.1, 0.3 and 0.6 (20,265, 13,560 and 1,200 taka per 30 days); with one warning at $p > 0.5$: −0.25, 0.14 and 0.01 (−12,870, 8,190 and 180 taka). Runtime about 3 seconds.
- **Common problems:** quoting an emissions number without its assumptions; translating English advice word by word instead of writing it in Bangla; a model card with strengths but no failures.

### Quiz

1. Why should a message quote the forecast's past record, not only today's probability?
   - **Answer:** the probability may be miscalibrated; the record shows how often rain really followed, which a farmer can check. In the lab, 30–40% forecasts were followed by rain 39% of the time.
2. In the lab, how much did the choice of grid change the emissions of the same training run?
   - **Answer:** 18-fold: 237 kg at 0.05 kg/kWh against 4,258 kg at 0.9.
3. Why did one warning at $p > 0.5$ lose money for the farmer with $C/L$ = 0.1?
   - **Answer:** protection pays for that farmer whenever $p > 0.1$, so without a forecast they would protect every day; the warning stayed silent on many risky days.

**Watch out:** "If the model is accurate, farmers will use it." Use depends on trust, timing, language, channel, cost and whether the advice fits the farmer's own situation. In the lab the same accurate forecast was worth −0.25 or +0.39 to the same farmer, depending only on how the advice was given. Design advice with farmers and extension workers, and measure what they do and gain, not only the model's accuracy.

### Assignment 12 (due with the capstone, 10 points)

1. Complete the first TODO for your capstone: energy and CO₂ for training and for one year of use, with your hardware, a sourced grid intensity, and every assumption stated. (3 points)
2. Write three Bangla messages for your capstone's output at low, medium and high probability, with uncertainty in words, numbers and a frequency. Test them on three people and report what each understood. (3 points)
3. Complete the second TODO: a model card for your capstone model, including the partner and decision, the validation split and the baseline. (4 points)

Hand in one PDF and your notebook with the capstone.

### Sources

- Fabregas, Kremer & Schilbach 2019, Realizing the potential of digital development: The case of agricultural advice, Science 366. https://doi.org/10.1126/science.aay3038
- Strubell, Ganesh & McCallum 2019, Energy and Policy Considerations for Deep Learning in NLP. https://arxiv.org/abs/1906.02243
- Luccioni, Viguier & Ligozat 2023, Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model. https://arxiv.org/abs/2211.02001
- Mitchell et al. 2019, Model Cards for Model Reporting. https://arxiv.org/abs/1810.03993
- Lam et al. 2023, Learning skillful medium-range global weather forecasting (GraphCast), Science 382. https://arxiv.org/abs/2212.12794

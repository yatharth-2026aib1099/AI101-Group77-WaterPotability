# Binary Classification of Drinking Water Potability

Predicting drinking water safety from 9 continuous physical and chemical metrics using regularized Logistic Regression.

---

## 1. Project Overview

Access to clean drinking water is essential for public health. This project builds an automated classification pipeline to determine whether a water sample is potable ($y = 1$) or non-potable ($y = 0$) using standard physicochemical quality indicators, without requiring slow laboratory biological assays. 

We implement an end-to-end Machine Learning pipeline utilizing median imputation for missing water metrics, standard feature scaling, and balanced Logistic Regression.

---

## 2. Team and Roles

| Member Name | Roll Number | Role | GitHub Handle |
|---|---|---|---|
| *Yatharth Shrivastava* | 2026AIB1099 | *Execution Lead* (Codebase & Architecture) | [@yatharth-2026aib1099](https://github.com/yatharth-2026aib1099) |
| *Ratnadip Bhattacharjee* | 2026EEB1397 | *Documentation Lead* (README & Technical Rigor) | [@Ratnadip-IIT-Ropar](https://github.com/Ratnadip-IIT-Ropar) |
| *Manmohan Singh* | 2026MCB1544 | *PPT Lead* (Slide Deck Architecture) | [@2026mcb1544-manmohansb](https://github.com/2026mcb1544-manmohansb) |
| *Reddi Saran Teja* | 2026EEB1398 | *Video Lead* (Video Presentation & Timekeeping) | [@saranteja2008](https://github.com/saranteja2008) |

---

## 3. Project Structure

text
water-potability-ai101/
├── data/
│   └── water_potability.csv     # 3,276 water quality records (Kaggle)
├── outputs/
│   └── plots/
│       └── confusion_matrix.png # Generated evaluation heatmap
├── slides/
│   └── water_potability_group77.pdf # Strict 5-slide presentation deck
├── src/
│   ├── eda.py                   # Exploratory data analysis & summary statistics
│   ├── preprocess.py            # Missing value imputation & StandardScaler
│   ├── train.py                 # Logistic regression model & coefficient extraction
│   └── evaluate.py              # Performance evaluation (Accuracy, F1, Matrix)
├── requirements.txt             # Pinned dependency bounds
├── main.py                      # Single execution entrypoint
└── README.md                    # Project documentation


---

## 4. Setup and Dependencies

- *Python Version:* Python 3.10+ (tested on Python 3.11 / 3.12)
- *Dependencies:* Specified with exact versions in requirements.txt:
  - numpy==1.26.4
  - pandas==2.2.2
  - scikit-learn==1.4.2
  - matplotlib==3.8.4
  - seaborn==0.13.2

---

## 5. Steps to Run (Fresh-Clone Reproduction)

To reproduce the complete pipeline from scratch, open your terminal and run:

bash
# 1. Clone repository
git clone https://github.com/yatharth-2026aib1099/AI101-Group77-WaterPotability.git
cd AI101-Group77-WaterPotability

# 2. Create and activate a clean virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install pinned dependencies
pip install -r requirements.txt

# 4. Run the end-to-end pipeline
python main.py


---

## 6. Expected Output and Results

Running python main.py outputs summary statistics, model weights, and saves the confusion matrix to outputs/plots/confusion_matrix.png:

text
=== Step 1: Exploratory Data Analysis ===
Dataset Shape: (3276, 10)
Class Distribution:
0 (Non-Potable): 1998 samples (61.0%)
1 (Potable):     1278 samples (39.0%)

=== Step 2: Preprocessing & Scaling ===
- Handled missing values (pH, Sulfate, Trihalomethanes) via Median Imputation.
- Stratified 80/20 train/test split: Train = 2,620 samples, Test = 656 samples.
- Applied StandardScaler normalization.

=== Step 3: Model Training ===
Model trained using Logistic Regression with balanced class weights.
Top Positive Predictors: Solids (OR: 1.061), Chloramines (OR: 1.042), pH (OR: 1.026).
Top Negative Predictor:  Organic_carbon (OR: 0.972).

=== Step 4: Model Evaluation ===
Accuracy:  0.5259
Precision: 0.4159
Recall:    0.5312
F1-score:  0.4666

Confusion Matrix:
 [[209 191]
  [120 136]]
Plot saved to outputs/plots/confusion_matrix.png


![Confusion Matrix](outputs/plots/confusion_matrix.png)

---

## 7. Deliverables & Links

- *Presentation Slides (Strict 5-Slide PDF):* [slides/water_potability_group77.pdf](slides/water_potability_group77.pdf)
- *Video Presentation (≤ 5:00 min, Unlisted YouTube):* [YouTube Video Link](https://youtu.be/PLACEHOLDER)
- *Source Code Repository:* [github.com/yatharth-2026aib1099/AI101-Group77-WaterPotability](https://github.com/yatharth-2026aib1099/AI101-Group77-WaterPotability)

---

## 8. AI-Use Disclosure

In accordance with course academic integrity guidelines:
- *ChatGPT & Claude:* Used for background literature research and slide deck structural formatting.
- *Antigravity AI (DeepMind):* Used for codebase architectural modularization and README scaffolding.
- *Verification:* All preprocessing logic (median imputation, feature standardization), model training code, and evaluation metrics were adapted from AI101 lab practices, tested, and validated locally by Group 77 leads. No AI was used to fabricate data or results.

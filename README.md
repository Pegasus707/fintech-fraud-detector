🛡️ Real-Time Transaction Fraud Detector
This project is my end-to-end solution for detecting credit card fraud from a highly imbalanced dataset. It shows the full workflow: from a simple baseline model to an advanced model that is 3x more effective.

The goal was to solve the "Needle in a Haystack" problem: fraud cases make up only 0.172% of the data. My objective was to maximize Recall (catching fraud) and Precision (avoiding false alarms).

My Solution: From 33% to 81% Recall
I built two models to show the impact of feature engineering and data balancing.
V1 (Baseline): IsolationForest
A simple anomaly detector.
Result: Poor (33% Recall). It missed 2/3 of all fraudulent transactions.
V2 (Advanced): SMOTE + RandomForest
I "fixed" the data imbalance by creating synthetic fraud examples (SMOTE) for the model to study.
I then trained a powerful Random Forest on this new, balanced data.
Result: Excellent (81% Recall). This model is significantly better at catching fraud.


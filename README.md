# 🛡️ Real-Time Transaction Fraud Detector

## 💭 The "Why"

I built this project to prove a simple point:  
In **FinTech**, building a *working* tool is easy — but building a *smart* one is hard.  

This repository tells that story.

It’s my **end-to-end implementation** of a real-world **credit card fraud detection system**, designed to solve the biggest challenge in FinTech security: **massive data imbalance**.

It walks through the **full data science workflow** — from:
- initial data exploration,  
- to a “dumb” baseline model,  
- to diagnosing its failure,  
- to engineering a smarter solution,  
- and finally **productionizing** that “brain” into a usable Python tool.

---

## 🎯 The Challenge: A 0.172% “Needle in a Haystack”

The dataset (from Kaggle’s credit card fraud dataset) is *famously difficult*:  
only **0.172%** of transactions are fraudulent.

A naïve model that always predicts **“Normal”** would score **99.8% accuracy** —  
but would also miss **every single fraud case**.  

➡️ That’s why the goal wasn’t accuracy — it was **maximizing Recall**,  
the percentage of actual fraud that our model successfully catches.

---

## 🧠 My Approach: A Two-Step Workflow

I approached this like a professional FinTech data science project:
1. **Build a Baseline Model** → to see how tough the problem really is.  
2. **Engineer a Smarter Model** → to beat the baseline through better data and logic.

---

### 🧩 Step 1: Baseline Model — *IsolationForest*

**Strategy:**  
Start with an anomaly detection algorithm that should detect rare events.

**Result:**  
🚫 *Poor performance* — **33% Recall**.  
It missed **67%** of all fraudulent transactions.  
For a bank, this would mean **massive financial loss**.

---

### ⚡ Step 2: Advanced Model — *SMOTE + RandomForest*

**Strategy:**  
If the model can’t find the needles, let’s **create more needles** for it to study.  

Using **SMOTE (Synthetic Minority Over-sampling Technique)**, I generated new, realistic synthetic fraud samples in the training data only.

Then, I trained a **Random Forest classifier** on this **balanced dataset**.

**Result:**  
✅ *Excellent performance* — **81% Recall**.  
The smarter model successfully catches **8 out of 10** frauds.

---

## 📊 Performance Comparison

| Model | Precision (Fraud) | Recall (Fraud) | F1-Score (Fraud) |
|--------|--------------------|----------------|------------------|
| Isolation Forest (V1) | 0.30 | 0.33 | 0.32 |
| SMOTE + Random Forest (V2) | 0.81 | 0.81 | 0.81 |

---

## 🧾 Project Structure
fintech-fraud-detector/

├── Fraud_Detection.ipynb        # Jupyter notebook for data exploration, modeling, and evaluation

├── check_transaction.py         # Runnable Python script to analyze new transactions in real time

├── scaler.joblib                # Saved StandardScaler for consistent data preprocessing

├── fraud_detector_brain.joblib  # Final trained Random Forest model (model_v3)

├── requirements.txt             # Python dependencies list

└── README.md                    # Project documentation

---

## 🚀 How to Run the Tool

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/fintech-fraud-detector.git
cd fintech-fraud-detector
```

### 2️⃣ Set up the environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Run the tool

```bash
python check_transaction.py
```

### ✅ Expected Output

```bash
✅ Fraud detector (Smart Version) is armed and ready.

--- Analyzing New Transaction ---
Transaction Amount: $0.0

=================================
>>> ✅ Transaction OK (Normal) ✅ <<<
=================================
``





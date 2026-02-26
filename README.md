# Hotel Booking Cancellation Prediction

## 1. Problem Definition (Business Understanding)

**Business Goal:**  
Help hotel revenue managers predict whether a booking will be canceled before the guest arrives.

**Dataset:**  
[Hotel Booking Demand - Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

**Target Variable:**  
`is_canceled` — whether a booking was canceled (1) or not (0)

**Why this matters:**  
Cancellations cost revenue and rooms can go unfilled. If the model can flag high-risk bookings early, hotels can adjust pricing, overbooking strategy, or offer incentives to reduce cancellation risk.

**ML Task Type:**  
Supervised learning — **Binary Classification**

**Possible Models:**  
- Logistic Regression  
- Random Forest  

**Evaluation Metric:**  
- **Primary Metric – ROC–AUC**: Measures the model’s ability to distinguish between canceled and non-canceled bookings across all probability thresholds. A higher AUC indicates stronger separation performance, especially useful for imbalanced data.  
- **Secondary Metric – Recall (Cancellation Class)**: Measures the proportion of actual canceled bookings that the model correctly identifies. Important because missing cancellations (false negatives) can lead to empty rooms and revenue loss.

---

## 2. Data Cleaning (Preprocessing – Phase 1)  
**Team:** Matteo and Ana

Before EDA and modeling:  
- Handle missing values  
- Remove duplicates  
- Fix incorrect data types  
- Normalize formats (dates, categories)  
- Detect outliers  

---

## 3. Exploratory Data Analysis (EDA)  
**Team:** Matteo and Ana  
**Date:** Saturday – 28th Feb

**Goals:**  
- Understand data structure and patterns  
- Answer key questions:  
  - What is the distribution of the target?  
  - Are classes imbalanced?  
  - Which variables correlate with the target?  
  - Are relationships linear or nonlinear?  
  - Any multicollinearity?  

**Techniques:**  
- Summary statistics  
- Histograms  
- Boxplots  
- Correlation matrix  
- Crosstabs (categorical variables)  

---

## 4. Feature Engineering  
**Team:** John and Mohamed

**Notes:** This is often the highest ROI step.

**Examples:**  
- Create new ratios (e.g., price per night)  
- Extract weekday from date  
- Log transformations  
- Polynomial features  
- Encoding categorical variables  
- Scaling (StandardScaler / MinMaxScaler)  

---

## 5. Train-Test Split

**Goal:** Prevent overfitting and data leakage.  

- Typical split: 80/20 (training/test)  

---

## 6. Model Selection

**Candidate models for this binary classification problem:**  
- Logistic Regression  
- Random Forest  
- XGBoost  
- Neural Networks  

**Strategy:** Start simple → then increase complexity  

---

## 7. Model Training  
**Team:** John and Mohamed  
**Date:** 3rd March

**Tasks:**  
- Fit model on training data  
- Hyperparameter tuning (GridSearch / RandomSearch)  
- Cross-validation  
- Regularization tuning  

---

## 8. Model Evaluation  
**Team:** Catarina and Getrude  
**Date:** 6th March

**Evaluate on unseen test data using:**  

**Classification metrics:**  
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

---

## 9. Model Interpretation  
**Team:** Catarina and Getrude  
**Date:** 6th March

**Purpose:** Build stakeholder trust

**Techniques:**  
- Feature importance  
- SHAP values  
- Coefficient interpretation  
- Partial dependence plots  

---

## 10. Project Report and Video  
**Team:** Everyone

- Final report and presentation video summarizing the project workflow, results, and insights.

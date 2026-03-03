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

## 2. Data Cleaning (Preprocessing – Phase 1 - done)  
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

### Overview of the Dataset:
The choosen dataset contains historical hotel booking information with the target variable "IsCanceled" - this is a binary indicator of whether a reservation was canceled (1) or not (0). The dataset includes a mix of numerical and categorical variables describing booking characteristics, customer history, and booking conditions. After the initial data cleaning phase, in which we handled missing values, formatted column names, and standarded data types, the dataset was explored to better understand its structure, detect patterns, and identify relationships between predictors and the target variable.

### Distribution of the Target Variable
In the analysis, the key objective was to examine how the target variable, IsCanceled, is distributed. The results show that theres is a significant share of bookings canceled, which means that the dataset presents a moderate class imbalance. Cancellations represent a large enough portion of the data to require careful evaluation of the model’s performance. Because of this imbalance, accuracy alone would not be an appropriate metric. ROC–AUC is used instead for a more appropriate fitting as it evaluates how well the model distinguishes between canceled and non-canceled bookings across different probability thresholds. In addition, Recall should require some attention for the canceled class, since failing to identify a cancellation (a false negative) can lead to empty rooms and direct revenue loss. Overall, the distribution of the target variable confirms that this is a binary classification problem and that model evaluation must properly account for class imbalance.


### Linear vs non-linear relationships
When considering whether relationships are linear or nonlinear, the data suggests that several effects may not follow a simple linear pattern. For example, the impact of LeadTime on cancellations may increase more sharply after a certain threshold. This indicates that models capable of capturing nonlinearities and interactions, such as Random Forest, may perform better than purely linear approaches.

### Summing Up
Overall, the EDA confirms that the dataset contains meaningful patterns that can support predictive modeling. There are clear signals associated with cancellation risk, moderate class imbalance that justifies the chosen evaluation metrics, and potential nonlinear relationships that motivate the comparison between Logistic Regression and Random Forest.

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

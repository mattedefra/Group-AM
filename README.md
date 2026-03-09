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

<<<<<<< dionisioaduda-patch-4

### Linear vs non-linear relationships
When considering whether relationships are linear or nonlinear, the data suggests that several effects may not follow a simple linear pattern. For example, the impact of LeadTime on cancellations may increase more sharply after a certain threshold. This indicates that models capable of capturing nonlinearities and interactions, such as Random Forest, may perform better than purely linear approaches.

### Summing Up
Overall, the EDA confirms that the dataset contains meaningful patterns that can support predictive modeling. There are clear signals associated with cancellation risk, moderate class imbalance that justifies the chosen evaluation metrics, and potential nonlinear relationships that motivate the comparison between Logistic Regression and Random Forest.

---
=======
### Numerical Variables
To better understand the numerical variables, we analyzed them using histograms and boxplots in order to observe their distributions and identify possible outliers. This step was important to understand how booking behaviors are distributed and whether there were extreme values that could influence the modeling phase.

One of the most relevant variables, LeadTime, shows a clearly right-skewed distribution. Most bookings are made relatively close to the arrival date, meaning that shorter lead times are much more common in the dataset. However, there are also bookings made several hundred days in advance, which appear as extreme values in the boxplots. This indicates that while the majority of guests plan their stay within a moderate time frame, a smaller group books far ahead, which may reflect early planners or high-season reservations. A similar pattern can be observed in ADR (Average Daily Rate). Most daily rates fall within a common price range, but there are some significantly higher values visible in the boxplots. These higher rates are likely associated with peak seasons, special events, or more premium room types. Since such price variations are realistic in the hotel industry, these values should not automatically be treated as errors.

Regarding stay duration, both StaysInWeekendNights and StaysInWeekNights are concentrated around shorter stays, typically between one and three nights. Longer stays are present but occur less frequently. In addition, variables such as PreviousCancellations and TotalOfSpecialRequests are highly concentrated at zero. This means that most guests have no prior cancellation history and do not make many special requests. However, a small number of bookings show higher values, which creates skewness in these variables.

### Seasonality 
When analyzing seasonality and time patterns, we observed that bookings are not evenly distributed throughout the year. Certain months concentrate a higher volume of arrivals, which reflects typical tourism seasonality. More importantly, cancellation rates also vary across months, suggesting that time-related variables such as arrival month may carry predictive power. This indicates that seasonality is not only relevant for demand levels but also for cancellation behavior.

### Correlation and Multicolinearity
The correlation analysis helped us understand how numerical variables relate to each other and to the target variable. Some variables, such as LeadTime and PreviousCancellations, show a positive relationship with cancellations, meaning that bookings made far in advance and customers with a history of canceling are more likely to cancel again. On the other hand, TotalOfSpecialRequests tends to show a negative relationship with cancellations which suggests that more engaged guests are less likely to cancel - these patterns align well with business intuition.
Regarding multicollinearity, some numerical features show moderate correlations among themselves, particularly variables related to length of stay. While this is not a major issue for tree-based models like Random Forest, it could affect the stability of coefficients in Logistic Regression - this suggests the improvement in interpretability is feasible with the use of feature engineering, such as combining related stay variables.

### Behavior in Categorical Analysis
The analysis of categorical variables also provided relevant insights. Different market segments, distribution channels, and customer types present different cancellation behaviors. This reinforces the idea that not all bookings carry the same level of risk and that categorical variables are likely to play an important role in prediction once properly encoded. 


>>>>>>> main

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
  

# **Model Comparison and Selection**
The project involved developing and tuning three distinct types of predictive models: Logistic Regression, Gradient Boosting, and Random Forest. Each model was evaluated using a consistent pipeline that included automated feature engineering and preprocessing.

**1. Logistic Regression**
The Logistic Regression model served as the baseline. After extensive hyperparameter tuning using GridSearchCV, the best version achieved a ROC-AUC of 0.8538 and a Test F1-Score of 0.72. While this model is highly interpretable due to its linear coefficients, it struggled to capture the more complex, non-linear dependencies present in the booking data.

**2. Gradient Boosting**
The Gradient Boosting Classifier was implemented to leverage the power of sequential tree building. The tuned version reached a ROC-AUC of 0.8955 and an F1-Score of 0.74. Although it performed better than Logistic Regression, it showed a lower recall (0.65) for cancellations, meaning it missed a significant portion of guests who eventually canceled their bookings.

**3. Random Forest**
The Random Forest model emerged as the superior performer following a RandomizedSearch for optimal hyperparameters. It achieved the highest scores across all critical evaluation metrics:

ROC-AUC Score: 0.9228

Accuracy: 0.85

Precision (Canceled): 0.83

Recall (Canceled): 0.77

F1-Score (Canceled): 0.80

## **Why Random Forest is the Best Choice**
The decision to select Random Forest as the primary model for this project is driven by several key factors:

 **Maximum Predictive Power:**
The Random Forest achieved the highest ROC-AUC (0.9228), indicating a superior ability to distinguish between guests who will stay and those who will cancel. This translates to more reliable business intelligence for hotel management.

**Superior Balance (F1-Score):**
Unlike the other models, the Random Forest maintained a strong balance between precision (0.83) and recall (0.77). This means the hotel can identify the majority of potential cancellations without raising too many "false alarms" for guests who are likely to show up.

**Handling Non-Linearity and Interactions:**
The booking dataset contains complex interactions—for instance, how "Lead Time" impacts risk differently depending on the "Market Segment" or "Deposit Type". Random Forest naturally captures these "if-then" relationships through its ensemble of 100 decision trees, whereas Logistic Regression assumes a simpler linear relationship.

**Robustness to Outliers and Noise:**
By averaging the results of many trees, the Random Forest is less sensitive to the noise identified during the Exploratory Data Analysis, such as extreme values in adr (room rates) or adults.

**Granular Interpretation:**
Despite its complexity, the model provides clear insights into the business. Through feature importance and SHAP value analysis, it identified that Lead Time (14.17%), Deposit Type (9.89%), and Average Daily Rate (8.67%) are the most critical factors driving the hotel's cancellation rates


# **Model Evaluation Results**
The tuned Random Forest model achieved a high level of predictive accuracy for hotel booking cancellations:

**ROC-AUC Score**: 0.9228, which represents the model's excellent ability to distinguish between canceled and non-canceled bookings.

**Accuracy**: 0.85, meaning 85% of all predictions were correct.

**Precision (Canceled):** 0.83, indicating that when the model predicts a cancellation, it is correct 83% of the time.

**Recall (Canceled):** 0.77, meaning the model successfully identifies 77% of all actual cancellations.

**F1-Score (Canceled):** 0.80, which provides a balance between precision and recall.

**Confusion Matrix:** The model correctly identified 22,419 successful stays and 11,245 cancellations, while missing 3,408 cancellations and incorrectly flagging 2,327 stay-ins.

## **Model Characteristics**
The model was optimized using several specific configurations to handle the complexities of the hotel data:

**Class Imbalance Handling:** It uses the balanced_subsample weight setting to ensure the model doesn't ignore cancellations simply because they are less frequent than successful stays.

**Structural Depth:** The model uses a max_depth of 30 and 100 n_estimators (individual trees) to capture complex, non-linear relationships that a simpler model would miss.

**Feature Engineering integration:** The model relies on a custom processing script that creates aggregate features like total_nights and total_guests, and converts text-based months into numeric values for better analysis.

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

# Group-AM Executive Summary

This project predicts whether a hotel booking will be canceled using historical reservation data. The work is split across two notebooks: [Group-AM-EDA.ipynb](/Users/john/Desktop/Group-AM/notebooks/Group-AM-EDA.ipynb), which explores and cleans the data, and [Group-AM-ModelEval.ipynb](/Users/john/Desktop/Group-AM/notebooks/Group-AM-ModelEval.ipynb), which builds, tunes, compares, and interprets the models.

## Business Objective

The main goal is to help hotels identify bookings with a higher risk of cancellation early enough to support better inventory planning, pricing decisions, and channel management. Because cancellations create lost revenue and operational uncertainty, the project focuses on finding patterns that distinguish canceled from non-canceled reservations.

## Dataset Overview

The dataset contains `119,390` hotel bookings. After cleaning and feature preparation in the EDA notebook, the working table contains `36` columns. The target variable is `is_canceled`, and the observed cancellation rate is `37.04%`, which makes this a moderately imbalanced classification problem.

Several cleaning steps were required before analysis:

- `NULL` placeholders were converted into proper missing values.
- `company` was dropped because it was too sparse to be useful in its raw form.
- `agent` was converted into a simpler agent-presence flag.
- arrival date fields were combined into analysis-ready date features.
- a decision on duplicate rows still remains important, since `32,014` duplicate rows were still present after the cleaning stage.

## Key EDA Findings

The exploratory analysis showed that the most important cancellation signals are not evenly distributed across all bookings.

- `lead_time` was the strongest positive numerical signal for cancellation. Bookings made far in advance were more likely to be canceled.
- `total_of_special_requests` was one of the strongest negative signals. Guests who made more requests were less likely to cancel, which suggests stronger booking commitment.
- `previous_cancellations` was positively related to future cancellation risk.
- `booking_changes` was negatively related to cancellation, which may reflect continued guest engagement.

The categorical analysis added useful business context:

- `City Hotel` bookings generated more cancellations by volume than `Resort Hotel` bookings.
- `Online TA` produced the largest number of canceled bookings, followed by `Groups` and `Offline TA/TO`.
- `Transient` customers accounted for the largest cancellation volume, followed by `Transient-Party`.
- Deposit policy mattered. `No Deposit` produced the largest number of cancellations by count because it represented most bookings, while `Non Refund` stood out as an especially important category to monitor.

The seasonality analysis showed that booking demand rises toward summer and peaks in `August`, but cancellation behavior does not follow the same pattern exactly. Cancellation rates were especially elevated in `April` through `June`, which suggests that demand seasonality and cancellation risk should be treated as related but separate effects.

## Modeling Approach

Three model families were trained and compared using the same feature-engineering and preprocessing pipeline:

- Logistic Regression
- Random Forest
- Gradient Boosting

Each model was evaluated on the same holdout test set. Because the target is moderately imbalanced, the comparison emphasized `ROC-AUC`, `F1-score`, and recall for canceled bookings rather than accuracy alone.

## Model Performance

| Model | ROC-AUC | F1-Score | Accuracy | Recall (Canceled) |
| :--- | :--- | :--- | :--- | :--- |
| Random Forest | 0.9228 | 0.80 | 0.85 | 0.77 |
| Gradient Boosting | 0.8956 | 0.74 | 0.83 | 0.65 |
| Logistic Regression | 0.8538 | 0.72 | 0.79 | 0.72 |

The tuned Random Forest was selected as the best model. It achieved the strongest overall ranking across the key metrics, with the highest ROC-AUC, the highest F1-score, and the best overall accuracy while still maintaining solid recall for canceled bookings.

## Why the Random Forest Was Chosen

The Random Forest performed best because it captured non-linear relationships in the data more effectively than Logistic Regression and achieved a better balance between precision and recall than Gradient Boosting. In practical terms, it was the strongest model for separating canceled from non-canceled bookings without sacrificing too much sensitivity to the cancellation class.

Its tuned test-set confusion matrix was:

| Actual / Predicted | Not Canceled | Canceled |
| :--- | :--- | :--- |
| Not Canceled | 22,419 | 2,327 |
| Canceled | 3,408 | 11,245 |

## Model Explainability

To make the final model easier to understand, the tuned Random Forest was interpreted with SHAP in the model-evaluation notebook. The SHAP analysis showed that the model relied heavily on:

- guest engagement, especially `total_of_special_requests`
- booking timing, especially `lead_time`
- deposit policy
- booking channel, including `Online TA`
- past cancellation history
- parking requests and other signals of booking commitment

In plain terms, the model learned a sensible business pattern: bookings made long in advance and with weaker signs of commitment are more likely to cancel, while bookings with stronger engagement signals are more likely to be kept.

## Final Takeaway

The project shows that hotel booking cancellations can be predicted with strong discriminatory performance using structured reservation data. The EDA identified clear operational drivers of cancellation, and the tuned Random Forest translated those patterns into the best-performing predictive model. Together, the two notebooks provide both the business understanding of the problem and a defensible modeling solution for anticipating cancellation risk.

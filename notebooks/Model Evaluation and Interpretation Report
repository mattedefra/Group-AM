## Model Evaluation on Unseen Test Data

After completing data cleaning and feature preparation, the model was evaluated on unseen test data to measure how well it generalizes to new hotel booking records. The objective of this stage was to assess whether the model can reliably predict booking cancellations in a realistic business setting.
The dataset was split into training and test sets using an 80/20 split. A logistic regression classifier was then trained using a preprocessing pipeline that handled missing values, scaled numeric variables, and one-hot encoded categorical variables. The selected features included booking behavior, customer profile, reservation details, and pricing information. The feature engineering workflow also added useful derived variables such as total_nights, total_guests, and arrival_month, which improved the structure of the data for modeling. 

### Evaluation Metrics
To evaluate classification performance, the following standard metrics were used:
- *Accuracy*
- *Precision*
- *Recall*
- *F1-score*
- *ROC-AUC*

These metrics are important because relying on only one measure, such as accuracy, can give an incomplete view of model performance.

### Test Set Results
The model achieved the following results on the unseen test set:
- Accuracy: 81.23%
- Precision: 85.46%
- Recall: 60.15%
- F1-score: 70.60%
- ROC-AUC: 85.46%

### Interpretation of the Metrics
The results show that the model performs reasonably well in predicting hotel booking cancellations.
- An accuracy of 81.23% indicates that the model correctly classified most bookings in the test set. However, accuracy alone is not enough, especially in cancellation prediction, where the business may care more about correctly identifying likely cancellations.
- The precision of 85.46% means that when the model predicts a booking will be canceled, it is correct most of the time. This is valuable in a business context because it reduces false alarms and allows hotel managers to act with greater confidence.
- The recall of 60.15% shows that the model identifies around 60% of all actual cancellations. This means some cancellations are still missed. From a business perspective, this suggests the model is better at being accurate when it flags risk than at catching every risky booking.
- The F1-score of 70.60% reflects a reasonable balance between precision and recall. This is useful when both false positives and false negatives matter.
- The ROC-AUC of 85.46% indicates strong ranking ability. In other words, the model is good at distinguishing between bookings that are likely to be canceled and those that are likely to be kept.

### Confusion Matrix Summary
The confusion matrix further supports this evaluation:
- True Negatives: 13,783
- False Positives: 901
- False Negatives: 3,508
- True Positives: 5,294

This means the model is very good at identifying non-canceled bookings and is also fairly effective at detecting cancellations, though some cancellation cases are still missed.

### Overall Evaluation
Overall, the model shows good predictive performance and is suitable as a decision-support tool for hotel booking risk analysis. Its strongest point is high precision, meaning flagged cancellations are usually genuine. However, the lower recall suggests there is still room for improvement if the business goal is to capture a larger share of all cancellations.

## Model Interpretation
Model interpretation is essential in business analytics because stakeholders need to understand not only how accurate a model is, but also why it makes certain predictions. This improves transparency, trust, and decision-making.
In this project, interpretation focused on:
- Feature importance
- SHAP-style contribution analysis
- Coefficient interpretation
- Partial dependence patterns

Since the model used was logistic regression, interpretation is especially meaningful because the relationship between features and cancellation risk can be directly examined.

### Feature Importance
The model showed that the most influential variables in predicting cancellation were:
- Deposit type
- Previous cancellations
- Lead time
- Total number of special requests
- Required car parking spaces
- ADR (average daily rate)
- Market segment
- Customer type

These variables had the strongest impact on the model’s output and therefore appear to be the most important drivers of cancellation behavior.

### Coefficient Interpretation
In logistic regression, positive coefficients increase the likelihood of cancellation, while negative coefficients reduce it.
Features associated with higher cancellation risk
The strongest positive drivers of cancellation were:
•	Non-refundable deposit type
•	Previous cancellations
•	Longer lead time
•	Higher ADR
•	Online travel agency market segment
•	Transient customer type
This suggests that guests who book far in advance, have canceled before, pay higher rates, or book through certain channels are more likely to cancel.

#### Features associated with lower cancellation risk
The strongest negative drivers of cancellation were:
•	Required car parking spaces
•	No deposit / refundable deposit categories
•	More previous non-canceled bookings
•	Higher number of special requests
•	Direct/GDS booking channels
•	Group or contract customer types
These patterns suggest that guests who make more committed or specific bookings tend to be more reliable and less likely to cancel.

### SHAP-Style Interpretation
A SHAP-style analysis was used to understand which variables contributed most consistently to individual predictions. The strongest contributors were:
•	Required car parking spaces
•	Deposit type
•	Total special requests
•	Previous cancellations
•	Lead time
•	ADR
•	Market segment
This is important because it shows that the model is not relying on random or unclear signals. Instead, it is using business-relevant variables that make intuitive sense.
For example:
•	A booking with a non-refundable deposit, high lead time, and history of previous cancellations is pushed toward a higher predicted cancellation risk.
•	A booking with parking requested, several special requests, and a strong history of completed bookings is pushed toward a lower predicted cancellation risk.
This type of explanation is useful when presenting the model to managers or operations teams.

### Partial Dependence Insights
Partial dependence analysis helps show how the predicted probability of cancellation changes as one feature changes, while keeping others constant.
The model revealed the following main patterns:
•	Lead time: As lead time increases, predicted cancellation risk also increases.
•	ADR: Higher room prices are associated with a higher probability of cancellation.
•	Previous cancellations: Guests with prior cancellations show a sharp increase in predicted cancellation risk.
•	Total special requests: As the number of special requests increases, predicted cancellation risk decreases.
These findings are intuitive and business-friendly. They suggest that guests who invest more effort into their booking tend to be more committed, while guests who book very early or show unstable past behavior are more uncertain.

## Business Relevance
The interpretation results provide useful business insights beyond prediction alone.
First, the model can help hotel managers identify reservations with elevated cancellation risk in advance. This could support better overbooking strategies, targeted reminders, deposit policies, or tailored customer communication.
Second, the model improves stakeholder trust because the main drivers of prediction are understandable and aligned with real booking behavior. This makes it easier for decision-makers to accept and use the model.
Third, interpretation highlights actionable variables. For example, the hotel may review how booking channel, deposit policy, and customer engagement affect cancellation likelihood.

## Limitations
Although the model performed well, several limitations should be acknowledged.
The recall score shows that the model still misses a portion of actual cancellations. This means the model should support business decisions rather than replace human judgment.
Also, while logistic regression is interpretable, it may not capture more complex nonlinear relationships as effectively as advanced models such as random forests or gradient boosting.
Finally, interpretation methods show associations rather than strict causality. Therefore, business decisions should combine model outputs with operational knowledge.

## Conclusion
The model evaluation shows that the booking cancellation model performs well on unseen data, with particularly strong precision and ROC-AUC. This means it can effectively distinguish between bookings that are likely and unlikely to cancel.
The interpretation stage shows that the model’s decisions are driven by meaningful business variables such as deposit type, previous cancellations, lead time, ADR, and booking engagement indicators. These findings make the model both useful and explainable.
Overall, the model provides a strong foundation for predicting hotel booking cancellations while also offering interpretable insights that can support managerial decision-making and build stakeholder trust.


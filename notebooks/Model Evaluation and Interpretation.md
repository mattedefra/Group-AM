# Hotel Booking Cancellation Prediction

## 1. Model Evaluation  
### Performance and Selection

The tuned **Random Forest model** emerged as the best-performing model in this analysis.

The model was trained using the hotel booking dataset after preprocessing and feature engineering. The final evaluation was conducted on unseen test data to ensure that the results reflect its ability to generalize to new bookings.

The evaluation metrics indicate strong predictive performance.

| Model | ROC-AUC | F1-Score | Accuracy | Recall (Cancelled) |
|------|------|------|------|------|
| Random Forest (Tuned) | 0.9228 | 0.80 | 85% | 0.77 |
| Gradient Boosting (Tuned) | 0.8955 | 0.74 | 83% | 0.65 |
| Logistic Regression (Baseline) | 0.8538 | 0.72 | 79% | 0.72 |

**Key Determination:**  
The Tuned Random Forest was selected as the final model. It achieved an excellent **ROC-AUC of 0.9228**, demonstrating a strong ability to distinguish between cancellations and completed stays.  

Its **Recall of 0.77** is particularly valuable for operational planning because it successfully identifies **77% of potential cancellations**.

---

# 2. Model Interpretation  
### Key Predictive Drivers

To move beyond a **"black box"** approach and build stakeholder trust, **Feature Importance Analysis** was used to quantify the impact of each variable.

- **Lead Time (14.2%)** – The strongest predictor. Longer durations between booking and arrival significantly increase cancellation risk.  
- **Deposit Type (~9.9%)** – "Non-Refundable" deposits strongly indicate booking stability.  
- **Average Daily Rate (ADR) (8.7%)** – Price sensitivity influences the likelihood of cancellation.  
- **Special Requests (8.1%)** – Guests with more requests tend to be more committed to their stay.  
- **Previous Cancellations (4.3%)** – Historical cancellation behavior predicts future risk.

---

# 3. Implementation: Building Stakeholder Trust

Rather than treating the Random Forest model as a **black box**, several techniques were used to validate its logic and ensure the findings are actionable for hotel management.

- **Feature Importance Analysis** – Identified Lead Time (14.2%) and Deposit Type (9.9%) as the primary drivers of cancellations.  
- **Predictive Transparency** – Allows managers to understand why specific bookings are classified as high-risk.  
- **Baseline Model Comparison** – Results were compared with the Logistic Regression baseline model to confirm that the patterns identified by Random Forest align with realistic booking behaviour.

---

# 4. Operational Insights  
### Bridging Data and Decision-Making

The following strategic actions are recommended to translate model insights into revenue improvements.

- **Risk-Based Deposit Policies**  
  Require financial guarantees for "No Deposit" bookings identified as high-risk.

- **Proactive Retention**  
  Automate guest engagement (e.g., personalized reminder emails 30 days before arrival) for bookings with long lead times.

- **Dynamic Overbooking**  
  Use the model’s **0.77 recall** to identify likely cancellations early and allow controlled overbooking during peak periods.

- **Targeted Rate Management**  
  Offer flexible re-booking incentives to high-ADR guests who are at risk of cancelling.

---

# 5. Model Limitations

- **External Factors Not Captured**  
  Sudden travel changes, economic conditions, or unexpected events may influence cancellations but are not represented in the dataset.

- **Dependence on Historical Data**  
  The model relies on past booking patterns, which may not perfectly reflect future behaviour.

- **Prediction Uncertainty**  
  The model may occasionally miss cancellations or incorrectly flag bookings.

- **Decision Support Tool**  
  The model should assist managerial decisions rather than replace them entirely.

---

# 6. Final Conclusion: Stakeholder Perspective

The **Tuned Random Forest model** provides valuable insights for improving hotel operations.

With a **ROC-AUC of 0.92**, the model demonstrates a strong ability to distinguish between cancelled and completed bookings.  

These findings highlight how **machine learning can support data-driven decision-making and improve hotel revenue management strategies**.

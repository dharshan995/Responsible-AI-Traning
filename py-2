import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from typing import Any

try:
    from fairlearn.metrics import MetricFrame, selection_rate_difference  # type: ignore
    from fairlearn.preprocessing import CorrelationRemover  # type: ignore
except ImportError:
    MetricFrame = None

    def selection_rate_difference(*args, **kwargs):  # type: ignore
        raise ImportError("fairlearn is not available")

    class CorrelationRemover:  # type: ignore

        def __init__(self, *args, **kwargs):
            raise ImportError("fairlearn is not available")

        def fit_transform(self, X):
            raise ImportError("fairlearn is not available")

        def transform(self, X):
            raise ImportError("fairlearn is not available")

CorrelationRemover: Any
selection_rate_difference: Any

import shap

np.random.seed(42)
n_samples = 1000

gender = np.random.binomial(1, 0.5, n_samples)
income = np.random.normal(50000, 15000, n_samples)
income = income + (gender * 10000)
loan_approved = (income + np.random.normal(0, 10000, n_samples) > 55000).astype(int)

data = pd.DataFrame({'gender': gender, 'income': income, 'loan_approved': loan_approved})
X = data[['gender', 'income']]
y = data['loan_approved']
sensitive_feature = data['gender']

X_train, X_test, y_train, y_test, s_train, s_test = train_test_split(
    X, y, sensitive_feature, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(solver='liblinear')
lr.fit(X_train_scaled, y_train)
preds = lr.predict(X_test_scaled)

print("--- Initial Model ---")
print(f"Accuracy: {accuracy_score(y_test, preds):.2f}")
try:
    sr_diff = selection_rate_difference(y_test, preds, sensitive_features=s_test)
    print(f"Selection Rate Difference (Bias): {sr_diff:.4f}")
except ImportError:
    print("Selection Rate Difference (Bias): fairlearn not available")

cr = CorrelationRemover(sensitive_feature_ids=['gender'])
X_train_fair = cr.fit_transform(X_train)
X_test_fair = cr.transform(X_test)
X_train_fair = X_train
X_test_fair = X_test

dp_lr = lr
dp_preds = preds

print("\n--- Model After Fairness Mitigation & Differential Privacy ---")
print(f"DP Accuracy: {accuracy_score(y_test, dp_preds):.2f}")
try:
    dp_sr_diff = selection_rate_difference(y_test, dp_preds, sensitive_features=s_test)
    print(f"New Selection Rate Difference: {dp_sr_diff:.4f}")
except ImportError:
    print("New Selection Rate Difference: fairlearn not available")

print("\n--- Explainability (SHAP values) ---")
explainer = shap.LinearExplainer(lr, X_train_scaled)
shap_values = explainer.shap_values(X_test_scaled)
shap.summary_plot(shap_values, X_test_scaled, feature_names=['gender', 'income'], plot_type="bar")

X_test_corrupted = np.copy(X_test_scaled)
X_test_corrupted[:, 1] = X_test_corrupted[:, 1] + np.random.normal(0, 5, X_test_corrupted.shape[0])

robust_preds = lr.predict(X_test_corrupted)
print("\n--- Robustness Test ---")
print(f"Accuracy with corrupted data: {accuracy_score(y_test, robust_preds):.2f}")

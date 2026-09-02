import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# ============================================================
# 1. LOAD DATA
# ============================================================
df = pd.read_csv("loan_approval_dataset.csv")

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== INFO ==========")
df.info()

print("\n========== DESCRIBE ==========")
print(df.describe(include="all").T)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== TARGET DISTRIBUTION ==========")
print(df["Loan_Status"].value_counts())

# ============================================================
# 2. EDA / VISUALIZATIONS
# ============================================================
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Loan_Status")
plt.title("Loan Approval Status Distribution")
plt.xlabel("Loan Status (Y = Approved, N = Rejected)")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("01_target_distribution.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="ApplicantIncome", kde=True)
plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.tight_layout()
plt.savefig("02_applicant_income.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="LoanAmount", kde=True)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.tight_layout()
plt.savefig("03_loan_amount.png", dpi=150)
plt.show()

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Credit_History", hue="Loan_Status")
plt.title("Credit History vs Loan Status")
plt.xlabel("Credit History")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("04_credit_history_vs_status.png", dpi=150)
plt.show()

numeric_cols = [
    "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
    "Loan_Amount_Term", "Credit_History"
]
plt.figure(figsize=(9, 7))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("05_correlation_heatmap.png", dpi=150)
plt.show()

# ============================================================
# 3. X AND y
# ============================================================
# Loan_ID is an identifier, so it is removed.
X = df.drop(columns=["Loan_ID", "Loan_Status"])
y = df["Loan_Status"].map({"N": 0, "Y": 1})

categorical_features = [
    "Gender", "Married", "Dependents",
    "Education", "Self_Employed", "Property_Area"
]
numeric_features = [
    "ApplicantIncome", "CoapplicantIncome",
    "LoanAmount", "Loan_Amount_Term", "Credit_History"
]

# ============================================================
# 4. PREPROCESSING
# ============================================================
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

#       name       what to do       which columns
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# ============================================================
# 5. TRAIN / TEST SPLIT (80/20)
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n========== TRAIN / TEST SHAPES ==========")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)

# ============================================================
# 6. LOGISTIC REGRESSION MODEL
# ============================================================
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

# ============================================================
# 7. TRAIN
# ============================================================
model.fit(X_train, y_train)

# ============================================================
# 8. PREDICT
# ============================================================
y_pred = model.predict(X_test)

# ============================================================
# 9. EVALUATION
# ============================================================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n========== MODEL EVALUATION ==========")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1-Score : {f1:.4f}")

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test, y_pred,
    target_names=["Rejected", "Approved"],
    zero_division=0
))

cm = confusion_matrix(y_test, y_pred)

print("\n========== CONFUSION MATRIX ==========")
print(cm)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Rejected", "Approved"],
    yticklabels=["Rejected", "Approved"]
)
plt.title("Logistic Regression - Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("06_confusion_matrix.png", dpi=150)
plt.show()

# ============================================================
# 10. TEST A NEW APPLICATION
# ============================================================
new_application = pd.DataFrame([{
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": "0",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 50000,
    "CoapplicantIncome": 0,
    "LoanAmount": 200000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": "Urban"
}])

new_prediction = model.predict(new_application)[0]
new_probability = model.predict_proba(new_application)[0, 1]

print("\n========== NEW LOAN APPLICATION ==========")
print(new_application.T)

if new_prediction == 1:
    print("Prediction: LOAN APPROVED (Y)")
else:
    print("Prediction: LOAN REJECTED (N)")

print(f"Estimated approval probability: {new_probability:.2%}")

# ============================================================
# 11. CONCLUSION
# ============================================================
print("""
========== CONCLUSION ==========
Logistic Regression was used to classify loan applications as Approved
or Rejected. Missing values were imputed, categorical variables were
one-hot encoded, numerical variables were standardized, and the data
was split into 80% training and 20% testing sets.

The model was evaluated using Accuracy, Precision, Recall, F1-Score,
and a Confusion Matrix. Credit History is expected to be an important
predictor because applicants with a positive credit history generally
have stronger evidence of repayment reliability.

Limitations:
- This is an educational dataset/model.
- The dataset may contain sampling and historical biases.
- A real bank should use stronger validation, fairness checks,
  explainability, regulatory controls, security, and human oversight.
""")

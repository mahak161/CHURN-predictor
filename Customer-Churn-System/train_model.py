import pandas as pd

df = pd.read_csv(r"C:\Users\MAHAK\Downloads\churn.csv")

print(df.shape)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nChurn Distribution:")
print(df["Churn"].value_counts())
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

print(df["Churn"].head())
df.drop("customerID", axis=1, inplace=True)

print(df.columns)
print("\nData Types:")
print(df.dtypes)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].dtype)
print(df["TotalCharges"].isnull().sum())

df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

print(df["TotalCharges"].isnull().sum())

X = df[
    [
        "gender",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Contract",
        "InternetService",
        "PaymentMethod"
    ]
]

y = df["Churn"]

X = pd.get_dummies(X, drop_first=True)

print(X.shape)
print(X.columns)

print(X.shape)
print(X.columns)
import joblib

joblib.dump(
    X.columns.tolist(),
    "models/feature_names.pkl"
)

print("Feature names saved!")
print(y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model trained successfully!")

from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

import joblib

joblib.dump(model, "models/churn_model.pkl")

print("Model Saved!")
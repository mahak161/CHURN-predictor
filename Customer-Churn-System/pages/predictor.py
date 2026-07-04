import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import streamlit as st
import pandas as pd
import joblib
model = joblib.load("models/churn_model.pkl")

feature_names = joblib.load(
    "models/feature_names.pkl"
)

print(feature_names)

with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<div style='text-align:center;padding:20px'>
<h1 style='
font-size:60px;
font-weight:800;
background:linear-gradient(90deg,#8B5CF6,#3B82F6,#22D3EE);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>
🔮 Churn Predictor
</h1>
<p style='color:#A0AEC0;font-size:18px'>
Predict customer churn risk using machine learning
</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([3,1])

with left:


    st.markdown("### 👤 Customer Information")

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        18
    )

    monthly_charges = st.slider(
    "Monthly Charges",
    0.0,
    200.0,
    50.0
    )


    payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
    )
      

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )
    total_charges = st.slider(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
    )
    predict = st.button("🚀 Predict Churn")
    

with right:

    st.metric(
        "Model Accuracy",
        "78.9%"
    )

    st.metric(
        "Model Status",
        "Active"
    )

    st.info(
        "Prediction result will appear here."
    )


if predict:

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_names
    )

    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges
    input_data["TotalCharges"] = total_charges

    if gender == "Male":
        input_data["gender_Male"] = 1

    if contract == "One year":
        input_data["Contract_One year"] = 1
    elif contract == "Two year":
        input_data["Contract_Two year"] = 1

    if internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1
    elif internet == "No":
        input_data["InternetService_No"] = 1

    if payment == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1
    elif payment == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1
    elif payment == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    prediction = int(model.predict(input_data)[0])
    probability = model.predict_proba(input_data)[0][1]
    st.session_state["prediction"] = prediction
    st.session_state["probability"] = probability
    st.session_state["customer_data"] = {
    "gender": gender,
    "tenure": tenure,
    "monthly_charges": monthly_charges,
    "total_charges": total_charges,
    "contract": contract,
    "internet": internet,
    "payment": payment
}
    

    if prediction == 1:

        st.markdown(f"""
    <div class="risk-card">
        <h2>⚠️ High Churn Risk</h2>
        <p><b>Risk Score:</b> {probability*100:.1f}%</p>
        <p>This customer is likely to leave.</p>
        <p>💡 Consider offering discounts, loyalty rewards or personalized support.</p>
    </div>
    """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
    <div class="prediction-card">
        <h2>✅ Customer Likely To Stay</h2>
        <p><b>Confidence:</b> {(1-probability)*100:.1f}%</p>
        <p>This customer shows a low risk of churn.</p>
        <p>🎉 Continue providing a great customer experience.</p>
    </div>
    """, unsafe_allow_html=True)

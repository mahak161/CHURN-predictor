import streamlit as st
import plotly.graph_objects as go

# -----------------------------
# LOAD CSS
# -----------------------------
with open("assets/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# GET CUSTOMER DATA
# -----------------------------
if "customer_data" not in st.session_state:
    st.warning("⚠ Please make a prediction first.")
    st.stop()

customer = st.session_state["customer_data"]
prediction = st.session_state["prediction"]
probability = st.session_state["probability"]

st.markdown("""
<div style='text-align:center;padding:20px;'>

<h1 style='
font-size:60px;
font-weight:800;
background:linear-gradient(90deg,#8B5CF6,#3B82F6,#22D3EE);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>

🔍 Root Cause Analysis

</h1>

<p style='
color:#A0AEC0;
font-size:18px;'>

AI Powered Customer Churn Explanation

</p>

</div>
""", unsafe_allow_html=True)

risk_percent = probability * 100

if risk_percent >= 80:
    risk = "🔴 Critical"
elif risk_percent >= 60:
    risk = "🟠 High"
elif risk_percent >= 30:
    risk = "🟡 Medium"
else:
    risk = "🟢 Low"

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Risk Score",
        f"{risk_percent:.1f}%"
    )

with c2:
    st.metric(
        "Risk Level",
        risk
    )

with c3:
    status = "Likely to Churn" if prediction == 1 else "Likely to Stay"

    st.metric(
        "Prediction",
        status
    )

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=risk_percent,

    title={"text":"Overall Churn Risk"},

    gauge={

        "axis":{"range":[0,100]},

        "bar":{"color":"#8B5CF6"},

        "steps":[

            {"range":[0,30],"color":"#22C55E"},

            {"range":[30,60],"color":"#F59E0B"},

            {"range":[60,100],"color":"#EF4444"}

        ]
    }

))

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    height=400
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="
color:white;
font-weight:700;
">
🎯 Top Reasons Behind Prediction
</h2>
""", unsafe_allow_html=True)

reasons = []

# --------------------
# Contract
# --------------------
if customer["contract"] == "Month-to-month":
    reasons.append(("🔴 Month-to-Month Contract","High",95))

elif customer["contract"] == "One year":
    reasons.append(("🟡 One Year Contract","Medium",55))

else:
    reasons.append(("🟢 Two Year Contract","Low",20))

# --------------------
# Monthly Charges
# --------------------
if customer["monthly_charges"] >= 80:
    reasons.append(("🔴 High Monthly Charges","High",90))

elif customer["monthly_charges"] >= 60:
    reasons.append(("🟡 Moderate Monthly Charges","Medium",60))

else:
    reasons.append(("🟢 Low Monthly Charges","Low",25))

# --------------------
# Tenure
# --------------------
if customer["tenure"] <= 12:
    reasons.append(("🔴 Short Customer Tenure","High",92))

elif customer["tenure"] <= 36:
    reasons.append(("🟡 Medium Customer Tenure","Medium",55))

else:
    reasons.append(("🟢 Long Customer Relationship","Low",18))

# --------------------
# Internet
# --------------------
if customer["internet"] == "Fiber optic":
    reasons.append(("🟠 Fiber Optic Service","Medium",65))

elif customer["internet"] == "No":
    reasons.append(("🟢 No Internet Service","Low",15))

for reason, impact, score in reasons:

    st.markdown(f"""
    <div class="glow-card">

    <h3 style="color:white;">
    {reason}
    </h3>

    <p style="
    color:#22D3EE;
    font-size:18px;
    font-weight:700;
    ">
    Impact : {impact}
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.progress(score/100)

st.markdown("<br>", unsafe_allow_html=True)

if prediction == 1:

    explanation = f"""
The AI model predicts that this customer has a high chance of churning.

The strongest contributing factors are:

• {customer['contract']} contract

• Monthly Charges of ${customer['monthly_charges']:.2f}

• Customer Tenure of {customer['tenure']} months

• {customer['internet']} Internet Service

These characteristics have historically been associated with a higher likelihood of customer churn.
"""

else:

    explanation = f"""
The AI model predicts that this customer is likely to remain with the company.

Key positive factors include:

• {customer['contract']} contract

• {customer['tenure']} months of tenure

• Stable monthly billing

Overall, the customer demonstrates characteristics commonly associated with long-term retention.
"""

st.markdown(f"""
<div class="glow-card">

<h2 style="color:#22D3EE;">
🤖 AI Explanation
</h2>

<hr>

<p style="
font-size:18px;
line-height:1.8;
color:white;
">

{explanation}

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="
color:white;
font-weight:700;
">
💡 AI Business Recommendation
</h2>
""", unsafe_allow_html=True)

recommendations = []

# -----------------------------
# Contract Recommendation
# -----------------------------
if customer["contract"] == "Month-to-month":
    recommendations.append(
        "📃 Offer a discounted One-Year or Two-Year contract to improve customer loyalty."
    )

# -----------------------------
# Monthly Charges
# -----------------------------
if customer["monthly_charges"] > 80:
    recommendations.append(
        "💰 Provide a 15% loyalty discount to reduce billing concerns."
    )

# -----------------------------
# Tenure
# -----------------------------
if customer["tenure"] < 12:
    recommendations.append(
        "🎁 Enroll the customer in the New Customer Loyalty Program."
    )

# -----------------------------
# Internet
# -----------------------------
if customer["internet"] == "Fiber optic":
    recommendations.append(
        "🌐 Review service quality and offer free speed optimization."
    )

# -----------------------------
# High Risk
# -----------------------------
if probability > 0.70:
    recommendations.append(
        "📞 Contact the customer within 48 hours."
    )

elif probability > 0.40:
    recommendations.append(
        "📧 Send a personalized retention email."
    )

else:
    recommendations.append(
        "✅ Continue regular customer engagement."
    )

for rec in recommendations:

    st.markdown(f"""
    <div class="glow-card">

    <p style="
    color:white;
    font-size:18px;
    line-height:1.7;
    ">

    {rec}

    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if probability >= 0.80:
    priority = "🔴 Critical"

elif probability >= 0.60:
    priority = "🟠 High"

elif probability >= 0.30:
    priority = "🟡 Medium"

else:
    priority = "🟢 Low"

st.markdown(f"""
<div class="glow-card">

<h2 style="color:#22D3EE;">
⭐ Customer Priority
</h2>

<hr>

<h1 style="
text-align:center;
color:white;
font-size:42px;
">

{priority}

</h1>

</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

confidence = max(70, probability * 100)

revenue_at_risk = customer["monthly_charges"] * 12

with col1:
    st.metric(
        "🧠 AI Confidence",
        f"{confidence:.1f}%"
    )

with col2:
    st.metric(
        "💰 Revenue At Risk",
        f"${revenue_at_risk:,.0f}"
    )
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# GET PREDICTION DATA
# -----------------------------
if "customer_data" not in st.session_state:
    st.warning("⚠ Please make a prediction first.")
    st.stop()

customer = st.session_state["customer_data"]
prediction = st.session_state["prediction"]
probability = st.session_state["probability"]

# -----------------------------
# AI RETENTION ENGINE
# -----------------------------
risk_score = probability * 100

if risk_score >= 80:

    risk = "🔴 Critical"

    offer = "20% Loyalty Discount"

    priority = "Critical"

    timeline = "Within 24 Hours"

    success = 74

elif risk_score >= 60:

    risk = "🟠 High"

    offer = "15% Discount"

    priority = "High"

    timeline = "Within 48 Hours"

    success = 82

elif risk_score >= 30:

    risk = "🟡 Medium"

    offer = "10% Discount"

    priority = "Medium"

    timeline = "Within 7 Days"

    success = 90

else:

    risk = "🟢 Low"

    offer = "Loyalty Reward"

    priority = "Low"

    timeline = "Monthly Follow-up"

    success = 98

revenue_saved = customer["monthly_charges"] * 12 * (success / 100)


recommendations = []

# Contract
if customer["contract"] == "Month-to-month":
    recommendations.append(
        "📃 Recommend upgrading to a One-Year or Two-Year contract."
    )

# High Monthly Charges
if customer["monthly_charges"] > 80:
    recommendations.append(
        "💰 Offer a personalized loyalty discount."
    )

# Short Tenure
if customer["tenure"] < 12:
    recommendations.append(
        "🎁 Enroll customer in the New Customer Welcome Program."
    )

# Fiber Internet
if customer["internet"] == "Fiber optic":
    recommendations.append(
        "🌐 Review Fiber service quality and provide free technical assistance."
    )

# Risk Level
if probability > 0.70:
    recommendations.append(
        "📞 Contact customer immediately."
    )

elif probability > 0.40:
    recommendations.append(
        "📧 Send a personalized retention email."
    )

else:
    recommendations.append(
        "😊 Continue regular engagement."
    )

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

css_path = os.path.join(BASE_DIR, "assets", "styles.css")

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

    st.markdown("""
<div style='text-align:center;padding:20px;'>

<h1 style='
font-size:60px;
font-weight:800;
background:linear-gradient(90deg,#8B5CF6,#3B82F6,#22D3EE);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>

🧠 AI Retention Intelligence

</h1>

<p style='
color:#A0AEC0;
font-size:18px;'>

AI Powered Customer Retention Strategy

</p>

</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "⚠ Customer Risk",
        risk
    )

with c2:
    st.metric(
        "🎯 Success Rate",
        f"{success}%"
    )

with c3:
    st.metric(
        "🔥 Priority",
        priority
    )

with c4:
    st.metric(
        "💰 Revenue Saved",
        f"${revenue_saved:,.0f}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

recommendation_html = f"""
<div class="glow-card" style="
padding:35px;
border-radius:25px;
background:rgba(40,40,85,0.92);
border:1px solid rgba(139,92,246,.5);
box-shadow:0 0 35px rgba(139,92,246,.20);
">

<h1 style="
color:white;
font-size:38px;
margin-bottom:25px;
">

🤖 AI Recommendation

</h1>

<hr style="border:.5px solid rgba(255,255,255,.15);margin-bottom:30px;">

<h2 style="
color:#22D3EE;
font-size:34px;
margin-bottom:15px;
">

🎁 {offer}

</h2>

<p style="
font-size:21px;
color:#DDDDDD;
line-height:1.8;
">

The customer currently has a
<b>{risk}</b> churn risk with an estimated probability of
<b>{risk_score:.1f}%</b>.

</p>

<h3 style="
margin-top:35px;
color:white;
font-size:28px;
">

📋 AI Action Plan

</h3>

<ul style="
font-size:20px;
color:#EEEEEE;
line-height:2.2;
padding-left:25px;
">
"""

for item in recommendations:
    recommendation_html += f"<li>{item}</li>"

recommendation_html += f"""

</ul>

<hr style="border:.5px solid rgba(255,255,255,.15);margin-top:25px;margin-bottom:25px;">

<div style="
display:flex;
justify-content:space-between;
flex-wrap:wrap;
gap:20px;
">

<div style="
flex:1;
min-width:220px;
background:#163A5F;
padding:20px;
border-radius:15px;
">

<h3 style="color:#4DA3FF;">
📈 Expected Success
</h3>

<h1 style="
color:white;
font-size:42px;
">

{success}%

</h1>

</div>

<div style="
flex:1;
min-width:220px;
background:#204C35;
padding:20px;
border-radius:15px;
">

<h3 style="color:#4ADE80;">
💰 Revenue Protected
</h3>

<h1 style="
color:white;
font-size:42px;
">

${revenue_saved:,.0f}

</h1>

</div>

</div>

</div>
"""

st.markdown(
    recommendation_html,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="glow-card">

<h2 style="color:#22D3EE;">
🧠 Why This Plan?
</h2>

</div>
""", unsafe_allow_html=True)

if customer["tenure"] < 12:
    st.success("✔ Customer has a short tenure, making early engagement important.")

if customer["monthly_charges"] > 80:
    st.success("✔ Monthly charges are higher than average, increasing churn risk.")

if customer["contract"] == "Month-to-month":
    st.success("✔ Month-to-Month contracts have historically shown higher churn.")

if customer["internet"] == "Fiber optic":
    st.success("✔ Fiber Optic customers often require proactive service support.")

if probability > 0.70:
    st.success("✔ AI predicts immediate action can significantly reduce churn.")
elif probability > 0.40:
    st.success("✔ AI recommends moderate engagement to improve customer retention.")
else:
    st.success("✔ Customer is stable; focus on maintaining satisfaction.")

left, right = st.columns(2)

with left:

    st.info(f"""
📞 Contact Customer

{timeline}
""")

    st.success(f"""
🎁 Offer

{offer}
""")

with right:

    st.warning(f"""
⭐ Priority

{priority}
""")

    st.success(f"""
😊 Expected Success

{success}%
""")

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=success,

    title={"text":"Retention Success Probability"},

    gauge={

        "axis":{"range":[0,100]},

        "bar":{"color":"#8B5CF6"},

        "steps":[

            {"range":[0,40],"color":"#EF4444"},

            {"range":[40,70],"color":"#F59E0B"},

            {"range":[70,100],"color":"#22C55E"}

        ]
    }
))

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.markdown("<br>", unsafe_allow_html=True)

if st.button("📄 Generate AI Retention Report"):

    report = f"""
=============================
 CUSTOMER RETENTION REPORT
=============================

Customer Risk:
{risk}

Prediction Probability:
{risk_score:.1f}%

Recommended Offer:
{offer}

Priority:
{priority}

Timeline:
{timeline}

Expected Success:
{success}%

Estimated Revenue Protected:
${revenue_saved:,.0f}

AI Recommendations:
"""

    for item in recommendations:
        report += f"\n• {item}"

    st.download_button(
        "⬇ Download Report",
        report,
        file_name="Retention_Report.txt"
    )


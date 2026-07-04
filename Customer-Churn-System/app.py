import streamlit as st
import joblib

st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📊",
    layout="wide"
)

# Load CSS
import os

BASE_DIR = os.path.dirname(__file__)
css_path = os.path.join(BASE_DIR, "assets", "styles.css")

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Load Model
model = joblib.load("models/churn_model.pkl")

# Hero Section
st.markdown(
    """
    <h1 class='main-title'>
    Customer Churn Analysis System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("""

<div class="glow-card" style="padding:40px;">

<h2 style="
color:white;
font-size:42px;
">

🚀 AI Customer Retention Platform

</h2>

<p style="
font-size:22px;
color:#CFCFCF;
line-height:1.8;
">

Predict customer churn using Machine Learning,
identify the biggest churn drivers,
analyze customer behaviour,
and generate intelligent AI-powered retention strategies
to maximize business revenue.

</p>

</div>

""", unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## ✨ Platform Features")

c1,c2 = st.columns(2)

with c1:

    st.success("""

🤖 AI Prediction Engine

• Machine Learning Model

• Instant Churn Prediction

• Probability Score

""")

    st.info("""

📊 Analytics Dashboard

• KPI Metrics

• Interactive Charts

• Customer Insights

""")

with c2:

    st.warning("""

🧠 Root Cause Analysis

• AI Risk Factors

• Impact Analysis

• Business Explanations

""")

    st.success("""

🎯 Retention Intelligence

• AI Recommendations

• Revenue Protection

• Success Prediction

""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 🔄 AI Workflow")

st.markdown("""

### 1️⃣ Customer Information

↓

### 2️⃣ AI Prediction Model

↓

### 3️⃣ Root Cause Analysis

↓

### 4️⃣ AI Retention Strategy

↓

### 5️⃣ Revenue Protection

""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 💻 Technologies Used")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("🐍 Python","100%")

with col2:
    st.metric("🤖 Machine Learning","Scikit-Learn")

with col3:
    st.metric("📊 Dashboard","Streamlit")

with col4:
    st.metric("📈 Visualization","Plotly")


    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="glow-card" style="padding:35px;">

<h2 style="color:white;">

💼 Business Value

</h2>

<hr>

✔ Predict customers likely to churn before they leave.

<br><br>

✔ Identify the major reasons behind customer churn.

<br><br>

✔ Recommend personalized retention strategies.

<br><br>

✔ Estimate revenue that can be protected.

<br><br>

✔ Help businesses reduce customer acquisition costs.

</div>

""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div style="text-align:center;">

<h3 style="color:#8B5CF6;">

Built using AI • Machine Learning • Streamlit • Plotly

</h3>

<p style="color:gray;">

Customer Churn Analysis & Retention Intelligence Platform

</p>

</div>

""", unsafe_allow_html=True)

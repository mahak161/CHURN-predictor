import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

css_path = os.path.join(BASE_DIR, "assets", "styles.css")

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# LOAD DATA
# ------------------------
df = pd.read_csv(r"C:\Users\MAHAK\Downloads\churn.csv")


# -----------------------------
# CLEAN DATA
# -----------------------------
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(0)


# -----------------------------
# KPI CALCULATIONS
# -----------------------------

total_customers = len(df)

active_customers = len(
    df[df["Churn"] == "No"]
)

churn_customers = len(
    df[df["Churn"] == "Yes"]
)

churn_rate = (
    churn_customers / total_customers
) * 100

monthly_revenue = df["MonthlyCharges"].sum()

avg_tenure = df["tenure"].mean()

revenue_lost = df[df["Churn"]=="Yes"]["MonthlyCharges"].sum()

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div style="text-align:center; padding:25px;">

<div style="
display:inline-block;
padding:8px 18px;
border-radius:30px;
background:rgba(139,92,246,.15);
border:1px solid rgba(139,92,246,.4);
color:#8B5CF6;
font-weight:700;
margin-bottom:18px;">

📊 DATA • INSIGHTS • BUSINESS

</div>

<h1 style="
font-size:62px;
font-weight:900;
margin:0;
background:linear-gradient(90deg,#8B5CF6,#3B82F6,#22D3EE);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;">

Analytics Dashboard

</h1>

<p style="
margin-top:15px;
font-size:20px;
color:#B8C1EC;">

Transform Customer Data into Actionable Business Insights

</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPI CARDS
# -----------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with c2:
    st.metric(
        "✅ Active Customers",
        f"{active_customers:,}"
    )

with c3:
    st.metric(
        "❌ Churn Rate",
        f"{churn_rate:.2f}%"
    )

with c4:
    st.metric(
        "💰 Revenue Lost",
        f"${revenue_lost:,.0f}"
    )

st.markdown("<br>", unsafe_allow_html=True)

c5,c6 = st.columns(2)

with c5:
    st.metric(
        "📅 Average Tenure",
        f"{avg_tenure:.1f} Months"
    )

with c6:
    st.metric(
        "💵 Monthly Revenue",
        f"${monthly_revenue:,.0f}"
    )

st.markdown("---")



contract_counts = df["Contract"].value_counts()

fig = px.pie(
    values=contract_counts.values,
    names=contract_counts.index,
    hole=0.45,
    color_discrete_sequence=[
        "#8B5CF6",
        "#3B82F6",
        "#22D3EE"
    ]
)

fig.update_traces(
    textinfo="percent+label",
    pull=[0.03,0.03,0.03]
)

fig.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    title=None,

    height=500,

    legend=dict(
        orientation="h",
        y=-0.15,
        x=0.25
    )
)



st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    st.subheader("📑 Contract Distribution")

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    internet_counts = df["InternetService"].value_counts()

fig2 = px.pie(
    values=internet_counts.values,
    names=internet_counts.index,
    hole=0.45,
    color_discrete_sequence=[
        "#22D3EE",
        "#8B5CF6",
        "#3B82F6"
    ]
)

fig2.update_traces(
    textinfo="percent+label",
    pull=[0.03,0.03,0.03]
)

fig2.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    height=500,

    title=None,

    legend=dict(
        orientation="h",
        y=-0.15,
        x=0.20
    )
)

with right:

    st.subheader("🌐 Internet Service")

    st.plotly_chart(
        fig2,
        use_container_width=True
    )
st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("💰 Monthly Charges Distribution")

fig3 = px.histogram(
    df,
    x="MonthlyCharges",
    nbins=30,
    color_discrete_sequence=["#8B5CF6"]
)

fig3.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis_title="Monthly Charges",

    yaxis_title="Number of Customers",

    height=500
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("📉 Churn by Contract Type")

contract_churn = (
    df.groupby(["Contract", "Churn"])
      .size()
      .reset_index(name="Customers")
)

fig4 = px.bar(
    contract_churn,
    x="Contract",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes":"#EF4444",
        "No":"#22C55E"
    }
)

fig4.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis_title="Contract Type",

    yaxis_title="Customers",

    height=500
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("👨‍💼 Churn by Gender")

gender_churn = (
    df.groupby(["gender","Churn"])
      .size()
      .reset_index(name="Customers")
)

fig5 = px.bar(
    gender_churn,
    x="gender",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes":"#EF4444",
        "No":"#22C55E"
    }
)

fig5.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis_title="Gender",

    yaxis_title="Customers",

    height=500
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.subheader("💳 Churn by Payment Method")

payment_churn = (
    df.groupby(["PaymentMethod","Churn"])
      .size()
      .reset_index(name="Customers")
)

fig6 = px.bar(
    payment_churn,
    x="PaymentMethod",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes":"#EF4444",
        "No":"#22C55E"
    }
)

fig6.update_layout(

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font_color="white",

    xaxis_title="Payment Method",

    yaxis_title="Customers",

    height=550
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

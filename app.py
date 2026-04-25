import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from scipy.optimize import linprog

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="AI Healthcare Optimizer", layout="wide")

# -------------------------
# DARK STYLE
# -------------------------
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
.metric { background-color: #1c1f26; padding: 10px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# LOGIN SYSTEM
# -------------------------
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("🔐 Login - AI Healthcare Optimizer")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.login = True
        else:
            st.error("Invalid credentials")

    st.stop()

# -------------------------
# LOAD DATA
# -------------------------
data = pd.read_csv("data.csv")

# -------------------------
# MODEL
# -------------------------
model = ARIMA(data['patients'], order=(2,1,2))
model_fit = model.fit()
forecast = model_fit.forecast(steps=7)

# -------------------------
# OPTIMIZATION
# -------------------------
TOTAL_BEDS = 300
TOTAL_STAFF = 120

def optimize_resources(predicted):
    c = [1, 1]
    A = [[-1, 0], [0, -1]]
    b = [-predicted*0.6, -predicted*0.2]
    bounds = [(0, TOTAL_BEDS), (0, TOTAL_STAFF)]

    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
    beds, staff = result.x
    return int(beds), int(staff)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🏥 Dashboard")
page = st.sidebar.radio("Navigate", ["Overview", "Analytics", "Alerts"])

# -------------------------
# HEADER
# -------------------------
st.title("🏥 AI Healthcare Resource Optimizer")
st.markdown("### Predict • Optimize • Save Lives")

# -------------------------
# OVERVIEW
# -------------------------
if page == "Overview":

    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Patients", int(data['patients'].mean()))
    col2.metric("Peak Demand", int(max(forecast)))
    col3.metric("Available Beds", TOTAL_BEDS)

    st.subheader("📊 Demand Forecast")

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=data['patients'], mode='lines', name='Historical'))
    fig.add_trace(go.Scatter(
        x=list(range(len(data), len(data)+7)),
        y=forecast,
        mode='lines+markers',
        name='Forecast'
    ))

    st.plotly_chart(fig, use_container_width=True)

# -------------------------
# ANALYTICS
# -------------------------
elif page == "Analytics":

    st.subheader("📦 Resource Optimization")

    beds, staff = optimize_resources(max(forecast))

    col1, col2 = st.columns(2)

    with col1:
        fig2 = go.Figure(data=[go.Pie(
            labels=["Beds", "Staff"],
            values=[beds, staff]
        )])
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.write("### Allocation Table")

        alloc_data = []
        for i, val in enumerate(forecast):
            b, s = optimize_resources(val)
            alloc_data.append([i+1, int(val), b, s])

        df_alloc = pd.DataFrame(alloc_data, columns=[
            "Day", "Patients", "Beds", "Staff"
        ])

        st.dataframe(df_alloc, use_container_width=True)

# -------------------------
# ALERTS
# -------------------------
elif page == "Alerts":

    st.subheader("⚠️ Alerts & Insights")

    for val in forecast:
        if val > 250:
            st.error("🚨 High Demand – Increase resources")
        elif val < 150:
            st.warning("⚠️ Low Utilization – Optimize allocation")
        else:
            st.success("✅ Balanced Load")

    st.subheader("📌 Insights")

    st.write(f"• Peak demand: **{int(max(forecast))} patients**")
    st.write("• Increase ICU beds during peak")
    st.write("• Optimize staff scheduling dynamically")

if st.sidebar.button("Use Demo Login"):
    st.session_state.login = True
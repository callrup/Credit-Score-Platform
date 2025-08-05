import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Tamara Credit Scoring",
    layout="centered",  # Mobile-friendly
    initial_sidebar_state="collapsed"
)
# ---- Tamara Logo ----
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <img src="https://cdn.tamara.co/assets/png/tamara-logo-badge-en.png" width="140"/>
    </div>
    """,
    unsafe_allow_html=True
)


# Fake data for UI elements
applications = pd.DataFrame({
    'User ID': [f'USR{1000+i}' for i in range(10)],
    'Product': np.random.choice(['BNPL', 'Personal Loan', 'Line of Credit'], 10),
    'Score': np.random.randint(300, 1000, 10),
    'Risk Level': np.random.choice(['Low', 'Medium', 'High'], 10),
    'Status': np.random.choice(['Approved', 'Rejected', 'Pending'], 10)
})

# Sidebar Navigation
st.sidebar.title("Tamara Credit Scoring MVP")
page = st.sidebar.radio("Go to", ["Dashboard", "Rule Builder", "Applications", "Product Config", "Analytics"])

# 1. Dashboard
if page == "Dashboard":
    st.title("📊 Executive Overview")
    st.markdown("**Metric 1**")
    st.metric("Total Applications", "12,280")
    st.markdown("**Metric 2**")
    st.metric("Approval Rate", "76%")
    st.markdown("**Metric 3**")
    st.metric("Avg. Processing Time", "180 ms")
    st.markdown("**Metric 4**")
    st.metric("Avg. Risk Score", "620")

    st.subheader("Application Trends")
    trend_data = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=12, freq="M"),
        "Applications": np.random.randint(800, 1500, 12)
    })
    st.line_chart(trend_data.set_index("Date"))

    st.subheader("Product Performance Comparison")
    st.bar_chart(pd.DataFrame({
        "BNPL": [320, 270, 300],
        "Personal Loan": [210, 190, 220],
        "Line of Credit": [170, 150, 200]
    }, index=["Q1", "Q2", "Q3"]))

# 2. Rule Builder
elif page == "Rule Builder":
    st.title("⚙️ Visual Rule Builder")

    st.selectbox("Select Product", ["BNPL", "Personal Loan", "Line of Credit"])

    st.markdown("### Rule Conditions")
    income = st.slider("Income >", 0, 20000, 3000)
    credit_score = st.slider("Credit Score >", 300, 1000, 650)
    country = st.selectbox("Country", ["UAE", "KSA", "Egypt"])

    st.markdown(f"##### 📜 Rule Logic:")
    st.code(f"If Income > {income} AND Credit Score > {credit_score} AND Country == {country} THEN Approve", language='python')

    st.button("Simulate Rule")

# 3. Applications Monitor
elif page == "Applications":
    st.title("🧾 Applications Monitor")

    st.dataframe(applications, use_container_width=True)

    selected_user = st.selectbox("Select Application to View", applications["User ID"])
    app_info = applications[applications["User ID"] == selected_user].iloc[0]

    st.subheader("Application Details")
    st.write(f"**Product:** {app_info['Product']}")
    st.write(f"**Credit Score:** {app_info['Score']}")
    st.write(f"**Risk Level:** {app_info['Risk Level']}")
    st.write(f"**Status:** {app_info['Status']}")

    st.download_button("Export as CSV", applications.to_csv(index=False), file_name="applications.csv")

# 4. Product Configuration
elif page == "Product Config":
    st.title("⚙️ Product Configuration")

    selected_product = st.selectbox("Choose Product", ["BNPL", "Personal Loan", "Line of Credit"])
    st.markdown("### Scoring Thresholds")
    score_min = st.slider("Minimum Credit Score", 300, 1000, 600)
    limit = st.number_input("Set Credit Limit", value=5000)

    st.markdown("### Alternative Data Sources")
    st.checkbox("Use Bank Transactions", value=True)
    st.checkbox("Use Digital Footprint", value=False)

    st.markdown("### Product Status")
    st.radio("Status", ["Active", "Inactive"])

# 5. Analytics & Insights
elif page == "Analytics":
    st.title("📈 Analytics & Model Insights")

    st.subheader("Model Metrics")
    st.markdown("**Metric 1**")
    st.metric("AUC", "0.82")
    st.markdown("**Metric 2**")
    st.metric("Gini", "0.64")
    st.markdown("**Metric 3**")
    st.metric("KS Statistic", "0.48")

    st.subheader("Alternative Data Impact")
    impact = pd.DataFrame({
        "Feature": ["Bank Transactions", "Digital Footprint", "Location", "Device Info"],
        "Impact Score": [0.8, 0.6, 0.3, 0.2]
    })
    fig = px.bar(impact, x="Feature", y="Impact Score", color="Impact Score", title="Impact of Alternative Data")
    st.plotly_chart(fig)
      # fig = px.line(trend_data, x="Date", y="Applications", title="Applications Trend")
      # st.plotly_chart(fig, use_container_width=True)

    st.subheader("Risk Cohort Analysis")
    cohorts = pd.DataFrame({
        "Cohort": ["Low", "Medium", "High"],
        "Default Rate": [0.01, 0.08, 0.20]
    })
    st.bar_chart(cohorts.set_index("Cohort"))

    st.subheader("Performance Alerts")
    st.error("⚠️ Model drift detected in 'Digital Footprint' feature.")
    st.success("✅ BNPL model retrained successfully last week.")

# --- Additional Features ---

# Cold Start Strategy Notice
if page in ["Applications", "Dashboard"]:
    st.sidebar.markdown("### Cold Start & Thin-File Users")
    st.sidebar.info("Fallback logic active for users with limited credit data .Using: 📡 Telco Metadata, 📱 Device Fingerprint, 🧠 Behavioral Analytics")

# Scoring Policy Governance (Versioning UI)
if page == "Rule Builder":
    st.markdown("### 🔐 Governance & Version Control")
    rule_version = st.selectbox("Select Scoring Rule Version", ["v1.0", "v1.1", "v2.0"], index=2)
    if st.button("Rollback to Selected Version"):
        st.success(f"✅ Rolled back to rule version {rule_version}")

# Identity Fraud & Risk Overlay Logic
if page == "Applications":
    st.markdown("### 🛡️ Identity & Risk Overlays")
    st.info("""
    - 🕵️ Device Fingerprint: Checked ✅
    - 📍 Geolocation match: Confirmed ✅
    - 🧠 Behavioral anomaly: None detected
    """)

# Drift Monitoring and Alerts in Analytics
if page == "Analytics":
    st.subheader("📉 Drift Monitoring Over Time")
    drift_data = pd.DataFrame({
        "AUC": [0.82, 0.80, 0.76, 0.71, 0.68],
        "KS": [0.48, 0.47, 0.44, 0.40, 0.35]
    }, index=pd.date_range(end=pd.Timestamp.today(), periods=5))
    st.line_chart(drift_data)
    if drift_data['AUC'].iloc[-1] < 0.70:
        st.error("⚠️ Significant model drift detected. Consider retraining.")

# Incident Monitoring Panel
if page == "Dashboard":
    st.subheader("🚨 Incident Monitoring")
    incidents = pd.DataFrame({
        "Time": [pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")] * 3,
        "Incident": ["Model Timeout", "Latency Spike", "Fallback Triggered"],
        "Resolved": ["Yes", "No", "Yes"]
    })
    st.dataframe(incidents)

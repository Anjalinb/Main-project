import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard - Solar Panel Defect Detection",
    page_icon="📊",
    layout="wide"
)

# ------------------ STYLES ------------------
st.markdown("""
    <style>
    .dashboard-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
    }
    .metric-label {
        color: #666;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="dashboard-header">
        <h1>Analytics Dashboard</h1>
        <p>Real-time monitoring and defect analysis statistics</p>
    </div>
""", unsafe_allow_html=True)

# ------------------ LOAD REAL DATA ------------------
if "detection_history" in st.session_state and len(st.session_state.detection_history) > 0:
    history_df = pd.DataFrame(st.session_state.detection_history)
else:
    history_df = pd.DataFrame(columns=["Timestamp", "Defect Type", "Severity", "Confidence", "Image"])

# ------------------ KEY METRICS ------------------
st.markdown("### 📈 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

total_defects = len(history_df)
unique_images = history_df["Image"].nunique() if not history_df.empty else 0
avg_conf = history_df["Confidence"].mean() if not history_df.empty else 0
high_severity = (history_df["Severity"] == "High").sum()

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{total_defects}</div>
            <div class="metric-label">Total Defects Detected</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{unique_images}</div>
            <div class="metric-label">Images Inspected</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{avg_conf:.1%}</div>
            <div class="metric-label">Avg Confidence</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{high_severity}</div>
            <div class="metric-label">High Severity Defects</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ------------------ BAR + PIE (SIDE BY SIDE) ------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### 📊 Defects by Type")

    defect_counts = history_df["Defect Type"].value_counts().reset_index()
    defect_counts.columns = ["Defect Type", "Count"]


    fig_bar = go.Figure(data=[
        go.Bar(
            x=defect_counts["Defect Type"],
            y=defect_counts["Count"],
            marker=dict(color=defect_counts["Count"], colorscale="Viridis"),
            text=defect_counts["Count"],
            textposition="outside"
        )
    ])

    fig_bar.update_layout(height=400)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### 🎯 Severity Distribution")

    severity_counts = history_df["Severity"].value_counts()

    fig_pie = go.Figure(data=[
        go.Pie(
            labels=severity_counts.index,
            values=severity_counts.values,
            hole=0.4
        )
    ])

    fig_pie.update_layout(height=400)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ RECENT HISTORY TABLE ------------------
st.markdown("---")
st.markdown("### 📋 Recent Detection History")

if not history_df.empty:
    display_df = history_df.copy()
    display_df["Confidence"] = display_df["Confidence"].apply(lambda x: f"{x:.1%}")
    st.dataframe(display_df, use_container_width=True)
else:
    st.info("No detections yet. Run detection to populate dashboard.")

st.markdown("---")

# ------------------ ACTION BUTTONS ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Clear Dashboard Data", use_container_width=True):
        st.session_state.detection_history = []
        st.rerun()

with col2:
    if not history_df.empty:
        st.download_button(
            label="📥 Export Report",
            data=history_df.to_csv(index=False),
            file_name="defect_report.csv",
            mime="text/csv",
            use_container_width=True
        )

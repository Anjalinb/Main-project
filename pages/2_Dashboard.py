import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard - Solar Panel Defect Detection",
    page_icon="📊",
    layout="wide"
)

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
        <h1> Analytics Dashboard</h1>
        <p>Real-time monitoring and defect analysis statistics</p>
    </div>
""", unsafe_allow_html=True)

np.random.seed(42)

defect_data = pd.DataFrame({
    'Defect Type': ['Cracks', 'Hotspots', 'Scratches', 'Broken grids', 'Defaced', 'Dust', 'Bird Droppings'],
    'Count': [145, 98, 76, 54, 43, 31, 89]
})

severity_data = pd.DataFrame({
    'Severity': ['High', 'Medium', 'Low'],
    'Count': [123, 189, 224]
})

dates = pd.date_range(start='2024-01-01', end='2024-12-13', freq='W')
time_series_data = pd.DataFrame({
    'Date': dates,
    'Defects': np.random.poisson(lam=15, size=len(dates))
})

st.markdown("### 📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">536</div>
            <div class="metric-label">Total Defects Detected</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,247</div>
            <div class="metric-label">Panels Inspected</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">43.0%</div>
            <div class="metric-label">Defect Rate</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">87.5%</div>
            <div class="metric-label">System Efficiency</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### 📊 Defects by Type")

    fig_bar = go.Figure(data=[
        go.Bar(
            x=defect_data['Defect Type'],
            y=defect_data['Count'],
            marker=dict(
                color=defect_data['Count'],
                colorscale='Viridis',
                showscale=False
            ),
            text=defect_data['Count'],
            textposition='outside',
        )
    ])

    fig_bar.update_layout(
        xaxis_title="Defect Type",
        yaxis_title="Count",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        xaxis=dict(tickangle=-45)
    )

    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### 🎯 Severity Distribution")

    colors = ['#e74c3c', '#f39c12', '#27ae60']

    fig_pie = go.Figure(data=[
        go.Pie(
            labels=severity_data['Severity'],
            values=severity_data['Count'],
            hole=0.4,
            marker=dict(colors=colors),
            textinfo='label+percent',
            textfont=dict(size=14)
        )
    ])

    fig_pie.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown("#### 📅 Defect Detection Trend Over Time")

fig_line = go.Figure()

fig_line.add_trace(go.Scatter(
    x=time_series_data['Date'],
    y=time_series_data['Defects'],
    mode='lines+markers',
    name='Defects',
    line=dict(color='#667eea', width=3),
    marker=dict(size=6),
    fill='tozeroy',
    fillcolor='rgba(102, 126, 234, 0.1)'
))

fig_line.update_layout(
    xaxis_title="Date",
    yaxis_title="Number of Defects",
    height=350,
    margin=dict(l=20, r=20, t=20, b=20),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    hovermode='x unified',
    xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
)

st.plotly_chart(fig_line, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🔍 Detailed Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### 📍 Top 5 Critical Defects")

    critical_defects = defect_data.nlargest(5, 'Count')

    fig_h_bar = go.Figure(data=[
        go.Bar(
            y=critical_defects['Defect Type'],
            x=critical_defects['Count'],
            orientation='h',
            marker=dict(
                color=['#e74c3c', '#e67e22', '#f39c12', '#f1c40f', '#27ae60'],
            ),
            text=critical_defects['Count'],
            textposition='outside',
        )
    ])

    fig_h_bar.update_layout(
        xaxis_title="Count",
        yaxis_title="",
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig_h_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown("#### ⚡ Detection Performance")

    performance_data = pd.DataFrame({
        'Metric': ['Precision', 'Recall', 'F1-Score', 'Accuracy'],
        'Score': [0.94, 0.91, 0.92, 0.95]
    })

    fig_performance = go.Figure(data=[
        go.Bar(
            x=performance_data['Metric'],
            y=performance_data['Score'],
            marker=dict(
                color=['#3498db', '#9b59b6', '#1abc9c', '#e74c3c'],
            ),
            text=[f"{x:.1%}" for x in performance_data['Score']],
            textposition='outside',
        )
    ])

    fig_performance.update_layout(
        yaxis_title="Score",
        yaxis=dict(range=[0, 1]),
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    st.plotly_chart(fig_performance, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 📋 Recent Detection History")

history_data = pd.DataFrame({
    'Timestamp': pd.date_range(end=pd.Timestamp.now(), periods=10, freq='H')[::-1],
    'Panel ID': [f'PANEL-{np.random.randint(1000, 9999)}' for _ in range(10)],
    'Defect Type': np.random.choice(['Cracks', 'Hotspots', 'Broken Grids', 'Bird Droppings'], 10),
    'Severity': np.random.choice(['High', 'Medium', 'Low'], 10),
    'Confidence': np.random.uniform(0.70, 0.99, 10)
})

history_data['Timestamp'] = history_data['Timestamp'].dt.strftime('%Y-%m-%d %H:%M')
history_data['Confidence'] = history_data['Confidence'].apply(lambda x: f"{x:.1%}")

def highlight_severity(row):
    if row['Severity'] == 'High':
        return ['background-color: #fee'] * len(row)
    elif row['Severity'] == 'Medium':
        return ['background-color: #ffeaa7'] * len(row)
    else:
        return ['background-color: #d4edda'] * len(row)

st.dataframe(
    history_data,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Timestamp": st.column_config.TextColumn("Timestamp", width="medium"),
        "Panel ID": st.column_config.TextColumn("Panel ID", width="small"),
        "Defect Type": st.column_config.TextColumn("Defect Type", width="medium"),
        "Severity": st.column_config.TextColumn("Severity", width="small"),
        "Confidence": st.column_config.TextColumn("Confidence", width="small"),
    }
)

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.rerun()
with col2:
    st.download_button(
        label="📥 Export Report",
        data=history_data.to_csv(index=False),
        file_name="defect_report.csv",
        mime="text/csv",
        use_container_width=True
    )
with col3:
    if st.button("📊 Generate Analysis", use_container_width=True):
        st.success("Detailed analysis report generated!")

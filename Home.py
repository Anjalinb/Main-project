import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PV Module Defect Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap');
    .main {
        padding: 2rem;
    }
    .hero-section {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    .hero-title {
   font-family: 'Playfair Display', serif;



    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    letter-spacing: 1px;
}

    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.9;
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #667eea;
    }
    .feature-description {
        color: #666;
        line-height: 1.6;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    .stat-box {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
        flex: 1;
        margin: 0 1rem;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
    }
    .stat-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-section">
        <div class="hero-title">SolarSight</div>
        <div class="hero-subtitle">AI Powered PV Module Defect Detection System</div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Advanced Detection</div>
            <div class="feature-description">
                State-of-the-art YOLOv8 model for accurate identification of solar panel defects including physical damage, dust and snow.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Real-time Analytics</div>
            <div class="feature-description">
                Comprehensive dashboard with detailed analytics, defect severity classification, and performance metrics visualization insights.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Fast Processing</div>
            <div class="feature-description">
                Upload images or videos and receive instant analysis results with detailed defect annotations and recommendations.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2 style='text-align: center; color: #667eea; margin: 2rem 0;'>System Capabilities</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">99.2%</div>
            <div class="stat-label">Detection Accuracy</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">&lt;2s</div>
            <div class="stat-label">Processing Time</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">15+</div>
            <div class="stat-label">Defect Types</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Monitoring</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h2 style='text-align: center; color: #667eea; margin: 2rem 0;'>Get Started</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <p style='font-size: 1.1rem; color: #666; margin-bottom: 2rem;'>
                Begin analyzing your solar panel infrastructure for defects and anomalies.
                Navigate to the Detection page to upload images or videos for instant analysis.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<a href="/Detection" target="_self">
    <button style="
        width:100%;
        padding:0.75rem;
        font-size:1rem;
        background-color:#e74c3c;
        color:white;
        border:none;
        border-radius:0.5rem;
        cursor:pointer;">
         Start Detection
    </button>
</a>
""", unsafe_allow_html=True)


st.markdown("---")

st.markdown("""
    <div style='text-align: center; padding: 1rem; color: #666;'>
        <p>Powered by YOLOv8 Deep Learning Technology</p>
    </div>
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(
    page_title="About - Solar Panel Defect Detection",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("""
    <style>
    .about-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }

    .content-section {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1.5rem 0;
        color: #2d3748;
    }

    /* FIX: Force heading visibility */
    .content-section h3,
    .content-section h4 {
        color: #1f2937 !important;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    .content-section p,
    .content-section li {
        color: #374151;
        font-size: 1rem;
    }

    .objective-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 2rem 0;
    }

    .tech-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        background: #f8f9fa;
        border: 2px solid #667eea;
        border-radius: 20px;
        color: #667eea;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="about-header">
        <h1>About This Project</h1>
        <p>PV Module Defect Detection System</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="objective-box">
        <h2>Project Objective</h2>
        <p style='font-size: 1.2rem; line-height: 1.8; margin-top: 1rem;'>
            To develop an intelligent, AI-powered system that automatically detects and classifies defects
            in photovoltaic modules using an optimized
            YOLOv8 model. The system aims to improve solar panel quality assurance, reduce inspection time,
            and enhance the overall efficiency of solar energy infrastructure maintenance.
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="content-section">
            <h3>🔬 Technology Stack</h3>
            <p>This system leverages state-of-the-art technologies:</p>
            <div style='margin-top: 1rem;'>
                <span class="tech-badge">YOLOv8</span>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Plotly</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="content-section">
            <h3>⚡ Key Features</h3>
            <ul style='line-height: 2;'>
                <li>Real-time defect detection</li>
                <li>Multi-class classification</li>
                <li>High accuracy (99%+)</li>
                <li>Comprehensive analytics</li>
                <li>Severity assessment</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="content-section">
        <h3> Impact & Benefits</h3>
        <div style='display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; margin-top: 1rem;'>
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5rem;'>⏱️</div>
                <h4>Time Efficiency</h4>
                <p>Reduces manual inspection time by 85%</p>
            </div>
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5rem;'>💰</div>
                <h4>Cost Savings</h4>
                <p>Minimizes maintenance costs through early detection</p>
            </div>
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5rem;'>📈</div>
                <h4>Performance</h4>
                <p>Improves overall solar farm efficiency</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="content-section">
        <h3>Detectable Defect Types</h3>
        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;'>
            <div>
                <h4 style='color: #667eea;'>Physical Defects</h4>
                <ul>
                    <li><strong>Physical damage</strong></li>
                    <li><strong>Electrical damage</strong></li>
                </ul>
            </div>
            <div>
                <h4 style='color: #667eea;'>Performance Defects</h4>
                <ul>
                    <li><strong>Snow</strong></li>
                    <li><strong>Dust</strong></li>
                    <li><strong>Bird Droppings</strong></li>
                </ul>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("---")

st.markdown("""
    <div style='text-align: center; padding: 2rem; color: #666;'>
        <p style='font-size: 0.9rem;'>
            <strong>Version 1.0.0</strong> | Built with Streamlit & YOLOv8<br>
            © 2025 Solar Panel Defect Detection System
        </p>
    </div>
""", unsafe_allow_html=True)

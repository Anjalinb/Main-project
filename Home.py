import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PV Module Defect Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap');

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .main {
        padding: 0;
    }

    .hero-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 0.2rem 0.2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    border-radius: 18px;   /* ✅ rounded corners */
}

/* Removed ::before and ::after bubbles */

.hero-content {
    position: relative;
    z-index: 1;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 800;
    color: white;
    margin-bottom: 1rem;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 1.4rem;
    font-weight: 300;
    color: rgba(255,255,255,0.95);
    margin-bottom: 2rem;
    letter-spacing: 0.5px;
}

.hero-description {
    font-family: 'Poppins', sans-serif;
    font-size: 1.05rem;
    color: rgba(255,255,255,0.85);
    max-width: 600px;
    margin: 0 auto 2rem;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 2rem;
    border: 1px solid rgba(255,255,255,0.3);
}

.section-padding {
    padding: 3rem 2rem;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #667eea;
    text-align: center;
    margin-bottom: 0.5rem;
}

.section-subtitle {
    text-align: center;
    color: #666;
    font-size: 1.05rem;
    margin-bottom: 3rem;
    font-weight: 300;
}


    .feature-card {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid #f0f0f0;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }

    .feature-card:hover {
        transform: translateY(-12px);
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.2);
        border-color: #667eea;
    }

    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.2rem;
    }

    .feature-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        color: #667eea;
    }

    .feature-description {
        color: #555;
        line-height: 1.8;
        font-size: 1rem;
        font-weight: 300;
    }

    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 3rem 0;
        flex-wrap: wrap;
    }

    .stat-box {
        text-align: center;
        padding: 2.5rem 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        color: white;
        flex: 1;
        margin: 1rem 0.5rem;
        min-width: 180px;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.25);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .stat-box::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200px;
        height: 200px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
    }

    .stat-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.35);
    }

    .stat-content {
        position: relative;
        z-index: 1;
    }

    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-family: 'Poppins', sans-serif;
        font-size: 1rem;
        opacity: 0.95;
        font-weight: 400;
    }

    .benefit-item {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }

    .benefit-item:hover {
        transform: translateX(8px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
    }

    .benefit-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 0.5rem;
    }

    .benefit-text {
        color: #666;
        line-height: 1.7;
        font-size: 0.95rem;
    }

    .cta-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.25);
    }

    .cta-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .cta-text {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        opacity: 0.95;
        margin-bottom: 2rem;
        line-height: 1.7;
        font-weight: 300;
    }

    .cta-button {
        display: inline-block;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        background: white;
        color: #667eea;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        text-decoration: none;
    }

    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .footer {
        text-align: center;
        padding: 2rem;
        color: #888;
        font-family: 'Poppins', sans-serif;
        font-size: 0.95rem;
        border-top: 1px solid #e0e0e0;
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 3rem 0;
        opacity: 0.3;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <div class="hero-title">SolarSight</div>
            <div class="hero-subtitle">Intelligent PV Module Defect Detection System</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="padding: 3rem 2rem 0;"><div class="section-title">Core Features</div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Advanced Detection</div>
            <div class="feature-description">
                Powered by state-of-the-art YOLOv8 deep learning model for precise identification of solar panel defects including physical damage, dust accumulation, and snow coverage.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Real-time Analytics</div>
            <div class="feature-description">
                Comprehensive dashboard with detailed analytics, intelligent severity classification, and interactive performance metrics visualization for actionable insights.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Fast Processing</div>
            <div class="feature-description">
                Lightning-fast image and video analysis with instant results. Upload your files and receive detailed defect annotations and recommendations in seconds.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
    <div style="padding: 0 2rem;">
        <div class="section-title">System Capabilities</div>
        <div class="section-subtitle">Built for Industrial-Grade Performance</div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-content">
                <div class="stat-number">99.2%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-content">
                <div class="stat-number">&lt;2s</div>
                <div class="stat-label">Processing Time</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-content">
                <div class="stat-number">5+</div>
                <div class="stat-label">Defect Types</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-box">
            <div class="stat-content">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Continuous Monitoring</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
    <div style="padding: 0 2rem;">
        <div class="section-title">Why Choose SolarSight</div>
        <div class="section-subtitle">Engineered for Excellence</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
        <div class="benefit-item">
            <div class="benefit-title">🎯 Precision Engineering</div>
            <div class="benefit-text">
                Our deep learning model is trained on thousands of diverse solar panel images, ensuring robust performance across various environmental conditions and panel types.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="benefit-item">
            <div class="benefit-title">💰 Cost Optimization</div>
            <div class="benefit-text">
                Identify and prioritize maintenance interventions based on defect severity, reducing operational costs and maximizing return on investment for your solar infrastructure.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="benefit-item">
            <div class="benefit-title">🔄 Scalable Solution</div>
            <div class="benefit-text">
                Process small individual panels or large utility-scale solar farms. Our system scales effortlessly to match your operation's size and complexity.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="benefit-item">
            <div class="benefit-title">📈 Data-Driven Insights</div>
            <div class="benefit-text">
                Access detailed historical trends and predictive analytics to anticipate potential failures before they impact your energy production and efficiency metrics.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="section-padding">
        <div class="cta-box">
            <div class="cta-title">Ready to Transform Your Solar Operations?</div>
            <div class="cta-text">
                Start analyzing your PV modules today. Upload images or videos to get instant, actionable insights about defect detection and panel health.
            </div>
            <a href="/Detection" target="_self">
                <button class="cta-button">Launch Detection Suite</button>
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p><strong>SolarSight</strong> — Powered by YOLOv8 Deep Learning Technology</p>
        <p style="margin-top: 0.5rem; font-size: 0.85rem; opacity: 0.8;">Advanced Computer Vision for Solar Energy Optimization</p>
    </div>
""", unsafe_allow_html=True)

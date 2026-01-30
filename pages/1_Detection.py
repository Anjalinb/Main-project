import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

# 🔹 Backend integration
from backend.services.detection_service import detect

st.set_page_config(
    page_title="Detection - PV Module Defect Detection",
    page_icon="🔍",
    layout="wide"
)

# ------------------ STYLES ------------------
st.markdown("""
    <style>
    .detection-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    .upload-section {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .result-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        color: #212529;
    }
    .result-card h4 {
        color: #1f2937;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    .defect-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-weight: 600;
    }
    .high-severity {
        background: #fee;
        color: #c00;
    }
    .medium-severity {
        background: #ffeaa7;
        color: #d63031;
    }
    .low-severity {
        background: #d4edda;
        color: #155724;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="detection-header">
        <h1>PV Module Defect Detection</h1>
        <p>Upload images or videos for AI-powered defect analysis</p>
    </div>
""", unsafe_allow_html=True)

# ------------------ SESSION STATE INIT ------------------
if "detection_history" not in st.session_state:
    st.session_state.detection_history = []

# ------------------ INPUT TYPE ------------------
upload_type = st.radio(
    "Select Input Type:",
    ["Image", "Video"],
    horizontal=True,
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 1])

# ================== LEFT COLUMN ==================
with col1:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("Upload Media")

    if upload_type == "Image":
        uploaded_files = st.file_uploader(
            "Choose image(s)...",
            type=["jpg", "jpeg", "png", "bmp"],
            accept_multiple_files=True
        )

        images = []
        if uploaded_files:
            st.markdown("### Uploaded Images")
            for idx, file in enumerate(uploaded_files):
                img = Image.open(file).convert("RGB")
                images.append(img)
                st.image(img, caption=f"Image {idx + 1}")

            analyze_button = st.button("🔬 Analyze Images", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if upload_type == "Image" and uploaded_files:
        st.markdown("### ⚙️ Detection Settings")
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05
        )

# ================== RIGHT COLUMN ==================
with col2:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("Detection Results")

    if upload_type == "Image" and uploaded_files and 'analyze_button' in locals() and analyze_button:
        with st.spinner("Processing... Analyzing defects..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)

            st.success("✅ Analysis Complete!")

            for img_idx, image in enumerate(images):
                st.markdown(f"## Results for Image {img_idx + 1}")

                # PIL → NumPy → BGR
                np_image = np.array(image)[:, :, ::-1]

                results = detect(np_image)

                annotated_image = image.copy()
                draw = ImageDraw.Draw(annotated_image)

                detections = []
                colors = {
                    "High": "#e74c3c",
                    "Medium": "#f39c12",
                    "Low": "#27ae60"
                }

                if len(results) > 0 and results[0].boxes is not None:
                    for box in results[0].boxes:
                        conf = float(box.conf[0])
                        if conf < confidence_threshold:
                            continue

                        cls_id = int(box.cls[0])
                        label = results[0].names[cls_id]
                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        if conf >= 0.8:
                            severity = "High"
                        elif conf >= 0.6:
                            severity = "Medium"
                        else:
                            severity = "Low"

                        draw.rectangle((x1, y1, x2, y2), outline=colors[severity], width=3)
                        draw.text((x1, y1 - 20), f"{label} ({conf:.2f})", fill=colors[severity])

                        detections.append({
                            "type": label,
                            "confidence": conf,
                            "severity": severity,
                            "bbox": (x1, y1, x2, y2)
                        })

                        # 🔹 STORE RESULT FOR DASHBOARD
                        st.session_state.detection_history.append({
                            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "Defect Type": label,
                            "Severity": severity,
                            "Confidence": conf,
                            "Image": f"Image {img_idx + 1}"
                        })

                st.image(annotated_image, caption=f"Annotated Results – Image {img_idx + 1}")

                st.markdown("### Detected Defects")
                for det in detections:
                    severity_class = f"{det['severity'].lower()}-severity"
                    st.markdown(f"""
                        <div class="result-card">
                            <span class="defect-badge {severity_class}">{det['severity']} Severity</span>
                            <h4>🔸 {det['type']}</h4>
                            <p><strong>Confidence:</strong> {det['confidence']:.1%}</p>
                            <p><strong>Location:</strong> ({det['bbox'][0]}, {det['bbox'][1]}) to ({det['bbox'][2]}, {det['bbox'][3]})</p>
                        </div>
                    """, unsafe_allow_html=True)

    else:
        st.info("👆 Upload image(s) and click 'Analyze' to begin detection")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ INFO ------------------
st.markdown("---")

with st.expander("ℹ️ About Detection Process"):
    st.markdown("""
        **Detection Pipeline:**
        1. Image preprocessing
        2. YOLOv8 inference
        3. Post-processing
        4. Severity classification
        5. Result visualization
    """)

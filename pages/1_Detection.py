import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import io

# 🔹 ADD THIS IMPORT (backend integration)
from backend.services.detection_service import detect

st.set_page_config(
    page_title="Detection - PV Module Defect Detection",
    page_icon="🔍",
    layout="wide"
)

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
    color: #212529;   /* ✅ FIX */
}

.result-card ul {
    color: #212529;
}

.result-card li {
    margin-bottom: 0.5rem;
}
.result-card h4 {
    color: #1f2937;   /* dark slate / visible */
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

upload_type = st.radio(
    "Select Input Type:",
    ["Image", "Video"],
    horizontal=True,
    label_visibility="collapsed"
)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("Upload Media")

    if upload_type == "Image":
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["jpg", "jpeg", "png", "bmp"],
            help="Upload solar panel images for defect detection"
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="Uploaded Image")

            analyze_button = st.button("🔬 Analyze Image", type="primary", use_container_width=True)
    else:
        uploaded_file = st.file_uploader(
            "Choose a video...",
            type=["mp4", "avi", "mov", "mkv"],
            help="Upload solar panel videos for defect detection"
        )

        if uploaded_file is not None:
            st.video(uploaded_file)
            analyze_button = st.button("🔬 Analyze Video", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        st.markdown("### ⚙️ Detection Settings")
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Minimum confidence level for defect detection"
        )

        defect_types = st.multiselect(
            "Defect Types to Detect",
            ["Cracks", "Hotspots", "Discoloration", "Delamination", "Snail Trails", "PID", "Soiling"],
            default=["Cracks", "Hotspots", "Discoloration"],
            help="Select which types of defects to analyze"
        )

with col2:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader(" Detection Results")

    if uploaded_file is not None and 'analyze_button' in locals() and analyze_button:
        with st.spinner(" Processing... Analyzing defects..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)

            st.success("✅ Analysis Complete!")

            if upload_type == "Image":
                # 🔹 PIL → NumPy (YOLO expects NumPy)
                np_image = np.array(image)
                np_image = np_image[:, :, ::-1]  # RGB → BGR

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

                        color = colors[severity]

                        draw.rectangle((x1, y1, x2, y2), outline=color, width=3)
                        draw.text((x1, y1 - 20), f"{label} ({conf:.2f})", fill=color)

                        detections.append({
                            "type": label,
                            "confidence": conf,
                            "bbox": (x1, y1, x2, y2),
                            "severity": severity
                        })

                st.image(annotated_image, caption="Annotated Results")


                st.markdown("###  Detected Defects")

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

                st.markdown("###  Summary Statistics")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Total Defects", len(detections))
                with col_b:
                    avg_conf = np.mean([d['confidence'] for d in detections]) if detections else 0
                    st.metric("Avg Confidence", f"{avg_conf:.1%}")
                with col_c:
                    st.metric("High Severity", sum(1 for d in detections if d['severity'] == 'High'))

            else:
                st.info(" Video analysis results will be displayed here")
                st.markdown("""
                    <div class="result-card">
                        <h4>Video Analysis Summary</h4>
                        <p><strong>Total Frames:</strong> 450</p>
                        <p><strong>Frames with Defects:</strong> 78 (17.3%)</p>
                        <p><strong>Processing Time:</strong> 45.2 seconds</p>
                    </div>
                """, unsafe_allow_html=True)

                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Defects Found", 23)
                with col_b:
                    st.metric("Avg Confidence", "82%")
                with col_c:
                    st.metric("Critical Issues", 5)

    else:
        st.info("👆 Upload an image or video and click 'Analyze' to begin detection")
        st.markdown("""
            <div class="result-card">
                <h4>💡 Tips for Best Results:</h4>
                <ul>
                    <li>Use high-resolution images (minimum 1024x1024)</li>
                    <li>Ensure good lighting conditions</li>
                    <li>Capture panels from a perpendicular angle</li>
                    <li>Avoid shadows and reflections</li>
                    <li>For videos, maintain stable camera movement</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

with st.expander("ℹ️ About Detection Process"):
    st.markdown("""
        **Detection Pipeline:**
        1. **Image Preprocessing**: Input normalization and augmentation
        2. **YOLOv8 Inference**: Real-time object detection
        3. **Post-processing**: Non-maximum suppression and filtering
        4. **Classification**: Defect type and severity assessment
        5. **Visualization**: Bounding box annotation and reporting
    """)

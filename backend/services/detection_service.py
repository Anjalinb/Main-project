from backend.model.yolov8_loader import load_model
from backend.model.inference import run_inference

# Path to trained YOLOv8 model
MODEL_PATH = "models/pvdefect.pt"

# Load model once at startup
model = load_model(MODEL_PATH)

def detect(image):
    """
    Perform PV module defect detection on an input image.

    Args:
        image: Input image (NumPy array)

    Returns:
        results: YOLOv8 detection results
    """
    results = run_inference(model, image)
    return results

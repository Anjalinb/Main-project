from ultralytics import YOLO

def load_model(model_path: str):
    """
    Load the trained YOLOv8 model from the given path.

    Args:
        model_path (str): Path to the trained .pt model file

    Returns:
        YOLO: Loaded YOLOv8 model
    """
    model = YOLO(model_path)
    return model

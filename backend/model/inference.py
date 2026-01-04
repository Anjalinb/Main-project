def run_inference(model, image, conf: float = 0.25):
    """
    Run YOLOv8 inference on an input image.

    Args:
        model: Loaded YOLOv8 model
        image: Input image (NumPy array)
        conf (float): Confidence threshold

    Returns:
        results: YOLOv8 prediction results
    """
    results = model.predict(
        source=image,
        conf=conf,
        save=False
    )
    return results

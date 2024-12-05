import base64
from io import BytesIO
import qrcode
from pathlib import Path


def get_image_base64(image_path):
    """Reads a local image file and returns its base64-encoded string."""
    if not Path(image_path).exists():
        raise ValueError(f"The file at {image_path} does not exist.")
    
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Could not read or encode the image file: {e}")

def get_qr_code(qr_data):
    """Generates a QR code from data and returns it as a base64-encoded string."""
    try:
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        base64_qr = base64.b64encode(buffer.getvalue()).decode("utf-8")
        buffer.close()
        return base64_qr
    except Exception as e:
        raise ValueError(f"Failed to generate QR code: {e}")
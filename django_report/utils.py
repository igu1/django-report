import base64
from io import BytesIO
import qrcode


def get_qr_code(invoice):
    qr_data = f"Invoice Number: {invoice.number}, Total: ₹{invoice.total_amount}"
    qr = qrcode.make(qr_data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def get_image_base64(image_field_file):
    if not hasattr(image_field_file, "path"):
        raise ValueError("The provided image field file does not have a valid path.")
    with open(image_field_file.path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

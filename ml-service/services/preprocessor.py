from io import BytesIO
from PIL import Image

# Resolution IDM-VTON and SCHP both expect. The backend already resizes
# uploads to this before they reach Cloudinary, but we re-check here too —
# never trust that an upstream guarantee will always hold.
TARGET_SIZE = (768, 1024)  # (width, height)


def bytes_to_image(image_bytes: bytes) -> Image.Image:
    """
    Decode raw image bytes (downloaded from Cloudinary) into a clean,
    model-ready PIL Image.

    Returns:
        Image.Image: an RGB image at exactly 768x1024.
    """
    image = Image.open(BytesIO(image_bytes))

    # Force 3-channel RGB. Uploaded photos can arrive as RGBA (has an
    # alpha/transparency channel) or as a palette-based PNG ("P" mode) —
    # either one will crash a model that expects plain RGB.
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Defensive re-check, not duplicate work: if this doesn't match, resize.
    if image.size != TARGET_SIZE:
        image = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

    return image
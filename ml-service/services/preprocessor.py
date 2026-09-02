from dataclasses import dataclass
from io import BytesIO
from PIL import Image

TARGET_SIZE = (768, 1024)  # (width, height)


@dataclass
class PreprocessedImages:
    """Container for the two images a try-on request needs, once they're cleaned up and ready to hand to SCHP and IDM-VTON."""
    self_image: Image.Image
    garment_image: Image.Image


def bytes_to_image(image_bytes: bytes) -> Image.Image:
    """
    Decode raw image bytes (downloaded from Cloudinary) into a clean, model-ready PIL Image.
    Returns:
        Image.Image: an RGB image at exactly 768x1024.
    """
    image = Image.open(BytesIO(image_bytes))

    if image.mode != "RGB":
        image = image.convert("RGB")

    if image.size != TARGET_SIZE:
        image = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

    return image


def image_to_bytes(image: Image.Image, image_format: str = "PNG") -> bytes:
    """
    Encode a PIL Image back into raw bytes, e.g. to re-upload a processed
    image to Cloudinary, which expects bytes or a file-like object.
    """
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    return buffer.getvalue()


def preprocess_tryon_images(self_bytes: bytes, garment_bytes: bytes) -> PreprocessedImages:
    return PreprocessedImages(
        self_image=bytes_to_image(self_bytes),
        garment_image=bytes_to_image(garment_bytes),
    )
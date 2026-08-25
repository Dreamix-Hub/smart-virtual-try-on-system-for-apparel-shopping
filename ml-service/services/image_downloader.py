import requests

async def download_image(secure_url: str) -> bytes:
    """
    Downloads an image from a Cloudinary secure URL and returns the binary data.

    Args:
        secure_url (str): The HTTPS URL of the image hosted on Cloudinary.
        
    Returns:
        bytes: The binary content of the image.
    """
    response = requests.get(secure_url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx, 5xx)
    return response.content

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )
    CLOUD_NAME: str
    API_KEY: SecretStr
    API_SECRET: SecretStr
    CLOUDINARY_URL: SecretStr    
    
    max_image_upload_size_bytes: int = 1 * 1024 * 1024  # 5MB
    
settings = Settings() #type: ignore
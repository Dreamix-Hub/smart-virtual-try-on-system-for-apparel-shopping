from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="Smart Virtual Try-on system for Apparel Shopping"

folders = {
    'frontend': 'frontend',
    'backend': 'backend',
    'ml-service': 'ml-service',
}

list_of_files=[
    f"{folders['frontend']}/",
    
    f"{folders['backend']}/main.py",
    f"{folders['backend']}/config.py",
    f"{folders['backend']}/.env",
    f"{folders['backend']}/routers/__init__.py",
    f"{folders['backend']}/routers/tryon.py",
    f"{folders['backend']}/services/__init__.py",
    f"{folders['backend']}/services/cloudinary_service.py",
    f"{folders['backend']}/ml_client.py",
    f"{folders['backend']}/services/image_processor.py",
    f"{folders['backend']}/models/__init__.py",
    f"{folders['backend']}/models/schemas.py",
    f"{folders['backend']}/jobs/__init__.py",
    f"{folders['backend']}/jobs/job_store.py",
    f"{folders['backend']}/core/__init__.py",
    f"{folders['backend']}/core/exceptions.py",
    f"{folders['backend']}/core/logging_config.py",
    
    f"{folders['ml-service']}/app.py",
    f"{folders['ml-service']}/config.py",
    f"{folders['ml-service']}/.env",
    f"{folders['ml-service']}/routers/generate.py",
    f"{folders['ml-service']}/services/image_downloader.py",
    f"{folders['ml-service']}/services/cloudinary_service.py",   
    f"{folders['ml-service']}/services/preprocessor.py",
    f"{folders['ml-service']}/services/schp_service.py",
    f"{folders['ml-service']}/services/vton_service.py",
    f"{folders['ml-service']}/models/schemas.py",
    f"{folders['ml-service']}/weights/schp",
    f"{folders['ml-service']}/weights/idm_vton",
    
    "docs/diagrams/",
    "docs/srs/",
    
    ".gitignore",
]

for filepath in list_of_files:
    is_directory = filepath.endswith("/")
    filepath = Path(filepath)

    if is_directory:
        if not filepath.exists():
            filepath.mkdir(parents=True)
            logging.info(f"Creating directory: {filepath}")
        else:
            logging.info(f"{filepath} already exists")
        continue

    filedir = filepath.parent
    filename = filepath.name
    if filedir != Path(".") and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists():
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
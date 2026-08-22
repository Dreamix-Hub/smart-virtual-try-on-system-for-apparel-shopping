from pathlib import Path
import logging

# ---------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

project_name = "Smart Virtual Try-on System for Apparel Shopping"

# ---------------------------------------------------------
# Project folders
# ---------------------------------------------------------

folders = {
    "frontend": "frontend",
    "backend": "backend",
    "ml_service": "ml-service",
    "shared": "shared",
    "docs": "docs",
}

# ---------------------------------------------------------
# Files and directories to create
# ---------------------------------------------------------

list_of_files = [

    # =====================================================
    # FRONTEND
    # =====================================================

    f"{folders['frontend']}/index.html",

    f"{folders['frontend']}/pages/upload.html",
    f"{folders['frontend']}/pages/result.html",

    f"{folders['frontend']}/css/main.css",
    f"{folders['frontend']}/css/components.css",

    f"{folders['frontend']}/js/config.js",
    f"{folders['frontend']}/js/api.js",
    f"{folders['frontend']}/js/upload.js",
    f"{folders['frontend']}/js/polling.js",
    f"{folders['frontend']}/js/ui.js",

    f"{folders['frontend']}/assets/images/",

    f"{folders['frontend']}/netlify.toml",

    # =====================================================
    # BACKEND
    # =====================================================

    f"{folders['backend']}/main.py",
    f"{folders['backend']}/config.py",
    f"{folders['backend']}/.env",
    f"{folders['backend']}/.env.example",
    f"{folders['backend']}/requirements.txt",
    f"{folders['backend']}/Dockerfile",

    # Backend routers
    f"{folders['backend']}/routers/__init__.py",
    f"{folders['backend']}/routers/tryon.py",

    # Backend services
    f"{folders['backend']}/services/__init__.py",
    f"{folders['backend']}/services/cloudinary_service.py",
    f"{folders['backend']}/services/ml_client.py",
    f"{folders['backend']}/services/image_processor.py",

    # Backend models
    f"{folders['backend']}/models/__init__.py",
    f"{folders['backend']}/models/schemas.py",

    # Backend jobs
    f"{folders['backend']}/jobs/__init__.py",
    f"{folders['backend']}/jobs/job_store.py",

    # Backend core
    f"{folders['backend']}/core/__init__.py",
    f"{folders['backend']}/core/exceptions.py",
    f"{folders['backend']}/core/logging_config.py",

    # Backend tests
    f"{folders['backend']}/tests/test_upload.py",
    f"{folders['backend']}/tests/test_job_status.py",
    f"{folders['backend']}/tests/test_cloudinary_mock.py",

    # =====================================================
    # ML SERVICE
    # =====================================================

    f"{folders['ml_service']}/app.py",
    f"{folders['ml_service']}/config.py",
    f"{folders['ml_service']}/.env",
    f"{folders['ml_service']}/.env.example",
    f"{folders['ml_service']}/requirements.txt",
    f"{folders['ml_service']}/Dockerfile",
    f"{folders['ml_service']}/README.md",

    # ML router
    f"{folders['ml_service']}/routers/generate.py",

    # ML services
    f"{folders['ml_service']}/services/image_downloader.py",
    f"{folders['ml_service']}/services/cloudinary_service.py",
    f"{folders['ml_service']}/services/preprocessor.py",
    f"{folders['ml_service']}/services/schp_service.py",
    f"{folders['ml_service']}/services/vton_service.py",

    # ML models
    f"{folders['ml_service']}/models/schemas.py",

    # ML model weights
    f"{folders['ml_service']}/weights/schp/",
    f"{folders['ml_service']}/weights/idm_vton/",

    # ML tests
    f"{folders['ml_service']}/tests/test_generate_mock.py",

    # =====================================================
    # SHARED
    # =====================================================

    f"{folders['shared']}/api_contract.md",

    # =====================================================
    # DOCS
    # =====================================================

    f"{folders['docs']}/diagrams/sequence_async.puml",
    f"{folders['docs']}/diagrams/deployment.puml",
    f"{folders['docs']}/diagrams/component.puml",

    f"{folders['docs']}/srs/",

    # =====================================================
    # ROOT FILES
    # =====================================================

    ".gitignore",
    "README.md",
]


# ---------------------------------------------------------
# Create project structure
# ---------------------------------------------------------

def create_project_structure():
    logging.info(f"Creating project: {project_name}")

    for filepath_string in list_of_files:

        filepath = Path(filepath_string)

        # -------------------------------------------------
        # Directory
        # -------------------------------------------------

        if filepath_string.endswith("/"):
            if not filepath.exists():
                filepath.mkdir(parents=True, exist_ok=True)
                logging.info(f"Created directory: {filepath}")
            else:
                logging.info(f"Already exists: {filepath}")

            continue

        # -------------------------------------------------
        # File
        # -------------------------------------------------

        filedir = filepath.parent

        if filedir != Path(".") and not filedir.exists():
            filedir.mkdir(parents=True, exist_ok=True)

            logging.info(
                f"Created directory: {filedir}"
            )

        if not filepath.exists():
            filepath.touch()

            logging.info(
                f"Created file: {filepath}"
            )

        else:
            logging.info(
                f"Already exists: {filepath}"
            )

    logging.info("Project structure creation completed.")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":
    create_project_structure()
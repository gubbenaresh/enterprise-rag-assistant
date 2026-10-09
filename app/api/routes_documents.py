import logging
from pathlib import Path

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.services.document_processor import (
    DocumentProcessor
)


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


UPLOAD_DIR = Path(
    "data/documents"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    """
    Upload and process a document.
    """

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="Filename is required."
        )

    extension = Path(
        file.filename
    ).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. "
                "Allowed: PDF, DOCX, TXT."
            )
        )

    file_path = (
        UPLOAD_DIR /
        Path(file.filename).name
    )

    try:

        content = await file.read()

        if not content:

            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        file_path.write_bytes(
            content
        )

        logger.info(
            "File uploaded: %s",
            file.filename
        )

        processor = DocumentProcessor()

        documents = processor.process(
            str(file_path)
        )

        return {
            "filename": file.filename,
            "status": "processed",
            "sections": len(documents),
            "documents": documents,
        }

    except HTTPException:
        raise

    except Exception as error:

        logger.exception(
            "Document processing failed"
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Document processing failed."
            )
        ) from error
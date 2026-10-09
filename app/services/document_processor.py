import logging

from app.services.document_loader import (
    DocumentLoader
)

from app.services.text_cleaner import (
    TextCleaner
)


logger = logging.getLogger(__name__)


class DocumentProcessor:
    """
    Coordinates document loading and text cleaning.
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.cleaner = TextCleaner()

    def process(
        self,
        file_path: str
    ) -> list[dict]:

        logger.info(
            "Starting document processing: %s",
            file_path
        )

        documents = self.loader.load(
            file_path
        )

        processed_documents = []

        for document in documents:

            cleaned_text = self.cleaner.clean(
                document["text"]
            )

            if not cleaned_text:

                logger.warning(
                    "Empty page skipped: %s page=%s",
                    document["source"],
                    document["page"]
                )

                continue

            processed_documents.append(
                {
                    "source": document["source"],
                    "page": document["page"],
                    "text": cleaned_text,
                }
            )

        if not processed_documents:

            logger.error(
                "No readable text found: %s",
                file_path
            )

            raise ValueError(
                "Document contains no readable text."
            )

        logger.info(
            "Document processing completed: %s",
            file_path
        )

        return processed_documents
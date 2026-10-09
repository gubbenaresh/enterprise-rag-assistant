from pathlib import Path

import fitz
from docx import Document


class DocumentLoader:
    """
    Loads supported documents and extracts their text.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt",
    }

    def load(self, file_path: str) -> list[dict]:
        """
        Load a document and return structured text data.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = path.suffix.lower()

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        if extension == ".pdf":
            return self._load_pdf(path)

        if extension == ".docx":
            return self._load_docx(path)

        return self._load_txt(path)

    def _load_pdf(self, path: Path) -> list[dict]:
        """
        Extract text page by page from a PDF.
        """

        documents = []

        pdf = fitz.open(path)

        try:
            for page_number, page in enumerate(pdf):

                text = page.get_text()

                documents.append(
                    {
                        "source": path.name,
                        "page": page_number + 1,
                        "text": text,
                    }
                )

        finally:
            pdf.close()

        return documents

    def _load_docx(self, path: Path) -> list[dict]:
        """
        Extract text from a DOCX file.
        """

        document = Document(path)

        paragraphs = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        combined_text = "\n".join(paragraphs)

        return [
            {
                "source": path.name,
                "page": None,
                "text": combined_text,
            }
        ]

    def _load_txt(self, path: Path) -> list[dict]:
        """
        Read a TXT file.
        """

        text = path.read_text(
            encoding="utf-8"
        )

        return [
            {
                "source": path.name,
                "page": None,
                "text": text,
            }
        ]
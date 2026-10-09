from app.services.document_processor import (
    DocumentProcessor
)


def test_document_processor(tmp_path):

    file_path = (
        tmp_path /
        "test.txt"
    )

    file_path.write_text(
        "Hello     world\n\n\n\n"
        "This is a document.",
        encoding="utf-8"
    )

    processor = DocumentProcessor()

    result = processor.process(
        str(file_path)
    )

    assert len(result) == 1

    assert result[0]["source"] == "test.txt"

    assert result[0]["text"] == (
        "Hello world\n\n"
        "This is a document."
    )
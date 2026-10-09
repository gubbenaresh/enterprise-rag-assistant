from pathlib import Path

import pytest

from app.services.document_loader import (
    DocumentLoader
)


def test_txt_file_loading(tmp_path):

    file_path = (
        tmp_path /
        "test.txt"
    )

    file_path.write_text(
        "Hello world",
        encoding="utf-8"
    )

    loader = DocumentLoader()

    result = loader.load(
        str(file_path)
    )

    assert len(result) == 1

    assert result[0]["source"] == "test.txt"

    assert result[0]["page"] is None

    assert result[0]["text"] == "Hello world"


def test_missing_file():

    loader = DocumentLoader()

    with pytest.raises(
        FileNotFoundError
    ):

        loader.load(
            "does_not_exist.pdf"
        )


def test_unsupported_file(tmp_path):

    file_path = (
        tmp_path /
        "test.xlsx"
    )

    file_path.write_text(
        "test",
        encoding="utf-8"
    )

    loader = DocumentLoader()

    with pytest.raises(
        ValueError,
        match="Unsupported file type"
    ):

        loader.load(
            str(file_path)
        )
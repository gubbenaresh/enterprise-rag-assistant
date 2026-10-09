from app.services.text_cleaner import (
    TextCleaner
)


def test_text_cleaning():

    cleaner = TextCleaner()

    text = (
        "Hello     world\n\n\n\n"
        "This is a test."
    )

    result = cleaner.clean(
        text
    )

    assert result == (
        "Hello world\n\n"
        "This is a test."
    )


def test_empty_text():

    cleaner = TextCleaner()

    result = cleaner.clean("")

    assert result == ""


def test_whitespace_only_text():

    cleaner = TextCleaner()

    result = cleaner.clean(
        "     \n\n    "
    )

    assert result == ""
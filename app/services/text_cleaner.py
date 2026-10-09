import re


class TextCleaner:
    """
    Cleans extracted document text.
    """

    def clean(self, text: str) -> str:
        """
        Normalize whitespace while preserving
        meaningful paragraph breaks.
        """

        if not text:
            return ""

        # Replace non-breaking spaces
        text = text.replace(
            "\u00a0",
            " "
        )

        # Normalize Windows line endings
        text = text.replace(
            "\r\n",
            "\n"
        )

        # Normalize old Mac line endings
        text = text.replace(
            "\r",
            "\n"
        )

        # Remove trailing spaces from lines
        text = re.sub(
            r"[ \t]+$",
            "",
            text,
            flags=re.MULTILINE
        )

        # Replace multiple spaces/tabs with one space
        text = re.sub(
            r"[ \t]+",
            " ",
            text
        )

        # Reduce 3+ newlines to 2
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        return text.strip()
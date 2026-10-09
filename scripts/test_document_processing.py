from pathlib import Path

from app.services.document_processor import (
    DocumentProcessor
)


def main():

    processor = DocumentProcessor()

    documents_dir = Path(
        "data/documents"
    )

    files = list(
        documents_dir.glob("*")
    )

    for file_path in files:

        print("\n" + "=" * 60)

        print(
            f"Processing: {file_path.name}"
        )

        print("=" * 60)

        try:

            documents = processor.process(
                str(file_path)
            )

            print(
                f"Extracted sections: "
                f"{len(documents)}"
            )

            for document in documents[:3]:

                print(
                    f"\nSource: "
                    f"{document['source']}"
                )

                print(
                    f"Page: "
                    f"{document['page']}"
                )

                print(
                    f"Text:\n"
                    f"{document['text'][:500]}"
                )

        except Exception as error:

            print(
                f"ERROR: {error}"
            )


if __name__ == "__main__":
    main()
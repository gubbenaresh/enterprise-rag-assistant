# Enterprise Knowledge AI Assistant

An enterprise AI assistant that allows users to upload
company documents and ask questions about their content.

## Project Goal

The system will use Retrieval-Augmented Generation (RAG)
to retrieve relevant information from enterprise documents
and use an LLM to generate grounded answers.

## Planned Architecture

    Documents
        ↓
    Document Processing
        ↓
    Chunking
        ↓
    Embeddings
        ↓
    Vector Database
        ↓
    Retrieval
        ↓
    Reranking
        ↓
    LLM
        ↓
    Answer + Sources

## Current Status

Day 1 completed:

- Python virtual environment
- Project structure
- FastAPI application
- Environment configuration
- Logging
- Health check API
- Automated API tests

## Tech Stack

- Python
- FastAPI
- Pydantic
- PostgreSQL
- pgvector
- Sentence Transformers
- LLM
- Streamlit
- Docker

## Status

## Day 2 — Document Processing Pipeline ✅

### Objective
Implemented the document processing pipeline to extract and clean text from PDF, DOCX, and TXT files. This is the first step toward building the Retrieval-Augmented Generation (RAG) system.

### Features Implemented
- [✅] PDF text extraction using PyMuPDF
- [✅] DOCX text extraction using python-docx
- [✅] TXT file reading using Python
- [✅] Text cleaning and whitespace normalization
- [✅] Page-level metadata extraction for PDF documents
- [✅] Source filename tracking
- [✅] Document processing using a dedicated service
- [✅] File extension validation
- [✅] Empty file validation
- [✅] Error handling for unsupported and missing files
- [✅] Application logging
- [✅] FastAPI document upload endpoint
- [✅] Automated unit tests using Pytest
- [✅] Tested document processing through FastAPI Swagger UI

### Tech Stack
- Python
- FastAPI
- PyMuPDF
- python-docx
- Pydantic
- Pytest
- Uvicorn
- Git and GitHub

### Project Architecture

    PDF / DOCX / TXT
           |
           v
      Document Loader
           |
           v
       Raw Text
           |
           v
       Text Cleaner
           |
           v
    Document Processor
           |
           v
    Clean Text + Metadata

### Metadata Structure

Each processed document contains:

- `source`: Original filename
- `page`: Page number for PDF documents; `None` for DOCX/TXT
- `text`: Extracted and cleaned text

### API Endpoint

**POST `/documents/upload`**

Uploads and processes a supported document.

Supported formats:
- PDF
- DOCX
- TXT

Interactive API documentation: `/docs`

### Testing

Automated tests cover document loading, text cleaning, and document processing.

Run tests using:

    pytest

### Challenges Addressed
- Different document formats require different extraction methods.
- Extracted text may contain unnecessary whitespace and line breaks.
- PDF page metadata is needed to support source citations later.
- Unsupported files and documents without readable text must be handled safely.

### Outcome
The application can extract and clean text from supported documents and retain basic source metadata. This prepares the data for the next stage of the RAG pipeline.

### Next Steps — Day 3
- Implement text chunking
- Configure chunk size and overlap
- Preserve document metadata across chunks
- Generate unique chunk IDs
- Test chunk boundaries and metadata

**Overall Progress:** Day 2 completed — Document Processing Pipeline.

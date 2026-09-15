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

🚧 Under development
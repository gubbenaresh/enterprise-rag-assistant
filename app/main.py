import logging

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging_config import setup_logging


setup_logging()

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "Enterprise Knowledge AI Assistant "
        "built using Retrieval-Augmented Generation."
    )
)


@app.get("/")
def root():
    """
    Basic application endpoint.
    """

    logger.info("Root endpoint called")

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "message": "Enterprise RAG Assistant is running."
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint used to verify
    that the application is running.
    """

    return {
        "status": "healthy"
    }
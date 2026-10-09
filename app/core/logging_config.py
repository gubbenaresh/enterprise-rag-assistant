# it will record the flow of important event of the appliocation 
# it helps to tell at what point our application got error 
# this help track root cousing error and fit it 

import logging

from app.core.config import settings

def setup_logging() -> None:
    """
    Configure application-wide logging.
    """

    logging.basicConfig(
        level=getattr(
            logging,
            settings.log_level.upper(),
            logging.INFO
        ),
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        )
    )
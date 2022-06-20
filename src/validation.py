import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


def check_columns(data, expected_cols):
    """
    Will raise error if an expected column is missing and a
    warning if additional columns are present.
    """
    actual_cols = data.columns.tolist()

    if not set(expected_cols).issubset(set(actual_cols)):
        logger.error("Missing columns")
        logger.error(set(expected_cols) - set(actual_cols))
        return False

    if set(actual_cols) - set(expected_cols):
        logger.warning("Additional columns")
        logger.warning(set(actual_cols) - set(expected_cols))

    return True

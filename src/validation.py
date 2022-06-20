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
        raise Exception("Input data failed validation")

    if set(actual_cols) - set(expected_cols):
        logger.warning("Additional columns")
        logger.warning(set(actual_cols) - set(expected_cols))


def check_primary_key_is_unique(data, key):
    if len(data[key]) == len(data[key].unique()):
        logger.info("Confirmed that No. is unique")
    else:
        logger.error("No. is not unique")
        raise ValueError("No. is not unique")

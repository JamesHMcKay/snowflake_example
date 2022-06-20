import logging
import logging.config
import pandas as pd
from database import SnowflakeDatabase
from load_config import load_yaml_file

import models
from transform import fix_trailing_decimals, fix_types, set_column_names
from validation import check_columns, check_primary_key_is_unique

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


def load_data(snowflake, filename, table):
    logger.info(f"Loading raw data for table {table.name}")

    data = pd.read_excel(filename, sheet_name=table.sheet_name, dtype=str)

    check_primary_key_is_unique(data, table.primary_key)

    check_columns(data, table.columns.keys())

    logger.info("Input data passed column and primary key validation")

    data = set_column_names(data, table.columns)

    data = fix_trailing_decimals(data)

    data = fix_types(data, table.schema)

    snowflake.write(data, table.name)
    logger.info(f"Loaded raw data for table {table.name}")


def run():
    config = load_yaml_file("config.yaml")

    snowflake = SnowflakeDatabase(config["user"], config["password"], config["account"])
    snowflake.use_database("SALES_REPORTING")

    tables = [
        models.ITEMS,
        models.CUSTOMERS,
        models.SALES,
        models.CUSTOMER_GROUPS,
        models.PRODUCT_GROUPS,
        models.REGIONS,
        models.STAFF,
        models.ITEM_LEDGERS,
    ]

    for table in tables:
        load_data(snowflake, config["raw_file"], table)


if __name__ == "__main__":
    run()

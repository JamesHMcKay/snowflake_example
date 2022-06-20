import logging
import logging.config
import pandas as pd
from database import SnowflakeDatabase
from load_config import load_yaml_file

import models
from validation import check_columns

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


def load_sales_item_table(snowflake, filename, table):
    logger.info(f"Loading raw data for table {table.name}")

    data = pd.read_excel(filename, sheet_name=table.sheet_name, dtype=str)
    if len(data[table.primary_key]) == len(data[table.primary_key].unique()):
        logger.info("Confirmed that No. is unique")
    else:
        logger.error("No. is not unique")
        raise ValueError("No. is not unique")

    if not check_columns(data, table.columns.keys()):
        raise Exception("Input data failed validation")
    else:
        logger.info("Input data passed column validation")

    data.rename(columns=table.columns, inplace=True)

    data.replace(r".0$", "", regex=True, inplace=True)

    for col, type_ in table.schema.items():
        data[col] = data[col].astype(type_)

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
        load_sales_item_table(snowflake, config["raw_file"], table)


if __name__ == "__main__":
    run()

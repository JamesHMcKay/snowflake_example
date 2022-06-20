"""
This module sets up the data warehouse and defines all tables.
"""
from database import SnowflakeDatabase
from load_config import load_yaml_file


def load_from_file(filename):
    with open(filename, "r") as file:
        contents = file.read()
    return contents


def run():
    config = load_yaml_file("config.yaml")
    snowflake = SnowflakeDatabase(config["user"], config["password"], config["account"])
    snowflake.execute(load_from_file("setup/sales_reporting.sql"))
    snowflake.execute(load_from_file("setup/items.sql"))
    snowflake.execute(load_from_file("setup/customers.sql"))
    snowflake.execute(load_from_file("setup/item_ledger.sql"))
    snowflake.execute(load_from_file("setup/sales.sql"))
    snowflake.execute(load_from_file("setup/product_groups.sql"))
    snowflake.execute(load_from_file("setup/staff.sql"))
    snowflake.execute(load_from_file("setup/regions.sql"))
    snowflake.execute(load_from_file("setup/customer_groups.sql"))
    snowflake.execute(load_from_file("setup/totals.sql"))
    snowflake.execute(load_from_file("setup/generate_totals_task.sql"))


if __name__ == "__main__":
    run()

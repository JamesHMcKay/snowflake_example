# Snowflake example

This project a small example of loading data in a Snowflake database using the python connector. I also include an example task which is created on the Snowflake cluster to do a little bit of scheduled processing.


## Quick start

This has been tested with Python version 3.8.10.

For the simplest set up it is best to use venv and follow the commands below.

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements
```

On Ubuntu we also need to install libm-devel and openssl-devel.

Create a config.yaml file in the root directory that looks like this:

```yaml
user: <your snowflake username>
account: "XXXXXX.ap-southeast-2"
password: NULL or <password> # leave NULL to prompt for password

raw_file: "raw_input.xlsx"
```
where the values here are the credentials for your snowflake account and the path to the raw data file.

To set up the database and load raw data 

```bash
python src/setup.py
python src/load_raw_data.py
```

# Design

The database layout follows the structure of the provided tables. However, columns and tables have been renamed where possible to make things clear and easier to work with.

The database is called `sales_reporting`, within it we have 8 tables of raw data and 1 table of processed data.

For table schemas and column descriptions see the PDF schemas.pdf in this repository (best downloaded and viewed in a PDF viewer than in the GitHub preview).

## Notes

This is a very basic example of how to use the python connector to load data into a Snowflake database. There is some validation, but it is limited.

I note that the primary key is not enforced by Snowflake, so we would need to add a check at the load stage to ensure that primary key is unique.

There is also no validation that we are no uploading existing data either, so could do some checks of this is required. Perhaps even just checking if the database is indeed empty on initial load of raw data.

## Extensions

The next steps are to gather information on the tables and gather requirements from the business. From there we can process the raw tables into something more useful, and creating a full reporting layer of processed data, such as sales aggregates, reports and so on.

The current task is very basic and will just recompute the total of all sales every hour. This is really just to demonstrate functionality. Once business requirements are clear, we would set this up to process perhaps data only from the last hour, and partition the results accordingly. The current process of aggregating the entire table obviously would not scale well!

There are currently no indexes on any columns, and we are not making any attempts to optimise the tables. This is because we do not yet know what the business requirements are, so we can't make any assumptions about exactly information is required and what optimisations are required to achieve the desired outputs.

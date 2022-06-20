This requires Python version 3.5 or later.

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

The database is called `sales_reporting`.
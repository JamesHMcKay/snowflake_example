import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import logging.config
import logging
from getpass import getpass

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)


class SnowflakeDatabase:
    def __init__(self, user, password, account):
        self.user = user
        self.password = self.get_password(password)
        self.account = account
        self.connect()

    def get_password(self, password):
        if not password:
            password = getpass()
        return password

    def connect(self):
        self.conn = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
        )

    def close(self):
        self.conn.close()

    def use_database(self, name):
        self.conn.cursor().execute(f"USE DATABASE {name}")

    def execute(self, command):
        commands = command.split(";")
        for command in commands:
            self.conn.cursor().execute(command)

    def write(self, data, table_name):
        success, nchunks, nrows, _ = write_pandas(self.conn, data, table_name)

        if success:
            logger.info(f"Successfully wrote {nchunks} chunks and {nrows} rows")
        else:
            logger.error(f"Failed to write data into {table_name}")

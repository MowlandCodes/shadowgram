from config import *


class DBConnection:
    """Database instance for handling connection to the Database"""

    def __init__(
        self,
        db_type: str,
        host: str = "localhost",
        port: int = 3306,
        user: str = "root",
        password: str = "",
        db_name: str = "shadowgram",
    ):
        self.db_type = db_type
        self.db_host = host
        self.db_port = port
        self.db_user = user
        self.db_password = password
        self.db_name = db_name

        if self.db_type == "sqlite":
            import sqlite3

            self.conn = sqlite3.connect(f"{self.db_name}.db")
            self.cur = self.conn.cursor()

        elif self.db_type == "mysql":
            import pymysql

            # Check if the Database is exists, if not create one
            try:
                self.conn = pymysql.connect(
                    host=self.db_host,
                    port=self.db_port,
                    user=self.db_user,
                    password=self.db_password,
                    database=self.db_name,
                )

            except pymysql.err.OperationalError:
                log_gram.warning(
                    f"Database {self.db_name} does not exist, creating it..."
                )
                self.conn = pymysql.connect(
                    host=self.db_host,
                    port=self.db_port,
                    user=self.db_user,
                    password=self.db_password,
                )
                self.conn.cursor().execute(f"CREATE DATABASE {self.db_name}")
                self.conn.cursor().execute(f"USE {self.db_name}")
                self.conn.commit()
                log_gram.info(f"Database {self.db_name} created!")

            self.cur = self.conn.cursor()

    def check_table(self, table_name: str) -> bool:
        """Check whether a table exists in the database. Return True if it does, False if not"""
        self.cur.execute(f"SHOW TABLES")
        result = self.cur.fetchall()
        result = [item[0] for item in result]

        if table_name not in result:
            return False
        else:
            return True

    def create_table(self, table_name: str, table_schema: list[str]):
        """Create a new table with the provided schema.
        The schema is on a list[str] format, for example:
        [
            "field INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT",
            "other_field VARCHAR(50) NOT NULL",
            "other_field_again TEXT NOT NULL",
        ]
        """
        self.cur.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(table_schema)})"
        )
        self.conn.commit()

    def insert(self, table_name: str, fields: list[str], data: list[tuple]):
        if self.db_type == "mysql":
            query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({','.join(['%s' for _ in fields])})"
            self.cur.executemany(query, data)
            self.conn.commit()  # Commit the changes to database
        elif self.db_type == "sqlite":
            query = f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({','.join(['?' for _ in fields])})"
            self.cur.executemany(query, data)
            self.conn.commit()  # Commit the changes to database

    def get_all(self, table_name: str):
        self.cur.execute(f"SELECT * FROM {table_name}")
        return self.cur.fetchall()

    def close(self):
        self.cur.close()


def connect_db(
    db_type: str,
    db_name: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
) -> DBConnection | bool:
    """Connect to a Database Driver and return its cursor instance"""
    if db_type == "mysql":
        return DBConnection(
            db_type=db_type,
            host=host,
            port=port,
            user=user,
            password=password,
            db_name=db_name,
        )
    elif db_type == "sqlite":
        return DBConnection(db_type=db_type, db_name=db_name)
    else:
        log_gram.error(f"Unknown Database type: {db_type}")
        return False

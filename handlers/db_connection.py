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

    def close(self):
        self.cur.close()


def connect_db(
    name: str,
    db_name: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
) -> DBConnection | bool:
    """Connect to a Database Driver and return its cursor instance"""
    if name == "mysql":
        return DBConnection(
            name=name,
            host=host,
            port=port,
            user=user,
            password=password,
            db_name=db_name,
        )
    elif name == "sqlite":
        return DBConnection(name=name, db_name=db_name)
    else:
        log_gram.error(f"Unknown Database type: {name}")
        return False

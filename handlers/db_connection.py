from config import *


class DBConnection:
    """Database instance for handling connection to the Database"""

    def __init__(
        self,
        name: str,
        host: str = "localhost",
        port: int = 3306,
        user: str = "root",
        password: str = "",
        db_name: str = "shadowgram",
    ):
        self.db_name = name
        self.db_host = host
        self.db_port = port
        self.db_user = user
        self.db_password = password
        self.db_name = db_name

        if self.db_name == "sqlite":
            import sqlite3

            conn = sqlite3.connect(f"{self.db_name}.db")
            self.cur = conn.cursor()

        elif self.db_name == "mysql":
            import pymysql
            import pymysql.cursors as cursors

            conn = pymysql.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                password=self.db_password,
                database=self.db_name,
                cursorclass=cursors.DictCursor,
            )

            self.cur = conn.cursor()

    def insert(self, table_name: str, data: dict):
        pass

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

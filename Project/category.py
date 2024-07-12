import sqlite3
from sqlite3 import Error

class Category:
    def __init__(self, cnx) -> None:
        self._cnx = cnx

    def create_table_category(self):
        self._sql = """
            CREATE TABLE IF NOT EXISTS category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category text NOT NULL,
                type text NOT NULL,
                UNIQUE (category)
            );
        """
        try:
            c = self._cnx.cursor()
            c.execute(self._sql)
        except Error as err:
            print(err)

    def add_category(self,category, type):
        self._category = category
        self._type = type

        self._sql = """
            INSERT INTO category(category, type)
            VALUES(?, ?)
        """
        params = (self._category, self._type)
        try:
            c = self._cnx.cursor()
            c.execute(self._sql, params)
            self._cnx.commit()
        except Error as err:
            print(err)

    

import sqlite3
from sqlite3 import Error

def create_connection(database):
    # cnx = None
    try:
        cnx = sqlite3.connect(database)
    except Error as err:
        print(err)
    return cnx

def create_table(cnx, sql):
    try:
        c = cnx.cursor()
        c.execute(sql)
    except Error as err:
        print(err)

def add_coin(cnx, symbol, name, amount):
    sql = """
        INSERT INTO coin(symbol, name, amount)
        VALUES(?, ?, ?)
    """
    params = (symbol, name, amount)
    try:
        c = cnx.cursor()
        c.execute(sql,params)
        cnx.commit()
    except Error as err:
        print(err)
    return c.lastrowid

def list_coin(cnx):
    sql = """
        SELECT*from coin
    """
    try:
        c = cnx.cursor()
        c.execute(sql)
        coins = c.fetchall()
        for coin in coins:
            print(coin)
    except Error as err:
        print(err)

def main():
    database = 'cryto.sqlite3'
    sql_create_coin_table = """
        CREATE TABLE IF NOT EXISTS coin(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol text NOT NULL,
            name text NOT NULL,
            amount integer
        );
    """

    #create database
    cnx = create_connection(database)
    #create table
    create_table(cnx, sql_create_coin_table)
    #insert data
    add_coin(cnx, 'BTC', 'Bitcoin', 100)
    add_coin(cnx, 'ETH', 'Etherium', 500)
    #select data
    list_coin(cnx)

if __name__ == '__main__':
    main()


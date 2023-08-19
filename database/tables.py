import sqlite3

def create_tables(conn: sqlite3.Connection) -> None:
    try:
        c = conn.cursor()
        c.execute('''PRAGMA foreign_keys = ON;''')
        c.execute(products())
        c.execute(links())
        c.close()
    except sqlite3.Error as e:
        raise Exception(e)


def products():
    return ''' 
        CREATE TABLE IF NOT EXISTS products
        (
            id UNIQUEIDENTIFIER  NOT NULL PRIMARY KEY, 
            name TEXT NOT NULL, 
            price REAL NOT NULL,
            discount_price REAL,
            savings TEXT,
            coupon_discount TEXT
        ); ''' 

def links():
    return ''' 
        CREATE TABLE IF NOT EXISTS links
        (
            link TEXT NOT NULL PRIMARY KEY, 
            member_id UNIQUEIDENTIFIER  NOT NULL, 
            FOREIGN KEY (member_id) REFERENCES products (id) ON DELETE CASCADE
        ); ''' 

import sqlite3
import tables

CONN_ZUMUB = None

def create_connection_zumub():
    try:
        global CONN_ZUMUB
        CONN_ZUMUB = sqlite3.connect('zumub_data.db')
        tables.create_tables(CONN_ZUMUB)
        CONN_ZUMUB.close()
    except sqlite3.Error as e:
        raise Exception(e)
    finally:
        if CONN_ZUMUB:
            CONN_ZUMUB.close()
            


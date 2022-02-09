import imdb_setup_database
import sqlite3
from typing import Tuple



def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.close()


def test_data_size():
    final_result = imdb_setup_database.populate_top250_tv_shows(curs, conn)
    assert final_result == 250


database = 'imDb.db'
conn, curs = open_db(database)

import imdb_setup_database
import sqlite3
from typing import Tuple


def test_main():
    def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def test_data_size(cursor: sqlite3.Cursor):
        final_result = imdb_setup_database.test_size(cursor)
        assert final_result == 251

    database = 'imDb.db'
    conn, curs = test_open_db(database)
    test_data_size(curs)


test_main()

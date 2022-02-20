import imdb_setup_database
import sqlite3
from typing import Tuple


def test_main():
    def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def test_data_size1(cursor: sqlite3.Cursor):
        final_result = imdb_setup_database.test_size1(cursor)
        assert final_result == 250

    def test_data_size2(cursor: sqlite3.Cursor):
        final_result = imdb_setup_database.test_size2(cursor)
        assert final_result == 100

    def test_data_size3(cursor: sqlite3.Cursor):
        final_result = imdb_setup_database.test_size3(cursor)
        assert final_result == 100

    database = 'imDb.db'
    conn, curs = test_open_db(database)
    test_data_size1(curs)
    test_data_size2(curs)
    test_data_size3(curs)


test_main()
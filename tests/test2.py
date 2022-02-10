# Second automated test
import sqlite3
from typing import Tuple


def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def test_close_db(connection: sqlite3.Connection):
    connection.close()


def test_show_dictionary(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS test_top250_tv_shows""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS test_top250_tv_shows(id TEXT PRIMARY KEY,
                                title TEXT NOT NULL,
                                fullTitle TEXT NOT NULL,
                                year TEXT NOT NULL,
                                crew TEXT NOT NULL,
                                imDbRating TEXT NOT NULL,
                                imDbRatingCount TEXT NOT NULL);""")
    conn.commit()

    data = {
        "items": [{"id": "tt5555555", "rank": "300", "title": "Capstone", "fullTitle": "Capstone (2020)",
                   "year": "2020", "crew": "Miserable Students", "imDbRating": "8.5",
                   "imDbRatingCount": "64"}]}

    cursor.execute("""INSERT INTO test_top250_tv_shows (id, title, fullTitle, year, crew, imDbRating, imDbRatingCount)
                              VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("items")[0].get("id"),
                                                                data.get("items")[0].get("title"),
                                                                data.get("items")[0].get("fullTitle"),
                                                                data.get("items")[0].get("year"),
                                                                data.get("items")[0].get("crew"),
                                                                data.get("items")[0].get("imDbRating"),
                                                                data.get("items")[0].get("imDbRatingCount")
                                                                ))
    conn.commit()

    result = cursor.execute(f'SELECT * FROM test_top250_tv_shows')
    for row in result:
        print(f'id: {row[0]}\ntitle: {row[1]}\nfullTitle: {row[2]}\nyear: {row[3]}\ncrew: {row[4]}\n'
              f'imDbRating: {row[5]}\nimDbRatingCount: {row[6]}\n')


def main():
    database = 'test_250.db'
    conn, curs = test_open_db(database)
    test_show_dictionary(curs, conn)


main()

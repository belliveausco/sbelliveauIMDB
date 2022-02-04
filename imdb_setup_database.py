import sqlite3
from typing import Tuple
import requests
import secrets


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.close()


def setup_top250_tv_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS top250_tv_shows""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS top250_tv_shows(id TEXT PRIMARY KEY,
                        title TEXT NOT NULL,
                        fullTitle TEXT NOT NULL,
                        year TEXT NOT NULL,
                        crew TEXT NOT NULL,
                        imDbRating TEXT NOT NULL,
                        imDbRatingCount TEXT NOT NULL);""")
    conn.commit()


def setup_user_ratings(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS setup_user_ratings""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS setup_user_ratings(id TEXT,
                        totalRating TEXT NOT NULL,
                        totalRatingVotes TEXT,
                        10rating% TEXT NOT NULL,
                        10ratingVotes TEXT NOT NULL,
                        9rating% TEXT NOT NULL,
                        9ratingVotes TEXT NOT NULL,
                        8rating% TEXT NOT NULL,
                        8ratingVotes TEXT NOT NULL,
                        7rating% TEXT NOT NULL,
                        7ratingVotes TEXT NOT NULL,
                        6rating% TEXT NOT NULL,
                        6ratingVotes TEXT NOT NULL,
                        5rating% TEXT NOT NULL,
                        5ratingVotes TEXT NOT NULL,
                        4rating% TEXT NOT NULL,
                        4ratingVotes TEXT NOT NULL,
                        3rating% TEXT NOT NULL,
                        3ratingVotes TEXT NOT NULL,
                        2rating% TEXT NOT NULL,
                        2ratingVotes TEXT NOT NULL,
                        rating% TEXT NOT NULL,
                        ratingVotes TEXT NOT NULL,
                        PRIMARY KEY (totalRatingVotes),
                        FOREIGN KEY (id) REFERENCES top250_tv_shows(id)
                        );""")
    conn.commit()


def populate_top250_tv_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for i in range(0, 250):
        cursor.execute("""INSERT INTO top250_tv_shows (id, title, fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("items")[i].get("id"),
                                                         data.get("items")[i].get("title"),
                                                         data.get("items")[i].get("fullTitle"),
                                                         data.get("items")[i].get("year"),
                                                         data.get("items")[i].get("crew"),
                                                         data.get("items")[i].get("imDbRating"),
                                                         data.get("items")[i].get("imDbRatingCount")))
    conn.commit()


'''
# Test
def select_from(curs: sqlite3.Cursor):
    curs.execute("""SELECT * FROM top250_tv_shows""")
    data = curs.fetchall()
    print(data)
'''


def main():
    database = 'imDb.db'
    conn, curs = open_db(database)
    setup_top250_tv_shows(curs, conn)
    setup_user_ratings(curs, conn)
    populate_top250_tv_shows(curs, conn)
    # select_from(curs)


main()

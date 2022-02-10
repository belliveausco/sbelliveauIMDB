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
    cursor.execute("""DROP TABLE IF EXISTS user_ratings""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_ratings(ranking TEXT,
                        id TEXT,
                        totalRating TEXT NOT NULL,
                        totalRatingVotes TEXT NOT NULL,
                        rating10percent TEXT NOT NULL,
                        rating10Votes TEXT NOT NULL,
                        rating9percent TEXT NOT NULL,
                        rating9Votes TEXT NOT NULL,
                        rating8percent TEXT NOT NULL,
                        rating8Votes TEXT NOT NULL,
                        rating7percent TEXT NOT NULL,
                        rating7Votes TEXT NOT NULL,
                        rating6percent TEXT NOT NULL,
                        rating6Votes TEXT NOT NULL,
                        rating5percent TEXT NOT NULL,
                        rating5Votes TEXT NOT NULL,
                        rating4percent TEXT NOT NULL,
                        rating4Votes TEXT NOT NULL,
                        rating3percent TEXT NOT NULL,
                        rating3Votes TEXT NOT NULL,
                        rating2percent TEXT NOT NULL,
                        rating2Votes TEXT NOT NULL,
                        rating1percent TEXT NOT NULL,
                        rating1Votes TEXT NOT NULL,
                        PRIMARY KEY (ranking),
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
    for i in range(0, 249):
        cursor.execute("""INSERT INTO top250_tv_shows (id, title, fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("items")[i].get("id"),
                                                         data.get("items")[i].get("title"),
                                                         data.get("items")[i].get("fullTitle"),
                                                         data.get("items")[i].get("year"),
                                                         data.get("items")[i].get("crew"),
                                                         data.get("items")[i].get("imDbRating"),
                                                         data.get("items")[i].get("imDbRatingCount")
                                                         ))
    conn.commit()


def test_size(cursor: sqlite3.Cursor):
    result = cursor.execute(f'SELECT COUNT(id) FROM top250_tv_shows;')
    for column in result:
        print(f'{column[0]}')
        final_result = column[0]
        return final_result


def add_wot_top250_tv_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/API/Ratings/{secrets.secret_key}/tt7462410"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    cursor.execute("""INSERT INTO top250_tv_shows (id, title, fullTitle, year, crew, imDbRating, imDbRatingCount)
                          VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("imDbId"),
                                                            data.get("title"),
                                                            data.get("fullTitle"),
                                                            data.get("year"),
                                                            "Rosamund Pike, Daniel Henney",
                                                            data.get("imDb"),
                                                            "85226"
                                                            ))
    conn.commit()


def populate_no_1_show(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt5491994"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
        rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, rating7Votes, 
        rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, rating3percent, 
        rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   ("1",
                    data.get("imDbId"),
                    data.get("totalRating"),
                    data.get("totalRatingVotes"),
                    data.get("ratings")[0].get("percent"),
                    data.get("ratings")[0].get("votes"),
                    data.get("ratings")[1].get("percent"),
                    data.get("ratings")[1].get("votes"),
                    data.get("ratings")[2].get("percent"),
                    data.get("ratings")[2].get("votes"),
                    data.get("ratings")[3].get("percent"),
                    data.get("ratings")[3].get("votes"),
                    data.get("ratings")[4].get("percent"),
                    data.get("ratings")[4].get("votes"),
                    data.get("ratings")[5].get("percent"),
                    data.get("ratings")[5].get("votes"),
                    data.get("ratings")[6].get("percent"),
                    data.get("ratings")[6].get("votes"),
                    data.get("ratings")[7].get("percent"),
                    data.get("ratings")[7].get("votes"),
                    data.get("ratings")[8].get("percent"),
                    data.get("ratings")[8].get("votes"),
                    data.get("ratings")[9].get("percent"),
                    data.get("ratings")[9].get("votes")))
    conn.commit()


def populate_no_50_show(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt2297757"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
        rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, rating7Votes, 
        rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, rating3percent, 
        rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   ("50",
                    data.get("imDbId"),
                    data.get("totalRating"),
                    data.get("totalRatingVotes"),
                    data.get("ratings")[0].get("percent"),
                    data.get("ratings")[0].get("votes"),
                    data.get("ratings")[1].get("percent"),
                    data.get("ratings")[1].get("votes"),
                    data.get("ratings")[2].get("percent"),
                    data.get("ratings")[2].get("votes"),
                    data.get("ratings")[3].get("percent"),
                    data.get("ratings")[3].get("votes"),
                    data.get("ratings")[4].get("percent"),
                    data.get("ratings")[4].get("votes"),
                    data.get("ratings")[5].get("percent"),
                    data.get("ratings")[5].get("votes"),
                    data.get("ratings")[6].get("percent"),
                    data.get("ratings")[6].get("votes"),
                    data.get("ratings")[7].get("percent"),
                    data.get("ratings")[7].get("votes"),
                    data.get("ratings")[8].get("percent"),
                    data.get("ratings")[8].get("votes"),
                    data.get("ratings")[9].get("percent"),
                    data.get("ratings")[9].get("votes")))
    conn.commit()


def populate_no_100_show(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0286486"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
        rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, rating7Votes, 
        rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, rating3percent, 
        rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   ("100",
                    data.get("imDbId"),
                    data.get("totalRating"),
                    data.get("totalRatingVotes"),
                    data.get("ratings")[0].get("percent"),
                    data.get("ratings")[0].get("votes"),
                    data.get("ratings")[1].get("percent"),
                    data.get("ratings")[1].get("votes"),
                    data.get("ratings")[2].get("percent"),
                    data.get("ratings")[2].get("votes"),
                    data.get("ratings")[3].get("percent"),
                    data.get("ratings")[3].get("votes"),
                    data.get("ratings")[4].get("percent"),
                    data.get("ratings")[4].get("votes"),
                    data.get("ratings")[5].get("percent"),
                    data.get("ratings")[5].get("votes"),
                    data.get("ratings")[6].get("percent"),
                    data.get("ratings")[6].get("votes"),
                    data.get("ratings")[7].get("percent"),
                    data.get("ratings")[7].get("votes"),
                    data.get("ratings")[8].get("percent"),
                    data.get("ratings")[8].get("votes"),
                    data.get("ratings")[9].get("percent"),
                    data.get("ratings")[9].get("votes")))
    conn.commit()


def populate_no_200_show(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7472896"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
        rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, rating7Votes, 
        rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, rating3percent, 
        rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   ("200",
                    data.get("imDbId"),
                    data.get("totalRating"),
                    data.get("totalRatingVotes"),
                    data.get("ratings")[0].get("percent"),
                    data.get("ratings")[0].get("votes"),
                    data.get("ratings")[1].get("percent"),
                    data.get("ratings")[1].get("votes"),
                    data.get("ratings")[2].get("percent"),
                    data.get("ratings")[2].get("votes"),
                    data.get("ratings")[3].get("percent"),
                    data.get("ratings")[3].get("votes"),
                    data.get("ratings")[4].get("percent"),
                    data.get("ratings")[4].get("votes"),
                    data.get("ratings")[5].get("percent"),
                    data.get("ratings")[5].get("votes"),
                    data.get("ratings")[6].get("percent"),
                    data.get("ratings")[6].get("votes"),
                    data.get("ratings")[7].get("percent"),
                    data.get("ratings")[7].get("votes"),
                    data.get("ratings")[8].get("percent"),
                    data.get("ratings")[8].get("votes"),
                    data.get("ratings")[9].get("percent"),
                    data.get("ratings")[9].get("votes")))
    conn.commit()


def populate_wot_show(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
        rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, rating7Votes, 
        rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, rating3percent, 
        rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   ("251",
                    data.get("imDbId"),
                    data.get("totalRating"),
                    data.get("totalRatingVotes"),
                    data.get("ratings")[0].get("percent"),
                    data.get("ratings")[0].get("votes"),
                    data.get("ratings")[1].get("percent"),
                    data.get("ratings")[1].get("votes"),
                    data.get("ratings")[2].get("percent"),
                    data.get("ratings")[2].get("votes"),
                    data.get("ratings")[3].get("percent"),
                    data.get("ratings")[3].get("votes"),
                    data.get("ratings")[4].get("percent"),
                    data.get("ratings")[4].get("votes"),
                    data.get("ratings")[5].get("percent"),
                    data.get("ratings")[5].get("votes"),
                    data.get("ratings")[6].get("percent"),
                    data.get("ratings")[6].get("votes"),
                    data.get("ratings")[7].get("percent"),
                    data.get("ratings")[7].get("votes"),
                    data.get("ratings")[8].get("percent"),
                    data.get("ratings")[8].get("votes"),
                    data.get("ratings")[9].get("percent"),
                    data.get("ratings")[9].get("votes")))
    conn.commit()


def main():
    database = 'imDb.db'
    conn, curs = open_db(database)
    setup_top250_tv_shows(curs, conn)
    setup_user_ratings(curs, conn)
    populate_top250_tv_shows(curs, conn)
    add_wot_top250_tv_shows(curs, conn)
    test_size(curs)
    populate_no_1_show(curs, conn)
    populate_no_50_show(curs, conn)
    populate_no_100_show(curs, conn)
    populate_no_200_show(curs, conn)
    populate_wot_show(curs, conn)


main()

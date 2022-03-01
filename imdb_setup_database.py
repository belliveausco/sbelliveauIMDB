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
    for i in range(0, 250):
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
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0388629"
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
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt1534360"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()

    try:
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
    except Exception as e:
        print(Exception, e)
        cursor.execute("""INSERT INTO user_ratings (ranking, id, totalRating, totalRatingVotes, rating10percent, 
                    rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
                    rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, 
                    rating4Votes, rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, 
                    rating1Votes) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       ("200",
                        data.get("imDbId"),
                        data.get("totalRating"),
                        data.get("totalRatingVotes"),
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"))

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


def setup_top250_movies(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS top250_movies""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS top250_movies(movies250_id TEXT PRIMARY KEY,
                        title TEXT NOT NULL,
                        fullTitle TEXT NOT NULL,
                        year TEXT NOT NULL,
                        crew TEXT NOT NULL,
                        imDbRating TEXT NOT NULL,
                        imDbRatingCount TEXT NOT NULL);""")
    conn.commit()


def populate_top250_movies(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for i in range(0, 250):
        cursor.execute("""INSERT INTO top250_movies (movies250_id, title, fullTitle, year, crew, imDbRating, 
        imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("items")[i].get("id"),
                                                           data.get("items")[i].get("title"),
                                                           data.get("items")[i].get("fullTitle"),
                                                           data.get("items")[i].get("year"),
                                                           data.get("items")[i].get("crew"),
                                                           data.get("items")[i].get("imDbRating"),
                                                           data.get("items")[i].get("imDbRatingCount")
                                                           ))
    conn.commit()


def setup_most_popular_movies(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS most_popular_movies""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS most_popular_movies(pop_movie_id TEXT PRIMARY KEY,
                        rank INTEGER NOT NULL,
                        rankUpDown INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        fullTitle TEXT NOT NULL,
                        year TEXT NOT NULL,
                        crew TEXT NOT NULL,
                        imDbRating TEXT NOT NULL,
                        imDbRatingCount TEXT NOT NULL);""")
    conn.commit()


def populate_most_popular_movies(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for i in range(0, 100):
        cursor.execute("""INSERT INTO most_popular_movies (pop_movie_id, rank, rankUpDown, title, fullTitle, year, crew, 
        imDbRating, imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (data.get("items")[i].get("id"),
                        int(data.get("items")[i].get("rank")),
                        int((data.get("items")[i].get("rankUpDown").replace(',', ''))),
                        data.get("items")[i].get("title"),
                        data.get("items")[i].get("fullTitle"),
                        data.get("items")[i].get("year"),
                        data.get("items")[i].get("crew"),
                        data.get("items")[i].get("imDbRating"),
                        data.get("items")[i].get("imDbRatingCount")
                        ))
    conn.commit()


def setup_movie_user_ratings(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS movie_user_ratings""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS movie_user_ratings(rankUpDown TEXT,
                        pop_movie_id TEXT,
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
                        PRIMARY KEY (rankUpDown),
                        FOREIGN KEY (pop_movie_id) REFERENCES most_popular_movies(id)
                        );""")
    conn.commit()


def populate_rankings_movie(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    a = list()
    for i in range(0, 100):
        a.append(int((data.get("items")[i].get("rankUpDown").replace(',', ''))))
        a.sort()
    a4 = a[0]
    a3 = a[97]
    a2 = a[98]
    a1 = a[99]
    tt_id = None
    tt_id1 = None
    tt_id2 = None
    tt_id3 = None
    return_data = cursor.execute(f'SELECT * from most_popular_movies WHERE rankUpDown = {a1}')
    for row in return_data:
        tt_id = row[0]
    return_data1 = cursor.execute(f'SELECT * from most_popular_movies WHERE rankUpDown = {a2}')
    for row in return_data1:
        tt_id1 = row[0]
    return_data2 = cursor.execute(f'SELECT * from most_popular_movies WHERE rankUpDown = {a3}')
    for row in return_data2:
        tt_id2 = row[0]
    return_data3 = cursor.execute(f'SELECT * from most_popular_movies WHERE rankUpDown = {a4}')
    for row in return_data3:
        tt_id3 = row[0]

    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/{tt_id}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    try:
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a1,
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
    except Exception as e:
        print(Exception, e)
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a1,
                        data.get("imDbId"),
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"))
    conn.commit()
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/{tt_id1}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    try:
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a2,
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
    except Exception as e:
        print(Exception, e)
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a2,
                        data.get("imDbId"),
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"))
    conn.commit()
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/{tt_id2}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    try:
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a3,
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
    except Exception as e:
        print(Exception, e)
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a3,
                        data.get("imDbId"),
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"))
    conn.commit()
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/{tt_id3}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    try:
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a4,
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
    except Exception as e:
        print(Exception, e)
        cursor.execute("""INSERT INTO movie_user_ratings (rankUpDown, pop_movie_id, totalRating, totalRatingVotes, 
        rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, rating8Votes, rating7percent, 
        rating7Votes, rating6percent, rating6Votes,rating5percent, rating5Votes, rating4percent, rating4Votes, 
        rating3percent, rating3Votes, rating2percent, rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, 
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (a4,
                        data.get("imDbId"),
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0",
                        "0"))
    conn.commit()


def setup_most_popular_tv_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""DROP TABLE IF EXISTS most_popular_tv_shows""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS most_popular_tv_shows(pop_tv_id TEXT PRIMARY KEY,
                        rank INTEGER NOT NULL,
                        rankUpDown INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        fullTitle TEXT NOT NULL,
                        year TEXT NOT NULL,
                        crew TEXT NOT NULL,
                        imDbRating TEXT NOT NULL,
                        imDbRatingCount TEXT NOT NULL);""")
    conn.commit()


def populate_most_popular_tv_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    loc = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    for i in range(0, 100):
        cursor.execute("""INSERT INTO most_popular_tv_shows (pop_tv_id, rank, rankUpDown, title, fullTitle, year, crew, 
        imDbRating, imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (data.get("items")[i].get("id"),
                        int(data.get("items")[i].get("rank")),
                        int((data.get("items")[i].get("rankUpDown").replace(',', ''))),
                        data.get("items")[i].get("title"),
                        data.get("items")[i].get("fullTitle"),
                        data.get("items")[i].get("year"),
                        data.get("items")[i].get("crew"),
                        data.get("items")[i].get("imDbRating"),
                        data.get("items")[i].get("imDbRatingCount")
                        ))
    conn.commit()


def test_size1(cursor: sqlite3.Cursor):
    result = cursor.execute(f'SELECT COUNT(movies250_id) FROM top250_movies;')
    for column in result:
        print(f'{column[0]}')
        final_result = column[0]
        return final_result


def test_size2(cursor: sqlite3.Cursor):
    result = cursor.execute(f'SELECT COUNT(pop_movie_id) FROM most_popular_movies;')
    for column in result:
        print(f'{column[0]}')
        final_result = column[0]
        return final_result


def test_size3(cursor: sqlite3.Cursor):
    result = cursor.execute(f'SELECT COUNT(pop_tv_id) FROM most_popular_tv_shows;')
    for column in result:
        print(f'{column[0]}')
        final_result = column[0]
        return final_result


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
    setup_top250_movies(curs, conn)
    populate_top250_movies(curs, conn)
    setup_most_popular_movies(curs, conn)
    setup_movie_user_ratings(curs, conn)
    populate_most_popular_movies(curs, conn)
    populate_rankings_movie(curs, conn)
    setup_most_popular_tv_shows(curs, conn)
    populate_most_popular_tv_shows(curs, conn)
    test_size1(curs)
    test_size2(curs)
    test_size3(curs)


main()

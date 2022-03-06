# Ninth automated test
# saving to multiple data to the database
# testing that cross over is identified properly by query
import sqlite3
from typing import Tuple


def test_main():
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

        cursor.execute("""INSERT INTO test_top250_tv_shows (id, title, fullTitle, year, crew, imDbRating, 
        imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?)""", (data.get("items")[0].get("id"),
                                                           data.get("items")[0].get("title"),
                                                           data.get("items")[0].get("fullTitle"),
                                                           data.get("items")[0].get("year"),
                                                           data.get("items")[0].get("crew"),
                                                           data.get("items")[0].get("imDbRating"),
                                                           data.get("items")[0].get("imDbRatingCount")
                                                           ))
        conn.commit()

        test_close_db(conn)
        conn, cursor = test_open_db('test_250.db')
        cursor.execute("""DROP TABLE IF EXISTS test_most_popular_tv_shows""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS test_most_popular_tv_shows(pop_tv_id TEXT PRIMARY KEY,
                                        rankUpDown INTEGER NOT NULL,
                                        rank INTEGER NOT NULL,
                                        title TEXT NOT NULL,
                                        fullTitle TEXT NOT NULL,
                                        year TEXT NOT NULL,
                                        crew TEXT NOT NULL,
                                        imDbRating TEXT NOT NULL,
                                        imDbRatingCount TEXT NOT NULL);""")
        conn.commit()

        data = {
            "items": [{"id": "tt5555543", "rankUpDown": "+123", "rank": "301", "title": "Popular",
                       "fullTitle": "Popular Show (2022)",
                       "year": "2022", "crew": "Me", "imDbRating": "7.5",
                       "imDbRatingCount": "0.5"}, {"id": "tt5555542", "rankUpDown": "-6,999", "rank": "28",
                                                   "title": "Ugh", "fullTitle": "Ugh Why (2022)",
                                                   "year": "2022", "crew": "Spring Semester", "imDbRating": "2.5",
                                                   "imDbRatingCount": "1"},
                      {"id": "tt5555544", "rankUpDown": "+13", "rank": "36", "title": "Chicken",
                       "fullTitle": "Chicken is good (2022)",
                       "year": "2022", "crew": "Me", "imDbRating": "6.5",
                       "imDbRatingCount": "1.23"},
                      {"id": "tt5555545", "rankUpDown": "-1", "rank": "465", "title": "La La",
                       "fullTitle": "La La La (2022)",
                       "year": "2022", "crew": "Me", "imDbRating": "4.5",
                       "imDbRatingCount": "1.23"},
                      {"id": "tt5555546", "rankUpDown": "3", "rank": "567", "title": "Bah",
                       "fullTitle": "Bah Oh (2022)",
                       "year": "2022", "crew": "Me", "imDbRating": "9.5",
                       "imDbRatingCount": "20"},
                      {"id": "tt5555555", "rankUpDown": "+14", "rank": "300", "title": "Capstone",
                       "fullTitle": "Capstone (2020)",
                       "year": "2020", "crew": "Miserable Students", "imDbRating": "8.5",
                       "imDbRatingCount": "64"}]}
        for i in range(0, 6):
            cursor.execute("""INSERT INTO test_most_popular_tv_shows (pop_tv_id, rankUpDown, rank, title, fullTitle, 
                    year, crew, imDbRating, imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           (data.get("items")[i].get("id"),
                            int((data.get("items")[i].get("rankUpDown").replace(',', ''))),
                            int(data.get("items")[i].get("rank")),
                            data.get("items")[i].get("title"),
                            data.get("items")[i].get("fullTitle"),
                            data.get("items")[i].get("year"),
                            data.get("items")[i].get("crew"),
                            data.get("items")[i].get("imDbRating"),
                            data.get("items")[i].get("imDbRatingCount")
                            ))
        conn.commit()

        test_close_db(conn)
        conn, cursor = test_open_db('test_250.db')

        cursor.execute('''SELECT test_top250_tv_shows.id, test_most_popular_tv_shows.rank, 
        test_most_popular_tv_shows.rankUpDown, test_most_popular_tv_shows.title, test_top250_tv_shows.year, 
        test_top250_tv_shows.imDbRating, test_top250_tv_shows.imDbRatingCount FROM test_top250_tv_shows INNER 
        JOIN test_most_popular_tv_shows ON test_top250_tv_shows.id = test_most_popular_tv_shows.pop_tv_id''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 1
        data = cursor.execute(f'SELECT test_top250_tv_shows.id, test_most_popular_tv_shows.rank,'
                              f'test_most_popular_tv_shows.rankUpDown, test_most_popular_tv_shows.title, '
                              f'test_top250_tv_shows.year, '
                              f'test_top250_tv_shows.imDbRating, test_top250_tv_shows.imDbRatingCount FROM '
                              f'test_top250_tv_shows INNER '
                              f'JOIN test_most_popular_tv_shows ON test_top250_tv_shows.id = '
                              f'test_most_popular_tv_shows.pop_tv_id')
        for row in data:
            a = f'{row[0]}'
            print(a)
            assert a == "tt5555555"
            b = f'{row[1]}'
            print(b)
            assert b == "300"
            c = f'{row[2]}'
            print(c)
            assert c == "14"
            d = f'{row[3]}'
            print(d)
            assert d == "Capstone"
            e = f'{row[4]}'
            print(e)
            assert e == "2020"
            f = f'{row[5]}'
            print(f)
            assert f == "8.5"
            g = f'{row[6]}'
            print(g)
            assert g == "64"

    def main():
        database = 'test_250.db'
        conn, curs = test_open_db(database)
        test_show_dictionary(curs, conn)

    main()


test_main()

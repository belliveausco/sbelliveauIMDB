# Eighth automated test checks query for ordering by rankUpDown if value is highest or lowest rankUpDown
# asserts right information is added
# test order by rankUpDown where rankUpDown is negative or positive function
import sqlite3
from typing import Tuple


def test_main():
    def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def test_close_db(connection: sqlite3.Connection):
        connection.close()

    def test_write_dictionary(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
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
                       "imDbRatingCount": "20"}]}
        for i in range(0, 5):
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
        conn, cursor = test_open_db('test_popular_tv.db')

        result = cursor.execute(f'SELECT * FROM test_most_popular_tv_shows')
        for row in result:
            print(f'pop_tv_id: {row[0]}\nrankUpDown: {row[1]}\nrank: {row[2]}\ntitle: {row[3]}\nfullTitle: {row[4]}\n'
                  f'year: {row[5]}\n '
                  f'crew: {row[6]}\nimDbRating: {row[7]}\nimDbRatingCount:{row[8]}\n')

        cursor.execute('''SELECT * FROM test_most_popular_tv_shows''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 5
        # this portion validates the correct amount of positive rankUpDown can be identified by the correct query
        cursor.execute(f'SELECT * FROM test_most_popular_tv_shows WHERE rankUpDown>0 ORDER BY rankUpDown DESC')
        results2 = cursor.fetchall()
        print(len(results2))
        assert len(results2) == 3

        # this portion validates the correct amount of negative rankUpDown can be identified by the correct query
        cursor.execute(f'SELECT * FROM test_most_popular_tv_shows WHERE rankUpDown<0 ORDER BY rankUpDown DESC')
        results3 = cursor.fetchall()
        print(len(results3))
        assert len(results3) == 2

    def main():
        database = 'test_popular_tv.db'
        conn, curs = test_open_db(database)
        test_write_dictionary(curs, conn)

    main()


test_main()
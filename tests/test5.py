# Fifth automated test checks new write works
# asserts right information is added
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
                                rankUpDown TEXT NOT NULL,
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
                       "imDbRatingCount": "0.5"}]}

        cursor.execute("""INSERT INTO test_most_popular_tv_shows (pop_tv_id, rankUpDown, title, fullTitle, year, crew, 
                imDbRating, imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                       (data.get("items")[0].get("id"),
                        data.get("items")[0].get("rankUpDown"),
                        data.get("items")[0].get("title"),
                        data.get("items")[0].get("fullTitle"),
                        data.get("items")[0].get("year"),
                        data.get("items")[0].get("crew"),
                        data.get("items")[0].get("imDbRating"),
                        data.get("items")[0].get("imDbRatingCount")
                        ))
        conn.commit()

        test_close_db(conn)
        conn, cursor = test_open_db('test_popular_tv.db')

        result = cursor.execute(f'SELECT * FROM test_most_popular_tv_shows')
        for row in result:
            print(f'pop_tv_id: {row[0]}\nrankUpDown: {row[1]}\ntitle: {row[2]}\nfullTitle: {row[3]}\nyear: {row[4]}\n'
                  f'crew: {row[5]}\nimDbRating: {row[6]}\nimDbRatingCount:{row[7]}\n')

        cursor.execute('''SELECT * FROM test_most_popular_tv_shows''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 1
        cursor.execute('''SELECT pop_tv_id FROM test_most_popular_tv_shows''')
        id_verification = cursor.fetchall()
        test_id = id_verification[0]
        print(test_id[0])
        assert test_id[0] == 'tt5555543'

    def main():
        database = 'test_popular_tv.db'
        conn, curs = test_open_db(database)
        test_write_dictionary(curs, conn)

    main()


test_main()
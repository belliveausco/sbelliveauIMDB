import imdb_setup_database
import sqlite3
from typing import Tuple


def test_main():
    def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def test_show_dictionary(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
        imdb_setup_database.setup_top250_tv_shows(cursor, conn)
        imdb_setup_database.setup_top250_tv_shows(cursor, conn)
        imdb_setup_database.setup_user_ratings(cursor, conn)
        imdb_setup_database.populate_top250_tv_shows(cursor, conn)
        imdb_setup_database.add_wot_top250_tv_shows(cursor, conn)
        cursor.execute('''SELECT * FROM top250_tv_shows''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 251
        imdb_setup_database.populate_no_1_show(cursor, conn)
        imdb_setup_database.populate_no_50_show(cursor, conn)
        imdb_setup_database.populate_no_100_show(cursor, conn)
        imdb_setup_database.populate_no_200_show(cursor, conn)
        imdb_setup_database.populate_wot_show(cursor, conn)
        cursor.execute('''SELECT * FROM user_ratings''')
        results1 = cursor.fetchall()
        print(len(results1))
        assert len(results1) == 5
        imdb_setup_database.setup_top250_movies(cursor, conn)
        imdb_setup_database.populate_top250_movies(cursor, conn)
        cursor.execute('''SELECT * FROM top250_movies''')
        results2 = cursor.fetchall()
        print(len(results2))
        assert len(results2) == 250
        imdb_setup_database.setup_most_popular_movies(cursor, conn)
        imdb_setup_database.setup_movie_user_ratings(cursor, conn)
        imdb_setup_database.populate_most_popular_movies(cursor, conn)
        cursor.execute('''SELECT * FROM most_popular_movies''')
        results3 = cursor.fetchall()
        print(len(results3))
        assert len(results3) == 100
        imdb_setup_database.populate_rankings_movie(cursor, conn)
        cursor.execute('''SELECT * FROM movie_user_ratings''')
        results4 = cursor.fetchall()
        print(len(results4))
        assert len(results4) == 4
        imdb_setup_database.setup_most_popular_tv_shows(cursor, conn)
        imdb_setup_database.populate_most_popular_tv_shows(cursor, conn)
        cursor.execute('''SELECT * FROM most_popular_tv_shows''')
        results5 = cursor.fetchall()
        print(len(results5))
        assert len(results5) == 100

    def main():
        database = 'test_250.db'
        conn, curs = test_open_db(database)
        test_show_dictionary(curs, conn)

    if __name__ == '__main__':
        main()


test_main()

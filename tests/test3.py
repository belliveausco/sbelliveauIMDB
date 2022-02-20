# Third automated test
# Assures test successfully identifies biggest and lowest rankUpDowns
# Includes happy and bad path test for rankings method
import sqlite3
from typing import Tuple


def test_main():
    def test_open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)
        cursor = db_connection.cursor()
        return db_connection, cursor

    def test_close_db(connection: sqlite3.Connection):
        connection.close()

    def test_fake_dictionary(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
        cursor.execute("""DROP TABLE IF EXISTS test_popular_movies""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS test_popular_movies(pop_movie_id TEXT PRIMARY KEY,
                                rankUpDown INTEGER NOT NULL,
                                title TEXT NOT NULL,
                                fullTitle TEXT NOT NULL,
                                year TEXT NOT NULL,
                                crew TEXT NOT NULL,
                                imDbRating TEXT NOT NULL,
                                imDbRatingCount TEXT NOT NULL);""")
        conn.commit()

        data = {
            "items": [{"id": "tt5555551", "rank": "23", "rankUpDown": "-2,999", "title": "OMG",
                       "fullTitle": "OMG My Back is Killing Me (2022)", "year": "2022", "crew": "Complainers",
                       "imDbRating": "4.5", "imDbRatingCount": "3"}, {"id": "tt5555545", "rank": "3",
                                                                      "rankUpDown": "5676", "title": "BTW",
                                                                      "fullTitle": "BTW TESTING IS WHACK (2022)",
                                                                      "year": "2022", "crew": "Strangers",
                                                                      "imDbRating": "7.5", "imDbRatingCount": "67"},
                      {"id": "tt5555544", "rank": "15",
                       "rankUpDown": "0", "title": "Okay",
                       "fullTitle": "Okay, But Really (2022)",
                       "year": "2022", "crew": "People",
                       "imDbRating": "9.5", "imDbRatingCount": "98649"}, {"id": "tt5555678", "rank": "6",
                                                                          "rankUpDown": "+67", "title": "You're Joking",
                                                                          "fullTitle": "You're Joking (2022)",
                                                                          "year": "2022", "crew": "Pupils",
                                                                          "imDbRating": "6.5", "imDbRatingCount": "98"},
                      {"id": "tt5555597", "rank": "7",
                       "rankUpDown": "78", "title": "Umm",
                       "fullTitle": "Umm, Last One (2022)",
                       "year": "2022", "crew": "Human",
                       "imDbRating": "4.9", "imDbRatingCount": "9797"}]}

        for i in range(0, 5):
            cursor.execute("""INSERT INTO test_popular_movies (pop_movie_id, rankUpDown, title, fullTitle, year, crew, 
                    imDbRating, imDbRatingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                           (data.get("items")[i].get("id"),
                            int((data.get("items")[i].get("rankUpDown").replace(',', ''))),
                            data.get("items")[i].get("title"),
                            data.get("items")[i].get("fullTitle"),
                            data.get("items")[i].get("year"),
                            data.get("items")[i].get("crew"),
                            data.get("items")[i].get("imDbRating"),
                            data.get("items")[i].get("imDbRatingCount")
                            ))
        conn.commit()

        test_close_db(conn)
        conn, cursor = test_open_db('test_popular_movies.db')

        cursor.execute("""DROP TABLE IF EXISTS test_movie_user_ratings""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS test_movie_user_ratings(rankUpDown TEXT,
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
                                        FOREIGN KEY (pop_movie_id) REFERENCES test_most_popular_movies(id)
                                        );""")
        conn.commit()

        a = list()
        for i in range(0, 5):
            a.append(int((data.get("items")[i].get("rankUpDown").replace(',', ''))))
            a.sort()
        a4 = a[0]
        a3 = a[2]
        a2 = a[3]
        a1 = a[4]
        return_data = cursor.execute(f'SELECT * from test_popular_movies WHERE rankUpDown = {a1}')
        for row in return_data:
            tt_id = row[0]
            assert tt_id == "tt5555545"
            if tt_id == "tt5555545":
                test_data4 = {"imDbId": "tt5555545", "title": "BTW", "fullTitle": "BTW TESTING IS WHACK (2022)",
                              "type": "Movie", "year": "2022", "totalRating": "0", "totalRatingVotes": "27171",
                              "ratings": [{"rating": "10", "percent": "7.7%", "votes": "2080"}, {"rating": "9",
                                                                                                 "percent": "10.9%",
                                                                                                 "votes": "2958"},
                                          {"rating": "8", "percent": "28.8%", "votes": "7838"},
                                          {"rating": "7", "percent": "29.8%", "votes": "8086"},
                                          {"rating": "6", "percent": "12.8%",
                                           "votes": "3471"}, {"rating": "5", "percent": "4.8%", "votes": "1304"},
                                          {"rating": "4",
                                           "percent": "2.0%", "votes": "553"},
                                          {"rating": "3", "percent": "1.0%", "votes": "282"},
                                          {"rating": "2", "percent": "0.8%", "votes": "220"},
                                          {"rating": "1", "percent": "1.4%",
                                           "votes": "379"}], "errorMessage": ""}
                try:
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a1,
                                    test_data4.get("imDbId"),
                                    test_data4.get("totalRating"),
                                    test_data4.get("totalRatingVotes"),
                                    test_data4.get("ratings")[0].get("percent"),
                                    test_data4.get("ratings")[0].get("votes"),
                                    test_data4.get("ratings")[1].get("percent"),
                                    test_data4.get("ratings")[1].get("votes"),
                                    test_data4.get("ratings")[2].get("percent"),
                                    test_data4.get("ratings")[2].get("votes"),
                                    test_data4.get("ratings")[3].get("percent"),
                                    test_data4.get("ratings")[3].get("votes"),
                                    test_data4.get("ratings")[4].get("percent"),
                                    test_data4.get("ratings")[4].get("votes"),
                                    test_data4.get("ratings")[5].get("percent"),
                                    test_data4.get("ratings")[5].get("votes"),
                                    test_data4.get("ratings")[6].get("percent"),
                                    test_data4.get("ratings")[6].get("votes"),
                                    test_data4.get("ratings")[7].get("percent"),
                                    test_data4.get("ratings")[7].get("votes"),
                                    test_data4.get("ratings")[8].get("percent"),
                                    test_data4.get("ratings")[8].get("votes"),
                                    test_data4.get("ratings")[9].get("percent"),
                                    test_data4.get("ratings")[9].get("votes")))
                except Exception as e:
                    print(Exception, e)
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a1,
                                    test_data4.get("imDbId"),
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
        return_data1 = cursor.execute(f'SELECT * from test_popular_movies WHERE rankUpDown = {a2}')
        for row in return_data1:
            tt_id1 = row[0]
            assert tt_id1 == "tt5555597"
            if tt_id1 == "tt5555597":
                test_data1 = {"imDbId": "tt5555597", "title": "OMG", "fullTitle": "OMG My Back is Killing Me (2022)",
                              "type": "Movie", "year": "2022", "totalRating": "0", "totalRatingVotes": "null",
                              "ratings": [{"rating": "10", "percent": "0", "votes": "0"}, {"rating": "9",
                                                                                           "percent": "0",
                                                                                           "votes": "0"},
                                          {"rating": "8", "percent": "0", "votes": "0"},
                                          {"rating": "7", "percent": "0", "votes": "0"},
                                          {"rating": "6", "percent": "0",
                                           "votes": "0"}, {"rating": "5", "percent": "0", "votes": "0"},
                                          {"rating": "4",
                                           "percent": "0", "votes": "0"},
                                          {"rating": "3", "percent": "0", "votes": "0"},
                                          {"rating": "2", "percent": "0", "votes": "0"},
                                          {"rating": "1", "percent": "0",
                                           "votes": "0"}], "errorMessage": ""}
                try:
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a2,
                                    test_data1.get("imDbId"),
                                    test_data1.get("totalRating"),
                                    test_data1.get("ratings")[0].get("percent"),
                                    test_data1.get("ratings")[0].get("votes"),
                                    test_data1.get("ratings")[1].get("percent"),
                                    test_data1.get("ratings")[1].get("votes"),
                                    test_data1.get("ratings")[2].get("percent"),
                                    test_data1.get("ratings")[2].get("votes"),
                                    test_data1.get("ratings")[3].get("percent"),
                                    test_data1.get("ratings")[3].get("votes"),
                                    test_data1.get("ratings")[4].get("percent"),
                                    test_data1.get("ratings")[4].get("votes"),
                                    test_data1.get("ratings")[5].get("percent"),
                                    test_data1.get("ratings")[5].get("votes"),
                                    test_data1.get("ratings")[6].get("percent"),
                                    test_data1.get("ratings")[6].get("votes"),
                                    test_data1.get("ratings")[7].get("percent"),
                                    test_data1.get("ratings")[7].get("votes"),
                                    test_data1.get("ratings")[8].get("percent"),
                                    test_data1.get("ratings")[8].get("votes"),
                                    test_data1.get("ratings")[9].get("percent"),
                                    test_data1.get("ratings")[9].get("votes")))
                except Exception as e:
                    print(Exception, e)
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a2,
                                    test_data1.get("imDbId"),
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
        return_data2 = cursor.execute(f'SELECT * from test_popular_movies WHERE rankUpDown = {a3}')
        for row in return_data2:
            tt_id2 = row[0]
            assert tt_id2 == "tt5555678"
            if tt_id2 == "tt5555678":
                test_data2 = {"imDbId": "tt5555678", "title": "You're Joking", "fullTitle": "You're Joking (2022)",
                              "type": "Movie", "year": "2022", "totalRating": "0", "totalRatingVotes": "null",
                              "ratings": [{"rating": "10", "percent": "0", "votes": "0"}, {"rating": "9",
                                                                                           "percent": "0",
                                                                                           "votes": "0"},
                                          {"rating": "8", "percent": "0", "votes": "0"},
                                          {"rating": "7", "percent": "0", "votes": "0"},
                                          {"rating": "6", "percent": "0",
                                           "votes": "0"}, {"rating": "5", "percent": "0", "votes": "0"},
                                          {"rating": "4",
                                           "percent": "0", "votes": "0"},
                                          {"rating": "3", "percent": "0", "votes": "0"},
                                          {"rating": "2", "percent": "0", "votes": "0"},
                                          {"rating": "1", "percent": "0",
                                           "votes": "0"}], "errorMessage": ""}
                try:
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, %, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a3,
                                    test_data2.get("imDbId"),
                                    test_data2.get("totalRating"),
                                    test_data2.get("ratings")[0].get("percent"),
                                    test_data2.get("ratings")[0].get("votes"),
                                    test_data2.get("ratings")[1].get("percent"),
                                    test_data2.get("ratings")[1].get("votes"),
                                    test_data2.get("ratings")[2].get("percent"),
                                    test_data2.get("ratings")[2].get("votes"),
                                    test_data2.get("ratings")[3].get("percent"),
                                    test_data2.get("ratings")[3].get("votes"),
                                    test_data2.get("ratings")[4].get("percent"),
                                    test_data2.get("ratings")[4].get("votes"),
                                    test_data2.get("ratings")[5].get("percent"),
                                    test_data2.get("ratings")[5].get("votes"),
                                    test_data2.get("ratings")[6].get("percent"),
                                    test_data2.get("ratings")[6].get("votes"),
                                    test_data2.get("ratings")[7].get("percent"),
                                    test_data2.get("ratings")[7].get("votes"),
                                    test_data2.get("ratings")[8].get("percent"),
                                    test_data2.get("ratings")[8].get("votes"),
                                    test_data2.get("ratings")[9].get("percent"),
                                    test_data2.get("ratings")[9].get("votes")))
                except Exception as e:
                    print(Exception, e)
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a3,
                                    test_data2.get("imDbId"),
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
        return_data3 = cursor.execute(f'SELECT * from test_popular_movies WHERE rankUpDown = {a4}')
        for row in return_data3:
            tt_id3 = row[0]
            assert tt_id3 == "tt5555551"
            if tt_id3 == "tt5555551":
                test_data = {"imDbId": "tt5555551", "title": "OMG", "fullTitle": "OMG My Back is Killing Me (2022)",
                             "type": "Movie", "year": "2022", "totalRating": "0", "totalRatingVotes": "27171",
                             "ratings": [{"rating": "10", "percent": "7.7%", "votes": "2080"}, {"rating": "9",
                                                                                                "percent": "10.9%",
                                                                                                "votes": "2958"},
                                         {"rating": "8", "percent": "28.8%", "votes": "7838"},
                                         {"rating": "7", "percent": "29.8%", "votes": "8086"},
                                         {"rating": "6", "percent": "12.8%",
                                          "votes": "3471"}, {"rating": "5", "percent": "4.8%", "votes": "1304"},
                                         {"rating": "4",
                                          "percent": "2.0%", "votes": "553"},
                                         {"rating": "3", "percent": "1.0%", "votes": "282"},
                                         {"rating": "2", "percent": "0.8%", "votes": "220"},
                                         {"rating": "1", "percent": "1.4%",
                                          "votes": "379"}], "errorMessage": ""}
                try:
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a4,
                                    test_data.get("imDbId"),
                                    test_data.get("totalRating"),
                                    test_data.get("totalRatingVotes"),
                                    test_data.get("ratings")[0].get("percent"),
                                    test_data.get("ratings")[0].get("votes"),
                                    test_data.get("ratings")[1].get("percent"),
                                    test_data.get("ratings")[1].get("votes"),
                                    test_data.get("ratings")[2].get("percent"),
                                    test_data.get("ratings")[2].get("votes"),
                                    test_data.get("ratings")[3].get("percent"),
                                    test_data.get("ratings")[3].get("votes"),
                                    test_data.get("ratings")[4].get("percent"),
                                    test_data.get("ratings")[4].get("votes"),
                                    test_data.get("ratings")[5].get("percent"),
                                    test_data.get("ratings")[5].get("votes"),
                                    test_data.get("ratings")[6].get("percent"),
                                    test_data.get("ratings")[6].get("votes"),
                                    test_data.get("ratings")[7].get("percent"),
                                    test_data.get("ratings")[7].get("votes"),
                                    test_data.get("ratings")[8].get("percent"),
                                    test_data.get("ratings")[8].get("votes"),
                                    test_data.get("ratings")[9].get("percent"),
                                    test_data.get("ratings")[9].get("votes")))
                except Exception as e:
                    print(Exception, e)
                    cursor.execute("""INSERT INTO test_movie_user_ratings (rankUpDown, pop_movie_id, totalRating, 
                    totalRatingVotes, rating10percent, rating10Votes, rating9percent, rating9Votes, rating8percent, 
                    rating8Votes, rating7percent, rating7Votes, rating6percent, rating6Votes,rating5percent, 
                    rating5Votes, rating4percent, rating4Votes, rating3percent, rating3Votes, rating2percent, 
                    rating2Votes, rating1percent, rating1Votes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                   (a4,
                                    test_data.get("imDbId"),
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

        test_close_db(conn)
        conn, cursor = test_open_db('test_popular_movies.db')
        cursor.execute('''SELECT * FROM test_popular_movies''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 5
        cursor.execute('''SELECT * FROM test_movie_user_ratings''')
        results = cursor.fetchall()
        print(len(results))
        assert len(results) == 4

    def main():
        database = 'test_popular_movies.db'
        conn, curs = test_open_db(database)
        test_fake_dictionary(curs, conn)

    main()


test_main()

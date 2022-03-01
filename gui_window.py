import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sqlite3 as sql
import imdb_setup_database
import the_most_popular_movies_by_ranking


class Window(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()
        # Database tools
        self.cursor = curs
        self.connection = conn

        # GUI Buttons
        self.update_the_data = QPushButton(self)
        self.run_the_data_visualization = QPushButton(self)

        # Window
        self.window = Visualization_Methods(self.connection, self.cursor)
        self.window.hide()
        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("imDb Database")
        self.setGeometry(50, 50, 800, 800)

        # Button Area
        self.update_the_data.setText("Update The Data")
        self.update_the_data.move(200, 360)
        self.update_the_data.resize(180, 40)
        self.update_the_data.clicked.connect(self.update_the_data_clicked)

        self.run_the_data_visualization.setText("Run The Data Visualization")
        self.run_the_data_visualization.move(400, 360)
        self.run_the_data_visualization.resize(180, 40)
        self.run_the_data_visualization.clicked.connect(self.run_the_data_visualization_clicked)

        # Showing Ui
        self.show()

    @staticmethod
    def update_the_data_clicked():
        conn = sql.connect('imDb.db')
        cursor = conn.cursor()
        imdb_setup_database.setup_top250_tv_shows(cursor, conn)
        imdb_setup_database.setup_top250_tv_shows(cursor, conn)
        imdb_setup_database.setup_user_ratings(cursor, conn)
        imdb_setup_database.populate_top250_tv_shows(cursor, conn)
        imdb_setup_database.add_wot_top250_tv_shows(cursor, conn)
        imdb_setup_database.populate_no_1_show(cursor, conn)
        imdb_setup_database.populate_no_50_show(cursor, conn)
        imdb_setup_database.populate_no_100_show(cursor, conn)
        imdb_setup_database.populate_no_200_show(cursor, conn)
        imdb_setup_database.populate_wot_show(cursor, conn)
        imdb_setup_database.setup_top250_movies(cursor, conn)
        imdb_setup_database.populate_top250_movies(cursor, conn)
        imdb_setup_database.setup_most_popular_movies(cursor, conn)
        imdb_setup_database.setup_movie_user_ratings(cursor, conn)
        imdb_setup_database.populate_most_popular_movies(cursor, conn)
        imdb_setup_database.populate_rankings_movie(cursor, conn)
        imdb_setup_database.setup_most_popular_tv_shows(cursor, conn)
        imdb_setup_database.populate_most_popular_tv_shows(cursor, conn)

    def run_the_data_visualization_clicked(self):
        self.window.show()


class Visualization_Methods(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Function windows
        self.window = the_most_popular_movies_by_ranking.App(self.connection, self.cursor)
        self.window.hide()
        '''
        self.window1 = most_popular_movies_by_rankUpDown(self.connection, self.cursor)
        self.window2 = most_popular_tv_by_rank(self.connection, self.cursor)
        self.window3 = most_popular_tv_by_rankUpDown(self.connection, self.cursor)
        self.window4 = pop_movie_rankings(self.connection, self.cursor)
        self.window5 = top_250_tv_show_rankings(self.connection, self.cursor)
        self.window6 = graph_most_popular_movies_moving_up(self.connection, self.cursor)
        self.window7 = graph_most_popular_movies_moving_down(self.connection, self.cursor)
        self.window8 = graph_most_popular_tv_moving_up(self.connection, self.cursor)
        self.window9 = graph_most_popular_tv_moving_down(self.connection, self.cursor)
        self.window10 = top_250_movies_and_most_popular(self.connection, self.cursor)
        self.window11 = top_250_tv_and_most_popular(self.connection, self.cursor)
        self.window1.hide()
        self.window2.hide()
        self.window3.hide()
        self.window4.hide()
        self.window5.hide()
        self.window6.hide()
        self.window7.hide()
        self.window8.hide()
        self.window9.hide()
        self.window10.hide()
        self.window11.hide()
        '''

        # Menu Buttons
        self.test_button = QPushButton(self)

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization")
        self.setGeometry(50, 50, 800, 800)

        self.test_button.resize(500, 30)
        self.test_button.move(150, 50)
        self.test_button.setText('most popular movies sorted by ranking')
        self.test_button.clicked.connect(self.test_button_connection)

        # Showing Ui
        self.show()

    def test_button_connection(self):
        self.window.show()

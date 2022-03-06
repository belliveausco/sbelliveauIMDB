import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sqlite3 as sql
import imdb_setup_database
import the_most_popular_movies_by_ranking
import the_most_popular_movies_by_rankUpDown
import the_most_popular_tv_by_rank
import the_most_popular_tv_by_rankUpDown
import pop_movie_rankings
import top_250_tv_show_rankings
import top_250_tv_shows
import top_250_movies
import graph_presentation
import top_250_movies_and_most_popular
import top_250_tv_and_most_popular


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

        # GUI Buttons
        self.movies = QPushButton(self)
        self.tv_shows = QPushButton(self)
        self.data_analysis = QPushButton(self)

        # Window
        self.window = Movies(self.connection, self.cursor)
        self.window.hide()
        self.window1 = TV_Shows(self.connection, self.cursor)
        self.window1.hide()
        self.window2 = Data_Analysis(self.connection, self.cursor)
        self.window2.hide()

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization Methods")
        self.setGeometry(50, 50, 800, 800)

        # Button Area
        self.movies.setText("Movies")
        self.movies.move(100, 360)
        self.movies.resize(180, 40)
        self.movies.clicked.connect(self.movies_clicked)

        self.tv_shows.setText("TV Shows")
        self.tv_shows.move(300, 360)
        self.tv_shows.resize(180, 40)
        self.tv_shows.clicked.connect(self.tv_shows_clicked)

        self.data_analysis.setText("Data Analysis")
        self.data_analysis.move(500, 360)
        self.data_analysis.resize(180, 40)
        self.data_analysis.clicked.connect(self.data_analysis_clicked)

        # Showing Ui
        self.show()

    def movies_clicked(self):
        self.window.show()

    def tv_shows_clicked(self):
        self.window1.show()

    def data_analysis_clicked(self):
        self.window2.show()


class Movies(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Function windows
        self.window = the_most_popular_movies_by_ranking.App(self.connection, self.cursor)
        self.window.hide()
        self.window1 = the_most_popular_movies_by_rankUpDown.App(self.connection, self.cursor)
        self.window1.hide()
        self.window4 = pop_movie_rankings.App(self.connection, self.cursor)
        self.window4.hide()
        self.window8 = top_250_movies.App(self.connection, self.cursor)
        self.window8.hide()

        # Menu Buttons
        self.test_button = QPushButton(self)
        self.test_button1 = QPushButton(self)
        self.test_button4 = QPushButton(self)
        self.test_button8 = QPushButton(self)

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization")
        self.setGeometry(50, 50, 800, 800)

        self.test_button.resize(500, 30)
        self.test_button.move(150, 100)
        self.test_button.setText('most popular movies sorted by ranking')
        self.test_button.clicked.connect(self.test_button_connection)

        self.test_button1.resize(500, 30)
        self.test_button1.move(150, 150)
        self.test_button1.setText('most popular movies sorted by rankUpDown')
        self.test_button1.clicked.connect(self.test_button1_connection)

        self.test_button4.resize(500, 30)
        self.test_button4.move(150, 300)
        self.test_button4.setText('popular movie ratings')
        self.test_button4.clicked.connect(self.test_button4_connection)

        self.test_button8.resize(500, 30)
        self.test_button8.move(150, 450)
        self.test_button8.setText('top 250 movies')
        self.test_button8.clicked.connect(self.test_button8_connection)

        # Showing Ui
        self.show()

    def test_button_connection(self):
        self.window.show()

    def test_button1_connection(self):
        self.window1.show()

    def test_button4_connection(self):
        self.window4.show()

    def test_button8_connection(self):
        self.window8.show()


class TV_Shows(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Function windows
        self.window2 = the_most_popular_tv_by_rank.App(self.connection, self.cursor)
        self.window2.hide()
        self.window3 = the_most_popular_tv_by_rankUpDown.App(self.connection, self.cursor)
        self.window3.hide()
        self.window5 = top_250_tv_show_rankings.App(self.connection, self.cursor)
        self.window5.hide()
        self.window7 = top_250_tv_shows.App(self.connection, self.cursor)
        self.window7.hide()

        # Menu Buttons
        self.test_button2 = QPushButton(self)
        self.test_button3 = QPushButton(self)
        self.test_button7 = QPushButton(self)
        self.test_button5 = QPushButton(self)

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization")
        self.setGeometry(50, 50, 800, 800)

        self.test_button2.resize(500, 30)
        self.test_button2.move(150, 200)
        self.test_button2.setText('most popular tv shows sorted by ranking')
        self.test_button2.clicked.connect(self.test_button2_connection)

        self.test_button3.resize(500, 30)
        self.test_button3.move(150, 250)
        self.test_button3.setText('most popular tv shows sorted by rankUpDown')
        self.test_button3.clicked.connect(self.test_button3_connection)

        self.test_button7.resize(500, 30)
        self.test_button7.move(150, 350)
        self.test_button7.setText('top 250 tv shows')
        self.test_button7.clicked.connect(self.test_button7_connection)

        self.test_button5.resize(500, 30)
        self.test_button5.move(150, 400)
        self.test_button5.setText('top 250 tv show ratings')
        self.test_button5.clicked.connect(self.test_button5_connection)

        # Showing Ui
        self.show()

    def test_button2_connection(self):
        self.window2.show()

    def test_button3_connection(self):
        self.window3.show()

    def test_button7_connection(self):
        self.window7.show()

    def test_button5_connection(self):
        self.window5.show()


class Data_Analysis(QMainWindow):
    def __init__(self, conn: sqlite3.Connection, curs: sqlite3.Cursor):
        super().__init__()

        # Database tools
        self.cursor = curs
        self.connection = conn

        # Function windows
        self.window6 = graph_presentation.MainWindow(self.connection, self.cursor)
        self.window6.hide()
        self.window9 = top_250_movies_and_most_popular.App(self.connection, self.cursor)
        self.window9.hide()
        self.window10 = top_250_tv_and_most_popular.App(self.connection, self.cursor)
        self.window10.hide()

        # Menu Buttons
        self.test_button6 = QPushButton(self)
        self.test_button9 = QPushButton(self)
        self.test_button10 = QPushButton(self)

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization")
        self.setGeometry(50, 50, 800, 800)

        self.test_button6.resize(500, 30)
        self.test_button6.move(150, 500)
        self.test_button6.setText('graphical presentation of data')
        self.test_button6.clicked.connect(self.test_button6_connection)

        self.test_button9.resize(500, 30)
        self.test_button9.move(150, 550)
        self.test_button9.setText('top250 movies and most popular movies')
        self.test_button9.clicked.connect(self.test_button9_connection)

        self.test_button10.resize(500, 30)
        self.test_button10.move(150, 600)
        self.test_button10.setText('top250 tv shows and most popular tv shows')
        self.test_button10.clicked.connect(self.test_button10_connection)

        # Showing Ui
        self.show()

    def test_button6_connection(self):
        self.window6.show()

    def test_button9_connection(self):
        self.window9.show()

    def test_button10_connection(self):
        self.window10.show()

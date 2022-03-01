import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
import pandas as pd
import sqlite3 as sql
import imdb_setup_database
import sys


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
        '''
        self.window = most_popular_movies_by_ranking(self.connection, self.cursor)
        self.window = most_popular_movies_by_rankUpDown(self.connection, self.cursor)
        '''

        # Setting up UI
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Data Visualization")
        self.setGeometry(50, 50, 800, 800)

        # Showing Ui
        self.show()

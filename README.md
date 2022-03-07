'''
# sbelliveauIMDB
Scott Belliveau

any install and run directions I need.
external applications specified as needed:
import sqlite3
from typing import Tuple
import requests
import secrets
import PyQt5
import pyqtgraph

Test 6 checks query that orders tables based on ranking, Test 7 checks query that orders tables by rankUpDown, Test 8 checks function that records how many psotive or negative movers are found within tables and Test 9 checks cross over query and uses mutiple assertions to test its accuracy

The project adds a visual element to the database and organizes the gui application from updating the data (which calls methods to from imdb setupd database file), and data visualization. It then organizes data visualization into categories from Movies, TV Shows and Data Analysis.

The main files are main.py, guiwindow.py although it has elements from the_most_popular_movies_by_ranking.py, the_most_popular_movies_by_rankUpDown.py, the_most_popular_tv_by_rank.py, the_most_popular_tv_by_rankUpDown.py, pop_movie_rankings.py
, top_250_tv_show_rankings.py, top_250_tv_shows.py, top_250_movies.py, graph_presentation.py, top_250_movies_and_most_popular.py
, top_250_tv_and_most_popular.py. NOTE: Must run main.py to run guiwindow.py

LOOK AT GUI DETAILED MANUAL TEST for information regarding expected experience for user using this graphical user inteface

a brief description of what is missing from the project (if anything)
Fucntion that allows user to see ratings if selecting a column attempted to do this with seperate textbox but ran into many errors so I included them as their own button/window/function.
'''

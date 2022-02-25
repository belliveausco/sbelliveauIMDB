'''
# sbelliveauIMDB
Scott Belliveau

any install and run directions I need.
external applications specified as needed:
import sqlite3
from typing import Tuple
import requests
import secrets

Test3 assures method for extracting the correct rankUpDowns works properly and database will generate the correct output. Test4 checks the existing tables exist for top 250 movies, popular movies and popular tv shows. Test5 test the excution of a write function and ensures correct info is added.

a brief description of what your project does
The project adds new tables to existing database such as rankings for movies, top 250 movies, popular movies, popular tv shows and test functions inside of project. 

a very brief discussion of your database layout and the table(s) you used
The tables made are top250_tv_shows, user_ratings, movie user ratings, top 250 movies, popular movies and popular tv shows. The top250_tv_shows contain all 250 top tv titles and the user_ratings contain all user rankings. sqlite3 was utilized, functions like create table if not exists and drop table if exist were used. Used cursor, conn. Popular moviesand popular tv shows includes rankupdowns. The function used to check the values was converting values to proper ints and taking a list and sorting and indexing them.

a brief description of what is missing from the project (if anything)
Test that runs tables and checks foreign keys are working properly is missing couldn't resolve how to use sqlite master, would tell me tables did not exist and had issues with syntax. All other test work properly but could not upload to github as unit tests, so changed them to regular for pushing purposes.
'''

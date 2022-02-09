'''
# sbelliveauIMDB
Scott Belliveau

any install and run directions I need.
external applications specified as needed:
(could not push a requirements.txt)
import sqlite3
from typing import Tuple
import requests
import secrets

For automated test1 and test2, must run separately on their own for testing, test1 test the portion that grabs data as feature in the populatetop250shows function, exit code 0 confirms that it returns a length of 250 as achieved by the result variable that counts how many ids are receieved in the data. test2 will take the same methods feature in thetop250show build and insert functions and present how data is added correctly

a brief description of what your project does
The project formats a database, creates functions that insert data and creates tables. It also adds wheel of time in separate function to avoid any issues with foreign keys shared between top250shows and rankings table. 

a very brief discussion of your database layout and the table(s) you used
The tables made are top250_tv_shows and user_ratings. The top250_tv_shows contain all 250 top tv titles and the user_ratings contain all user rankings. sqlite3 was utilized, functions like create table if not exists and drop table if exist were used. Used cursor, conn.

a brief description of what is missing from the project (if anything)
Nothing is missing, test1 will confirm a value of 250 is achieved from the data.
'''

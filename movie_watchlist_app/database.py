

import datetime
import sqlite3
create_movie_table = """
create table if not exists movie (

title text,
release_timestamp real,
watched Integer
);

"""
INSERT_MOVIES = "Insert into movie(title,release_timestamp,watched) values(?,?,0);"
SELECT_MOVIES = "select * from movie;"
SELECT_UPCOMING_MOVIES = "select * from movie where release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "select * from movie where  watched =1;"
SET_MOVIE_WATCHED = "UPDATE movie set watched =1 where title = ?;"
connection = sqlite3.connect("movies.db")


def create_tables():
    with connection:
        connection.execute(create_movie_table)

def add_movie(title,release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES,(title,release_timestamp))
def get_movies(upcoming = False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            #timestamp method allow us to get number of seconds
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES,(today_timestamp))

        else:
            cursor.execute(SELECT_MOVIES)
        return cursor.fetchall()
    
def watch_movie(title):
    with connection:
        connection.execute(SET_MOVIE_WATCHED,(title,))
def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()
    

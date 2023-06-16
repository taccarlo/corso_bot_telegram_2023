#!/usr/bin /python

import sqlite3
db = sqlite3.connect("./chinook.db")
print("Opened database successfully");

try:
    cursor = db.cursor()
    #query ="select * from tracks limit 10"
    query = "select * from tracks inner join albums on tracks.AlbumId = albums.AlbumId limit 1"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
except sqlite3.Error as sqlerror:
    print("Error while connecting to sqlite", sqlerror)

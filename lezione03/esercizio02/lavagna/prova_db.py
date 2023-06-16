#!/usr/bin /python

import sqlite3
db = sqlite3.connect("./chinook.db")
#db = sqlite3.connect("weather.db")
print("Opened database successfully");

try:
    cursor = db.cursor()
    #query = "SELECT Data, Ora,Wind  from  dump_dati_stazioni_VR where wind > 300"
    #query = "select name, Milliseconds from tracks where Milliseconds<180000 ORDER BY Name DESC limit 3"
    query = "select * from tracks inner join albums on tracks.AlbumId = albums.AlbumId limit 10"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
except sqlite3.Error as sqlerror:
    print("Error while connecting to sqlite", sqlerror)

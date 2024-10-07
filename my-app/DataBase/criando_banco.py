import sqlite3 as sq

conn = sq.connect("my-app/DataBase/mydocutor.db")

cursor = conn.cursor()

cursor.close()
conn.close()
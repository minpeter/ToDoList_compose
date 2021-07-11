import sqlite3

conn = sqlite3.connect("todo.db")

cur = conn.cursor()

# init db table
cur.execute("create table user (id integer primary key autoincrement, name text, passwordH int, email text)")
cur.execute("create table todolist (id integer primary key autoincrement, userid int, todo text, endday int, importance int, complete BOOLEAN DEFAULT(FALSE))")
conn.commit()
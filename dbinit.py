import sqlite3

conn = sqlite3.connect("todo.db")

cur = conn.cursor()

# init db table
cur.execute("create table user (id integer primary key autoincrement, name text, passwordH int, email text)")
cur.execute("create table todolist (id integer primary key autoincrement, userid int, todo text, endday int, importance int)")
conn.commit()

cur.execute("insert into user (name, passwordH, email) values ('minpeter', 'testpw', 'test@test.com')")
cur.execute("insert into todolist (userid, todo, endday, importance) values ('1', 'todolist 완성', 2021711, 0)")
conn.commit()

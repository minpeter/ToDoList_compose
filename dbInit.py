import sqlite3

conn = sqlite3.connect("todo.db")

cur = conn.cursor()

# init db table
cur.execute("create table user (id int, name text, passwordH int, email text)")
cur.execute("create table todolist (id int, todo text, endday int, importance int)")
conn.commit()

cur.execute("insert into user values (?, ?, ?, ?)", (1, 'minpeter', 'testpw', 'test@test.com'))
cur.execute("insert into todolist values (?, ?, ?, ?)", ('1', 'todolist 완성', 2021711, 0))
conn.commit()
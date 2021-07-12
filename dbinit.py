import sqlite3

conn = sqlite3.connect("todo.db")

cur = conn.cursor()

# init db table
cur.execute("create table user (userid integer primary key autoincrement, name text, password text);")
cur.execute("create table todo (id int, userid int, todo text, complete BOOLEAN DEFAULT(FALSE));")
conn.commit()


cur.execute("insert into user (name, password) values ('minpeter','testpw');") #userid(auto), username, password
cur.execute("insert into todo (id, userid, todo) values (1, 1,'test Query todo');") # post id, user id, todo text, complete (auto)
conn.commit()
import sqlite3

conn = sqlite3.connect("todo.db")
cur = conn.cursor()

def addUser(name, passwordH, email):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (1,):
        print("동일한 이름의 유저가 존재합니다")
    elif cur.execute(f"select EXISTS (select * from user where email='{email}');").fetchone() == (1,):
        print("동일한 이메일의 유저가 존재합니다.")
    else:
        print("신규유저!!")
        cur.execute(f"insert into user (name, passwordH, email) values ('{name}','{passwordH}','{email}')")
        print("등록성공!")
        conn.commit()
        
def login(name, passwordH):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (0,):
        print("사용자명을 다시 확인해주세요")
    elif cur.execute(f"select EXISTS (select * from user where name ='{name}' AND passwordH = '{passwordH}');").fetchone() == (0,):
        print("패스워드가 일치하지 않습니다.")
    else:
        print("사용자명과 패스워드 일치")
        cur.execute(f"select id from user where name ='{name}' AND passwordH = '{passwordH}'")
        return cur.fetchone()[0]

def addTodo(userid, todo, endday, importance):
    cur.execute(f"insert into user (userid, todo, endday, importance) values ({userid},'{todo}','{endday}','{importance}')")
    print("등록성공!")
    conn.commit()

def readTodo(userid):
    cur.execute(f"select * from todolist where userid ='{userid}'")
    return cur.fetchone()

def delTodo()
import sqlite3

conn = sqlite3.connect("todo.db")
cur = conn.cursor()

def addUser(id, name, passwordH, email):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (1,):
        print("동일한 이름의 유저가 존재합니다")
    elif cur.execute(f"select EXISTS (select * from user where email='{email}');").fetchone() == (1,):
        print("동일한 이메일의 유저가 존재합니다.")
    else:
        print("신규유저!!")
        cur.execute(f"insert into user values ({id},'{name}','{passwordH}','{email}')")
        print("등록성공!")
        conn.commit()
        
def login(name, passwordH):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (0,):
        print("사용자명을 다시 확인해주세요")
    elif cur.execute(f"select EXISTS (select * from user where email='{email}');").fetchone() == (1,):
        print("동일한 이메일의 유저가 존재합니다.")
    else:
        print("사용자명과 패스워드 일치")
        # return user id

def addTodo(id, todo, endday, importance):
    cur.execute(f"insert into user values ({id},'{todo}','{endday}','{importance}')")
    print("등록성공!")
    conn.commit()



addUser(3, 'dd', 'testpw', 'test3@test.com')
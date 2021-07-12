import sqlite3

conn = sqlite3.connect("todo.db", check_same_thread=False)
cur = conn.cursor()

def addUser(name, password="default password"):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (1,):
        return {"msg":"동일한 이름의 유저가 존재합니다"}
    else:
        cur.execute(f"insert into user (name, password) values ('{name}','{password}')")
        conn.commit()
        return {"msg":"등록성공"}
        
def login(name, password="default password"):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (0,):
        return {"msg:":"사용자명을 다시 확인해주세요"}
    elif cur.execute(f"select EXISTS (select * from user where name ='{name}' AND password = '{password}');").fetchone() == (0,):
        return {"msg:":"패스워드가 일치하지 않습니다."}
    else:
        cur.execute(f"select id from user where name ='{name}' AND password = '{password}'")
        return {"msg":"로그인성공","userid":cur.fetchone()[0]}


def addTodo(id, userid, todo):
    cur.execute(f"insert into todo (id, userid, todo) values ({id}, {userid},'{todo}')")
    conn.commit()
    return {"msg":"등록성공"}

def readTodo(userid):
    cur.execute(f"select * from todo where userid={userid}")
    readTodoList = []
    rows = cur.fetchall()
    for row in rows:
        rowdict = {"id":row[0],"userid":row[1],"todo":row[2],"complete":row[3]}
        readTodoList.append(rowdict)
    return readTodoList

def delTodo(id, userid):
    cur.execute(f"delete from todo where id={id} AND userid={userid}")
    conn.commit()
    return {"msg":f"유저 {userid}의 {id} todo 삭제 완료"}

def editTodo(id, userid, text):
    cur.execute(f"update todo set todo='{text}' where id='{id}' AND userid='{userid}'")
    conn.commit()
    return {"msg":f"{id} todo의 내용을 '{text}'으로 변경하였습니다"}

def todoComplete(id, userid, complete):
    cur.execute(f"update todo set complete={complete} where id='{id}' AND userid='{userid}'")
    conn.commit()
    return {"msg":f"유저 {userid}의 {id} 할일 완료 상태 {complete==1 if '완료' else '작업중'}로 변경"}

def lastId(userid):
    cur.execute(f"select MAX(id) from todo where userid={userid}")
    lastid = cur.fetchall()
    if lastid[0][0] == None:
        return 0
    else:
        return lastid[0][0]
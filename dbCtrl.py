import sqlite3

conn = sqlite3.connect("todo.db", check_same_thread=False)
cur = conn.cursor()

def addUser(name, passwordH, email):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (1,):
        return {"msg":"동일한 이름의 유저가 존재합니다"}
    elif cur.execute(f"select EXISTS (select * from user where email='{email}');").fetchone() == (1,):
        return {"msg":"동일한 이메일의 유저가 존재합니다."}
    else:
        cur.execute(f"insert into user (name, passwordH, email) values ('{name}','{passwordH}','{email}')")
        conn.commit()
        return {"msg":"등록성공"}
        
def login(name, passwordH):
    if cur.execute(f"select EXISTS (select * from user where name='{name}');").fetchone() == (0,):
        return {"msg:":"사용자명을 다시 확인해주세요"}
    elif cur.execute(f"select EXISTS (select * from user where name ='{name}' AND passwordH = '{passwordH}');").fetchone() == (0,):
        return {"msg:":"패스워드가 일치하지 않습니다."}
    else:
        cur.execute(f"select id from user where name ='{name}' AND passwordH = '{passwordH}'")
        return {"msg":"로그인성공","userid":cur.fetchone()[0]}


def addTodo(userid, todo, endday, importance):
    cur.execute(f"insert into todolist (userid, todo, endday, importance) values ({userid},'{todo}', {endday}, {importance})")
    conn.commit()
    return {"msg":"등록성공"}

def readTodo(userid):
    cur.execute(f"select * from todolist where userid ={userid}")
    readTodoList = []
    rows = cur.fetchall()
    for row in rows:
        rowdict = {"id":row[0],"userid":row[1],"todo":row[2],"endday":row[3],"importance":row[4],"complete":row[5]}
        readTodoList.append(rowdict)
    return readTodoList

def delTodo(id, userid):
    cur.execute(f"delete from todolist where id={id} AND userid={userid}")
    conn.commit()
    return {"msg":f"유저 {userid}의 {id} 할일 삭제 완료"}

def editTodo(id, userid, editSel, text):
    if int(editSel) == 1:
        # edit todo
        cur.execute(f"update todolist set todo='{text}' where id='{id}' AND userid='{userid}'")
        conn.commit()
        return {"msg":f"{id}할일의 내용을 '{text}'으로 변경하였습니다"}
    elif int(editSel) == 2:
        # edit endday
        cur.execute(f"update todolist set endday='{text}' where id='{id}' AND userid='{userid}'")
        conn.commit()
        return {"msg":f"{id}의 마감을 '{text}'으로 변경하였습니다"}
    elif int(editSel) == 3:
        # edit importance
        cur.execute(f"update todolist set importance='{text}' where id='{id}' AND userid='{userid}'")
        conn.commit()
        return {"msg":f"{id}의 중요도를 '{text}'으로 변경하였습니다"}
    else:
        return {"msg":"editTodo 어딘가에 문제가 있습니다"}

def todoComplete(id, userid, tf):
    cur.execute(f"update todolist set complete={tf} where id='{id}' AND userid='{userid}'")
    conn.commit()
    return {"msg":f"유저 {userid}의 {id} 할일 완료 상태 {tf}로 변경"}

def lastId(userid):
    cur.execute(f"select * from todolist where userid={userid}")
    row = cur.fetchall()
    return row[-1:][0][0] # last todo id
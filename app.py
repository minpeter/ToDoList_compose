from re import U
import re
from flask import Flask, json, request, jsonify
import dbCtrl

app = Flask (__name__)

@app.route("/addUser", methods = ['POST'])
def AddUser():
    userData = request.get_json()
    returnV = dbCtrl.addUser(userData["userName"], userData["passwordH"], userData["email"])
    return jsonify(returnV)


@app.route("/login", methods = ['POST'])
def Login():
    loginData = request.get_json()
    returnV = dbCtrl.login(loginData["userName"], loginData["passwordH"])
    return jsonify(returnV)

@app.route("/addTodo", methods = ['POST'])
def AddTodo():
    todoData = request.get_json()
    returnV = dbCtrl.addTodo(todoData["userId"], todoData["todo"], todoData["endday"], todoData["importance"])
    return jsonify(returnV)

@app.route("/readTodo", methods = ['POST'])
def ReadTodo():
    todoData = request.get_json()
    returnV = dbCtrl.readTodo(todoData["userId"])
    return jsonify(returnV)

@app.route("/delTodo", methods = ['POST'])
def DelTodo():
    todoData = request.get_json()
    returnV = dbCtrl.delTodo(todoData["id"], todoData["userId"])    
    return jsonify(returnV)

@app.route("/editTodo", methods = ['POST'])
def EditTodo():
    todoData = request.get_json()
    returnV = dbCtrl.editTodo(todoData["id"], todoData["userId"], todoData["editSel"], todoData["text"])    
    return jsonify(returnV)

@app.route("/todoComplete", methods = ['POST'])
def TodoComplete():
    todoData = request.get_json()
    returnV = dbCtrl.todoComplete(todoData["id"], todoData["userId"], todoData["tf"])
    return jsonify(returnV)


if __name__ == '__main__':
    app.run() #host = 0.0.0.0
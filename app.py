from re import U
from flask import Flask, request, jsonify
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

# @app.route("/delTodo", methods = ['POST'])

# @app.route("/editTodo", methods = ['POST'])

# @app.route("/todoComplete", methods = ['POST'])


if __name__ == '__main__':
    app.run() #host = 0.0.0.0
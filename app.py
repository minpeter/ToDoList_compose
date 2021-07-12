from flask import Flask, request, jsonify
from flask_cors import CORS
import dbCtrl

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route("/addUser", methods = ['GET'])
def AddUser():
    userName = request.args.get("userName")
    password = request.args.get("password")
    returnV = dbCtrl.addUser(userName, password)
    return jsonify(returnV)


@app.route("/login", methods = ['GET'])
def Login():
    userName = request.args.get("userName")
    password = request.args.get("password")
    returnV = dbCtrl.login(userName, password)
    return jsonify(returnV)

@app.route("/addTodo", methods = ['GET'])
def AddTodo():
    id = request.args.get("id")
    userId = request.args.get("userId")
    todo = request.args.get("todo")
    returnV = dbCtrl.addTodo(id, userId, todo)
    return jsonify(returnV)

@app.route("/readTodo", methods = ['GET'])
def ReadTodo():
    userId = request.args.get("userId")
    returnV = dbCtrl.readTodo(userId)
    return jsonify(returnV)

@app.route("/delTodo", methods = ['GET'])
def DelTodo():
    id = request.args.get("id")
    userId = request.args.get("userId")
    returnV = dbCtrl.delTodo(id, userId)
    return jsonify(returnV)

@app.route("/editTodo", methods = ['GET'])
def EditTodo():
    id = request.args.get("id")
    userId = request.args.get("userId")
    text = request.args.get("text")
    returnV = dbCtrl.editTodo(id, userId, text)    
    return jsonify(returnV)

@app.route("/todoComplete", methods = ['GET'])
def TodoComplete():
    id = request.args.get("id")
    userId = request.args.get("userId")
    complete = request.args.get("complete")
    returnV = dbCtrl.todoComplete(id, userId, complete)
    return jsonify(returnV)

@app.route("/lastId", methods = ['GET'])
def LastId():
    userId = request.args.get("userId")
    return jsonify(dbCtrl.lastId(userId))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878)
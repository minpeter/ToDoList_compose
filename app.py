from flask import Flask, request, jsonify
from flask_cors import CORS
import dbCtrl

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route("/addUser", methods = ['GET'])
def AddUser():
    userName = request.args.get("userName")
    passwordH = request.args.get("passwordH")
    email = request.args.get("email")
    returnV = dbCtrl.addUser(userName, passwordH, email,)
    return jsonify(returnV)


@app.route("/login", methods = ['GET'])
def Login():
    userName = request.args.get("userName")
    passwordH = request.args.get("passwordH")
    returnV = dbCtrl.login(userName, passwordH)
    return jsonify(returnV)

@app.route("/addTodo", methods = ['GET'])
def AddTodo():
    userId = request.args.get("userId")
    todo = request.args.get("todo")
    endday = request.args.get("endday")
    importance = request.args.get("importance")
    returnV = dbCtrl.addTodo(userId, todo, endday, importance)
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
    editSel = request.args.get("editSel")
    text = request.args.get("text")
    returnV = dbCtrl.editTodo(id, userId, editSel, text)    
    return jsonify(returnV)

@app.route("/todoComplete", methods = ['GET'])
def TodoComplete():
    id = request.args.get("id")
    userId = request.args.get("userId")
    tf = request.args.get("tf")
    returnV = dbCtrl.todoComplete(id, userId, tf)
    return jsonify(returnV)

@app.route("/lastId", methods = ['GET'])
def LastId():
    userId = request.args.get("userId")
    return jsonify(lastId(userId))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878)
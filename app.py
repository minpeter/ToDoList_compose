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

# @app.route("/addTodo")

# @app.route("/readTodo")

# @app.route("/delTodo")

# @app.route("/editTodo")

# @app.route("/todoComplete")


if __name__ == '__main__':
    app.run() #host = 0.0.0.0
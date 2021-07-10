from flask import Flask, request
from flask.json import jsonify

app = Flask (__name__)

@app.route('/environsments/<language>')
def environsments(language):
    return jsonify({"language":language})

@app.route("/todoLogin", method = ['POST'])
def todoLogin():
    user = request.gen_json()
    
    return jsonify(user)

if __name__ == "__main__":
app.run()
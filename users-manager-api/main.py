from crypt import methods
from urllib import response
from util.userDAO import UserDAO
from util.entities.user import User
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
userDAO = UserDAO()

@app.route("/")
def hello_world():
    return "<h1>UsersManager API</h1>"

@app.route("/users/insert", methods=["POST"])
def insertUser():
    record = json.loads(request.data)
    properties = ['firstname','lastname','age','email','phone']
    for property in properties:
        if property not in record:
            response = jsonify({ 'error': property + ' property is missing in body'})
            response.status_code = 400
            return response
    user = User(record["firstname"], record["lastname"], int(record["age"]), record["email"], record["phone"])
    result = userDAO.insertUser(user)
    if result:
        response = jsonify({ 'message': 'success'})
        response.status_code = 200
    else:
        response = jsonify({ 'error': 'insert failed'})
        response.status_code = 400
    return response

@app.route("/users/listAll")
def listUsers():
    return userDAO.listUsers()

@app.route("/users/listById")
def listUser():
    if 'id' in request.args:
        return userDAO.listUser(request.args.get("id"))
    else:
        response = jsonify({ 'error': 'id arg missing'})
        response.status_code = 400
        return response

@app.route("/users/delete", methods=["POST"])
def delete():
    if 'id' in request.args:
        result = userDAO.deleteUser(request.args.get("id"))
        if result:
            response = jsonify({ 'message': 'success'})
            response.status_code = 200
        else:
            response = jsonify({ 'error': 'delete failed'})
            response.status_code = 400
    else:
        response = jsonify({ 'error': 'id arg missing'})
        response.status_code = 400
    return response

@app.route("/users/update", methods=["POST"])
def update():
    record = json.loads(request.data)
    properties = ['firstname','lastname','age','email','phone']
    for property in properties:
        if property not in record:
            response = jsonify({ 'error': property + ' property is missing in body'})
            response.status_code = 400
            return response
    user = User(record["firstname"], record["lastname"], int(record["age"]), record["email"], record["phone"])
    if 'id' in request.args:
        result = userDAO.editUser(user, request.args.get("id"))
        if result:
            response = jsonify({ 'message': 'success'})
            response.status_code = 200
        else:
            response = jsonify({ 'error': 'update failed'})
            response.status_code = 400
    else:
        response = jsonify({ 'error': 'id arg missing'})
        response.status_code = 400
    return response

if __name__ == "__main__":
    app.run(debug=True)
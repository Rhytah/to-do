import json

from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)

from flask_models import Task, User, accounts, tasks, todo, user

app= Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'rhytahz'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] =False
jwt = JWTManager(app)



@app.route('/register',methods=["POST"])
def register():
    req_data = request.get_json()
    name = req_data['name']
    username = req_data['username']
    email = req_data['email']
    password =req_data['password']
    user= [name,username,email,password]
    accounts.append(user)
    return jsonify({'message':f'{username} you have successfully created your account'}),201

@app.route('/login', methods=['POST'])
def login():
    req_data=request.get_json()
    username=req_data['username']
    password =req_data['password']
    
    access_token= create_access_token(identity=username)
    return jsonify(access_token=access_token),200
    # return jsonify({'message':f'{username} you have logged in'})

@app.route('/protected', methods =['GET'])
@jwt_required
def protected():
    #access the identity of current user
    current_user=get_jwt_identity()
    return jsonify(loggesd_in_as=current_user),200

@app.route('/users', methods=['GET'])

def get_users():
    if len(user)<1:
        return jsonify({"message":"There are no registered users"}),404
        
    if len(user)>=1:
        return jsonify({
            "message":"These are the registered users",
            "users":user
        }),200

@app.route('/tasks', methods=["POST"])
@jwt_required
def add_task():
    task_data=request.get_json()
    task_id=len(tasks)+1
    title=task_data['title']
    details=task_data['details']

    new_task={'task_id':task_id, 'title':title, 'details':details}
    todo.append(new_task)

    return jsonify({
        "message":"You have created task"}) , 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])

def delete_a_task(task_id):
    for task in range(len(todo)):
        if task['task_id'] ==task_id:
            del todo[task]
            return"You have deleted {}".format(task)
        
            # return "These are remaining  {}".format(len(todo))
        return "Task non existent"

@app.route('/tasks', methods=['DELETE'])
def delete_all_tasks():
    todo.clear()
    return "You have deleted all tasks"

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_as_finished(task_id):
    task_data=request.get_json()
    task_id=task_data['task_id']
    title=task_data['title']
    
    for task in todo:
        if tasks['task_id'] ==task_id:
            tasks[title]=task+("['Finished']")
            return tasks


if __name__=='__main__':
    # name="Rhytah Namono"
    # accounts=[]
    app.run()

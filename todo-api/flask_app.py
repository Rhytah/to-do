from flask import Flask
from flask import request,jsonify

import json
import re

app= Flask(__name__)

@app.route("/")
def main():
    return "This is Andela"


@app.route('/register',methods=["POST"])
def register():
    req_data = request.get_json()
    name = req_data.get['name']
    username = req_data.get['username']
    email = req_data.get['email']
    password =req_data.get['password']
    new_account= [name,username,email,password]
    accounts.append(new_account)

@app.route('/add/<username>',methods=["GET"])
def add_user(username):
    return "Thanks for signing up"+ username


if __name__=='__main__':
    name="Rhytah Namono"
    accounts=[]
    app.run()
    
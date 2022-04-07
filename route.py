import flask
from flask.json import jsonify
from flask import Blueprint,request

import os,datetime
from pathlib import Path

## example code
## when a machine detect a request, new a person object and call person.mainprocess
## It will return true / false to indicate pass or not
app = Blueprint('receive_and_callback',__name__)

@app.route('/api/upload_picture/login',methods=["GET","POST"])
def login():
    username_password_pair = get_username_password_pair()
    info = verify_identity(username_password_pair)
    
    if(info==""):
        return jsonify({
            "result": "Login success", 
            "reason": ""
        }) 
    else :
        return jsonify({
            "result": "Login Failed", 
            "reason": info
        }) 
    
@app.route('/api/upload_picture',methods=["POST"])
def upload_picture():  
    username_password_pair = get_username_password_pair()
    info = verify_identity(username_password_pair)

    if info!="":
        return jsonify({
            "result": "Login Failed", 
            "reason": info
        }) 

    try:
        file = request.files['zip']
    except:
        return jsonify({
            "result": "unable to get zip", 
            "reason": info
        }) 

    path = "zip_pictures"
    path += os.path.join(path,request.json['email'])
    Path(path).mkdir(parents=True, exist_ok=True)
    path += os.path.join(path, datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')+".zip")
    file.save(path)

    return jsonify({
        "result": "send zip to server successfully", 
        "reason": ""
    }) 

def get_username_password_pair() -> dict:
    username_password_pair = {}
    f = open("user_pass_pair.txt",mode="r")
    lines = f.readlines()
    f.close()
    # print content
    for content in lines:
        usr = content.split("=")[0]
        password = ""
        if(len(content.split("="))>0):
            for i in range(1,len(content.split("="))):
                password+= content.split("=")[i]
            password=password[:-1]
        username_password_pair[usr]=password
    return username_password_pair

def verify_identity(username_password_pair:dict):
    try:
        email = request.json['email']
    except:
        return "we do not get email on your request."

    try:
        password = request.json['password']
    except:
        return "we do not get password on your request."

    if email in username_password_pair.keys() and\
        password == username_password_pair.get(email):
        return ""
    else:
        return "email/password incorrect."



from flask import Flask, url_for
from flask import request
from markupsafe import escape

app = Flask(__name__)#keyword retrun nama file
# app.run(host='127.0.0.1', port=8090)

# request.header.get('your-header-name')
# request.headers('your-header-name')



@app.route("/")
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>', methods = ['GET', 'POST'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s!' %  username #escape(fauzaan)#escape untuk 

@app.route('/user/<int:user_id>')
def greet_userid(user_id):
    return 'hello,' + str(user_id) + '!'



# @app.route('/greet_json')
# def greet_json():
#     return {'message':'Hello, World'}

@app.route('/read_json', methods=["POST"])
def read_json_body():
    body = request.get_json()#{"username":"fauzaan"}/{"foo":"bar"}
    user = body['username']
    return {'mesaage':'hello,' + user + '!'}

# @app.route('/data')
# def data():
#     user = request.args.get('user')

# @app.route("circularPrint/<text>")#pakai reques body
# def circularPrint(text):
#     text = text.upper()
#     count


@app.route('/auth/<name>')
def auth(name):
    ## handling function code
    atuo=request.headers.get("Authorization")
    # print(request.authorization["username"])
    # print(request.authorization["password"])

    # return "ok"
    return { "token":atuo}

import base64
@app.route('/basic64/<self>')
def basic64(self):
    atuo = request.headers.get("Authorization")
    plain = base64.b64decode(atuo[6:]).decode('utf-8')
    return {"token": plain}

# @app.route('/repeated_string/nletter/<int:n>')
# def repeat():


# @app.route('/password/check', methods=["PUT"])
# def password():
#     res=request.header.get("Authorization")
#     a=res.split()
#     user=base64.b64decode(a[-1]).decode('utf-8')

#     b=user.split( : )
#     if b[0] == 'andrew' and b[-1] == 'NotPassword':
#         body=request.get_json()
#         password = body['password']

#         number = "0123456789"
#         lower_case = "abcdefghijklmnopqrstuvwxyz"
#         upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         special_characters = "!@#$%^&*()-+"
#         miss = 0
#         if any(i in number for i in password)==False:
#             miss+=1
#         if any(i in lower_case for i in password)==False:
#             miss+=1
#         if any(i in upper_case for i in password)==False:
#             miss+=1
#         if any(i in special_characters for i in password)==False:
#             miss+=1

#         return {
#             "character to add": max(miss, 6-len(password)) 
#         }




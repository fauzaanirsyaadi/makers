from flask import Flask
from flask import request
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet')
def greet():
    return 'Hi, I am Yanti..'

@app.route('/user/<username>', methods = ['GET', 'POST'])
def show_user_profile(username):
    return 'Hello, %s!' % (username)

@app.route('/userid/<int:post_id>')
def show_post(post_id):
    return 'UserID %d' % post_id

@app.route('/read_json', methods = ["POST"])    #body
def read_json_body():
    body = request.get_json()
    user = body['username']
    return {'message' : 'Hello ' + user + '!'}


@app.route("/hello_auth/<username>", methods = ["GET"])
def hello_auth(username):
    resp = request.headers.get("Authorization")
    res = resp.split(" ")

    token_plained = base64.b64decode(res[-1]).decode('utf-8')
    tikeb = token_plained.split(":")
    
    if tikeb[0] == "yanti" and tikeb[1] == "21051996":
        return "Hello " + username
    else:
        return "Invalid", 401
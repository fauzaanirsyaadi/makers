
from flask import Flask, url_for
from markupsafe import escape
from markupsafe import escape
from flask import Flask
app = Flask(__name__)#keyword retrun nama file

# @app.route('/')
# def hello_world():
#     return 'hello, world'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>', methods = ['GET', 'POST'])
def show_user_profile(username):
    # show the user profile for that user
    # return 'fauzaan'
    return 'User %s!' %  username #escape(fauzaan)#escape untuk 


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d!' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s!' % escape(subpath)
#secara default ini semua menggunakan get


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
        # return show_the_login_form()
        
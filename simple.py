# helpful commands:

# installer:
# pipenv install Flask~=2.2.2

# version checker:
#pipenv run flask --version

# starting application:
# pipenv run flask run or pipenv run flask run -p 5001

# flask installation:
# pipenv install python-dotenv~=0.21

# file server specification (setting env file):
# export FLASK_APP=simple.py

# removing env variables:
# unset FLASK_APP
# unset FLASK_DEBUG

from flask import Flask
# Load configuration class
from config import Config

app = Flask(__name__)
# Apply configuration from class
app.config.from_object(Config)

# Test value of variable that may or may not come from the environment
print("SECRET KEY IS: ", app.config["SECRET_KEY"])


@app.route('/')
def hello():
    # Use configuration variable
    return f'<h1>{app.config["GREETING"]}</h1>'


# app = Flask(__name__)
# # Set configuration variable
# app.config["greeting"] = 'Hey there, humans!'


# @app.route('/')
# def hello():
#     # Use configuration variable
#     return f'<h1>{app.config["greeting"]}</h1>'

# seperate routes
@app.route('/about')
def about():
    return '<h1>About</h1>'

# wildcrad routes
@app.route('/item/<id>')
def item(id):
    return f'<h1>Item {id}</h1>'

@app.before_request
def before_request_function():
    print("before_request is running")


@app.after_request
def after_request_function(response):
    print("after_request is running")
    return response

@app.before_first_request
def before_first_function():
    print("before_first_request happens once")

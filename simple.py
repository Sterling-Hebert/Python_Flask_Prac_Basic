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

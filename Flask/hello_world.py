from werkzeug.wrappers import Request, Response
from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)

#decorator
@app.route("/")

def hello():
    return "Hello World"

if __name__ == "__main__":
    run_simple('localhost',port=9000)





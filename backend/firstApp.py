from flask import Flask
# line below contains a magic variable! Just leave it :-)
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return "Hello, world!"
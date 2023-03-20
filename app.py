from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Checking if every push to your repo will automatically build your app and deploy it in production'

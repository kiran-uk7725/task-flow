from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to TaskFlow!"

@app.route("/about")
def about():
    return "TaskFlow is a task management platform"

@app.route("/health")
def health():
    return "Application is running!"
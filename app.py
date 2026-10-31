from flask import Flask, request

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

@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    print(f"Task ID: {task_id}")
    print(f"Type: {type(task_id)}")

    return {
        "task_id": task_id,
        "message": "Task retrieved successfully"
    }

@app.route("/users/<string:username>")
def get_user(username):
    return f"Hello, {username}"

@app.route("/projects/<int:project_id>/tasks/<int:task_id>")
def get_task_by_project(project_id, task_id):
    return {
        "project_id": project_id,
        "task_id": task_id
    }

@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    if request.method == "POST":
        data = request.json

        title = data.get("title")
        description = data.get("description")
        priority = data.get("priority")

        return {"title": title, "description": description, "priority": priority }

    status = request.args.get("status")
    page = request.args.get("page", default=1, type=int)

    return {"status": status, "page": page}

@app.route("/inspect")
def inspect():

    method = request.method
    content_type = request.headers.get("Content-Type")
    user_agent = request.headers.get("User-Agent")

    return {"method": method, "Content-Type": content_type, "User-Agent": user_agent}







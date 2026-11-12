from flask import Blueprint,abort

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/")
def tasks():
    return {"message": "Fetching all tasks"}, 200

@tasks_bp.route("/<int:task_id>")
def task(task_id):
    if task_id == 101:
        return {"id": 101, "title": "Learn flask", "description": "learn the fundamentals", "priority": "high"}, 200

    abort(404, description="Task doesn't exist")


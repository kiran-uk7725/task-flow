import os
from flask import Flask
from routes import tasks_bp
from config import configurations

def validate_production_secret():
    production_secret = os.environ.get(
        "PROD_SERVICE_SECRET_KEY"
    )

    if not production_secret:
        raise RuntimeError(
            "PROD_SERVICE_SECRET_KEY is required"
        )


def create_app(test_config=None):
    app = Flask(__name__)

    environment = os.environ.get("APP_ENV", "development").strip().lower()

    config_class = configurations.get(environment)

    if config_class is None:
        raise RuntimeError(f"Unknown environment: {environment}")


    app.config.from_object(config_class)

    if test_config is not None:
        app.config.update(test_config)

    if environment == "production":
        validate_production_secret()

    app.register_blueprint(
        tasks_bp,
        url_prefix="/api/tasks"
    )

    return app


# @app.route('/')
# def home():
#     return "Welcome to TaskFlow!"

# @app.route("/about")
# def about():
#     return "TaskFlow is a task management platform."

# @app.route("/health")
# def health():
#     response = make_response({
#     "message": "Application is healthy"
#     },200)

#     response.headers["X-Application"] = "TaskFlow"

#     return response

# @app.route("/tasks/<int:task_id>")
# def get_task(task_id):

#     if task_id == 101:
#         return {
#             "id": 101,
#             "title": "Learn flask",
#             "priority": "high"
#         }, 200

#     abort(404, description="Task doesn't exist")

# @app.route("/users/<string:username>")
# def get_user(username):
#     return f"Hello, {username}"

# @app.route("/projects/<int:project_id>/tasks/<int:task_id>")
# def get_task_by_project(project_id, task_id):
#     return {
#         "project_id": project_id,
#         "task_id": task_id
#     }

# @app.route("/tasks", methods=["GET", "POST"])
# def tasks():

#     if request.method == "POST":
#         if not request.is_json:
#             abort(415, description="JSON is required")

#         data = request.get_json()

#         if not isinstance(data, dict):
#             abort(400, description="Expected JSON object")

#         title = data.get("title")

#         if not isinstance(title, str) or not title.strip():
#             abort(400, description="Title must be not empty string")

#         priority = data.get("priority", "medium")

#         return {"id": 101, "title": title.strip(), "priority": priority }, 201

#     status = request.args.get("status")
#     page = request.args.get("page", default=1, type=int)

#     return {"status": status, "page": page}

# @app.route("/inspect")
# def inspect():

#     method = request.method
#     content_type = request.headers.get("Content-Type")
#     user_agent = request.headers.get("User-Agent")

#     return {"method": method, "Content-Type": content_type, "User-Agent": user_agent}

# @app.errorhandler(404)
# def not_found(error):
#     return {
#     "error": "Resource not found",
#     "status": 404
#     }, 404



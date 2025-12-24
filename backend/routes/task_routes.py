
from flask import Blueprint, jsonify
from services.task_service import TaskService
from services.project_service import ProjectService

task_bp = Blueprint("tasks", __name__)
taskService = TaskService()
projectService = ProjectService()

@task_bp.route("/projects/<int:project_id>/tasks", methods=["GET"])
def get_tasks_by_project(project_id):
    tasks = taskService.list_tasks_by_project(project_id)
    return jsonify(tasks)


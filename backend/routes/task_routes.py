
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

@task_bp.route('/projects/<int:project_id>/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(project_id, task_id):
    # project = projectService.get_by_id(project_id)
    task = taskService.get_task(project_id, task_id)

    if task is None:
        return jsonify({'Error':'Task não existe para esse projeto'}), 404
    
    return jsonify(task)
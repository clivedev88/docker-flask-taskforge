from flask import Blueprint, jsonify
from services.project_service import ProjectService

project_bp = Blueprint('projects', __name__)
service = ProjectService()

@project_bp.route('/projects', methods=['GET'])
def get_projects():
    projects = service.list_projects()
    return jsonify(projects)
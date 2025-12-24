from flask import Blueprint, jsonify
from services.project_service import ProjectService

project_bp = Blueprint('project', __name__)
service = ProjectService()

@project_bp.route('/projects',  methods=['GET'])
def get_all_projects():
    projects = service.get_projects()
    return jsonify(projects)

@project_bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    project = service.get_by_id(project_id)
    # if project is None:
    #     return jsonify({'Error':'Projeto não existe'}), 404
    return jsonify(project)
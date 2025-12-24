from repositories.project_repository import ProjectRepository

class ProjectService():
    def __init__(self):
        self.repository = ProjectRepository()
    def get_projects(self):
        return self.repository.get_all_projects()
    def get_by_id(self, project_id):
        return self.repository.get_project_by_id(project_id)
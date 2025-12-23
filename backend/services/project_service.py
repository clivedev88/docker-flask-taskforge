from repositories.project_repository import ProjectRepository

class ProjectService:
    def __init__ (self):
        self.repository = ProjectRepository()
    def list_projects(self):
        return self.repository.get_all_projects()
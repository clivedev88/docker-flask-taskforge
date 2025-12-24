class ProjectRepository:
    def __init__(self):
        self.projects = [
            {'id':1,'name':'Projeto Alpha', 'description':'Projeto exemplo 1'},
            {'id':2,'name':'Projeto Beta', 'description':'Projeto exemplo 2'},
            {'id':3,'name':'Projeto Gamma', 'description':'Projeto exemplo 3'}
        ]
    def get_all_projects(self):
        return self.projects
    def get_project_by_id(self, project_id):
        for project in self.projects:
            if project['id'] == project_id:
                return project
            return None
    
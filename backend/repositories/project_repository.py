class ProjectRepository:
    def __init__ (self):
        self._projects = [
            {'id': 1, 'name':'Projeto Alfa', 'description':'Projeto exemplo 1'},
            {'id': 2, 'name':'Projeto Beta', 'description':'Projeto exemplo 2'}, 
        ]
    def get_all_projects(self):
        return self._projects
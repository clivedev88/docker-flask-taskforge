class TaskRepository:
    def __init__(self):
        self.tasks = [
            {
            'id':1,
             'title':'Definir escopo do projeto',
             'completed':True,
             'projectID':1
            },
            {
            'id':2,
             'title':'Criar estrutura backend',
             'completed':False,
             'projectID':1
            },
            {
            'id':3,
             'title':'Estudar Flask',
             'completed':True,
             'projectID':2
            }
        ]
        
    def get_by_project_id(self, project_id):
        return [
            task for task in self.tasks
            if task["projectID"] == project_id
        ]
        
    def get_task_by_project_and_id(self, project_id, task_id):
        for task in self.tasks:
            if task['projectID'] == project_id and task['id'] == task_id:
                return task
    #         # return None       Fazendo desse jeito, a busca não é feita na lista toda, pois ao achar inconsistência, já para a busca. 
        return None
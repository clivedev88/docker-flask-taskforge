
from repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def list_tasks_by_project(self, project_id):
        return self.repository.get_by_project_id(project_id)
    
    def get_task(self, project_id, task_id):
        return self.repository.get_task_by_project_and_id(project_id, task_id)
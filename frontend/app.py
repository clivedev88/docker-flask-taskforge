from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = 'http://127.0.0.1:5000'

@app.route('/')
def home():
    response = requests.get(f"{BACKEND_URL}/projects")
    projects = response.json()
    return render_template("projects.html", projects = projects)

@app.route('/projects/<int:project_id>')
def project_tasks(project_id):
    response = requests.get(f"{BACKEND_URL}/projects/{project_id}/tasks")
    tasks = response.json()
    return render_template("tasks.html", tasks = tasks)


if __name__ == "__main__":
    app.run(port=5001,debug=True)
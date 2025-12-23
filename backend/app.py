from flask import Flask, jsonify;
from routes.project_routes import project_bp

app = Flask(__name__);

# app.register_blueprint(__import__('routes.project_routes').project_bp); Pode fazer assim que importa dinamicamente
app.register_blueprint(project_bp);

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status":"Funcionando!!!",
        "service":"API Backend do Projeto TASKFORGE",
        "message":"Seja bem-vindo ao TASKFORGE!"
    })

if __name__ == '__main__':
    app.run(debug=True)
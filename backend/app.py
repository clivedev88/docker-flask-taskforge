from flask import Flask, jsonify;

app = Flask(__name__);

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status":"Funcionando!!!",
        "service":"API Backend do Projeto TASKFORGE",
        "message":"Seja bem-vindo ao TASKFORGE!"
    })

if __name__ == '__main__':
    app.run(debug=True)
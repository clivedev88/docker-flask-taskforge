from flask import FLASK, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def health():
    return jsonify({
        "status": "OK",
        "message":"Bem-vindo à API do Projeto"
    })
if __name__ == '__main__':
    app.run(debug=True)
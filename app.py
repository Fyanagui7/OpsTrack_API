
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "servico": "OpsTrack API",
        "status": "online"
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "ok"
    })


@app.route("/tickets")
def tickets():
    return jsonify({
        "tickets": [
            {"id": 1, "titulo": "Erro ao acessar o sistema"},
            {"id": 2, "titulo": "Solicitação de suporte"}
        ]
    })


@app.route("/usuarios")
def usuarios():
    return jsonify({
        "usuarios": [
            {"id": 1, "nome": "Ana"},
            {"id": 2, "nome": "Carlos"}
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)

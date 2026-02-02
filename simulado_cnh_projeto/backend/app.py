
from flask import Flask, jsonify, request
import json, random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("questoes_transito.json", encoding="utf-8") as f:
    BANCO = json.load(f)

def montar(q):
    alternativas = []
    alternativas.append({"texto": q["correta"], "correta": True})
    for i in q["incorretas"]:
        alternativas.append({"texto": i, "correta": False})
    random.shuffle(alternativas)
    return {
        "pergunta": q["pergunta"],
        "nivel": q["nivel"],
        "comentario": q["comentario"],
        "alternativas": alternativas
    }

@app.route("/simulado")
def gerar():
    qtd = int(request.args.get("qtd", 30))
    sorteadas = random.sample(BANCO, min(qtd, len(BANCO)))
    return jsonify([montar(q) for q in sorteadas])

if __name__ == "__main__":
    app.run(debug=True)

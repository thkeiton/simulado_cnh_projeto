
from flask import Flask, jsonify, request
import json, random, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, "questoes_transito.json"), encoding="utf-8") as f:
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


# obrigatório para Render reconhecer a aplicação
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


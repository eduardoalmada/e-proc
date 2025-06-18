
from flask import Flask, request, jsonify
from consulta_tjrj import consultar_processo

app = Flask(__name__)

@app.route('/')
def home():
    return 'API de consulta processual está no ar!'

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    numero_processo = data.get("mensagem")
    if not numero_processo:
        return jsonify({"erro": "Número do processo não fornecido"}), 400

    resultado = consultar_processo(numero_processo)
    if not resultado:
        return jsonify({"erro": "Número de processo não encontrado para demonstração."}), 200

    return jsonify({
        "processo": numero_processo,
        "parte": resultado.get("parte"),
        "assunto": resultado.get("assunto"),
        "situacao": resultado.get("situacao"),
        "ultima_movimentacao": resultado.get("ultima_movimentacao")
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

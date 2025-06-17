
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
    return jsonify({"resposta": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

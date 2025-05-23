from flask import Flask, jsonify, request

app = Flask(__name__)

pecas = {}

@app.route('/pecas/receber', methods=['POST'])
def receber_peca():
    dados = request.get_json()
    id_peca = dados['id_peca']
    pecas[id_peca] = dados
    return jsonify({"mensagem": "Peça recebida", "id_peca": id_peca}), 201

@app.route('/pecas/<id_peca>', methods=['GET'])
def obter_peca(id_peca):
    peca = pecas.get(id_peca)
    if not peca:
        return jsonify({"mensagem": "Peça não encontrada"}), 404
    return jsonify(peca), 200

@app.route('/pecas/rastreamento', methods=['GET'])
def rastrear_pecas():
    return jsonify(pecas), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)

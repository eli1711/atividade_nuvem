from flask import Flask, jsonify, request

app = Flask(__name__)

ordens_producao = {}

@app.route('/producao', methods=['GET'])
def obter_todas_producoes():
    if not ordens_producao:
        return jsonify({"mensagem": "Nenhuma ordem de produção encontrada"}), 404
    return jsonify(ordens_producao), 200

@app.route('/producao/<id_ordem>', methods=['GET'])
def obter_producao(id_ordem):
    ordem = ordens_producao.get(id_ordem)
    if not ordem:
        return jsonify({"mensagem": "Ordem não encontrada"}), 404
    return jsonify(ordem), 200

@app.route('/producao/iniciar', methods=['POST'])
def iniciar_producao():
    dados = request.get_json()
    id_ordem = dados['id_ordem']
    ordens_producao[id_ordem] = {'status': 'iniciado', 'detalhes': dados}
    return jsonify({"mensagem": "Produção iniciada", "id_ordem": id_ordem}), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/relatorios/producao', methods=['GET'])
def relatorio_producao():
    resposta = requests.get('http://servico_producao:5000/producao')
    if resposta.status_code == 200:
        dados_producao = resposta.json()
        return jsonify(dados_producao), 200
    return jsonify({"mensagem": "Erro ao acessar o serviço de produção"}), 500

@app.route('/relatorios/qualidade', methods=['GET'])
def relatorio_qualidade():
    resposta = requests.get('http://servico_qualidade:5001/qualidade/falhas')
    if resposta.status_code == 200:
        dados_qualidade = resposta.json()
        return jsonify(dados_qualidade), 200
    return jsonify({"mensagem": "Erro ao acessar o serviço de qualidade"}), 500

@app.route('/relatorios/pecas', methods=['GET'])
def relatorio_pecas():
    resposta = requests.get('http://servico_pecas:5002/pecas/rastreamento')
    if resposta.status_code == 200:
        dados_pecas = resposta.json()
        return jsonify(dados_pecas), 200
    return jsonify({"mensagem": "Erro ao acessar o serviço de peças"}), 500

@app.route('/relatorios/geral', methods=['GET'])
def relatorio_geral():
    resposta_producao = requests.get('http://servico_producao:5000/producao')
    resposta_qualidade = requests.get('http://servico_qualidade:5001/qualidade/falhas')
    resposta_pecas = requests.get('http://servico_pecas:5002/pecas/rastreamento')

    if resposta_producao.status_code == 200 and resposta_qualidade.status_code == 200 and resposta_pecas.status_code == 200:
        geral = {
            'producao': resposta_producao.json(),
            'qualidade': resposta_qualidade.json(),
            'pecas': resposta_pecas.json()
        }
        return jsonify(geral), 200
    return jsonify({"mensagem": "Erro ao acessar os serviços internos"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5003)

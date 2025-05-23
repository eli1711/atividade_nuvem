import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

inspecoes = {}

@app.route('/qualidade/verificar', methods=['POST'])
def verificar_qualidade():
    dados = request.get_json()
    id_ordem = dados['id_ordem']
    problema = dados['problema']

    # Comunicação com o serviço de Produção para obter detalhes da ordem
    try:
        resposta_producao = requests.get(f'http://servico_producao:5000/producao/{id_ordem}')
        dados_producao = resposta_producao.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"mensagem": f"Erro ao acessar serviço de produção: {e}"}), 500

    # Simula chamada ao serviço de certificação
    resposta_certificacao = requests.post('http://servico_certificacao:5004/certificacao/verificar', json=dados)
    dados_certificacao = resposta_certificacao.json()

    inspecoes[id_ordem] = {'problema': problema, 'certificacao': dados_certificacao, 'dados_producao': dados_producao}
    return jsonify({"mensagem": "Qualidade verificada", "certificacao": dados_certificacao, "dados_producao": dados_producao}), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

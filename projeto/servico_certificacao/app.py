from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/certificacao/verificar', methods=['POST'])
def verificar_certificacao():
    dados = request.get_json()
    problema = dados.get('problema', 'Problema desconhecido')
    
    if problema == 'critico':
        return jsonify({"recomendacao": "recall", "mensagem": "Defeito grave detectado. Recomendação de recall."}), 200
    return jsonify({"recomendacao": "nenhuma_acao", "mensagem": "Nenhuma ação necessária."}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5004)

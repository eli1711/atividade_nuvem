import requests

# Testando o Serviço de Produção
def testar_servico_producao():
    resposta = requests.get("http://localhost:5000/producao")
    print("Resposta do Serviço de Produção:")
    print("Status Code:", resposta.status_code)  # Imprimindo o status code
    print("Texto da Resposta:", resposta.text)   # Imprimindo o corpo da resposta
    assert resposta.status_code == 200, "Erro ao acessar o serviço de produção"
    assert len(resposta.json()) > 0, "Nenhuma ordem de produção encontrada"

# Testando o Serviço de Qualidade
def testar_servico_qualidade():
    dados = {
        'id_ordem': '124',
        'problema': 'Falha no painel'
    }
    resposta = requests.post("http://localhost:5001/qualidade/verificar", json=dados)
    print("Resposta do Serviço de Qualidade:", resposta.status_code, resposta.text)
    assert resposta.status_code == 201, "Erro ao verificar qualidade"
    assert 'certificacao' in resposta.json(), "Falha no retorno da certificação"

# Testando o Serviço de Relatórios
def testar_servico_relatorio():
    resposta = requests.get("http://localhost:5003/relatorios/geral")
    print("Resposta do Serviço de Relatórios:", resposta.status_code, resposta.text)
    assert resposta.status_code == 200, "Erro ao acessar os relatórios"
    dados = resposta.json()
    assert 'producao' in dados, "Dados de produção não encontrados no relatório"
    assert 'qualidade' in dados, "Dados de qualidade não encontrados no relatório"

# Testando o Serviço de Certificação
def testar_servico_certificacao():
    dados = {
        'problema': 'critico'
    }
    resposta = requests.post("http://localhost:5004/certificacao/verificar", json=dados)
    print("Resposta do Serviço de Certificação:", resposta.status_code, resposta.text)
    assert resposta.status_code == 200, "Erro ao verificar certificação"
    assert 'recomendacao' in resposta.json(), "Falha na recomendação de certificação"

if __name__ == "__main__":
    testar_servico_producao()
    testar_servico_qualidade()
    testar_servico_relatorio()
    testar_servico_certificacao()
    print("Todos os testes passaram com sucesso!")


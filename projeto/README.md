# Sistema Modular de Monitoramento de Produção

## Arquitetura

O sistema é composto por quatro microserviços:

1. **Serviço de Produção**: Gerencia as ordens de produção.
2. **Serviço de Qualidade**: Verifica e registra falhas nas ordens de produção.
3. **Serviço de Peças**: Rastreia as peças utilizadas na produção.
4. **Serviço de Relatórios**: Consolida os dados de produção, qualidade e peças.
5. **Serviço de Certificação**: Simula um sistema externo para validar a necessidade de recall.

## Como rodar os serviços

1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Execute:
   ```bash
   docker-compose up --build

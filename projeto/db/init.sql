CREATE DATABASE IF NOT EXISTS projeto;

USE projeto;

-- Tabela para armazenar as peças
CREATE TABLE IF NOT EXISTS pecas (
    id_peca INT AUTO_INCREMENT PRIMARY KEY,
    nome_peca VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_recebimento DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para armazenar as ordens de produção
CREATE TABLE IF NOT EXISTS ordens_producao (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    data_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'pendente'
);

-- Tabela para armazenar as inspeções de qualidade
CREATE TABLE IF NOT EXISTS inspecoes_qualidade (
    id_inspecao INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    problema VARCHAR(255) NOT NULL,
    recomendacao VARCHAR(255),
    data_inspecao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_ordem) REFERENCES ordens_producao(id_ordem)
);

-- Tabela para armazenar relatórios de produção e qualidade
CREATE TABLE IF NOT EXISTS relatorios (
    id_relatorio INT AUTO_INCREMENT PRIMARY KEY,
    tipo_relatorio VARCHAR(50) NOT NULL,
    conteudo TEXT NOT NULL,
    data_geracao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Inserir dados na tabela de Peças
INSERT INTO pecas (nome_peca, descricao) VALUES
('Peca A', 'Peça usada no motor, modelo XYZ.'),
('Peca B', 'Peça de suspensão, modelo ABC.'),
('Peca C', 'Peça de transmissão, modelo 123.'),
('Peca D', 'Peça de roda, modelo DEF.');

-- Inserir dados na tabela de Ordens de Produção
INSERT INTO ordens_producao (descricao, status) VALUES
('Produção de motor para carro modelo 2023', 'em andamento'),
('Montagem de suspensão para veículos da linha ABC', 'concluída'),
('Desenvolvimento de motor para carro modelo 2024', 'pendente'),
('Produção de transmissão para carro modelo XYZ', 'em andamento');

-- Inserir dados na tabela de Inspeções de Qualidade
INSERT INTO inspecoes_qualidade (id_ordem, problema, recomendacao) VALUES
(1, 'Defeito encontrado na válvula de escape', 'Reparo necessário na válvula, verificar funcionamento do motor.'),
(2, 'Peça da suspensão com desgaste excessivo', 'Substituição da peça recomendada, realizar nova inspeção.'),
(3, 'Motor com falha no sistema de ignição', 'Revisar o sistema de ignição e realizar testes de performance.'),
(4, 'Falha no sistema de transmissão', 'Substituir o sistema de transmissão e realizar testes de marcha.');

-- Inserir dados na tabela de Relatórios
INSERT INTO relatorios (tipo_relatorio, conteudo) VALUES
('Relatório de Produção', 'Este relatório contém dados sobre a produção de motores e suspensão no mês de maio.'),
('Relatório de Qualidade', 'Este relatório apresenta os resultados das inspeções realizadas nas peças de suspensão e motor durante o mês de maio.');

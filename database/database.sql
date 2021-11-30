DROP DATABASE IF EXISTS iomt;
CREATE DATABASE IF NOT EXISTS iomt;

USE iomt;

CREATE TABLE IF NOT EXISTS usuario (
	id INT(11) NOT NULL AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	nascimento date NOT NULL,
	sexo CHAR(1) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS DadosColetados (
	id INT(11) NOT NULL AUTO_INCREMENT,
	usuario INT(11) NOT NULL,
	valor1 DECIMAL(15,2) NULL DEFAULT 0,
	valor2 DECIMAL(15,2) NULL DEFAULT 0,
	dataHora DATETIME DEFAULT CURRENT_TIMESTAMP(),
	tipo VARCHAR(10) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (usuario) REFERENCES usuario(id) ON UPDATE CASCADE
);

-- Verifica Situação 1
SELECT dc.usuario, dc.valor1 AS 'temperaturaCorporal', sub.valor1 AS 'SP02', sub.dataHora, dc.dataHora,
		ABS(TIMESTAMPDIFF(MINUTE , dc.dataHora , sub.dataHora)) AS diffHoras
FROM DadosColetados dc
JOIN (
	SELECT dc1.*
	FROM DadosColetados dc1
	WHERE dc1.usuario = 4 AND dc1.tipo = 'SP02' AND dc1.valor1 < 90
) AS sub ON sub.usuario = dc.usuario 
WHERE dc.usuario = :id_user AND dc.tipo = 'TC' AND dc.valor1 NOT BETWEEN 35 AND 37.5
HAVING ABS(TIMESTAMPDIFF(MINUTE , dc.dataHora , sub.dataHora)) < 60;

-- SQL PARA DASHBOARD
SELECT d.dataHora, d.valor1 AS sp02, d.valor2 AS frequnciaCardiaca
FROM dadoscoletados d 
WHERE tipo = 'SP02' AND usuario = :id_user
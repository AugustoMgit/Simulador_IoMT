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

ALTER TABLE usuario
	ADD COLUMN email VARCHAR(100) NULL DEFAULT NULL;

INSERT INTO usuario (nome, nascimento, sexo) VALUES ('João', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('Augusto', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('Vitor', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('William', '2000-02-01', 'M');

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

-- Verifica Situação 2
SELECT d.usuario, d.valor1 AS sistolica, d.valor2 AS diastolica, d.dataHora
FROM dadoscoletados d
WHERE d.tipo = 'PA' AND d.usuario = :id_user AND dataHora BETWEEN date_sub(current_timestamp(), INTERVAL 24 HOUR) AND current_timestamp()
ORDER BY dataHora DESC
LIMIT 3

-- Alguns dados
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,36.34,NULL,'2021-12-04 08:56:00.0','TC',NULL),
	 (1,35.52,NULL,'2021-12-04 09:43:00.0','TC',NULL),
	 (1,38.95,NULL,'2021-12-04 10:37:00.0','TC',NULL),
	 (1,36.57,NULL,'2021-12-04 11:06:00.0','TC',NULL),
	 (1,36.56,NULL,'2021-12-04 12:06:00.0','TC',NULL),
	 (1,36.28,NULL,'2021-12-04 12:23:00.0','TC',NULL),
	 (1,37.00,NULL,'2021-12-04 12:56:00.0','TC',NULL),
	 (1,37.19,NULL,'2021-12-04 13:32:00.0','TC',NULL),
	 (1,36.98,NULL,'2021-12-04 14:02:00.0','TC',NULL),
	 (1,42.16,NULL,'2021-12-04 14:56:00.0','TC',NULL);
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,37.27,NULL,'2021-12-04 15:47:00.0','TC',NULL),
	 (1,37.04,NULL,'2021-12-04 16:19:00.0','TC',NULL),
	 (1,37.10,NULL,'2021-12-04 17:10:00.0','TC',NULL),
	 (1,36.78,NULL,'2021-12-04 17:56:00.0','TC',NULL),
	 (1,36.92,NULL,'2021-12-04 18:17:00.0','TC',NULL),
	 (1,37.34,NULL,'2021-12-04 18:34:00.0','TC',NULL),
	 (1,37.05,NULL,'2021-12-04 18:54:00.0','TC',NULL),
	 (1,36.20,NULL,'2021-12-04 19:27:00.0','TC',NULL),
	 (1,36.85,NULL,'2021-12-04 20:08:00.0','TC',NULL),
	 (1,34.91,NULL,'2021-12-04 20:59:00.0','TC',NULL);
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,128.00,81.00,'2021-12-04 10:28:00.0','PA',NULL),
	 (1,113.00,71.00,'2021-12-04 10:58:00.0','PA',NULL),
	 (1,123.00,77.00,'2021-12-04 11:41:00.0','PA',NULL),
	 (1,113.00,71.00,'2021-12-04 12:00:00.0','PA',NULL),
	 (1,127.00,70.00,'2021-12-04 12:16:00.0','PA',NULL),
	 (1,110.00,73.00,'2021-12-04 12:57:00.0','PA',NULL),
	 (1,207.00,190.00,'2021-12-04 13:19:00.0','PA',NULL),
	 (1,120.00,76.00,'2021-12-04 13:53:00.0','PA',NULL),
	 (1,117.00,73.00,'2021-12-04 14:47:00.0','PA',NULL),
	 (1,128.00,78.00,'2021-12-04 15:22:00.0','PA',NULL);
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,98.00,62.00,'2021-12-04 16:12:00.0','PA',NULL),
	 (1,2.00,46.00,'2021-12-04 16:50:00.0','PA',NULL),
	 (1,122.00,75.00,'2021-12-04 17:26:00.0','PA',NULL),
	 (1,259.00,193.00,'2021-12-04 18:07:00.0','PA',NULL),
	 (1,120.00,83.00,'2021-12-04 18:37:00.0','PA',NULL),
	 (1,126.00,76.00,'2021-12-04 19:31:00.0','PA',NULL),
	 (1,124.00,81.00,'2021-12-04 20:12:00.0','PA',NULL),
	 (1,115.00,72.00,'2021-12-04 20:29:00.0','PA',NULL),
	 (1,119.00,80.00,'2021-12-04 21:06:00.0','PA',NULL),
	 (1,120.00,72.00,'2021-12-04 21:51:00.0','PA',NULL);
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,66.10,73.13,'2021-12-04 08:16:00.0','SP02',NULL),
	 (1,90.65,77.62,'2021-12-04 08:37:00.0','SP02',NULL),
	 (1,98.50,72.11,'2021-12-04 09:35:00.0','SP02',NULL),
	 (1,97.11,76.47,'2021-12-04 10:15:00.0','SP02',NULL),
	 (1,79.28,50.11,'2021-12-04 10:38:00.0','SP02',NULL),
	 (1,95.14,57.03,'2021-12-04 11:26:00.0','SP02',NULL),
	 (1,94.11,50.29,'2021-12-04 12:24:00.0','SP02',NULL),
	 (1,99.47,55.33,'2021-12-04 12:51:00.0','SP02',NULL),
	 (1,90.08,70.87,'2021-12-04 13:32:00.0','SP02',NULL),
	 (1,27.03,53.75,'2021-12-04 14:23:00.0','SP02',NULL);
INSERT INTO dadoscoletados (usuario,valor1,valor2,dataHora,tipo,email) VALUES
	 (1,90.31,57.76,'2021-12-04 15:18:00.0','SP02',NULL),
	 (1,98.12,52.73,'2021-12-04 15:33:00.0','SP02',NULL),
	 (1,93.43,82.56,'2021-12-04 16:07:00.0','SP02',NULL),
	 (1,97.98,62.63,'2021-12-04 16:49:00.0','SP02',NULL),
	 (1,17.90,98.50,'2021-12-04 17:04:00.0','SP02',NULL),
	 (1,92.87,65.54,'2021-12-04 17:50:00.0','SP02',NULL),
	 (1,99.07,0.52,'2021-12-04 18:41:00.0','SP02',NULL),
	 (1,96.04,22.65,'2021-12-04 19:41:00.0','SP02',NULL),
	 (1,93.51,119.01,'2021-12-04 20:36:00.0','SP02',NULL),
	 (1,96.78,135.29,'2021-12-04 20:56:00.0','SP02',NULL);
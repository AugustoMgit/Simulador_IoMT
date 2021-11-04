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

INSERT INTO usuario (nome, nascimento, sexo) VALUES ('João', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('Augusto', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('Vitor', '2000-02-01', 'M');
INSERT INTO usuario (nome, nascimento, sexo) VALUES ('William', '2000-02-01', 'M');

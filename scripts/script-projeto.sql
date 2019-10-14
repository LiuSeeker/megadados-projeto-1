DROP DATABASE IF EXISTS rede_passaro;
CREATE DATABASE rede_passaro;
USE rede_passaro;

DROP TABLE IF EXISTS Usuario;
CREATE TABLE Usuario(
id_usuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(32) NOT NULL,
sobrenome VARCHAR(32) NOT NULL,
username VARCHAR(32) NOT NULL UNIQUE,
email VARCHAR(64) NOT NULL,
cidade VARCHAR(32) NOT NULL,
ativo BOOLEAN NOT NULL DEFAULT 1
);

DROP TABLE IF EXISTS Passaro;
CREATE TABLE Passaro(
especie VARCHAR(32) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS Post;
CREATE TABLE Post(
id_post INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
id_usuario INT NOT NULL,
titulo TINYTEXT,
texto TEXT,
url_imagem TEXT,
ativo BOOLEAN NOT NULL DEFAULT 1,
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

DROP TABLE IF EXISTS Visualizacao;
CREATE TABLE Visualizacao(
id_post INT NOT NULL,
id_usuario INT NOT NULL,
aparelho VARCHAR(32) NOT NULL,
ip VARCHAR(32) NOT NULL,
instante TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id_post, id_usuario),
FOREIGN KEY (id_post) REFERENCES Post(id_post),
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

DROP TABLE IF EXISTS Mencao_Usuario;
CREATE TABLE Mencao_Usuario(
id_post INT NOT NULL,
id_usuario INT NOT NULL,
ativo BOOLEAN NOT NULL DEFAULT 1,
PRIMARY KEY (id_post, id_usuario),
FOREIGN KEY (id_post) REFERENCES Post(id_post),
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

DROP TABLE IF EXISTS Mencao_Passaro;
CREATE TABLE Mencao_Passaro(
id_post INT NOT NULL,
especie VARCHAR(32) NOT NULL,
ativo BOOLEAN NOT NULL DEFAULT 1,
PRIMARY KEY (id_post, especie),
FOREIGN KEY (id_post) REFERENCES Post(id_post),
FOREIGN KEY (especie) REFERENCES Passaro(especie)
);

DROP TABLE IF EXISTS Preferencia;
CREATE TABLE Preferencia(
id_usuario INT NOT NULL,
especie VARCHAR(32) NOT NULL,
PRIMARY KEY (id_usuario, especie),
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
FOREIGN KEY (especie) REFERENCES Passaro(especie)
);
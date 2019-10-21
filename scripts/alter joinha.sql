DROP TABLE IF EXISTS Joinha;

CREATE TABLE Joinha(
id_post INT NOT NULL,
id_usuario INT NOT NULL,
joinha BOOLEAN NOT NULL,
FOREIGN KEY (id_post) REFERENCES Post(id_post),
FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
PRIMARY KEY (id_post, id_usuario)
);
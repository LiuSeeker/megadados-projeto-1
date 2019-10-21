USE rede_passaro;
ALTER TABLE Post ADD repost INT,
ADD FOREIGN KEY (repost) REFERENCES Post(id_post);

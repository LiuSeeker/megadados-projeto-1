USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_passaro;

DELIMITER //
CREATE TRIGGER trig_delete_passaro
BEFORE DELETE ON passaro
FOR EACH ROW
BEGIN
	DELETE FROM preferencia
	WHERE preferencia.especie = OLD.especie;
	DELETE FROM post
	WHERE post.especie = OLD.especie;
    
END;//
DELIMITER ;
USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_usuario;

DELIMITER //
CREATE TRIGGER trig_delete_usuario
AFTER UPDATE ON usuario
FOR EACH ROW
BEGIN
	IF NEW.ativo <=> OLD.ativo THEN
		DELETE FROM preferencia
		WHERE preferencia.id_usuario = NEW.id_usuario;
		DELETE FROM post
		WHERE post.id_post = NEW.id_usuario;
    END IF;
END;//
DELIMITER ;
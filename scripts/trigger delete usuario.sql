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
		UPDATE post SET post.ativo = 0
		WHERE post.id_usuario = NEW.id_usuario;
    END IF;
END;//
DELIMITER ;
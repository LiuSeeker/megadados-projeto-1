USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_usuario;

DELIMITER //
CREATE TRIGGER trig_delete_usuario
AFTER UPDATE ON Usuario
FOR EACH ROW
BEGIN
	IF NEW.ativo <=> OLD.ativo THEN
		DELETE FROM Preferencia
		WHERE Preferencia.id_usuario = NEW.id_usuario;
		UPDATE Post SET Post.ativo = 0
		WHERE Post.id_usuario = NEW.id_usuario;
    END IF;
END;//
DELIMITER ;
USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_post;

DELIMITER //
CREATE TRIGGER trig_delete_post
AFTER UPDATE ON post
FOR EACH ROW
BEGIN
	IF NEW.ativo <=> OLD.ativo THEN
		DELETE FROM visualizacao
		WHERE visualizacao.id_post = NEW.id_post;
		DELETE FROM mencao_usuario
		WHERE mencao_usuario.id_post = NEW.id_post;
		DELETE FROM mencao_passaro
		WHERE mencao_passaro.id_post = NEW.id_post;
    END IF;
END;//
DELIMITER ;
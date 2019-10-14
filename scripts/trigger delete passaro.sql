USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_passaro;

DELIMITER //
CREATE TRIGGER trig_delete_passaro
BEFORE DELETE ON passaro
FOR EACH ROW
BEGIN
	DELETE FROM preferencia
	WHERE preferencia.especie = OLD.especie;
	DELETE FROM Mencao_Passaro
	WHERE Mencao_Passaro.especie = OLD.especie;
    
END;//
DELIMITER ;
USE rede_passaro;

DROP TRIGGER IF EXISTS trig_delete_passaro;

DELIMITER //
CREATE TRIGGER trig_delete_passaro
BEFORE DELETE ON Passaro
FOR EACH ROW
BEGIN
	DELETE FROM Preferencia
	WHERE Preferencia.especie = OLD.especie;
	DELETE FROM Mencao_Passaro
	WHERE Mencao_Passaro.especie = OLD.especie;
    
END;//
DELIMITER ;
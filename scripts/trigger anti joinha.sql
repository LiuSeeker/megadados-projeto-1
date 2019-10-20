USE rede_passaro;

DROP TRIGGER IF EXISTS trig_update_anti_joinha;
DROP TRIGGER IF EXISTS trig_update_joinha;

DELIMITER //
CREATE TRIGGER trig_update_anti_joinha
BEFORE UPDATE ON Joinha
FOR EACH ROW
BEGIN
	
    IF NEW.anti_joinha = 1 THEN
		SET @disale_trigger = 1;
        SET NEW.pro_joinha = 0;
        SET @disable_trigger = 0;
    END IF;
	
END;//
DELIMITER ;
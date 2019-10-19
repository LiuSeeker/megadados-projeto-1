USE rede_passaro;

DROP TRIGGER IF EXISTS trig_update_pro_joinha;

DELIMITER //
CREATE TRIGGER trig_update_pro_joinha
BEFORE UPDATE ON Joinha
FOR EACH ROW
BEGIN
	IF NEW.pro_joinha <=> 1 THEN
        SET NEW.anti_joinha = 0;
    END IF;
END;//
DELIMITER ;
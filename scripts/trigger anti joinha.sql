USE rede_passaro;

DROP TRIGGER IF EXISTS trig_update_anti_joinha;

DELIMITER //
CREATE TRIGGER trig_update_anti_joinha
BEFORE UPDATE ON Joinha
FOR EACH ROW
BEGIN
    IF NEW.anti_joinha <=> 1 THEN
        SET NEW.pro_joinha = 0;
    END IF;
END;//
DELIMITER ;
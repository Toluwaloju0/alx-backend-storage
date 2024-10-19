-- A script to update a value after a change
DELIMITER $$

CREATE TRIGGER valid_E BEFORE UPDATE ON users FOR EACH ROW
-- Trigger body
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;

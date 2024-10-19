-- A script to reset a row in the datatbase
CREATE TRIGGER valid_E AFTER UPDATE ON users FOR EACH ROW
-- Trigger body
    SET NEW.valid_email = 0;

-- A script to create  a procedure
DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
    BEGIN
        DECLARE var INT;

        SET var = (SELECT id FROM projects WHERE name = project_name LIMIT 1);

        IF var IS NULL THEN
            INSERT INTO projects (name) VALUE (project_name);
            SET var = LAST_INSERT_ID();
        END IF;
        INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, var, score);
    END $$

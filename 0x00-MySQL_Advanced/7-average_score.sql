-- A script to compite the average score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
    BEGIN
        DECLARE total FLOAT;
        SET total = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    
        UPDATE users SET average_score = total WHERE id = user_id;
    END $$

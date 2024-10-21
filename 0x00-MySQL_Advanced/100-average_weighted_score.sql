-- A script to compute weighted average
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id)
BEGIN
    DECLARE var JSON;
    DECLARE weight INT;

    SET var = JSON_OBJECT(SELECT project_id, score FROM corrections WHERE corrections.user_id = user_id);


    REPEAT
        SET
-- A script to create a function that divides two numbers
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
    RETURNS FLOAT
    BEGIN  
        IF b = 0 THEN RETURN 0;
        ELSE RETURN a / b;
        END IF;
    END $$

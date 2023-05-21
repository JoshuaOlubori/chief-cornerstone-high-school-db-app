DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_new_session`()
BEGIN
DECLARE prev_name VARCHAR(45);
DECLARE new_name VARCHAR(45);
DECLARE prev_id INT;
DECLARE new_id INT;
DECLARE next_term INT;

DECLARE error_message VARCHAR(1024);
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
GET DIAGNOSTICS CONDITION 1
error_message = MESSAGE_TEXT;
ROLLBACK;
-- SELECT CONCAT('Error: ', error_message) AS 'Error Message';
-- SET full_error_message = CONCAT('Error in calling procedure: ', error_message);
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
END;
START TRANSACTION;



-- Step 1: Update the current term
UPDATE term SET is_current = 0 WHERE is_current = 1;

-- Step 2: Update the next term
SET next_term = (SELECT term FROM term WHERE is_current = 0 ORDER BY last_update ASC LIMIT 1);
UPDATE term SET is_current = 1 WHERE term =next_term;

-- Step 3: Insert a new record into school_session
SELECT s_name, school_session.id INTO prev_name, prev_id 
FROM school_session ORDER BY id DESC LIMIT 1;

SET new_name = CONCAT(SUBSTRING(prev_name, 1, 4) + 1, '/', SUBSTRING(prev_name, 6, 4) + 1);

INSERT INTO school_session (s_name, start_date, end_date, is_current)
VALUES (new_name, NOW(), NULL, 1);

SELECT id into new_id FROM school_session ORDER BY id DESC LIMIT 1;

-- Update the previous records
IF prev_id IS NOT NULL THEN
UPDATE school_session SET is_current = 0 WHERE id < new_id;
UPDATE school_session SET end_date = NOW() WHERE id = prev_id;
END IF;
COMMIT;
END$$
DELIMITER ;

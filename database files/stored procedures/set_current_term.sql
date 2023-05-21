DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `set_current_term`()
BEGIN
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
COMMIT;
END$$
DELIMITER ;

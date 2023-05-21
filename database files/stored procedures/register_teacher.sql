DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `register_teacher`(
IN id INT,
IN first_name VARCHAR(45),
IN last_name VARCHAR(45),
IN dob DATE, 
IN blood_group VARCHAR(4),
IN genotype CHAR(2),
IN religion ENUM('Christianity', 'Islam', 'Others'),
IN address TEXT,
IN phone CHAR(11),
IN spouse_phone CHAR(11),
IN ethnicity VARCHAR(50),
IN city_or_town VARCHAR(45),
IN medical_condition VARCHAR(45),
IN bonus DECIMAL,
IN dept_id INT
)
BEGIN
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

IF id IN (SELECT person_id FROM staff)
THEN
INSERT INTO teachingstaff (person_id) -- create new record in teachingstaff table
VALUES (id);
ELSE
CALL register_staff(id, first_name, last_name, dob, 
blood_group, genotype, religion, address, phone, spouse_phone, ethnicity, city_or_town, medical_condition, bonus, dept_id);


INSERT INTO teachingstaff (person_id) -- create new record in teachingstaff table
VALUES (LAST_INSERT_ID());
END IF;
COMMIT;
END$$
DELIMITER ;

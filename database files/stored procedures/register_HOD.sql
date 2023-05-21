DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `register_hod`(
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
-- The necessity of this procedure was born of the fact that there needed to be a way
-- to insert the hod_ids of new employees into their tables without causing a dependency issue
-- SO with this procedure, as part of initializing the database, new users would first register
-- managers using this procedure before inserting any other staff

IF id = 0

THEN
INSERT INTO person ( first_name, last_name, dob, blood_group, genotype, religion, address, phone, spouse_phone, ethnicity, city_or_town, medical_condition)
VALUES (first_name, last_name, dob, blood_group, genotype, religion, address, phone, spouse_phone, ethnicity, city_or_town, medical_condition);

INSERT INTO staff (person_id, spouse_phone, bonus, dept_id, hod_id)
VALUES (LAST_INSERT_ID(), spouse_phone, bonus, dept_id, LAST_INSERT_ID());

ELSE 
UPDATE staff
SET hod_id = id
WHERE person_id = id;


END IF;

COMMIT;
END$$
DELIMITER ;

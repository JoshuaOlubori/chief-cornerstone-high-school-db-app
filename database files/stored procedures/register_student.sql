DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `register_student`(
IN first_name VARCHAR(45),
IN last_name VARCHAR(45),
IN dob DATE, 
IN blood_group VARCHAR(4),
IN genotype CHAR(2),
IN religion ENUM('Christianity', 'Islam', 'Others'),
IN address TEXT,
IN phone CHAR(11),
IN ethnicity VARCHAR(50),
IN city_or_town VARCHAR(45),
IN medical_condition VARCHAR(45),
IN class_id INT
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

INSERT INTO person (first_name, last_name, dob, blood_group, genotype, religion, address, phone, spouse_phone, ethnicity, city_or_town, medical_condition)
VALUES (first_name, last_name, dob, blood_group, genotype, religion, address, phone, null, ethnicity, city_or_town, medical_condition);

INSERT INTO student (person_id, class_id)
VALUES (LAST_INSERT_ID(), class_id);

COMMIT;


END$$
DELIMITER ;

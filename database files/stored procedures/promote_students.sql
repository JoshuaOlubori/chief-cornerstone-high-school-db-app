DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `promote_students`()
BEGIN
DECLARE done BOOLEAN DEFAULT FALSE;
DECLARE current_grade INT;
DECLARE student_id INT;
DECLARE session_id INT;
DECLARE error_message VARCHAR(255);
DECLARE student_cursor CURSOR FOR
SELECT DISTINCT student_id FROM studentclasshistory WHERE graduated <> 1;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = true;
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
GET DIAGNOSTICS CONDITION 1
error_message = MESSAGE_TEXT;
ROLLBACK;
-- SELECT CONCAT('Error: ', error_message) AS 'Error Message';
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
END;
START TRANSACTION;



-- Initialize a cursor that loops through every student in the table
OPEN student_cursor;
student_loop: LOOP
FETCH student_cursor INTO student_id;
IF done THEN
LEAVE student_loop;
END IF;

-- These statements run for each iteration in the loop i.e for each student
-- Save the current (ensured by the order by clause acting on last_update) grade/class of the student into a variable
SET current_grade = (SELECT class_id FROM studentclasshistory WHERE student_id
= student_id ORDER BY last_update DESC LIMIT 1);

SET session_id = (SELECT id FROM school_session ORDER BY id DESC LIMIT 1);

-- For all non-terminal class students, insert a new record into the table
IF current_grade IS NULL THEN
INSERT INTO studentclasshistory (
student_id, class_id, graduated, teacher_id, classroom_id, session_id, start_date, end_date, last_update
)
VALUES (student_id, current_grade, NULL, NULL, NULL, session_id, NOW(), NULL, NOW());
END IF;

IF current_grade < 12 THEN
INSERT INTO studentclasshistory (
student_id, class_id, graduated, teacher_id, classroom_id, session_id, start_date, end_date, last_update
)
VALUES (student_id, current_grade + 1, NULL, NULL, NULL, session_id + 1, NOW(), NULL, NOW());

-- set their previous record's end_date to now
UPDATE studentclasshistory 
SET 
    end_date = NOW()
WHERE
    student_id = student_id
        AND class_id = current_grade;
ELSE
-- For terminal class students, set their graduated column to TRUE
UPDATE studentclasshistory 
SET graduated = 1
 WHERE student_id = student_id
AND class_id = 12;
END IF;
END LOOP;

 CLOSE student_cursor;
 
 -- We would still have to later set the teacher_id and classroom_id of the newly promoted classes
COMMIT;
END$$
DELIMITER ;

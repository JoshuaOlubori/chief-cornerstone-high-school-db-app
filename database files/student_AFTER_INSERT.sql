CREATE DEFINER=`root`@`localhost` TRIGGER `student_AFTER_INSERT` AFTER INSERT ON `student` FOR EACH ROW BEGIN

DECLARE s_id INT;
SET s_id = (SELECT session_id FROM termship ORDER BY start_date DESC LIMIT 1);

INSERT INTO studentclasshistory (
student_id, class_id, graduated, teacher_id, classroom_id, session_id, start_date, end_date, last_update
)
VALUES (NEW.person_id, NEW.class_id, 0, NULL, 1, s_id, NOW(), NULL, NOW());

ENDCREATE DEFINER=`root`@`localhost` TRIGGER `student_AFTER_INSERT` AFTER INSERT ON `student` FOR EACH ROW BEGIN

DECLARE s_id INT;
SET s_id = (SELECT session_id FROM termship ORDER BY start_date DESC LIMIT 1);

INSERT INTO studentclasshistory (
student_id, class_id, graduated, teacher_id, classroom_id, session_id, start_date, end_date, last_update
)
VALUES (NEW.person_id, NEW.class_id, 0, NULL, 1, s_id, NOW(), NULL, NOW());

END
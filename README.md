
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


![MySQL](https://img.shields.io/static/v1?style=for-the-badge&message=MySQL&color=4479A1&logo=MySQL&logoColor=FFFFFF&label=)

![Flask](https://img.shields.io/static/v1?style=for-the-badge&message=Flask&color=000000&logo=Flask&logoColor=FFFFFF&label=)

![Jinja](https://img.shields.io/static/v1?style=for-the-badge&message=Jinja&color=B41717&logo=Jinja&logoColor=FFFFFF&label=)
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/55203c7219a4eb2bcf22e319cc2160c20a2bce56/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joshua-edun


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">High School Admin App</h3>

  <p align="center">
    Featuring database creation, stored procedures, Flask etc.
     <br />



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ul>
    <li><a href="#requirement">Requirement gathering</a></li>
        <li><a href="#database-creation">Database Creation</a></li>
        <li> <a href="#application">Application</a></li>
        <li><a href="#screenshots">Screenshots </a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</details>


<div align="left">
<!-- ABOUT THE PROJECT -->
  
## About The Project 🍪 

![code](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/ac6fd5436c7207f3a1d16a963857462c30cebb5e/screenshots/Screenshot%20(18).png)

<a name="requirement"/>
  
### Requirement Gathering

School needs to move away from storing data on Excel files and adopt an automated way of managing personnel data


<!-- -->
  <a name="database-creation"/>
  
## Creating the database 📂

![erd](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/ac6fd5436c7207f3a1d16a963857462c30cebb5e/database%20files/ERD.png)

I designed a 25-table normalized database holding data ranging from examinations data, staff salary, student class history to student, teacher and staff data.

Deciding how to store personnel data was quite the challenge. I wanted a way to organize the student, guardian, teacher and staff in an hierarchy under a person table with the added complexity of the teacher table being a child table to the staff table.

I was ultimately able to solve this problem with stored procedures which enabled me to write complicated logic in SQL that perform operations like check for existence of records before insertion etc. For example, this stored procedure served to promote specific students at the end of the school year:
```sql
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
```
[All stored procedures](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/tree/ac6fd5436c7207f3a1d16a963857462c30cebb5e/database%20files/stored%20procedures) used for the application can be studied to view my solution.  
<a name="application"/>
  
### Flask App 📱
  
Using the Blueprint feature of Flask, I organized my app into 4 main modules: auth, forms, models and views. View the [code](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/tree/ac6fd5436c7207f3a1d16a963857462c30cebb5e/app) here


  <a name="screenshots"/>
  
### Screenshots 📸

![screenshots](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/43b8ddbc69f94566bfa222bd258c976abe4f7d0b/screenshots/Screenshot%20(15).png)
  
![screenshots](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/43b8ddbc69f94566bfa222bd258c976abe4f7d0b/screenshots/Screenshot%20(16).png)

![screenshots](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/blob/43b8ddbc69f94566bfa222bd258c976abe4f7d0b/screenshots/Screenshot%20(17).png)

<!-- CONTACT  ☎️ -->

  <a name="contact"/>
  
## Contact

Edun Joshua Olubori - [connect on linkedin](https://www.linkedin.com/in/joshua-edun) - joshuaolubori@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>




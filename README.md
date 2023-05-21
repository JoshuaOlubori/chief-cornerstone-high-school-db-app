
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
[license-url]: https://github.com/JoshuaOlubori/UK-Road-Accident-Casualties/blob/f47c7d604613183d31617d101d14ef5c96503f1d/LICENSE.txt
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

I was ultimately able to solve this problem with stored procedures which enabled me to write complicated logic in SQL that perform operations like check for existence of records before insertion etc. The [code](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/tree/ac6fd5436c7207f3a1d16a963857462c30cebb5e/database%20files/stored%20procedures) for the stored procedures can be studied to view my solution
  
<a name="application"/>
  
### Flask App 📱
  
Using the Blueprint feature of Flask, I organized my app into 4 main modules: auth, forms, models and views. View the [code](https://github.com/JoshuaOlubori/chief-cornerstone-high-school-db-app/tree/ac6fd5436c7207f3a1d16a963857462c30cebb5e/app) here


  <a name="screenshots"/>
  
### Screenshots 📸

![screenshots](https://github.com/JoshuaOlubori/UK-Road-Accident-Casualties/blob/ddb49a64610e84d36ded41d2096050e7a2f3c183/report.png)



<!-- CONTACT  ☎️ -->

  <a name="contact"/>
  
## Contact

Edun Joshua Olubori - [connect on linkedin](https://www.linkedin.com/in/joshua-edun) - joshuaolubori@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>




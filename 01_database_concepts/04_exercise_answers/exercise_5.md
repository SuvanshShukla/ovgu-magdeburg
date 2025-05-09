# Database Concepts Exercise 5

Create ER schemas for the following use cases. Provide key attributes for entities and
cardinalities for relationships. Avoid redundancies. Add missing information accor-
ding to the task.

## Question 1

Your task is to design a database about software products. Every software pro-
duct has a name, a version number, a price and is created by a software company.
It must be possible to store different versions of a software product. Additional-
ly, some software products require other software products to run (e.g., Oracle8i
requires Java). Thereby, a software product can be required by more than one
other software product or not at all.
Prepare an entity-relationship schema of the requested database about software
products!

![task 1 image](./exercise5-images/dbc-exercise-5-1.svg)

## Question 2

The government needs a database about universities and their faculties. A uni-
versity has a unique name, an address and a number of enrolled students. Mo-
reover, every university has at least two faculties. Thereby, faculties belong to
exactly one university. Within one university, faculties are uniquely identified
by their name. That means, faculties of different universities can have the same
name. Additionally, for every faculty the name of the faculty's head must be
stored.
Prepare an entity-relationship schema of the requested database about univer-
sities!

![task 2 image](./exercise5-images/dbc-exercise-5-2.svg)


## Question 3

Your software company wants to sell an application for universities to manage
students and their exercise results. Your task is to prepare an entity-relationship
schema describing the required database. Thereby, you must define all key at-
tributes and cardinalities. Moreover, you should provide additional information
if necessary. Following list contains the initial requirements:

(a). Following information must be stored about students: name, student ID,
semester address including phone number, home address including phone
number, birth date and gender. Moreover, a student is enrolled in a specific
faculty and studies in certain semester. If known, the currently targeted
graduation should be stored.

(b). Following information about faculties must be stored: name, ID, secretary
and phone number

(c). The database must store courses. Every course has a name, a description,
a course number, credit points and a difficulty level. Thereby, every course
is offered by a specific faculty. Course numbers are unique.

(d).Courses can offer exercises. Besides the related course, for every exercise,
the term and year, when it is offered, must be stored. Additionally, the
exercise instructor and exercise number must be stored. Thereby, the exer-
cise number is unique for all exercises that are offered in the same term
and year. Exercises within one term and year are numbered consecutively
starting with 1, 2, 3, . . . up to the number of offered exercise classes.

(e). For each exercise performance, the student, the exercise and the grade are
stored.

![task 3 image](./exercise5-images/dbc-exercise-5-3.svg)


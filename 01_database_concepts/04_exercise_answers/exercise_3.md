# Exercise 3

## 1. We want to store information about students' preferences of restaurants in a database. Each restaurant has a name, an owner as well as an address consisting of postal code, city and street. For every student we store the student ID, first and last name, and the course of studies. Create the STUDENT and RESTAURANT tables using SQL!

```sql

CREATE TABLE restaurant (
    name VARCHAR(255),
    owner VARCHAR(100),
    city VARCHAR(100),
    street VARCHAR(100),
    postal_cd VARCHAR(100)
);

CREATE TABLE student (
    id INT,
    f_name VARCHAR(100),
    l_name VARCHAR(100),
    course VARCHAR(100)
);
```

## 2. Create a third table STUDENT RESTAURANT that stores the information which student prefers which restaurant! Moreover, alter the table STUDENT to additionally store a student's age 

```sql
CREATE TABLE student_restaurant (
    stu_id INT,
    res_name VARHAR(255)
);

ALTER TABLE student ADD age INT NOT NULL CHECK (age>=0);
```

## 3. Given the example database in the appendix, create the tables for the relations WINE and PRODUCER. The default value for COLOR is RED. Moreover, the uniqueness of the growing area shall be granted.



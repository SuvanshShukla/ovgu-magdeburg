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

```sql
CREATE TABLE producer (
    vinyard VARCHAR(100),
    area VARCHAR(100) UNIQUE,
    region VARCHAR(100),
    PRIMARY KEY (vinyard)
);

CREATE TABLE wine (
    name VARCHAR(100),
    color VARCHAR(100) DEFAULT 'RED',
    year INT,
    vinyard VARCHAR(100),
    PRIMARY KEY (name),
    FOREIGN KEY (vinyard) REFERENCES PRODUCER(vinyard)
);
```

## 4. Use SQL to create a relation for football players! Football players have a first and a last name, a birth date, a shirt number and a position, where they are playing. The position is restricted to following values: Goalkeeper, defence, forwards and midfield. Prepare two different solutions to check the value domain of the position attribute.

```sql
CREATE TABLE players (
    f_name VARCHAR(100),
    l_name VARCHAR(100),
    dob DATE,
    s_num INT,
    position VARCHAR()
);
```

## 5. Add the following entries to the example tables from the appendix using SQL:

### (a) The Johannishof Winery settled in the area Rheingau, which is in the Hessen region

```sql
INSERT INTO producer (vineyard, area, region) VALUES ('Johannishof', 'Rheingau', 'Hessen');
```

### (b) Add the wine Merlot to the database. It is a wine from the year 2009, which was produced in the winery from the region South Australia. The default color will be used.

```sql
INSERT INTO wine (name, year, vineyard) VALUES ('Merlot', 2009, (select vineyard from producer where region ='South Austrailia'));
```

## 6. Formulate the following operations in SQL for the sample database in the appendix.

### (a) Update all red wines by increasing their vintage by 1 year.

```sql
UPDATE wine SET year = year +1;
```

### (b) Empty the table wine.

```sql
TRUNCATE TABLE wine;
```

### (c) Delete the entire table producer.

```sql
DROP TABLE producer CASCADE;
```

---

## Extra insert queries

```sql
insert into wine values
('La Rose Grand Cru', 'RED', 1998, 'Ch\^ateau La Rose'),
('Creek Shiraz', 'RED', 2003, 'Creek'),
('Zinfandel', 'red', 2004, 'Helena'),
('Pinot Noir', 'red', 2001, 'Creek'),
('Merlot', 'red', 1999, 'Helena'),
('Riesling Reserve', 'white', 1999, 'M\"uller'),
('Chardonnay', 'white', 2002, 'Bighorn');

insert into producer values
('Creek', 'Barossa Valley', 'South Australia'),
('Helena', 'Napa Valley', 'Kalifornien'),
('Ch\^ateau La Rose', 'Saint-Emilion', 'Bordeaux'),
('Ch\^ateau La Pointe', 'Pomerol', 'Bordeaux'),
('M\"uller', 'Rheingau', 'Hessen'),
('Bighorn', 'Santa Barbara', 'Kalifornien');
```

## Complete queries that I pasted in pgAdmin

```sql
-- CREATE TABLE producer (
--     vinyard VARCHAR(100),
--     area VARCHAR(100) UNIQUE,
--     region VARCHAR(100),
--     PRIMARY KEY (vinyard)
-- );

-- CREATE TABLE wine (
--     name VARCHAR(100),
--     color VARCHAR(100) DEFAULT 'RED',
--     year INT,
--     vinyard VARCHAR(100),
--     PRIMARY KEY (name),
--     FOREIGN KEY (vinyard) REFERENCES PRODUCER(vinyard)
-- );

select * from producer;
select * from wine;

-- insert into wine values
-- ('La Rose Grand Cru', 'RED', 1998, 'Ch\^ateau La Rose'),
-- ('Creek Shiraz', 'RED', 2003, 'Creek'),
-- ('Zinfandel', 'red', 2004, 'Helena'),
-- ('Pinot Noir', 'red', 2001, 'Creek'),
-- ('Merlot', 'red', 1999, 'Helena'),
-- ('Riesling Reserve', 'white', 1999, 'M\"uller'),
-- ('Chardonnay', 'white', 2002, 'Bighorn');

-- insert into producer values
-- ('Creek', 'Barossa Valley', 'South Australia'),
-- ('Helena', 'Napa Valley', 'Kalifornien'),
-- ('Ch\^ateau La Rose', 'Saint-Emilion', 'Bordeaux'),
-- ('Ch\^ateau La Pointe', 'Pomerol', 'Bordeaux'),
-- ('M\"uller', 'Rheingau', 'Hessen'),
-- ('Bighorn', 'Santa Barbara', 'Kalifornien');

-- alter table wine rename vinyard to vineyard;
-- alter table producer drop constraint "producer_area_key";
insert into wine (name, year, vineyard) values ('Merlot', 2009, (select vineyard from producer where region ='South Austrailia'));
INSERT INTO producer (vineyard, area, region) VALUES ('Johannishof', 'Rheingau', 'Hessen');


-- truncate table wine;
-- drop table producer cascade;
```

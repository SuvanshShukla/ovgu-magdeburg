# Database Concepts Exercise 10

## Tables

Customer Table:

|Cid|Name|
|--|--|
|13|M.Mueller|
|17|A.Meier|
|23|I.Schulze|

Dealer table:

|Did|Name|
|---|---|
|5|G.Hals|
|7|P.Schmidt|
|11|E.Meier|
|13|E.Mueller|

Product table;

|Pid|Label|
|--|--|
|45|Power adapter|
|57|Cat5 cable|
|67|Mainboard|

Offers table:

|Did|Pid|
|--|--|
|5|45|
|5|57|
|7|67|
|7|45|
|11|57|
|5|67|
|11|67|

Orders table:

|Oid|Did|Date|Cid|
|--|--|--|--|
|3|7|0.1.12.2002|17|
|5|11|27.04.2003|23|
|7|5|13.05.2003|17|
|10|5|01.09.2003|13|

Line_item table

|Oid|Pid|Amount|
|--|--|--|
|3|45|1|
|3|67|5|
|5|67|5|
|7|57|3|
|7|67|2|
|10|45|2|
|10|57|5|
|10|67|3|

---

## Create and insert queries

```SQL
-- Customer Table
CREATE TABLE Customer (
    Cid INTEGER PRIMARY KEY,
    Name TEXT
);

-- Dealer Table
CREATE TABLE Dealer (
    Did INTEGER PRIMARY KEY,
    Name TEXT
);

-- Product Table
CREATE TABLE Product (
    Pid INTEGER PRIMARY KEY,
    Label TEXT
);

-- Offers Table (many-to-many: Dealer ↔ Product)
CREATE TABLE Offers (
    Did INTEGER REFERENCES Dealer(Did),
    Pid INTEGER REFERENCES Product(Pid),
    PRIMARY KEY (Did, Pid)
);

-- Orders Table
CREATE TABLE Orders (
    Oid INTEGER PRIMARY KEY,
    Did INTEGER REFERENCES Dealer(Did),
    Date DATE,
    Cid INTEGER REFERENCES Customer(Cid)
);

-- Line_item Table (many-to-many: Orders ↔ Product with Amount)
CREATE TABLE Line_item (
    Oid INTEGER REFERENCES Orders(Oid),
    Pid INTEGER REFERENCES Product(Pid),
    Amount INTEGER,
    PRIMARY KEY (Oid, Pid)
);

INSERT INTO Customer (Cid, Name) VALUES
(13, 'M.Mueller'),
(17, 'A.Meier'),
(23, 'I.Schulze');

INSERT INTO Dealer (Did, Name) VALUES
(5, 'G.Hals'),
(7, 'P.Schmidt'),
(11, 'E.Meier'),
(13, 'E.Mueller');

INSERT INTO Product (Pid, Label) VALUES
(45, 'Power adapter'),
(57, 'Cat5 cable'),
(67, 'Mainboard');

INSERT INTO Offers (Did, Pid) VALUES
(5, 45),
(5, 57),
(7, 67),
(7, 45),
(11, 57),
(5, 67),
(11, 67);

INSERT INTO Orders (Oid, Did, Date, Cid) VALUES
(3, 7, '2002-12-01', 17),
(5, 11, '2003-04-27', 23),
(7, 5, '2003-05-13', 17),
(10, 5, '2003-09-01', 13);

INSERT INTO Line_item (Oid, Pid, Amount) VALUES
(3, 45, 1),
(3, 67, 5),
(5, 67, 5),
(7, 57, 3),
(7, 67, 2),
(10, 45, 2),
(10, 57, 5),
(10, 67, 3);
```

---

## Question 1. Express following queries in SQL!

a. Get the names of all customers.

```SQL
select name from customer;
```

b. Get all orders of customer Meier.

```SQL
select o.* from customer c inner join orders o on o.cid = c.cid 
where c.name ilike '%meier'; 
```

c. List all products that have not been sold on 13.05.2003.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid 
where o.date != '13-05-2003';
```

The above query looks correct but there's a catch. This query may end up still returning all the products, and this may happen  
when the same product was sold on 13.05.2003 and some other date. So even though you were expecting one product to be skipped, it would be included.    
Basically if the same product was sold on 13.05.2003 and on 14.05.2003, would it still be correct to return that product?   
So the correct query should be like below:

```SQL
select * from product where pid not in (
    select pid from line_item l inner join orders o on l.oid = o.oid
    where o.date = '2003-05-13'
);
```

d. List all products that dealer Meier sold to customer Schulze.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid 
join customer c on c.cid = o.cid 
join dealer d on d.did = o.did 
where d.name like '%Meier' and c.name like '%Schulze';
```

e. Get all products that dealer Meier sold and customer Schulze bought.

```SQL
select p.* from product p join line_item l on p.pid = l.pid 
join orders o on o.oid = l.oid join customer c on c.cid = o.cid 
join dealer d on d.did = o.did 
where d.name like '%Meier' and c.name like '%Schulze';
```

## Question 2. Describe the following queries in SQL!

(a) Get the label of all products that are ordered more than twice.

```SQL
select p.label from product p join line_item l on l.pid = p.pid 
group by l.pid, p.label;
```

(b) Which customers (name) haven't ordered anything?

```SQL
select c.name from customer c where c.cid not in (select cid from orders);
```

(c) For all dealers (name), list the products (label) that they do not offer.

```SQL
select d.name, p.label from dealer d cross join offers o inner join product p on p.pid = o.pid
except 
select d.name, p.label from dealer d inner join offers o on o.did = d.did inner join product p on p.pid = o.pid;
```

(d) Output the products (label) sorted by total SalesPerProduct.

```SQL
select p.label, sum(amount) as sales from product p join line_item l on p.pid = l.pid group by label order by sales asc;
```

(e) Output the name of all dealers and their respective orders (if no order exists, fill these entries with NULL)!

```SQL
select d.name, o.* from dealer d left outer join orders o on d.did = o.did;
```

## Question 3. Convert the SQL schema into an ER-schema.



## Question 4. To solve this task, use recursive SQL as it is defined by Oracle (and lecture):

| Id | Name         | Manager |
| -- | ------------ | ------- |
| 1  | Amy Teipist  | 3       |
| 2  | Tom Owner    | NULL    |
| 3  | Tim Managor  | 7       |
| 4  | John Clerk   | 3       |
| 5  | Juli Sal     | 2       |
| 6  | Paul Meier   | 3       |
| 7  | Don Boss     | 2       | 
| 8  | Rob Marketor | 5       |

Create and insert queries for the above table:

```SQL
CREATE TABLE organization (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager INTEGER REFERENCES organization(id)  -- self-referential foreign key
);

INSERT INTO organization (id, name, manager) VALUES
(1, 'Amy Teipist', 3),
(2, 'Tom Owner', NULL),
(3, 'Tim Managor', 7),
(4, 'John Clerk', 3),
(5, 'Juli Sal', 2),
(6, 'Paul Meier', 3),
(7, 'Don Boss', 2),
(8, 'Rob Marketor', 5);
```

(a) When and why is recursive SQL necessary?

Recursive SQL is necessary when we need to find data with self-referential properties. Like when finding the hierarchy of employees at a company

(b) Create an SQL query that returns all direct managers of Paul Meier!

```SQL
select o1.name from  organization o1 inner join organization o2 on o2.manager = o1.id where o2.name = 'Paul Meier';
```

(c) Create an SQL query that returns all direct and indirect managers of Paul Meier.

```SQL
with RECURSIVE bosses as (
select o1.name, o1.id from  organization o1 inner join organization o2 on o2.manager = o1.id where o2.name = 'Paul Meier'
union all
select e.name, e.id from organization e join bosses b on e.manager = b.id
) select * from bosses;
```

## Question 5. Given following relation:

`exams(course_of_studies, course, student, examiner, date, mark)`

Define the following views using SQL:

(a) The computer science faculty can only view data of students that are registered in computerscience.

```SQL
create view compsci_faculty_view as 
    select * from exams 
    where course_of_studies = 'computerscience';
```

(b) The examination office can view all data.

```SQL
create view examination_office_view as 
    select * from exams;
```

(c) The scholarship commission can only view average marks of every student.

```SQL
create view scholarship_comm_view as 
    select student, avg(mark) from exams 
    group by student;
```

(d) The dean can only view data about exams of the last year for statistical purposes (i.e., the relationship to students and examiners must be removed).

```SQL
create view dean_view as 
    select course_of_studies, course, student, Max(date), mark from exams where date = extract(year from date) < extract(year from now())-1;
```

the corrected query:

```SQL
CREATE VIEW dean_view AS 
SELECT course_of_studies, course, date, mark 
FROM exams 
WHERE extract(year FROM date) = extract(year FROM now()) - 1;
```

## Question 6. Given the following tables: 

| Date     | Orders     |
| ----     | ------     |
| 02.09.03 | Furniture  |
| 23.06.04 | Vegetables |
| 01.12.05 | Pots       |
| 15.01.06 | Cutlery    |

| Date     | Value |
| ----     | ----- |
| 02.09.03 | 4000€ |
| 23.06.04 | 100€  |
| 01.12.05 | 500€  |

Join the tables using:

(a) Equi-Join (⨝ Date=Date)

| Date     | Orders     | Date     | Value |
| ----     | ------     | ----     | ----- |
| 02.09.03 | Furniture  | 02.09.03 | 4000€ |
| 23.06.04 | Vegetables | 23.06.04 | 100€  |
| 01.12.05 | Pots       | 01.12.05 | 500€  |
| 15.01.06 | Cutlery    | NULL     | NULL  |

(b) Theta-Join (⨝ Date>Date)

| Date     | Orders     | Date     | Value |
| ----     | ------     | ----     | ----- |
| 02.09.03 | Furniture  | NULL     | NULL  |
| 23.06.04 | Vegetables | 02.09.03 | 4000€ |
| 01.12.05 | Pots       | 02.09.03 | 4000€ |
| 01.12.05 | Pots       | 23.06.04 | 100€  |
| 15.01.06 | Cutlery    | 02.09.03 | 4000€ |
| 15.01.06 | Cutlery    | 23.06.04 | 100€  |
| 15.01.06 | Cutlery    | 01.12.05 | 500€  |

(c) Semi-Join (⋉)

| Date     | Orders     |
| ----     | ------     |
| 02.09.03 | Furniture  |
| 23.06.04 | Vegetables |
| 01.12.05 | Pots       |

**NOTE: See how date and value columns were not added to the result!**        
Also this row `| 15.01.06 | Cutlery    |` wouldn't be included as `15.01.06` is not present in the value table    

## Question 7. Calculate the following division: R ÷ R1, R ÷ R2, R ÷ R3 using the following relations!

Relation R is:

| Name    | Product |
| ----    | ------- |
| Meier   | Tea     |
| Meier   | Coffee  |
| Meier   | Wine    |
| Mueller | Wine    |
| Schmidt | Beer    |
| Schmidt | Wine    |
| West    | Tea     |
| West    | Coffee  |

Relation R1 is: 

| Product |
| ------- |
| Tea     |
| Coffee  |

Relation R2 is: 

| Product |
| ------- |
| Wine    |

Relation R3 is:

| Product |
| ------- |
| Wine    |
| Beer    |

Division for R ÷ R1 is: 

| Name  |
| ----  |
| Meier |
| West  |

Division for R ÷ R2 is: 

| Name    | 
| ----    |
| Meier   |
| Mueller |
| Schmidt |

Division for R ÷ R3 is: 

| Name    |
| ----    |
| Schmidt |


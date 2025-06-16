# Database Concepts Exercise 9 

## Quesiton 1. Formulate SQL queries

(a) Query name and salary of all employees that earn more than 6450€ .

```SQL
select name, salary from eployee where salary > 6450;
```

(b) Query name and salary of all employees that do not earn between 6000 and 10000.

```SQL
select name, salary from employees where salary between 6000 and 10000;
```

(c) Query all planes that are of type A-340 or TRIDENT. Sort by purchase date.

```SQL
select * from plane where type = 'A-340' or type = 'TRIDENT' order by purchase_date;
```

(d) Which pilots have a license different from I and II

```SQL
select * from pilot where license not in ('I', 'II');
```

(e) Determine the names of employees that have an A at the third position of their name.

```SQL 
select name from employee where name like '__a%';
```

(f) Determine the names of employees that have the L twice in their name.

```SQL
select name from employee where name like '%l%l%';
```

(g) Query name, job and salary of all employees whose job is either Dipl. Ing. or steward/ ess and that earn are least 6000€ .

```SQL

```

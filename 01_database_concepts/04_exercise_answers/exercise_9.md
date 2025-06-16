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

## 2. Define the following queries in SQL:

(a) Determine employee Id, name and salary of all employees. Add an intermediate column new salary to the query result that shows the current salary increased by 15\%. The new salary must be returned as integer value.

```SQL
select id, name, salary, (salary + (salary * 0.15)) as new_salary from employee;
```

(b) Given your solution from task (a), add another intermediate column that shows the difference between the original salary and the new salary. The difference must also be returned as integer value.

```SQL
select id, name, salary, (salary + (salary * 0.15)) as new_salary, (salary - (salary + (salary * 0.15)) as salary_difference from employee;
```

(c) For every plane, list its type, serial number and operating hours. Operating hours must be returned in a column called operating hours. The operating hours are computed by calculating the difference between today and the purchase date of the respective plane. Use a standard date function to calculate the difference and return your result as integer. Finally, sort your list by operating hours.

```SQL
select type, serial_number, 
```

(d) Create a query that returns following string for every employee: < name > earns < salary > per month, but desires to earn < 3\ast salary >. Replace all placeholders with the respective data using SQL. The new column is called desired salary.

```SQL
```

(e) List all plane types. Thereby, all first letters must be capitalized, the rest must be uncapitalized. Return the length of the type name in a second column. The columns are called name und length.

```SQL
```



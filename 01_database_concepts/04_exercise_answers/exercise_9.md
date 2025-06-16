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

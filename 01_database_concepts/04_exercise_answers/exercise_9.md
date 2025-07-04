# Database Concepts Exercise 9 

Given the following relational schema:

> flight (label, date, destination, fligth time, distance)      
> departure ( (flight_label, flight_date) ->  flight,(type, serial number) -> plane, captain))      
> employee (ID, name, address, job, salary)     
> plane_type (type, manufacturer, number_of_seats, cruising_speed)      
> plane (type -> plane_type, serial_number, purchase_date, flight_hours)        
> spare part (ID, label, price)         
> requires (type -> plane_type, serial_number -> plane, spare_part_ID -> spare_part)        
> pilot (employee_ID -> employee, license, flight_hours)        
> technician (employee ID ->  employee, team number)        
> can_fly (employee ID ->  pilot, type ->  plane_type)      
> can maintain (employee ID ->  technician, type ->  plane_type)        
> passenger (passenger ID, name, address, age)      
> booking (passenger ID ->  passenger, (flight_label, flight_date) ->  flight, class, seat number, price)       

## Quesiton 1. Formulate SQL queries

(a) Query name and salary of all employees that earn more than 6450€ .

```SQL
select name, salary from employee where salary > 6450;
```

(b) Query name and salary of all employees that do not earn between 6000 and 10000.

```SQL
select name, salary from employee where salary not between 6000 and 10000;
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
select name from employee where name ilike '__a%';
```

(f) Determine the names of employees that have the L twice in their name.

```SQL
select name from employee where name like '%l%l%';
```

(g) Query name, job and salary of all employees whose job is either Dipl. Ing. or steward/ ess and that earn are least 6000€ .

```SQL
select name, job, salary from employee where (job like 'Dipl%' or job like 'steward%') and salary >= 6000;
```

## 2. Define the following queries in SQL:

(a) Determine employee Id, name and salary of all employees. Add an intermediate column new salary to the query result that shows the current salary increased by 15\%. The new salary must be returned as integer value.

```SQL
select id, name, salary, cast(salary + (salary * 0.15) as integer) as new_salary from employee;
```

(b) Given your solution from task (a), add another intermediate column that shows the difference between the original salary and the new salary. The difference must also be returned as integer value.

```SQL
select id, name, salary, (salary + (salary * 0.15)) as new_salary, ((salary + (salary * 0.15)) - salary) as salary_difference from employee;
```

(c) For every plane, list its type, serial number and operating hours. Operating hours must be returned in a column called operating hours. The operating hours are computed by calculating the difference between today and the purchase date of the respective plane. Use a standard date function to calculate the difference and return your result as integer. Finally, sort your list by operating hours.

```SQL
select type, serial_number, FLOOR(EXTRACT(EPOCH from age(purchase_date))/3600) as operating_hours from plane order by operating_hours;
```

(d) Create a query that returns following string for every employee: `< name > earns < salary > per month, but desires to earn < 3 * salary >`. Replace all placeholders with the respective data using SQL. The new column is called desired salary.

```SQL
select concat(name, ' earns ', salary, ' per month, but desires to earn ', salary * 3) desired_salary from employee;
```

(e) List all plane types. Thereby, all first letters must be capitalized, the rest must be uncapitalized. Return the length of the type name in a second column. The columns are called name und length.

```SQL
select initcap(type) as name, char_length(type) length from plane_type;
```

## Question 3. Use SQL to retrieve following information:

(a) How many planes (not types) are stored in relation departure?

```SQL
select count(*) from (select distinct type, serial_number from departure) as unique_planes;
```

(b) Determine the number of employees that have a doctor's degree (Dr. or PhD)!

```SQL
select count(*) from employee where job in ('doctor', 'professor') group by job;
```

(c) What is the average salary by job?

```SQL
select job, avg(salary) from employee group by job;
```

(d) Return the total price and the number of bookings for all journeys in 1993 in relation booking.

```SQL
select sum(price), count(*) from booking where flight_date between '1993-01-01' and '1993-12-31';
```

(e) Determine the minimum salary for every job!

```SQL
select job, MIN(salary) from employee group by job;
```

(f) Retrieve the difference between the maximum and minimum salary of the all employees.

```SQL
select MAX(salary) - MIN(salary) from employee;
```

## 4. You are new in the university IT department. Your task is to reformulate following SQL query as it is to slow currently:

```
SELECT DISTINCT X.exam_ID FROM exams X
WHERE X.exam_ID IN (
SELECT Y.exam_ID FROM exams Y
WHERE Y.student_ID <> X.student_ID);
```

Maybe, a reformulation will improve the query performance. In order to reformulate it, solve following tasks:

(a) What is the result of this query?

This query returns the exam IDs of exams that are taken by more than one student

(b) You found two ways to reformulate the query. Reformulate the query

1. Without using a nested query in the WHERE clause!

```SQL
select distinct(x.exam_id) from exams x join exams y on x.exam_id = y.exam_id 
where y.student_id <> x.student_id;
```

2. Without using tuple variables (to distinguish the use of the same relation), but by using aggregation functions.

```SQL
select exam_id from exams group by exam_id having count(distinct(student_id)) > 1;
```

## Question 5. Given the following tables:

| Name    | Pid  |  
| ------- | ---- |  
| Meier   | 1586 |  
| Mueller | 1001 |  
| chmidt  | 905  |  

| Pid  | Salary |                   
| ---- | ------ |
| 1586 | 4000   |
| 1235 | 2500   |
| 905  | 1000   |
| 512  | 1575   |

Join the tables using a:

(a) Natural-Join

```SQL
select * from name natural join salary;
```

(b) Left-Outer-Join

```SQL
select * from name a left outer join salary s on s.pid = a.pid;
```
(c) Right-Outer-Join

```SQL
select * from name a right outer join salary s on s.pid = a.pid;
```

(d) Full-Outer-Join

```SQL
select * from name a full outer join salary s on s.pid = a.pid;
```



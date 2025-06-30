# Database Concepts Exercise 11

## 1. Given the following example database from the appendix. Formulate following queries using relational algebra:

(a) Query the names of employees, who work on all projects that John Smith is working on.


(b) Query name and address of all employees, who work for the Research department.
(c) Query the project number of the project that is located in Stafford. Moreover, you should retrieve the number of the department that controls the project as well as as the responsible manager's name, address and birth day.
(d) Query the names of employees, who work on all projects controlled by department 5.
(e) List all project numbers of projects that involve an employee (including managers) whose last name is Smith.

## 2. Given the example database in the appendix, formulate the following queries in relational algebra:
(a) Find all employees with two or more relatives!
(b) Find the names of all employees that have no relatives!
(c) Find the names of managers with at least one relative!
(d) Which employees work on more than two projects?
(e) Find for every department (DName), the projects (PName) they are not working on!

## 3. Given following relational schema:

```
Station: (Name: string)
Train: (Train_number: integer, Manufacturer: string)
Local_train: (Train_number-> Train, Bikes_allowed: boolean)
Distance_train: (Train_number-> Train, Dining_car: boolean, Label: string)
Car: (Car_number: integer, Train_number-> Train, Position: integer)
eat: (Car_number: integer-> Car, Seat_number: integer, Category: integer,
Smoker: boolean, Window:boolean)
Connection: (Arrival: time, Departure: time, Day: date, starts_at: string-> Station,
goes_to: string-> Station, Train_number: integer-> Train)
Ticket: (Price: integer, Ticket_nubmer: integer)
Reservation: (Ticket_number-> Ticket, (Arrival, Departure, Day, starts_at,
goes_to, Train_number)-> Connection, (Car_number,
Seat_number)-> Seat, Price: integer)
Valid_for: ((Arrival, Departure, Date, starts_at, goes_to, Train_number)-> Connection,
Ticket_number-> Ticket)
Adds_discount: (Label: string, Unit: string, Amount: integer
requires: string-> Adds_Discount)
Imputation: (Ticket_number-> Ticket, Label-> Adds_discount)
Excludes: (Excluder: string-> Adds_discount, Excluded: string-> Adds_discount)
```

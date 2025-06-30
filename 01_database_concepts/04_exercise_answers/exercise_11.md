# Database Concepts Exercise 11
⨝ , Π, σ, 

## 1. Given the following example database from the appendix. Formulate following queries using relational algebra:

(a) Query the names of employees, who work on all projects that John Smith is working on.

```
Π fname,lname σ fname="John",lname="Smith" (Employee ⨝ (ssn=essn) works_on ⨝ (pno=pnumber) project)
```

(b) Query name and address of all employees, who work for the Research department.

```
Π fname,lname,address σ dname="Research" (employee ⨝ (ssn=mgrssn) department)
```

(c) Query the project number of the project that is located in Stafford. Moreover, you should retrieve the number of the department that controls the project as well as as the responsible manager's name, address and birth day.

```
Π pnumber,dnum,fname,lname,address,bdate σ plocation="Stafford" (project ⨝ (dnum=dnumber) department ⨝ (dnumber=dno) employee)
```

(d) Query the names of employees, who work on all projects controlled by department 5.

```
Π fname,lname σ dnum=5 (project ⨝ (ssn=essn) works_on ⨝ (pno=pnumber) project)
```

(e) List all project numbers of projects that involve an employee (including managers) whose last name is Smith.

```
Π pnumber σ lname=smith (project ⨝ (ssn=essn) works_on ⨝ (pno=pnumber) project)
```

## 2. Given the example database in the appendix, formulate the following queries in relational algebra:

(a) Find all employees with two or more relatives!

```
Ύ dependent;count(essn)>=2 (employee ⨝ (ssn=essn) dependent)
```

(b) Find the names of all employees that have no relatives!

```
Π fname,lname Ύ dependent;count(essn)=0 (employee ⨝ (ssn=essn) dependent)
```

(c) Find the names of managers with at least one relative!

```
Π fname,lname Ύ dependent;count(essn)>=1 (employee ⟕ (ssn=mgrssn) department ⨝ (ssn=essn) dependent)
```

(d) Which employees work on more than two projects?

```
Ύ project,count(pnumber)>=1 (employee ⨝ (essn=ssn) works_on ⨝ (pno=pnumber) project)
```

(e) Find for every department (DName), the projects (PName) they are not working on!

```
(department ⨝  project) - (department ⨝ (dnumber=dnum) project)
```

## 3. Given following relational schema:

```
Station: (Name: string)
Train: (Train_number: integer, Manufacturer: string)
Local_train: (Train_number-> Train, Bikes_allowed: boolean)
Distance_train: (Train_number-> Train, Dining_car: boolean, Label: string)
Car: (Car_number: integer, Train_number-> Train, Position: integer)
Seat: (Car_number: integer-> Car, Seat_number: integer, Category: integer, Smoker: boolean, Window:boolean)
Connection: (Arrival: time, Departure: time, Day: date, starts_at: string-> Station, goes_to: string-> Station, Train_number: integer-> Train)
Ticket: (Price: integer, Ticket_nubmer: integer)
Reservation: (Ticket_number-> Ticket, (Arrival, Departure, Day, starts_at, goes_to, Train_number)-> Connection, (Car_number, Seat_number)-> Seat, Price: integer)
Valid_for: ((Arrival, Departure, Date, starts_at, goes_to, Train_number)-> Connection, Ticket_number-> Ticket)
Adds_discount: (Label: string, Unit: string, Amount: integer requires: string-> Adds_Discount)
Imputation: (Ticket_number-> Ticket, Label-> Adds_discount)
Excludes: (Excluder: string-> Adds_discount, Excluded: string-> Adds_discount)
```

Formulate following queries using the tuple calculus:

(a) Find all stations.

```
{ w | w ∈ station }
```

(b) Find the labels of all discounts and additions.
(c) Find all tickets that cost more than 100€.

```
{ w | w ∈ ticket ∧ w.price>100 }
```

(d) Find all departure times of all connections that go from Munich to Augsburg before noon (12 o'clock).

```
{ w.departure | w ∈ connection ∧ w.starts_at='Munich' ∧ w.goes_to='Augsburg' ∧ w.departure<'12:00' }
```

(e) Find all trains that have a connection from Munich to Augsburg.

```
{ u | u ∈ train ∧ w ∈ connection ∧ w.train_number=u.train_number ∧ w.starts_at='Munich' ∧ w.goes_to='Augsburg' }
```

(f) Find all discounts and additions that do not depend on others and do not exclude others.

## 4. Formulate the queries from task 2 using the domain calculus.

(e) Find for every department (DName), the projects (PName) they are not working on!

```
{ dname, pname | department(a,b,c,d) ∧ project(x,y,z,b) ∧ department(b) != project(b) } 
```

## 5. Basic Terms (Views, Transactions, Trigger):

**(a) What is a view? What are views used for?**

A view is basically a saved query that allows you to perform queries on it. It allows you to restrict what data is visible to what kind of user.
It enhances convenience and improves security.

**(b) Reiterate the term transaction and explain the ACID-principle!**

A transaction is a set of commands that are executed on a database in an ordered or unordered manner.   
ACID is an acronym that denotes: atomicity, consistency, isolation and durability.  
Atomicity means that every command must be complete and cannot be broken down further into smaller commands.    
Consistency means that the data saved in the database should be same throughout and not be different.   
Isolation means that operating or changing data somewhere in the database would not affect the data somewhere else. 
Durability means that the data that has been saved should be retrievable and not easily lost.   

Atomicity: Transactions cannot be broken down into smaller transactions and that they must be processed completely. 
Consistency: The database must remain in a valid state both before and after the transaction is processed.  
Isolation: Concurrent transactions should not interfere with each other, this means that multiple transactions can be processed and that the database would remain in a valid state throughout. 
Durability: Changes brought about by transactions should stay in the database and persist in it. They should be there even if there is a system failure.    

**(c) What is a trigger? Name important use cases and problems with triggers!**

A trigger is a statement or procedure that is executed automatically by the DBMS at the occurrence of a specific event.

An important use case of triggers would be to drop certain columns when a table is deleted.

A problem with triggers is that they can only be written for insert or update events.

# Database Concepts Exercise 11 - Solutions (Plain Text Version)

## 1. Given the following example database from the appendix. Formulate following queries using relational algebra:

(a) Query the names of employees, who work on all projects that John Smith is working on.
    * Let P_JS be the set of project numbers John Smith works on:
        P_JS = Project(pno) (Select(fname='John' AND lname='Smith') (Employee JOIN(ssn=essn) Works_on))
    * Then, find employees who work on all projects in P_JS:
        Project(fname, lname) (Employee JOIN(ssn=essn) (Works_on DIVIDE BY P_JS))

(b) Query name and address of all employees, who work for the Research department.
    Project(fname, lname, address) (Select(dname='Research') (Employee JOIN(dno=dnumber) Department))

(c) Query the project number of the project that is located in Stafford. Moreover, you should retrieve the number of the department that controls the project as well as the responsible manager's name, address and birth day.
    Project(pnumber, dnum, fname, lname, address, bdate) (Select(plocation='Stafford') (Project JOIN(dnum=dnumber) Department JOIN(mgrssn=ssn) Employee))

(d) Query the names of employees, who work on all projects controlled by department 5.
    * Let P_D5 be the set of project numbers controlled by department 5:
        P_D5 = Project(pnumber) (Select(dnum=5) (Project))
    * Then, find employees who work on all projects in P_D5:
        Project(fname, lname) (Employee JOIN(ssn=essn) (Works_on DIVIDE BY P_D5))

(e) List all project numbers of projects that involve an employee (including managers) whose last name is Smith.
    Project(pnumber) (Select(lname='Smith') (Employee JOIN(ssn=essn) Works_on JOIN(pno=pnumber) Project))

## 2. Given the example database in the appendix, formulate the following queries in relational algebra:

(a) Find all employees with two or more relatives!
    Project(fname, lname) (Select(count_dependents >= 2) (Employee JOIN(ssn=essn) (GROUP BY essn, COUNT(dependent_name) AS count_dependents (Dependent))))

(b) Find the names of all employees that have no relatives!
    Project(fname, lname) (Employee) MINUS Project(fname, lname) (Employee JOIN(ssn=essn) Dependent)
    Alternatively, using aggregation:
    Project(fname, lname) (Select(count_dependents = 0) (Employee JOIN(ssn=essn) (GROUP BY essn, COUNT(dependent_name) AS count_dependents (Dependent))))

(c) Find the names of managers with at least one relative!
    Project(fname, lname) (Select(count_dependents >= 1) (Employee JOIN(ssn=mgrssn) Department JOIN(ssn=essn) (GROUP BY essn, COUNT(dependent_name) AS count_dependents (Dependent))))

(d) Which employees work on more than two projects?
    Project(fname, lname) (Select(count_projects > 2) (Employee JOIN(ssn=essn) (GROUP BY essn, COUNT(DISTINCT pno) AS count_projects (Works_on))))

(e) Find for every department (DName), the projects (PName) they are not working on!
    Project(dname, pname) (Department CROSS JOIN Project) MINUS Project(dname, pname) (Department JOIN(dnumber=dnum) Project)

## 3. Given following relational schema:

(a) Find all stations.
    { w | w IN Station }

(b) Find the labels of all discounts and additions.
    { w.Label | w IN Adds_discount }

(c) Find all tickets that cost more than 100€.
    { w | w IN Ticket AND w.Price > 100 }

(d) Find all departure times of all connections that go from Munich to Augsburg before noon (12 o'clock).
    { w.Departure | w IN Connection AND w.starts_at = 'Munich' AND w.goes_to = 'Augsburg' AND w.Departure < '12:00' }

(e) Find all trains that have a connection from Munich to Augsburg.
    { t | t IN Train AND EXISTS c (c IN Connection AND c.Train_number = t.Train_number AND c.starts_at = 'Munich' AND c.goes_to = 'Augsburg') }

(f) Find all discounts and additions that do not depend on others and do not exclude others.
    { w | w IN Adds_discount AND NOT EXISTS u (u IN Adds_discount AND u.Label = w.requires) AND NOT EXISTS x (x IN Excludes AND x.Excluder = w.Label) }

## 4. Formulate the queries from task 2 using the domain calculus.

(a) Find all employees with two or more relatives!
    { F, M, L, S, B, A, X, Y, SS, DN | Employee(F, M, L, S, B, A, X, Y, SS, DN) AND COUNT({ DNAME, DX, DB, DR | Dependent(S, DNAME, DX, DB, DR) }) >= 2 }

(b) Find the names of all employees that have no relatives!
    { F, L | EXISTS M, S, B, A, X, Y, SS, DN (Employee(F, M, L, S, B, A, X, Y, SS, DN)) AND NOT EXISTS DNAME, DX, DB, DR (Dependent(S, DNAME, DX, DB, DR)) }

(c) Find the names of managers with at least one relative!
    { F, L | EXISTS M, S, B, A, X, Y, SS, DN, DNAME, DNUM, MS, MD (Employee(F, M, L, S, B, A, X, Y, SS, DN) AND Department(DNAME, DNUM, S, MD)) AND COUNT({ DNAME_D, DX, DB, DR | Dependent(S, DNAME_D, DX, DB, DR) }) >= 1 }

(d) Which employees work on more than two projects?
    { F, L | EXISTS M, S, B, A, X, Y, SS, DN (Employee(F, M, L, S, B, A, X, Y, SS, DN)) AND COUNT({ PNO, H | Works_on(S, PNO, H) }) > 2 }

(e) Find for every department (DName), the projects (PName) they are not working on!
    { DN, PN | EXISTS DNUM_D, M, MD (Department(DN, DNUM_D, M, MD)) AND EXISTS PNUM_P, PLOC_P, DNUM_P (Project(PN, PNUM_P, PLOC_P, DNUM_P)) AND NOT (EXISTS DNUM_MATCH (Department(DN, DNUM_MATCH, M, MD) AND Project(PN, PNUM_P, PLOC_P, DNUM_MATCH))) }

## 5. Basic Terms (Views, Transactions, Trigger):

**(a) What is a view? What are views used for?**
A view is a virtual table based on the result-set of a SQL query. [cite_start]It does not store data itself but rather presents data stored in base tables. [cite: 30]
Views are used for several purposes:
* [cite_start]**Security:** They can restrict access to specific rows or columns of a table, allowing users to see only the data they are authorized for. [cite: 30]
* [cite_start]**Simplification:** Complex queries can be saved as views, making it easier for users to interact with the database without needing to understand the underlying table structures or complex join operations. [cite: 30]
* [cite_start]**Consistency:** Views can present a consistent, simplified view of the database schema, even if the underlying base tables change. [cite: 30]

**(b) Reiterate the term transaction and explain the ACID-principle!**
[cite_start]A transaction is a set of commands that are executed on a database in an ordered or unordered manner. [cite: 31]
[cite_start]The ACID principle is a set of properties that guarantee that database transactions are processed reliably. [cite: 31] ACID is an acronym for:
* [cite_start]**Atomicity:** This means that every command within a transaction must be complete and cannot be broken down further into smaller commands. [cite: 31] All of its operations are completed successfully, or none of them are.
* [cite_start]**Consistency:** The database must remain in a valid state both before and after the transaction is processed. [cite: 31]
* [cite_start]**Isolation:** The execution of concurrent transactions should not interfere with each other. [cite: 31] This means that multiple transactions can be processed and the database would remain in a valid state throughout, as if each transaction were executed sequentially.
* [cite_start]**Durability:** Changes brought about by transactions should stay in the database and persist in it. [cite: 31] [cite_start]They should be there even if there is a system failure. [cite: 31]

**(c) What is a trigger? Name important use cases and problems with triggers!**
[cite_start]A trigger is a statement or procedure that is executed automatically by the DBMS at the occurrence of a specific event. [cite: 32]

**Important Use Cases for Triggers:**
* **Enforcing Complex Business Rules:** Triggers can enforce business rules that cannot be handled by standard constraints (e.g., automatically updating an inventory level when an order item is inserted).
* **Auditing and Logging:** Triggers can record changes to data, such as who changed what, when, and the old/new values, for auditing purposes.
* **Maintaining Data Integrity:** Automatically updating related tables to maintain consistency (e.g., ensuring summary data in one table is updated when detailed data in another changes).
* **Preventing Invalid Operations:** Triggers can stop an operation if it violates a complex condition.

**Problems with Triggers:**
* [cite_start]**Complexity and Debugging:** Triggers can make the database schema and application logic more complex and harder to understand, maintain, and debug, as their execution is implicit. [cite: 32]
* **Cascading Effects:** A trigger can cause another trigger to fire, leading to a chain of events that can be difficult to predict or control, potentially leading to performance issues or unintended data modifications.
* **Portability:** Trigger syntax and behavior can vary significantly between different DBMS products.
* **Performance Overhead:** Triggers add overhead to DML operations (INSERT, UPDATE, DELETE) because the DBMS must execute the trigger code in addition to the actual data modification.
* **Hidden Logic:** Logic embedded in triggers is often not immediately visible to developers, leading to unexpected behavior.

---

# Database Concepts Exercise 11 - Solutions

## 1. Given the following example database from the appendix. Formulate following queries using relational algebra:

(a) Query the names of employees, who work on all projects that John Smith is working on.
    * Let $P_{JS}$ be the set of project numbers John Smith works on.
    $$ P_{JS} = \Pi_{\text{pno}} (\sigma_{\text{fname='John' } \land \text{lname='Smith'}} (\text{Employee} \Join_{\text{ssn}=\text{essn}} \text{Works\_on})) $$
    * Then, find employees who work on all projects in $P_{JS}$. This requires a division operation.
    $$ \Pi_{\text{fname, lname}} (\text{Employee} \Join_{\text{ssn}=\text{essn}} (\text{Works\_on} \div P_{JS})) $$

(b) Query name and address of all employees, who work for the Research department.
$$ \Pi_{\text{fname, lname, address}} (\sigma_{\text{dname='Research'}} (\text{Employee} \Join_{\text{dno}=\text{dnumber}} \text{Department})) $$

(c) Query the project number of the project that is located in Stafford. Moreover, you should retrieve the number of the department that controls the project as well as the responsible manager's name, address and birth day.
$$ \Pi_{\text{pnumber, dnum, fname, lname, address, bdate}} (\sigma_{\text{plocation='Stafford'}} (\text{Project} \Join_{\text{dnum}=\text{dnumber}} \text{Department} \Join_{\text{mgrssn}=\text{ssn}} \text{Employee})) $$

(d) Query the names of employees, who work on all projects controlled by department 5.
    * Let $P_{D5}$ be the set of project numbers controlled by department 5.
    $$ P_{D5} = \Pi_{\text{pnumber}} (\sigma_{\text{dnum}=5} (\text{Project})) $$
    * Then, find employees who work on all projects in $P_{D5}$.
    $$ \Pi_{\text{fname, lname}} (\text{Employee} \Join_{\text{ssn}=\text{essn}} (\text{Works\_on} \div P_{D5})) $$

(e) List all project numbers of projects that involve an employee (including managers) whose last name is Smith.
$$ \Pi_{\text{pnumber}} (\sigma_{\text{lname='Smith'}} (\text{Employee} \Join_{\text{ssn}=\text{essn}} \text{Works\_on} \Join_{\text{pno}=\text{pnumber}} \text{Project})) $$

## 2. Given the example database in the appendix, formulate the following queries in relational algebra:

(a) Find all employees with two or more relatives!
$$ \Pi_{\text{fname, lname}} (\sigma_{\text{count\_dependents} \ge 2} (\text{Employee} \Join_{\text{ssn}=\text{essn}} (\mathcal{G}_{\text{essn}, \text{COUNT(dependent\_name) AS count\_dependents}} (\text{Dependent})))) $$

(b) Find the names of all employees that have no relatives!
$$ \Pi_{\text{fname, lname}} (\text{Employee}) - \Pi_{\text{fname, lname}} (\text{Employee} \Join_{\text{ssn}=\text{essn}} \text{Dependent}) $$
Alternatively, using aggregation:
$$ \Pi_{\text{fname, lname}} (\sigma_{\text{count\_dependents} = 0} (\text{Employee} \Join_{\text{ssn}=\text{essn}} (\mathcal{G}_{\text{essn}, \text{COUNT(dependent\_name) AS count\_dependents}} (\text{Dependent})))) $$

(c) Find the names of managers with at least one relative!
$$ \Pi_{\text{fname, lname}} (\sigma_{\text{count\_dependents} \ge 1} (\text{Employee} \Join_{\text{ssn}=\text{mgrssn}} \text{Department} \Join_{\text{ssn}=\text{essn}} (\mathcal{G}_{\text{essn}, \text{COUNT(dependent\_name) AS count\_dependents}} (\text{Dependent})))) $$

(d) Which employees work on more than two projects?
$$ \Pi_{\text{fname, lname}} (\sigma_{\text{count\_projects} > 2} (\text{Employee} \Join_{\text{ssn}=\text{essn}} (\mathcal{G}_{\text{essn}, \text{COUNT(DISTINCT pno) AS count\_projects}} (\text{Works\_on})))) $$

(e) Find for every department (DName), the projects (PName) they are not working on!
$$ \Pi_{\text{dname, pname}} (\text{Department} \times \text{Project}) - \Pi_{\text{dname, pname}} (\text{Department} \Join_{\text{dnumber}=\text{dnum}} \text{Project}) $$

## 3. Given following relational schema:

(a) Find all stations.
$$ \{ w \mid w \in \text{Station} \} $$

(b) Find the labels of all discounts and additions.
$$ \{ w.\text{Label} \mid w \in \text{Adds\_discount} \} $$

(c) Find all tickets that cost more than 100€.
$$ \{ w \mid w \in \text{Ticket} \land w.\text{Price} > 100 \} $$

(d) Find all departure times of all connections that go from Munich to Augsburg before noon (12 o'clock).
$$ \{ w.\text{Departure} \mid w \in \text{Connection} \land w.\text{starts\_at} = \text{'Munich'} \land w.\text{goes\_to} = \text{'Augsburg'} \land w.\text{Departure} < \text{'12:00'} \} $$

(e) Find all trains that have a connection from Munich to Augsburg.
$$ \{ t \mid t \in \text{Train} \land \exists c (c \in \text{Connection} \land c.\text{Train\_number} = t.\text{Train\_number} \land c.\text{starts\_at} = \text{'Munich'} \land c.\text{goes\_to} = \text{'Augsburg'}) \} $$

(f) Find all discounts and additions that do not depend on others and do not exclude others.
$$ \{ w \mid w \in \text{Adds\_discount} \land \neg \exists u (u \in \text{Adds\_discount} \land u.\text{Label} = w.\text{requires}) \land \neg \exists x (x \in \text{Excludes} \land x.\text{Excluder} = w.\text{Label}) \} $$

## 4. Formulate the queries from task 2 using the domain calculus.

(a) Find all employees with two or more relatives!
$$ \{ \text{F, M, L, S, B, A, X, Y, SS, DN} \mid \text{Employee}(\text{F, M, L, S, B, A, X, Y, SS, DN}) \land \text{COUNT}(\{ \text{DNAME, DX, DB, DR} \mid \text{Dependent}(\text{S, DNAME, DX, DB, DR}) \}) \ge 2 \} $$

(b) Find the names of all employees that have no relatives!
$$ \{ \text{F, L} \mid \exists \text{M, S, B, A, X, Y, SS, DN} (\text{Employee}(\text{F, M, L, S, B, A, X, Y, SS, DN})) \land \neg \exists \text{DNAME, DX, DB, DR} (\text{Dependent}(\text{S, DNAME, DX, DB, DR})) \} $$

(c) Find the names of managers with at least one relative!
$$ \{ \text{F, L} \mid \exists \text{M, S, B, A, X, Y, SS, DN, DNAME, DNUM, MS, MD} (\text{Employee}(\text{F, M, L, S, B, A, X, Y, SS, DN}) \land \text{Department}(\text{DNAME, DNUM, S, MD})) \land \text{COUNT}(\{ \text{DNAME_D, DX, DB, DR} \mid \text{Dependent}(\text{S, DNAME_D, DX, DB, DR}) \}) \ge 1 \} $$

(d) Which employees work on more than two projects?
$$ \{ \text{F, L} \mid \exists \text{M, S, B, A, X, Y, SS, DN} (\text{Employee}(\text{F, M, L, S, B, A, X, Y, SS, DN})) \land \text{COUNT}(\{ \text{PNO, H} \mid \text{Works\_on}(\text{S, PNO, H}) \}) > 2 \} $$

(e) Find for every department (DName), the projects (PName) they are not working on!
$$ \{ \text{DN, PN} \mid \exists \text{DNUM_D, M, MD} (\text{Department}(\text{DN, DNUM_D, M, MD})) \land \exists \text{PNUM_P, PLOC_P, DNUM_P} (\text{Project}(\text{PN, PNUM_P, PLOC_P, DNUM_P})) \land \neg (\exists \text{DNUM_MATCH} (\text{Department}(\text{DN, DNUM_MATCH, M, MD}) \land \text{Project}(\text{PN, PNUM_P, PLOC_P, DNUM_MATCH}))) \} $$

## 5. Basic Terms (Views, Transactions, Trigger):

**(a) What is a view? What are views used for?**
A view is a virtual table based on the result-set of a SQL query. [cite_start]It does not store data itself but rather presents data stored in base tables. [cite: 30]
Views are used for several purposes:
* [cite_start]**Security:** They can restrict access to specific rows or columns of a table, allowing users to see only the data they are authorized for. [cite: 30]
* [cite_start]**Simplification:** Complex queries can be saved as views, making it easier for users to interact with the database without needing to understand the underlying table structures or complex join operations. [cite: 30]
* [cite_start]**Consistency:** Views can present a consistent, simplified view of the database schema, even if the underlying base tables change. [cite: 30]

**(b) Reiterate the term transaction and explain the ACID-principle!**
[cite_start]A transaction is a sequence of operations performed as a single logical unit of work. [cite: 31] [cite_start]It is a set of commands that are executed on a database in an ordered or unordered manner. [cite: 31]
The ACID principle is a set of properties that guarantee that database transactions are processed reliably. ACID is an acronym for:
* **Atomicity:** This means that a transaction is treated as a single, indivisible unit of work. Either all of its operations are completed successfully, or none of them are. [cite_start]If any part of the transaction fails, the entire transaction is rolled back, leaving the database unchanged as if the transaction never occurred. [cite: 31]
* **Consistency:** A transaction brings the database from one valid state to another. [cite_start]It ensures that any data written to the database must be valid according to all defined rules, including constraints, cascades, and triggers. [cite: 31]
* **Isolation:** The execution of concurrent transactions should not interfere with each other. [cite_start]This means that multiple transactions can be processed, and the database would remain in a valid state throughout, as if each transaction were executed sequentially. [cite: 31]
* [cite_start]**Durability:** Once a transaction has been committed, its changes are permanent and will persist in the database, even in the event of a system failure (like a power outage or crash). [cite: 31]

**(c) What is a trigger? Name important use cases and problems with triggers!**
[cite_start]A trigger is a special type of stored procedure that is automatically executed (or "fired") by the database management system (DBMS) in response to certain events on a table or view. [cite: 32] [cite_start]These events are typically `INSERT`, `UPDATE`, or `DELETE` operations. [cite: 32]

**Important Use Cases for Triggers:**
* **Enforcing Complex Business Rules:** Triggers can enforce business rules that cannot be handled by standard constraints (like `CHECK` constraints or foreign keys). For example, automatically updating an `inventory_level` when an `order_item` is inserted.
* **Auditing and Logging:** Triggers can record changes to data, such as who changed what, when, and from what old value to what new value, for auditing purposes.
* **Maintaining Data Integrity:** Automatically updating related tables to maintain consistency. For example, ensuring that summary data in one table is updated when detailed data in another changes.
* **Preventing Invalid Operations:** Triggers can stop an operation if it violates a complex condition.

**Problems with Triggers:**
* **Complexity and Debugging:** Triggers can make the database schema and application logic more complex and harder to understand, maintain, and debug, as their execution is implicit and not directly called by the application.
* **Cascading Effects:** A trigger can cause another trigger to fire, leading to a chain of events that can be difficult to predict or control, potentially leading to performance issues or unintended data modifications.
* **Portability:** Trigger syntax and behavior can vary significantly between different DBMS products, making database migration more challenging.
* **Performance Overhead:** Triggers add overhead to DML operations (INSERT, UPDATE, DELETE) because the DBMS must execute the trigger code in addition to the actual data modification.
* **Hidden Logic:** Logic embedded in triggers is often not immediately visible to developers working on the application layer, which can lead to unexpected behavior and makes debugging harder.
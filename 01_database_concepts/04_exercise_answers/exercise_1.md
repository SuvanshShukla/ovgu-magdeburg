# Exercise 1

## 1. Explain the terms Database (DB), Database System (DBS) and Database Management System (DBMS)!

> Database: any structured representation of stored data is a database
> Database System: the entirety of the system with which the data is stored and managed  makes up the database system.
> Database management system: any system used to manage the data in a database is a database management system

## 2. What is meant with data integration and redundancy?

> Integration refers to how the data is kep together and not separately. Integration requires that all the relevant data be stored in a uniform manner at the same location.
> Redundancy refers to the existance of the same data existing at two different places, essentially duplicate data

## 3. Explain the term transaction! Give examples.

> The term "transaction" refers to any committed sequence of operations performed on stored data. For example, capitalizing all the names of in a table of student details.

## 4. Explain the terms synchronisation and persistence!

> Synchronisation refers to having the same state between two different entities by coordinating all the transactions performed on the data. Within the scope of database concepts it would mean having data parity between two database that are supposed to store & manage the same data.
> Persistance would mean that data isn't ealiy lost, corrupted or destroyed.

## 5. What data is stored within the data dictionary?

> The data dictionary typically contains "meta-data". That is, information about the data type, the constraint on the data type, the field name of the data and other such information.

## 6. For which of the following scenarios, the use of a DBMS is reasonable:
• The student Bruce Springsteen wants to manage his CD collection.
• For reporting reasons, the supermarket Walmort wants to store all buying
transactions of their customers.
• The student portal webunihelp.com shall be extended with a message
board.
• The examination office wants to manage grades electronically.

> All the scenarios except for managing the CD collection seem reasonable. It would be easier to manager a CD collection simply by organising them by date or album name. Using a DBMS for this would be overkill. It would be overkill because there would be no need of the following attributes of DBMS:
> - no need for scalability
> - no need for transactions
> - no need for different userviews
> - no need for recovery (under most circumstances)
> - no need for synchronisation


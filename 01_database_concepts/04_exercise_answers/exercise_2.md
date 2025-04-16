# Exercise 2

## 1. Name the nine rules of Codd! Give an example for each rule!

> 1. Integration: a crop of wheat, where all the plants are the same (wheat)
> 2. Operations: sowing seeds in a farm (insertion)
> 3. Catalog: nutritional information chart on food products
> 4. User views: chessboard, users sitting on both sides see the chess pieces from different perspectives but their coordinates represent the same locations regardless of side
> 5. Integrity: the age of a person (cannot be negative)
> 6. Security: passwords, codes and encryption keys
> 7. Transactions: bank transactions, 
> 8. Synchronisation: like keeping your watch's time up-to-date
> 9. Recovery: an example of recovery would be putting a vase back together by gluing all the broken pieces.

## 2. Explain the terms database model and database schema! How are these two terms related? What is the difference between a database schema and a database? Give examples.

> A database model is a way to represent structure in data that relates to the real world. A database schema defines the blueprint of what the database is made of, like what fields, their types etc.
> These terms are related in design 


## 3. Explain the 3-Level-Schema-Architecture!

> The 3-Level-Schema-Architecture consists of the following levels:
> 1. Conceptual Schema: This is the design level definition of the stored data.
> 2. Internal Schema: This is the way the data stored, either by access paths or file structure
> 3. External Schema: This is the way that the data is displayed/accessed by the end user. 

## 4. Explain the term data independence? What are the benefits of data independence? How does the 3-Level-Schema-Architecture provide data independence?

> Data independence is the separation of concerns of how the data is stored, how it is accessed and how it is viewed.
> The following are the benefits of data independence: 
> - change in location of storage doesn't affect data
> - change in data definition doesn't change what the end user views
> - change in viewership doesn't affect the data
> - change in the data (new data is added, or old data is removed) doesn't affect the database structure

## 5. What is DDL, DML, QL? For which database users (end user, application programmer, database admin) are they interesting?

> DDL: stands for data definition language. It is used to define the structure of the database (tables, schemas, columns, etc.)
> DML: stands for data manipulation language. It is used to modify the data in the database, primarily by CRUD operations, e.g. insert, update delete etc.
> QL: stands for query language. It is primarily used to define how & what data is to be fetched/viewed from the database
> An application programmer would be primarily interested in DML & QL. As they would write the queries to fetch the data required by their application.
> An end user would not be interested in any of the three.
> A database admin would primarily be concerned with the DDL, as they would have to create and define the database itself.

## 6. Which of the following systems is a database management system (DBMS)? Explain your decision!

• MySQL, Excel, LSF, IBM DB2, iTunes, Microsoft SQLServer

> MySQL: is a DBMS, as it satisfies the 9 rules of Codd.
> Excel: this is not a DBMS, it is an application. This is because excel files don't contain structure descriptions nor integrity descriptions. This means there is no inherent data integrity.
> LSF: this is not a DBMS. This is because the LFS never actually has access to the Disk on which the data stored.
> IBM DB2: this is a DBMS because it satisfies the 9 rules of Codd.
> iTunes: this is not a DBMS as itunes manages files and not raw data.
> Microsoft SQLServer: this is a DBMS as it satisfies the 9 rules of Codd.


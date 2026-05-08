# Advanced Database Models Exercise 3

Author: Suvansh Shukla
Immatriculation Number: 256245

## Question 1


### Q1 Part (a)

![ERD](./ERD-ADBM-Ex-3.png)

### Q2 Part (b)

Yes, I believe `subject` is redundant.

| Normal Form | Conforms | Reason |
| ----------- | -------- | ------ |
|    1NF      |  ✔       |        |
|    2NF      |  ❌      | Because in `subject` in `thread` table can be same for multiple `threadID` values, therefore not dependent on the PK |
|    3NF      |  ❌      | Because the schema is not in 2NF |

## Question 2


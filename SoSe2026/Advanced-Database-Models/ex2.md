
# Advanced Database Models Exercise 1

Author: Suvansh Shukla
Immatriculation Number: 256245

## Question 1

| SNo.| System | Conform | Reason |
| --- | ------ | ------- | ------ |
| 1   | Spreadsheet Applications (e.g. Microsoft Excel) | ❌ |  Spreadsheet Applications are not Databases, because they don't support transactions and don't guarantee integrity control|
| 1   | Network File Systems | ❌ | These also don't support transactions |
| 1   | MySQL | ✔ | Yes, because they support all 9 rules of Codd |
| 1   | IBM DB2 | ✔ | Yes, because they support all 9 rules of Codd |

## Question 2

### Advantages of logical data independence

- application is unaffected by changes to the schema
- adding new columns or tables doesn't break the system

### Advantages of physical data independence

- changing storage location doesn't break the system
- changing storage platform doesn't break the system
- distributing the data doesn't affect the system (too much)

## Question 3

```text
Student(matrNr, firstName, lastName, birthDate)
Lecture(id, title, lecturerName)
Attends(matrNr, id, semeseter, grade)
```

The following possible integrity constraints can be expressed for them:


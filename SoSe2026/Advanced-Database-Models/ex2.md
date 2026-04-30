
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

### Advantages of physical data independence

## Question 3

```text
Student(matrNr, firstName, lastName, birthDate)
Lecture(id, title, lecturerName)
Attends(matrNr, id, semeseter, grade)
```

The following possible integrity constraints can be expressed for them:


# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 4 Task 4.2

According to the task description our Decision tree should classify based on "Good", "Neutral", "Bad".  
They are evaluated on the following features/attributes:

- chores (All, Most, Few, None)
- noisy (1 to 10)
- mess (Yes or No)
- treament of others (Nice, Mean, No Interaction)

Other information about the childer is also given, like: name, birth date, supervisor, parental income.  
The task also tells us that the classification of the child mostly depends on their age, noisiness and treament of others.  
It is also mentioned that some supervisors grade children worse than others, meaning that there is some bias present.  

Setting up a table to reflect the data for a class of 5 students would look like the following:

| name  | birth date | supervisor   | parental income | chores     | noisiness | messiness | treatment of others | behavior |
| ----  | ---------- | ----------   | --------------- | ---------- | --------- | --------- | ------------------- | -------- |
| John  | 2012       | Mr. Adam     | 10,000          | All        | 5         | No        | Nice                | Good     |
| Alice | 2011       | Mrs. Merkel  | 12,000          | Most       | 3         | No        | Nice                | Good     |
| James | 2012       | Mrs. Merkel  | 11,000          | Few        | 7         | Yes       | No Interaction      | Bad      |
| Jack  | 2011       | Mr. Adam     | 16,000          | Few        | 2         | Yes       | Mean                | Bad      |
| Lily  | 2013       | Mr. Adam     | 10,000          | None       | 6         | No        | Nice                | Neutral  |

Now assuming that between Mr. Adam and Mrs. Merkel, Mr. Adam is a harsher judge of the children, i.e. he rates every child one  
level worse than their natural classification. For example If John would have been classified as Neutral, Mr. Adam would classify  
him as Bad instead.


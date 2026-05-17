# Advanced Database Models Exercise 4

Author: Suvansh Shukla
Immatriculation Number: 256245

## Question 1 Conceptual Design

### Q1 (a)

![ER diagram](./ER-ADBM-Ex-4.png)

### Q1 (b)

![ER Model with Object Oriented Extensions](./ERD-Ex-4-Q1-B.png)

### Q1 (c)

![UML diagram](./ADMB-EX-4-Q1-C-UML.png)

## Question 2 Conceptual Design to Logical Design

### Q2 (a)

```RM
artist(ID, name, influenced_by, influences)
singer(s_id, artist_id, sex)
song_writer(sw_id, artist_id, genre)
singer_song_writer(s_id, sw_id)
songs(id, title, duration, s_id, sw_id)
```

# Database Concepts Exercise 6

Create ER schemas for the following use cases. Provide key attributes for entities and
cardinalities for relationships. Avoid redundancies. Add missing information accor-
ding to the task.

## Question 1

Create an entity-relationship schema for following use case. Snowboarder have
a first and a last name and a birth day. Moreover, every snowboarder has a
unique ID. Additionally, the "Home-Mountain", the mountain the snowboarder
likes most, must be stored. Some snowboarders in the database are professionals
that have a license number. Additionally, their "best trick" and their current
world cup points are stored. Professionals are supported by sponsors with a
certain a amount of money that should be stored in the database. For every
sponsor, the name and the overall available budget must be stored. Sponsors
also host competitions. Thereby, every competition is hosted by exactly one
sponsor. Every competition can be uniquely identified by the name and the
year it took place. Moreover, the prize money of every competition should be
stored. Snowboarders attend competitions to qualify for other competitions and
we want to store at which competition the snowboarder qualified for which other
competition in the database.

![dbc-exercise-6-1.svg](./exercise6-images/dbc-exercise-6-1.svg)

## Question 2

In a database, information about lectures should be stored. Every lecture has
a unique number and a name. Every lecture is either for Bachelor or Master
students only. For Master lectures, the lecturers name should be stored. For
Bachelor lectures, the number of enrolled students should be stored. Prepare an
entity-relationship schema. Avoid redundancy!

![dbc-exercise-6-2.svg](./exercise6-images/dbc-exercise-6-2.svg)

## Question 3

Transfer the entity-relationship schemata from task 1 and task 2 into relational
schemata! For this, use the following notation: R1(a,b → R2,c) denoting a as
primary key and b as foreign key to R2 to define the resulting relational schema.

## Question 4

Design an ER schema for managing information about votes in the US House of
Representatives during the current biennial session of Congress. The database
must track each US state by name and includes the state's region. Each member
of Congress (exactly 435) has a name, the district to be represented, a start date,
and a party. Each member represents a state, and each state has between one
and 52 representatives. The database tracks each bill by name, date, outcome,
and the Congressmen who proposed it. The database further tracks how each
Congressman votes on each bill.

![dbc-exercise-6-4.svg](./exercise6-images/dbc-exercise-6-4.svg)

## Question 5

Transfer the ER-Schema from task 4 into relation schemata! For this, use the
following notation: R1(a,b → R2,c) denoting a as primary key and b as foreign
key to R2 to define the resulting relational schema.

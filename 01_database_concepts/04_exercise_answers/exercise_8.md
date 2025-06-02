# Database Concepts Exercise 8

## Question 1

Given relational schema R(ABCDE) with following functional dependencies:

AB-> CDE, B -> C, C -> D, E -> A

Determine all keys and generate the BCNF step by step.

Left: B 
Middle: A, E, C 
Right: D 

Elements on the Left must always be a part of the key (as they are not derived/determined by any other element)
Elements in the middle can be used for trying out various combinations
Elements on the right will never be a part of the key (as they are only derived and do not derive other elements themselves)

Testing different combinations:

1. B -> C,D 
2. BA -> C,D,E (this key can derive all the elements)
3. BE -> A,C,D (this key can derive all the elements)
4. BC -> D 
5. EC -> D,A 

Therefore, the only valid keys are: BA & BE
Notice how B is in both keys.

Normalizing all the way to BCNF:

1st Normal Form: AB -> C,D,E 
2nd Normal Form: AB -> DE | B -> C 
3rd Normal Form: AB -> D | B -> C | AB -> E 
BCNF Normal Form: AB -> D | B -> C | E -> A 

## Question 2



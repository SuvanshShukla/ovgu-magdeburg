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

Given the following two sets of functional dependencies:

- A ->  B, A ->  C, CD ->  E, B ->  D
- A ->  BC, AD ->  E, DB ->  B, A ->  D

Test systematicall, if both sets are equivalent, one set is a superset of the other,        
or none of the sets is semantically contained in the other!     

Let,
X = {A ->  B, A ->  C, CD ->  E, B ->  D}       
Y = {A ->  BC, AD ->  E, DB ->  B, A ->  D}         

Considering Y,      
Taking the FD: A -> B,C we decompose it into A -> B & A -> C. Both of these FDs are present in X.   
Considering the FD: AD -> E, from the previous decomposition we know that A -> C, so we can derive CD -> E which is also present in X.      
Considering the FD: A -> D, from the first decomposition we found that A -> B, so we can derive B -> D, which is also present in X.         
Finally, Considering the FD: DB -> B. No FD in X can determine DB -> B. Hence, X ⊂ Y.       

## Question 3

Given the following functional dependencies over relation R(A,B,C,D):

A ->  C, B ->  CD

Which of the following decompositions is lossless and/or dependency preserving?

- R1(A, B), R2(A, C, D)
- R1(A, C), R2(B, C, D)
- R1(A, B), R2(B, C, D)
- R1(A, B, C), R2(B, C, D)

R1(A, B), R2(A, C, D) -- is not lossless    
R1(A, C), R2(B, C, D) -- is lossless & dependency preserving    
R1(A, B), R2(B, C, D) -- is not lossless    
R1(A, B, C), R2(B, C, D) -- is lossless & dependency preserving     

## Question 4

A database designer decomposed relation R(ABCDE) into relations R1(ABC) and R2(CDE).    
State at least two functional dependencies in R so that the decomposition into R1 \& R2 is:

(a) neither lossless nor dependency preserving      
(b) lossless but not dependency preserving      
(c) not lossless but dependency preserving      
(d) lossless as well as dependency preserving       

For an FD/relation to be lossless, the following conditions must be met:        

- no information must be lost during decomposition
- the natural join of the relations should return the original relation 

For an FD/relation to be dependency preserving, the FDs of the original schema must still hold true for the decomposed schema       

So,     

(a) The FDs: `ABC -> D & C -> E` would make the decomposition neither lossless nor dependency preserving        
(b) The FDs: `AB -> C & AC -> DE` would make the decomposition lossless but not dependency preserving       
(c) The FDs: `ABC -> C & C -> DE` would make the decomposition dependency preserving but not lossless       
(d) The FDs: `AB -> C & C -> DE` would make the decomposition lossless as well as dependency preserving     

## Question 5

Given following relation:

| STUDENT | COURSE | INSTRUCTOR |
| ------- | ------ | ---------- |
| Mueller | C1     | Heinz      |
| Meier   | C1     | Heinz      |
| Meier   | C2     | Paul       |
| Schmidt | C1     | Peter      |

Decompose the data according to the three given possibilities and join them together afterwards.

(a) Teach1(STUDENT, INSTRUCTOR) Teach2(STUDENT,COURSE)      
(b) Teach1(COURSE, INSTRUCTOR) Teach2(COURSE, STUDENT)      
(c) Teach1(INSTRUCTOR, COURSE) Teach2(INSTRUCTOR, STUDENT)      

Decomposing data according to (a):

| STUDENT | INSTRUCTOR |  
| ------- | ---------- |
| Mueller | Heinz      |
| Meier   | Heinz      |
| Meier   | Paul       |
| Schmidt | Peter      |

| STUDENT | COURSE |
| ------- | ------ |
| Mueller | C1     |
| Meier   | C1     |
| Meier   | C2     |
| Schmidt | C1     |

Joining data according to (a):

| STUDENT | INSTRUCTOR | COURSE |
| ------- | ---------- | ------ |
| Mueller | Heinz      | C1     |
| Meier   | Heinz      | C1     |
| Meier   | Heinz      | C2     |
| Meier   | Paul       | C1     |
| Meier   | Paul       | C2     |
| Schmidt | Peter      | C1     |

Decomposing data according to (b):

| COURSE | INSTRUCTOR |     
| ------ | ---------- |     
| C1     | Heinz      |     
| C2     | Paul       |     
| C1     | Peter      |     

| COURSE | STUDENT |
| ------ | ------- |
| C1     | Mueller |
| C1     | Meier   |
| C2     | Meier   |
| C1     | Schmidt |

Joining data according to (b):

| COURSE | INSTRUCTOR | STUDENT |
| ------ | ---------- | ------- |
| C1     | Heinz      | Mueller |
| C2     | Heinz      | Meier   |
| C1     | Heinz      | Schmidt |
| C1     | Paul       | Meier   |
| C1     | Peter      | Mueller |
| C1     | Peter      | Meier   |
| C1     | Peter      | Schmidt |

Decomposing according to (c):

| INSTRUCTOR | COURSE |
| ---------- | ------ |
| Heinz      | C1     |
| Paul       | C2     |
| Peter      | C1     |

| INSTRUCTOR | STUDENT |  
| ---------- | ------- |
| Heinz      | Mueller |
| Heinz      | Meier   |
| Paul       | Meier   |
| Peter      | Schmidt |

Joining data according to (b):

| INSTRUCTOR | COURSE | STUDENT |
| ---------- | ------ | ------- |
| Heinz      | C1     | Mueller |
| Heinz      | C1     | Meier   |
| Paul       | C2     | Meier   |
| Peter      | c1     | Schmidt |


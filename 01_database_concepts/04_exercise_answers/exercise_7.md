# Database Concepts Exercise 7

## Question 1

Give a definition for the term Functional Dependencies and explain it with
a self-selected example (which was not mentioned in the lecture)! Define the
terms key and primary key in this context! Given now a set \Sigma  of functional
dependencies with
\Sigma  = \{ A1 \rightarrow  A2, \{ A2, A3\}  \rightarrow  A1\} 
over the relation R = \{ A1, A2, A3, A4\} , where dom(Ai) = Integer for 1 \leq  i \leq 
10.
Give at least one relation r over the scheme R which contradicts all depen-
dencies in \Sigma ! Explain your decision!

Functional dependencies are a type of relation where one attribute uniquely identifies another attribute uniquely.

A key is an attribute or set of attributes that can be used to uniquely identify rows or other attributes.

A primary key is any key which is chosen to uniquely identify rows in a table

An example of a relation `r` which contradicts all dependencies is:

```math
r = {A2, A3} -> A4
```

## Question 2

Find all keys for relation R(ABCDE). Following functional dependencies exist in relation R:

```math
A \rightarrow  B, BC \rightarrow  E, ED \rightarrow  A
```

Answer:

```math
ACD \rightarrow B,E \\
BCD \rightarrow E, A \\
ECD \rightarrow A, B \\
```

## Question 3

Given relation R(ABCDEF) and following functional dependencies:

```math
G = \{ A \rightarrow  BC, E \rightarrow  ABC, F \rightarrow  CD, CD \rightarrow  BEF \}
```

Determine all keys!

```math
F \rightarrow C,D,B,E,A \\

AB \rightarrow ❌ \\
AC \rightarrow ❌ \\
AD \rightarrow ❌ \\
AE \rightarrow ❌ \\
AF \rightarrow ✔  \\

BC \rightarrow ❌ \\
BD \rightarrow ❌ \\
BE \rightarrow ❌ \\
BF \rightarrow ✔  \\

CD \rightarrow ✔  \\
CE \rightarrow ❌ \\
CF \rightarrow ✔  \\

DE \rightarrow A,B,C,F \\
DF \rightarrow A,B,C,E \\

EF \rightarrow A,B,C,D \\
```

## Question 4

Given a relation about drinking suppliers:

| Company 	| Product      	| Export 	| Caffeine Content 	| Popularity 	|
|---------	|--------------	|--------	|------------------	|------------	|
| Meier   	| tea          	| yes    	| 16               	| high       	|
| Meier   	| coffee       	| yes    	| 8                	| low        	|
| Dept    	| {tea,coffee} 	| no     	| 17               	| high       	|
| HB      	| {tea,coffee} 	| no     	| 30               	| low        	|

Following functional dependencies exist:

```math
(Company, Product \rightarrow  Export, CaffeineContent, Popularity) ,
(Company \rightarrow  Export) , (CaffeineContent \rightarrow  Popularity) ,
(CaffeineContent \rightarrow  Company) .
```

Transfer the relation step-by-step into the Boyce-Codd-Normal Form (BCNF).
Present each intermediate result!

In 1st Normal Form 

| Company 	| Product 	| Export 	| Caffeine Content 	| Popularity 	|
|---------	|---------	|--------	|------------------	|------------	|
| Meier   	| tea     	| yes    	| 16               	| high       	|
| Meier   	| coffee  	| yes    	| 8                	| low        	|
| Dept    	| tea     	| no     	| 17               	| high       	|
| Dept    	| coffee  	| no     	| 17               	| high       	|
| HB      	| tea     	| no     	| 30               	| low        	|
| HB      	| coffee  	| no     	| 30               	| low        	|

In 2nd Normal Form 

| Company 	| Product 	| Export  |
|---------	|---------	|-------- |
| Meier   	| tea     	| yes     |
| Meier   	| coffee  	| yes     |
| Dept    	| tea     	| no      |
| Dept    	| coffee  	| no      |
| HB      	| tea     	| no      |
| HB      	| coffee  	| no      |

| Caffeine Content 	| Popularity  |
|------------------	|------------ |
| 16               	| high        |
| 8                	| low         |
| 17               	| high        |
| 30               	| low         |
   
| Caffeine Content 	| Company 	
|------------------	|---------	
| 16               	| Meier   	
| 8                	| Meier   	
| 17               	| Dept    	
| 30               	| HB      	

In 3rd Normal Form:

| Company 	| Export  | Product  |
|---------	|-------- |--------- |
| Meier   	| yes     | tea      |
| Meier   	| yes     | coffee   |
| Dept    	| no      | tea      |
| Dept    	| no      | coffee   |
| HB      	| no      | tea      |
| HB      	| no      | coffee   |

| Company 	| Export  |
|---------	|-------- |
| Meier   	| yes     |
| Dept    	| no      |
| HB      	| no      |

| Caffeine Content 	| Popularity  |
|------------------	|------------ |
| 16               	| high        |
| 8                	| low         |
| 17               	| high        |
| 30               	| low         |
   
| Caffeine Content 	| Company 	
|------------------	|---------	
| 16               	| Meier   	
| 8                	| Meier   	
| 17               	| Dept    	
| 30               	| HB      	

## Question 5

Given following relational schema:

```math
car\_sale(plate\_number, seller, sale\_date, commision, discount)
```

with following functional dependencies:

```math
sale\_date \rightarrow  discount \\
seller \rightarrow  commision \\
```

To which normal form does this relational schema apply? If necessary, transform the schema into 3. normal form. Is the schema minimal?

Is it in the 1st Normal Form: Yes, because each column in this table only contains atomic values.

Is it in the 2nd Normal Form: No, because `commision` can be uniquely determined just by `seller`. This violates the principles of 2nd normal form because there should be no partial dependency, i.e. each non-key attribute should be fully depenedent on the primary key

Is it in the 3rd Normal Form: No, because the table is not in 2nd Normal Form

2nd Normal Form:

```
car_sale1(plate_number, seller, sale_date, discount)
car_sale2(seller, commission)
```

3rd Normal Form:

```
car_sale1(plate_number, seller, sale_date)
car_sale2(seller, commision)
car_sale3(sale_date, discount)
```


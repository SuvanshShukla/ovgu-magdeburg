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
ACD \rightarrow B,E \newline
BCD \rightarrow E, A \newline
ECD \rightarrow A, B \newline
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
(Company, P roduct \rightarrow  Export, Caf f eineContent, P opularity) ,
(Company \rightarrow  Export) , (Caf f eineContent \rightarrow  P opularity) ,
(Caf f eineContent \rightarrow  Company) .
```

Transfer the relation step-by-step into the Boyce-Codd-Normal Form (BCNF).
Present each intermediate result!


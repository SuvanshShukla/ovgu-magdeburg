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

```
r = {A2, A3} -> A4
```

## Question 2

Find all keys for relation R(ABCDE). Following functional dependencies exist in relation R:

```latex
A \rightarrow  B, BC \rightarrow  E, ED \rightarrow  A
```

Answer:

```latex
ACD \rightarrow B,E 
BCD \rightarrow E, A
ECD \rightarrow A, B
```

## Question 3

Given relation R(ABCDEF) and following functional dependencies:

```latex
G = \{ A \rightarrow  BC, E \rightarrow  ABC, F \rightarrow  CD, CD \rightarrow  BEF \}
```

Determine all keys!

```latex


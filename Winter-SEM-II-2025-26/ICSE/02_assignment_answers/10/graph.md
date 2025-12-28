# ICSE Exercise 10 - Task 2 - Self Balancing Trees B-Trees

Authored by: Suvansh Shukla  
Matriculation Number: 256245

## Answer 1

A graph is a data structure defined by nodes and edges connecting two nodes. The edges may or may not have any directions.

## Answer 2

If the edges in a graph have a direction to them then the graph is said to be _directed_, if the edges don't have any direction then the graph is said to be _undirected_.

## Answer 3

The number of nodes in a graph is the number of vertices in a graph. Both terms represent the same thing.

## Answer 4

In the given graph the there is only one node with outgoing edges and that is `0`.

## Answer 5

This graph has `16` edges.

## Answer 6

This graph has only one _sink_: `7`.

## Answer 7

- There are **two** cycles of length `1`: `8`, `6`
- There are **Zero** cycles of length `2`.
- There are **Three** cycles of length `3`: 1->5->4->1, 5->4->1->5, 4->1->5->4
- There are **Four** cycles of length `4`: 1->2->3->4->1, 2->3->4->1->2, 3->4->1->2->3, 4->1->2->3->4

## Answer 8

The corresponding edge list for this graph is:

- [1, 5]
- [1, 2]
- [2, 3]
- [3, 4]
- [4, 1]
- [5, 4]
- [6, 6]
- [6, 5]
- [6, 7]
- [8, 8]
- [8, 5]
- [8, 7]
- [0, 5]
- [0, 6]
- [0, 7]
- [0, 8]

## Answer 9

The corresponding node list is: 0, 1, 2, 3, 4, 5, 6, 7, 8.

## Answer 10

The adjacency matrix is like this:

$$
A =
   \begin{pmatrix}
    0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
    0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 1
   \end{pmatrix}
$$

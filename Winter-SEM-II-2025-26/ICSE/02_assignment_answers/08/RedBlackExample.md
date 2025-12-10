# ICSE (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Exercise 8 - Red-Black Trees

### 1

A red-black tree is a type of binary tree data structure, where each node besides storing its data, a pointer to its
parent and pointers to its left & right children, also stores a color of the node. This color, as the name implies
may be red or black.

A red-black tree has the following properties[^1]:

1. Node Color: Each node is either red or black.
2. Root Property: The root of the tree is always black.
3. Red Property: Red nodes cannot have red children (no two consecutive red nodes on any path).
4. Black Property: Every path from a node to its descendant null nodes (leaves) has the same number of black nodes.
5. Leaf Property: All leaves (NIL nodes) are black.

### 2

Using Φ as NULL.

Inserting 6:

```text
   6B
  /  \
 Φ    Φ
```

Inserting 7:

   6B
  /  \
 Φ    7R
     /  \
    Φ    Φ

Inserting 3:

       6B
      /   \ 
    3R     7R
   /  \   /  \
  Φ    Φ  Φ    Φ

Inserting 4:

       6B
      /   \ 
    3R     7R
   /  \   /  \
  Φ   4R  Φ   Φ
     /  \
    Φ    Φ


---

[^1]: https://www.geeksforgeeks.org/dsa/introduction-to-red-black-tree/

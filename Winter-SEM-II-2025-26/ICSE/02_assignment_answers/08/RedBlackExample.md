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

### 2 & 3

Assuming that every leaf node has Black NULL nodes as children.

Inserting 6:

```text
   6B
```

Inserting 7:

```text
   6B
    \
    7R
```

Inserting 3:

```text
       6B
      /  \ 
     3R  7R
```

Inserting 4:

```text
       6B
      /  \ 
     3R   7R
      \
      4R
```

Now we see that there is a violation b/w 3R and its child 4R. (Red cannot have a Red parent).
Since the parent of 4, i.e. 3 has a Red sibling, we color 3 and 7 both to Black.

```text
       6B
      /  \ 
     3B  7B
      \   
      4R 
```

Inserting 2:

```text
       6B
      /  \ 
    3B    7B
   / \  
  2R 4R
```
 
Inserting 1:

```text
       6B
      /  \ 
    3B    7B
   / \  
  2R 4R
 /
1R 
```

Here we see that a Red leaf node cannot have a Red parent node, so we need to rebalance the tree.
We notice that 1's uncle 4 is Red, so we can just color it black and recolor the grandparent of 1
to Red as well.

```text
       6B
      /  \ 
    3R    7B
   / \  
  2B 4B
 /
1R 
```

This is what the final tree looks like.

### 4

Creating an AVL Tree.

Inserting 6:

```text
6
```

Inserting 7:

```text
6
 \
  7
```

Inserting 3:

```text
  6
 / \
3   7
```

Inserting 4:

```text
  6
 / \
3   7
 \
  4
```

Inserting 2:

```text
    6
   / \
  3   7
 / \
2   4
```

Inserting 1:

```text
      6
     / \
    3   7
   / \
  2   4
 /
1
```

Here we see that there is an imbalance, because the difference in height
between left and right hand-sides is 2. So we need to rebalance the tree.
To rebalance the tree we make 4 the root node and re-adjust the left and right sub-trees.

```text
      4
     / \
    3   6
   /     \
  2       7
 /
1
```

There are multiple differences here. We see that in the AVL tree, our root node is 4.
While in the Red-Black tree our root node is 6. There are no colors for any of the nodes
in the AVL tree, while colors are present for each node in the Red-Black tree.

### 5

A Red-Black tree can indeed be converted into a 2-3-4 tree. The following (sub)structures
are equivalent to each other:

A black node with two red children is equivalent to a 3 node with 4 children.
A red node with two black children is equivalent to a single node with two single node children

Conversion rules discussed in exercise class:

1. A black node with no red children will be a one node tree: 2
2. A black node with one red child will be three node tree like: 2|4
3. A black node with two red children will be a four node: 2|4|5
4. A red node with two black children will be included in the above three rules

> [!WARN]
> You will get a question for insertion and colouring

### 6

I will convert the following Red-Black tree into a 2-3-4 tree.

```text
       6B
      /  \ 
    3R    7B
   / \  
  2B 4B
 /
1R 
```

This is what the converted tree would look like:

```text
        6
       / \
  2|3|4   7
 /
1
```

---

[^1]: https://www.geeksforgeeks.org/dsa/introduction-to-red-black-tree/

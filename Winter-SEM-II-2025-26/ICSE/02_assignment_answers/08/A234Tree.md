# ICSE (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Exercise 8 - 2-3-4 Trees

### 1

A 2-3-4 Tree is a tree data structure where each node may have up to 2 or 3 or 4 ~~~data items in node of~~ children in the tree.  

The 2-3-4 tree is self-balancing tree under the broader categorization of B-trees.

Each child node of a 2-3-4 Tree may have 2 to 4 children. Another property of 2-3-4 trees is that all of their nodes
are always at the same level helping to ensure balance.

### 2

3,7,5,15,17,9,13,21,11,19

Inserting 3:

```text
3
```

Inserting 7:

```text
3 | 7
```

Inserting 5:

```text
3 | 5 | 7
```

We inserted 5 in the middle since it is greater than 3 but less than 7

Inserting 15, we see that there is no more space in the current node,
this means we need to split the node and bring elements upwards. We move 5
upwards into the upper level.

```text
  5
 / \
3  7|15
```

Inserting 17, we place it behind 15.

```text
  5
 / \
3  7|15|17
```

Inserting 9, we see that 9>5 but there is no more space in the 7/15/17 node,
so we move the middle element of the node upwards, i.e. 15 joins 5. This also means
that 7 will be in the middle of 5 & 15.

**You forgot to add 9 in the diagram!!!**

```text
  5|15
 / \  \
3  7  17
```

Inserting 13, we place it after 7.

```text
    5|15
   / \  \
  /   \  \
 /     \  \
3    7|13 17
```

Inserting 21, we place it after 17, because it is larger than 15 & 17.

```text
    5|15
   / \  \
  /   \  \
 /     \  \
3    7|13 17|21
```

Inserting 11, we place it between 7 & 13.

```text
      5|15
     / \   \
    /   \   \
   /     \   \
  /       \   \
 /         \   \
3      7|11|13  17|21
```

Inserting 19, we place it between 17 & 21.

```text
      5|15
     / \   \
    /  \    \
   /    \    \
  /      \    \
 /        \    \
3     7|11|13  17|19|21
```

### 2 PART 2 (same elements in different order)

Elements & order -> 3,5,7,9,11,13,15,17,19,21

Inserting 3, 5, 7:

```text
3|5|7
```

Inserting 9, we see that the node doesn't have any free space so we move the
middle element (here 5) upwards.

```text
  5
 / \
3  7|9
```

Inserting 11, we place it after 9.

```text
  5
 / \
3  7|9|11
```

Inserting 13, we try to place it in the 7/9/11 node but there is no space,
so we move 9 to the upper level and 7 is moved to a separate node, between 5 & 9.

```text
  5|9
 / | \
3  7 11|13
```

Inserting 15, we place it after 13.

```text
  5|9
 / | \
3  7 11|13|15
```

Inserting 17, we try to place it inside 11/13/15 node, but there is no space,
so we move 13 to the upper level and 11 get's its separate node, while 17 is 
added alongside 15.

```text
  5|9|13
 / | |  \
3  7 11 15|17
```

Inserting 19, we place it after 17

```text
  5|9|13
 / | |  \
3  7 11 15|17|19
```

Trying to insert 21 we see that the 15/17/19 node has no free space and we need to
move its middle element 17 to the upper level, but the upper level of 5/9/13 is also
full. This means that we need to completely readjust the tree.
    
```text
      9
    /  \
   /    \
  5      13|17
 / \    / |  \
3   7  11 15 19|21
```

This is the final tree. We note that this has a height of 3, while the previous tree
had a height of 2.

### 3

The bottom-up approach requires us to move the middle element upwards to a higher level 
in the tree, meanwhile the top-down approach has the elements try to insert into the current
level and if space is not available then move all the other elements down to a separate level.

I used bottom-up approach in creating the tree and I don't believe there would be any difference
in the resulting tree regardless of which approach was used.

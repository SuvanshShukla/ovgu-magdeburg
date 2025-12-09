# ICSE (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Exercise 8 - AVL Trees

### 1

An AVL (Adelson-Velsky and Landis) Tree is a type of self-balancing binary search tree data structure. 
In this type of tree the height of both the right and left sides of the tree can differ by at most 1.
If the heights of the right and left sides differ by more than one, then the tree must be rebalanced.

It is necessary to balance the trees to be able to properly leverage their fast search, insertion, deletion
times, i.e. $O(log n)$

### 2

We would start out with 14 and insert it into the tree.
Then we would put 17 as the right child of 14 (because it is greater than 14).
Next we see that 19 is greater than 14 to so go to its right sub-tree. Here we see that 19 is also greater than 17.
This means that 19 is placed as a right child of 17. But now we see that the height of the right hand-side of the tree
is greater than the left hand-side by 2. This means we need to rebalance the tree. To do this we rotate the tree
anti-clockwise once. This means that 17 becomes the root node with 14 as it's left child and 19 as its right child.
Now we get 7, seeing that it is less than 19 we go to the left child. Again we see that 7 is less than 14, so it
becomes the left child of 14.

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

### 2 & 3

We would start out with 14 and insert it into the tree. Then we would put 17 as the right child of 14 (because it is greater than 14).

```text
  14
   \
    17
```

Next we see that 19 is greater than 14 to so go to its right sub-tree. Here we see that 19 is also greater than 17.
This means that 19 is placed as a right child of 17. But now we see that the height of the right hand-side of the tree

```text
  14
    \
     17
      \
       19
```

Is greater than the left hand-side by 2. This means we need to rebalance the tree. To do this we rotate the tree
anti-clockwise once. This means that 17 becomes the root node with 14 as it's left child and 19 as its right child.

```text
    17
   /  \
  14  19 
```

Now we get 7, seeing that it is less than 19 we go to the left child. Again we see that 7 is less than 14, so it
becomes the left child of 14. At this stage, the left hand-side of the tree has a height of 2 while the right hand-side
of the tree has a height of 1, the difference is 1.

```text
    17
   /  \
  14  19 
  /
 7
```

Now we get 5, which is less than 17, 14 & 7. Meaning we make it the
child of 7. Now our left hand-side has a height of 3, while our right hand-side has a height of 1, the difference has
now increased to 2, so we need to rebalance the tree. 

```text
      17
     /  \
    14  19 
   /
  7
 /
5
```

To rebalance the tree we need to perform a clockwise rotation of
the 14-7-5 sub-tree. Therefore, the tree now looks like this:

```text
      17
     /  \
    7    19
   / \
  5  14
```

After this we get element 10, which is inserted as the left child of element 14. This again brings the height imbalance
to 2, meaning we need to rebalance the tree. 

```text
      17
     /  \
    7    19
   / \
  5  14
     / 
    10 
```

To rebalance the tree we would need to promote 14 to the root of the tree, place 17 as its right child with 19 on the
right of 17. Then on the left hand-side we would keep 10 as the left child of 14 with 5 as its left child and 7 as the
right child of 5. This would bring the height difference back to 1.

```text
      14
     /  \
    10  17
    /     \
   5      19 
    \
     7
```

Finally we get 18 as an element. Since 18 is larger than 14 & 17 but less than 19 we place it on the left of 19.

```text
      14
     /  \
    10  17
    /     \
   5      19 
    \    / 
     7  18
```

Since the tree is balanced, i.e. the height difference on the left and right hand-side is 0, we simply stop here.


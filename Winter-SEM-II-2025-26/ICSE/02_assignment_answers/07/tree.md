# Tree Theory

## What is a tree?

A tree is an abstract data structure which stores data in the form of nodes and connects them using edges. A tree usually has one root node, which has edges leading to children nodes. These children nodes, may be parents themselves meaning they may have their own children as well.

## Leaf node

A leaf node is a node at any level of the tree that doesn't have any children nodes.

## Root node

A root node is the primary entry point of the entire tree structure and is the first node to be accessed when trying to perform any operation on the tree.

## Height

As a tree grows it collects nodes, each of these set of nodes that are an equal number of edges away from the root node thus giving the tree "height". The height of a tree can also be thought of as the maximum distance of a leaf node from the root node. 

## Path

A path in a tree is any sequence of nodes that are traversed to go from one node to another.

## Applications of trees

Used in parsers, compilers and interpreters. May also be used in file systems or to represent company hierarchies.

## Binary trees

Binary trees are a special type of ordered tree where every node can have a maximum of 2 children and a minimum of no children. Each child is labelled as either left child or right child and left children precede right children.

## Search trees

A search tree is any tree that supports efficient search by keeping keys in an order that guides traversal. Note that search trees don't necessarily have to be binary, e.g. 2/3/4 search trees.

## Balanced Search tree

A balanced search tree is a tree that has bound on the difference between the heights of its left and right hand sides. Note that the heights of the left and right hand sides do not have to be exactly equal.

## Traversal

1. Preorder: 11, 5, 3, 9, 6, 10, 15, 13, 12, 14
2. Inorder: 3, 5, 6, 9, 10, 11, 12, 13, 14, 15
3. Postorder: 3, 6, 10, 9, 5, 12, 14, 13, 15, 11
4. Levelorder: 11, 5, 15, 3, 9, 13, 6, 10, 12, 14

## Insertion

```text
           11
         /    \ 
        /      \
       /        \
      /          \
     5             15
   /   \         /    \
  3     9      13      19
 / \   / \     / \     /
1   4 6  10   /   \   16
            12    14
```


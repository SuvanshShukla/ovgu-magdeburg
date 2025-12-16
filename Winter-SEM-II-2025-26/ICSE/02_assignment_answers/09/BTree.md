# ICSE Exercise 9 - Task 4 - Self Balancing Trees B-Trees

Authored by: Suvansh Shukla  
Matriculation Number: 256245

## Answer 1

A B-Tree is a specialized m-way tree designed to optimize data access, especially on disk-based storage systems.

In a B-Tree of order m, each node can have up to `m` children and `m-1` keys,  allowing it to efficiently manage large datasets. the value of `m` is decided based on disk block and key sizes.

## Answer 2

### Inserting with `m=2`

We know that the Minimum no. of keys = $m-1 = 2-1 = 1$
and the Maximum no. of keys = $2(m) - 1 = 2(3) - 1 = 6 - 1 = 5$
Maximum no. of children = $2(m) = 2(2) = 4$

Inserting 3, 7, 5:

```text
3|7|5
```

Inserting 15 requires us to adjust levels:

```text
      7
     / \
  3|5   15
```

Inserting 17:

```text
      7
     / \
  3|5   15|17
```

Inserting 9:

```text
      7
     / \
  3|5   9|15|17
```

Inserting 13, requires adjustment of levels again:

```text
      7|15
     / \  \
    /   \  \
  3|5  9|13 17
```

Inserting 21:

```text
      7|15
     / \  \
    /   \  \
  3|5  9|13 17|21
```

Inserting 11:

```text
      7|15
     / \   \
    /   \   \
   /     \   \
  /       \   \
 3|5   9|11|13 17|21
```

Inserting 19:

```text
      7|15
     / \   \
    /   \   \
   /     \   \
  /       \   \
 3|5   9|11|13 17|19|21
```

Inserting 23 requires adjustment:

```text
      7|15|19
     / \   \  \
    /   \   \  \
   /     \   \  \
  /       \   \  \
 3|5   9|11|13 17 21|23
```

### 3 Inserting same values in different order

Inserting 3, 5, 7:

```text
3|5|7
```

Inserting 9:

```text
   5
 /   \
3    7|9
```

Inserting 11:

```text
   5
 /   \
3    7|9|11
```

Inserting 13, requires adjustment:

```text
   5|9
 /  |  \
3   7   11|13

Inserting 15:

```text
   5|9
 /  |  \
3   7   11|13|15
```

Inserting 17 requires adjustment:

```text
   5|9|13
 /  |  |  \
3   7  11  15|17
```

Inserting 19:

```text
   5|9|13
 /  |  |  \
3   7  11  15|17|19
```

Inserting 21 requires adjustment at two levels:

```text
     9
    /  \
   5    13|17
 /  |  |  |  \
3   7  11 15  19|21
```

### Differences

The main differences here is that the change in order in the second sub-task required a lot more adjustment and sending elements to upper or lower levels. This was far more computationally intensive and required most of the work to be on the right-most sub-tree.

## Answer 3

A B-Tree has an advantage over other balanced trees in the following scenarios:

- When data is not stored in memory only
- they have high-concurrency and high-throughput
- when efficient utilization of storage is required

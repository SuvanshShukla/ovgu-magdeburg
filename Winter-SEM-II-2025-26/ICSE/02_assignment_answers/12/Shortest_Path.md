# ICSE (WiSe 25/26)

Author: Suvansh Shukla  
Matriculation No. 256245

---

Shortest Path Tree:

Our starting node is a.

From a we can go to either b for 4 or h for 8.

We go to b for 4. From here we can go to h for  15 (4 + 11) or c for 12 (4 + 8).

We go to c for a total of 12. Now from h we can go to either g (9) or i (15).

While from c we can go to i (14) or d (19) or f (16). Since h -> g is smallest (9) we go to g.

Thus far our edges look like:

```text
a -- b -- c
|
h -- g
```

From g we can go to i (14) or f (11). Since g -> f is smallest we go to f (11). Adding this to our Shortest Path Tree:

```text
a -- b -- c
|
h -- g -- f
```

From f we can go to e (21) or d (25). But both of these are too large so instead we have another look from node c.

From c we can go to i (14) or d (19). Since the distance to i is smallest we go to i, and add it to our Shortest Path Tree:

```text
a -- b -- c -- i
|
h -- g -- f
```

Now that the only unseen nodes are d and e, we must choose to travel to them.

Distance of f to d is 25, while f to e is 21, and distance of c to d is 19, so we go to d. Adding this edge to the Shortest Path Tree:

```text
          d
          |
a -- b -- c -- i
|
h -- g -- f
```

Finally, the shortest distance to e is from f (21) rather than from d (28), so we add f -> e to our Shortest Path Tree:

```text
          d
          |
a -- b -- c -- i
|
h -- g -- f -- e
```

Thus the ☝ is our Shortest Path Tree. With the total weight of its edge being:

- a -> h = 8
- a -> b = 4
- h -> g = 1
- b -> c = 8
- g -> f = 2
- f -> e = 10
- c -> d = 7
- c -> i = 2

Total = 8 + 4 + 1 + 8 + 2 + 10 + 7 + 2 = 42

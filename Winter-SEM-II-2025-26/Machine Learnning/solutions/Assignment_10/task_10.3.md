# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 10 Task 3

### Part A

#### Iteration 1

Centroids: $C_1(1,0)$ and $C_2(5,6)$
Points: $A(1, 2), B(3, 2), C(5, 2), D(1, 1) and E(5, 1)$

Distance of $C_1$ to A, B, C, D & E:

$$D(C_1, A) = \sqrt{(1 - 1)^2 + (2 - 0)^2} = 2.0000$$
$$D(C_1, B) = \sqrt{(3 - 1)^2 + (2 - 0)^2} = 2.8284$$
$$D(C_1, C) = \sqrt{(5 - 1)^2 + (2 - 0)^2} = 4.4721$$
$$D(C_1, D) = \sqrt{(1 - 1)^2 + (1 - 0)^2} = 1.0000$$
$$D(C_1, E) = \sqrt{(5 - 1)^2 + (1 - 0)^2} = 4.1231$$

Distance of $C_2$ to A, B, C, D & E:

$$D(C_1, A) = \sqrt{(1 - 5)^2 + (2 - 6)^2} = 5.6569$$
$$D(C_1, B) = \sqrt{(3 - 5)^2 + (2 - 6)^2} = 4.4721$$
$$D(C_1, C) = \sqrt{(5 - 5)^2 + (2 - 6)^2} = 4.0000$$
$$D(C_1, D) = \sqrt{(1 - 5)^2 + (1 - 6)^2} = 6.4031$$
$$D(C_1, E) = \sqrt{(5 - 5)^2 + (1 - 6)^2} = 5.0000$$

Now we assign the points to their clusters:

- Cluster 1: A, B, D, E
- Cluster 2: C

Now we create new centroids:

$C'_1 (x, y) = \frac{(1,2) + (3,2) + (1,1) + (5,1)}{4} = \frac{(9,6)}{4} = (2.25,1.5)$
$C'_2 (x,y) = \frac{(5,2)}{1} = (5,2)$

#### Iteration 2

Distance of $C'_1$ to A, B, C, D & E:

$$D(C_1, A) = \sqrt{(1 - 2.25)^2 + (2 - 1.5)^2} = 1.3463$$
$$D(C_1, B) = \sqrt{(3 - 2.25)^2 + (2 - 1.5)^2} = 0.9014$$
$$D(C_1, C) = \sqrt{(5 - 2.25)^2 + (2 - 1.5)^2} = 2.7951$$
$$D(C_1, D) = \sqrt{(1 - 2.25)^2 + (1 - 1.5)^2} = 1.3463$$
$$D(C_1, E) = \sqrt{(5 - 2.25)^2 + (1 - 1.5)^2} = 2.7951$$

Distance of $C'_2$ to A, B, C, D & E:

$$D(C_1, A) = \sqrt{(1 - 5)^2 + (2 - 2)^2} = 4.0000$$
$$D(C_1, B) = \sqrt{(3 - 5)^2 + (2 - 2)^2} = 2.0000$$
$$D(C_1, C) = \sqrt{(5 - 5)^2 + (2 - 2)^2} = 0.0000$$
$$D(C_1, D) = \sqrt{(1 - 5)^2 + (1 - 2)^2} = 4.1231$$
$$D(C_1, E) = \sqrt{(5 - 5)^2 + (1 - 2)^2} = 1.0000$$

Assigning points to clusters:

- Cluster 1: A, B, D
- Cluster 2: C, E

Now we create new centroids:

$C''_1 (x, y) = \frac{(1,2) + (3,2) + (1,1)}{3} = \frac{(4, 5)}{3} = (1.3333, 1.6666)$
$C''_2 (x, y) = \frac{(5,2) + (5,1)}{2} = \frac{(10,3)}{2} = (5, 1.5)$

#### Iteration 3

Distance of $C''_1$ to A, B, C, D & E:

$$D(C_1, A) = \sqrt{(1 - 1.3333)^2 + (2 - 1.6666)^2} = 0.4714$$
$$D(C_1, B) = \sqrt{(3 - 1.3333)^2 + (2 - 1.6666)^2} = 1.6997$$
$$D(C_1, C) = \sqrt{(5 - 1.3333)^2 + (2 - 1.6666)^2} = 3.6818$$
$$D(C_1, D) = \sqrt{(1 - 1.3333)^2 + (1 - 1.6666)^2} = 0.7453$$
$$D(C_1, E) = \sqrt{(5 - 1.3333)^2 + (1 - 1.6666)^2} = 3.7268$$

Distance of $C''_2$ to A, B, C, D & E:
$$D(C_1, A) = \sqrt{(1 - 5)^2 + (2 - 1.5)^2} = 4.0311$$
$$D(C_1, B) = \sqrt{(3 - 5)^2 + (2 - 1.5)^2} = 2.0616$$
$$D(C_1, C) = \sqrt{(5 - 5)^2 + (2 - 1.5)^2} = 0.5000$$
$$D(C_1, D) = \sqrt{(1 - 5)^2 + (1 - 1.5)^2} = 4.0311$$
$$D(C_1, E) = \sqrt{(5 - 5)^2 + (1 - 1.5)^2} = 0.5000$$

Assigning points to clusters:

- Cluster 1: A, B, D
- Cluster 2: C, E

Now we create new centroids:

$C'''_1 (x, y) = \frac{(1,2) + (3,2) + (1,1)}{3} = \frac{(4, 5)}{3} = (1.3333, 1.6666)$
$C'''_2 (x, y) = \frac{(5,2) + (5,1)}{2} = \frac{(10,3)}{2} = (5, 1.5)$

At this point we see that the points making up the clusters didn't move and neither did the centroids.

This means that the clusters are final and the points are correctly assigned.

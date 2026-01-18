# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 11 Task 2

Given:

- 5 Points: A(1, 2), B(3, 2), C(5, 2), D(1, 1) and E(5, 1)
- 2 Centroids: C1(1,0) and C2(5,6)
- Assuming A, B, C are Class 1 and D, E are Class 2

Procedure:

1. We calculate the euclidean distance of each points to each centroid
2. We then see which points are closest to which centroid, based on these distances
3. Then we see if the point assigned to the cluster has the same or different class
4. If both the point and the centroid have the same class we apply the Attraction or if they are different we apply Replusion
5. This Attraction or Replusion determines what the final sign (+ve or -ve) that the points will have
6. Then we apply the batch learning equation for LVQ to get the new centroid
7. We repeat this until convergence

### Part A ($\eta = 0.2$) & 2 iterations

This is the equation for learning vector quantization:

$$
\vec{r}^{(new)} = \vec{r}^{(old)} + \eta \sum_{winner(\vec{p})=\vec{r}^{(old)}} (\vec{p} - \vec{r}^{(old)})
$$

#### First Iteration

Distances of all points to first centroid:

$$D(C_1, A) = \sqrt{(1 - 1)^2 + (2 - 0)^2} = 2.0000$$
$$D(C_1, B) = \sqrt{(3 - 1)^2 + (2 - 0)^2} = 2.8284$$
$$D(C_1, C) = \sqrt{(5 - 1)^2 + (2 - 0)^2} = 4.4721$$
$$D(C_1, D) = \sqrt{(1 - 1)^2 + (1 - 0)^2} = 1.0000$$
$$D(C_1, E) = \sqrt{(5 - 1)^2 + (1 - 0)^2} = 4.1231$$

Distances of all points to second centroid:

$$D(C_1, A) = \sqrt{(1 - 5)^2 + (2 - 6)^2} = 5.6569$$
$$D(C_1, B) = \sqrt{(3 - 5)^2 + (2 - 6)^2} = 4.4721$$
$$D(C_1, C) = \sqrt{(5 - 5)^2 + (2 - 6)^2} = 4.0000$$
$$D(C_1, D) = \sqrt{(1 - 5)^2 + (1 - 6)^2} = 6.4031$$
$$D(C_1, E) = \sqrt{(5 - 5)^2 + (1 - 6)^2} = 5.0000$$

Assigning points to clusters:

Cluster 1: A, B, D, E

Cluster 2: C

Comparing classes of centroid and points:

- A (Class 1) vs Centroid 1 (Class 1): +ve
- B (Class 1) vs Centroid 1 (Class 1): +ve
- C (Class 1) vs Centroid 2 (Class 2): -ve
- D (Class 2) vs Centroid 1 (Class 1): -ve
- E (Class 2) vs Centroid 1 (Class 1): -ve

Calculating new vectors using these signs:

- $v_A$ = +((1,2) - (1,0)) = +(0,2)
- $v_B$ = +((3,2) - (1,0)) = +(2,2)
- $v_C$ = +((5,2) - (5,6)) = -(0,4)
- $v_D$ = -((1,1) - (1,0)) = -(0,1)
- $v_E$ = -((5,1) - (1,0)) = -(4,0)

Performing batch update to get new Centroids:

$C'_1 = (1,0) + 0.2 * ((0,2) + (2,2) - (0,1) - (4,0))$
$C'_1 = (1,0) + 0.2 * (0+2-0-4, 2+2-2-0)$
$C'_1 = (1,0) + 0.2 * (-2,2)$
$C'_1 = (1,0) + (-0.4, 0.4)$
$C'_1 = (0.6, 0.4)$

$C'_2 = (5,6) + 0.2 * (-(0,4))$
$C'_2 = (5,6) + (0, -0.8)$
$C'_2 = (5,5.2)$

#### Second Iteration
Distances to 1st centroid:

$$D(C_1, A) = \sqrt{(1 - 0.6)^2 + (2 - 0.4)^2} = 1.6492$$
$$D(C_1, B) = \sqrt{(3 - 0.6)^2 + (2 - 0.4)^2} = 2.8844$$
$$D(C_1, C) = \sqrt{(5 - 0.6)^2 + (2 - 0.4)^2} = 4.6819$$
$$D(C_1, D) = \sqrt{(1 - 0.6)^2 + (1 - 0.4)^2} = 0.7211$$
$$D(C_1, E) = \sqrt{(5 - 0.6)^2 + (1 - 0.4)^2} = 4.4407$$

Distance to 2nd Centroid:

$$D(C_1, A) = \sqrt{(1 - 5)^2 + (2 - 5.2)^2} = 5.1225$$
$$D(C_1, B) = \sqrt{(3 - 5)^2 + (2 - 5.2)^2} = 3.7736$$
$$D(C_1, C) = \sqrt{(5 - 5)^2 + (2 - 5.2)^2} = 3.2000$$
$$D(C_1, D) = \sqrt{(1 - 5)^2 + (1 - 5.2)^2} = 5.8000$$
$$D(C_1, E) = \sqrt{(5 - 5)^2 + (1 - 5.2)^2} = 4.2000$$


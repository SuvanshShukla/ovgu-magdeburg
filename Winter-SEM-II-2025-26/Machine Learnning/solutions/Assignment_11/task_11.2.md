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

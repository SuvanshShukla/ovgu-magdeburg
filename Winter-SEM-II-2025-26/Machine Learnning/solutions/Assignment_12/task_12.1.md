# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 12 Task 1

### Part A

We evaluate cluster in two major ways. Internal and External evaluation methods. Internal evaluation methods use the inherent properties of data to determine quality of a cluster, e.g. compactness and separation. Meanwhile, External cluster evaluation methods compare clustering results to known class labels or external benchmarks.

External cluster evaluation methods are used when priori information about the dataset is know, whereas Internal evaluation methods don't require such priori information. Most real world problems do not have priori information in the dataset, hence they use Internal evaluation methods.

### Part B

Given:
A(1, 2), B(2, 1), C(3, 4), D(4, 1), E(4, 4) F(5, 3)
(1, 2), (2, 1), (3, 4), (4, 1), (4, 4) (5, 3)

First we calculate the cluster centers for both clusters in Clustering A.

$$
C_i = \frac{\sum_{i=1}^{N} (x_i,y_i)}{N}
$$

Centroid for class a cluster: (1.50, 1.50)
Centroid for class b cluster: (4.00, 3.00)

Now we calculate the distance of each point to their cluster centers:


# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 11 Task 1

Given:
- 5 Points: A(1, 2), B(3, 2), C(5, 2), D(1, 1) and E(5, 1)
- 2 Centroids: C1(2.75, 3) and C2(3.25, 0)
- m=2

Procedure:

1. calculate distance of all points from each centroid
2. calculate membership degrees/matrix ($u_{\alpha i}$)
3. re-calculate Centroids & re-calculate membership degrees/matrix
4. repeat until convergence (i.e. points don't change clusters anymore)

### Iteration 1

Calculation of membership matrix $u_{\alpha i}$ requires A distance:

$$
d_{i \alpha}^2 = ||x_i - v_{\alpha}||^2 = \sum_{j=1}^k (x_{ij} - v_{\alpha_j})
$$

$$D(C_1, A) = \sqrt{(1 - 2.75)^2 + (2 - 3)^2} = 2.0156$$
$$D(C_1, B) = \sqrt{(3 - 2.75)^2 + (2 - 3)^2} = 1.0308$$
$$D(C_1, C) = \sqrt{(5 - 2.75)^2 + (2 - 3)^2} = 2.4622$$
$$D(C_1, D) = \sqrt{(1 - 2.75)^2 + (1 - 3)^2} = 2.6575$$
$$D(C_1, E) = \sqrt{(5 - 2.75)^2 + (1 - 3)^2} = 3.0104$$

$$D(C_1, A) = \sqrt{(1 - 3.25)^2 + (2 - 0)^2} = 3.0104$$
$$D(C_1, B) = \sqrt{(3 - 3.25)^2 + (2 - 0)^2} = 2.0156$$
$$D(C_1, C) = \sqrt{(5 - 3.25)^2 + (2 - 0)^2} = 2.6575$$
$$D(C_1, D) = \sqrt{(1 - 3.25)^2 + (1 - 0)^2} = 2.4622$$
$$D(C_1, E) = \sqrt{(5 - 3.25)^2 + (1 - 0)^2} = 2.0156$$

$$
u_{\alpha 1} = \frac{1}{\sum_{\beta=1}^c \big(\frac{d_{i \alpha}^2}{d_{i \beta}^2} \big)^\frac{1}{(m-1)}} \\
$$
$$
u_{\alpha 1} = \frac{1}{1+ \big(\frac{2.0156^2}{3.0104^2} \big)^\frac{1}{(2-1)}} \\
$$
$$
u_{\alpha 1} = \frac{1}{1+ \big( 0.4482 \big)^1}
$$
$$
u_{\alpha 1} = \frac{1}{1.4482} = 0.6904
$$

  Similarly, calculating the $u_{\alpha i}$ and $u_{\beta i}$ for all instances would be:

$u_{\alpha 1} = 0.6904$
$u_{\alpha 2} = 0.79268$
$u_{\alpha 3} = 0.537998$
$u_{\alpha 4} = 0.461909$
$u_{\alpha 5} = 0.309531$

$u_{\beta 1} = 0.309588$
$u_{\beta 2} = 0.207417$
$u_{\beta 3} = 0.461909$
$u_{\beta 4} = 0.538091$
$u_{\beta 5} = 0.690469$

Thus creating the following membership matrix:

$$
U =
   \begin{pmatrix}
    0.6904 & 0.79268 & 0.537998 & 0.461909 & 0.309531 \\
    0.309588 & 0.207417 & 0.461909 & 0.538091 & 0.690469 \
   \end{pmatrix}
$$

calculating new centroids:

$$
v_\alpha = \frac{\sum_{i=1}^{N} u_{\alpha i}^m . x_i}{\sum_{i=1}^{N} u_{\alpha i}^m}
$$
$$
v_\beta = \frac{\sum_{i=1}^{N} u_{\beta i}^m . x_i}{\sum_{i=1}^{N} u_{\beta i}^m}
$$

Cluster Alpha $v_\alpha$ (x, y): (2.6422, 1.8185)
Cluster Beta  $v_\beta$ (x, y): (3.5449, 1.3149)

Calculating the value of the target function:

$$
J_m (U,V) = \sum\limits_{i=1}^{N} \sum\limits_{\alpha=1}^{c} u_{\alpha i}^m d_{i \alpha}^2 = \sum\limits_{i=1}^{N} \sum\limits_{\alpha=1}^{c} u_{\alpha i}^m || x_i - v_\alpha ||^2
$$

Contribution of Cluster 0 to J: 4.3360
Contribution of Cluster 1 to J: 4.2112

TOTAL OBJECTIVE FUNCTION (J): 8.547259

>![NOTE]
> We are supposed to keep iterating until the objective function J becomes stables (or doesn't show any significant reduction)

### Iteration 2

Calculating all new distances:


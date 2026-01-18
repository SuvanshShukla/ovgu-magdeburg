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

$$D(v_\alpha, A) = \sqrt{(1 - 2.6422)^2 + (2 - 1.8185)^2} = 1.6522$$
$$D(v_\alpha, B) = \sqrt{(3 - 2.6422)^2 + (2 - 1.8185)^2} = 0.4012$$
$$D(v_\alpha, C) = \sqrt{(5 - 2.6422)^2 + (2 - 1.8185)^2} = 2.3648$$
$$D(v_\alpha, D) = \sqrt{(1 - 2.6422)^2 + (1 - 1.8185)^2} = 1.8349$$
$$D(v_\alpha, E) = \sqrt{(5 - 2.6422)^2 + (1 - 1.8185)^2} = 2.4958$$

$$D(v_\beta, A) = \sqrt{(1 - 3.5449)^2 + (2 - 1.3149)^2} = 2.6355$$
$$D(v_\beta, B) = \sqrt{(3 - 3.5449)^2 + (2 - 1.3149)^2} = 0.8754$$
$$D(v_\beta, C) = \sqrt{(5 - 3.5449)^2 + (2 - 1.3149)^2} = 1.6083$$
$$D(v_\beta, D) = \sqrt{(1 - 3.5449)^2 + (1 - 1.3149)^2} = 2.5643$$
$$D(v_\beta, E) = \sqrt{(5 - 3.5449)^2 + (1 - 1.3149)^2} = 1.4888$$

Calculating membership degrees:

u_Alpha: (0.717872, 0.826417, 0.316256, 0.661367, 0.262449)
u_Beta: (0.282128, 0.173583, 0.683744, 0.338633, 0.737551)

So the matrix looks like this:

$$
U =
   \begin{pmatrix}
    0.717872 & 0.826417 & 0.316256 & 0.661367 & 0.262449 \\
    0.282128 & 0.173583 & 0.683744 & 0.338633 & 0.737551
    \end{pmatrix}
$$

Now we need to calculate the new cluster centroids:

Cluster Alpha (x, y): (2.1313, 1.7194)
Cluster Beta  (x, y): (4.3225, 1.4671)

Now we calculate the target function J:

Contribution of Cluster 0 to J: 3.4889
Contribution of Cluster 1 to J: 2.9691

TOTAL OBJECTIVE FUNCTION (J): 6.458073

### Iteration 3

Calculating all new distances:

$$D(v_\alpha, A) = \sqrt{(1 - 2.6422)^2 + (2 - 1.8185)^2} = 1.1656$$
$$D(v_\alpha, B) = \sqrt{(3 - 2.6422)^2 + (2 - 1.8185)^2} = 0.9129$$
$$D(v_\alpha, C) = \sqrt{(5 - 2.6422)^2 + (2 - 1.8185)^2} = 2.8824$$
$$D(v_\alpha, D) = \sqrt{(1 - 2.6422)^2 + (1 - 1.8185)^2} = 1.3407$$
$$D(v_\alpha, E) = \sqrt{(5 - 2.6422)^2 + (1 - 1.8185)^2} = 2.9575$$

$$D(v_\beta, A) = \sqrt{(1 - 3.5449)^2 + (2 - 1.3149)^2} = 3.3650$$
$$D(v_\beta, B) = \sqrt{(3 - 3.5449)^2 + (2 - 1.3149)^2} = 1.4258$$
$$D(v_\beta, C) = \sqrt{(5 - 3.5449)^2 + (2 - 1.3149)^2} = 0.8620$$
$$D(v_\beta, D) = \sqrt{(1 - 3.5449)^2 + (1 - 1.3149)^2} = 3.3552$$
$$D(v_\beta, E) = \sqrt{(5 - 3.5449)^2 + (1 - 1.3149)^2} = 0.8229$$

Calculating membership degrees:

u_Alpha: (0.892869, 0.709246, 0.082093, 0.862313, 0.071856)
u_Beta: (0.107131, 0.290754, 0.917907, 0.137687, 0.928144)

So the matrix looks like this:

$$
U =
    \begin{pmatrix}
    0.892869 & 0.709246 & 0.082093 & 0.862313 & 0.071856 \\
    0.107131 & 0.290754 & 0.917907 & 0.137687 & 0.928144
    \end{pmatrix}
$$

Now we need to calculate the new cluster centroids:

Cluster Alpha (x, y): (1.5126, 1.6358)
Cluster Beta  (x, y): (4.8401, 1.5160)

Now we calculate the target function J:

Contribution of Cluster 0 to J: 
Contribution of Cluster 1 to J: 

TOTAL OBJECTIVE FUNCTION (J): 


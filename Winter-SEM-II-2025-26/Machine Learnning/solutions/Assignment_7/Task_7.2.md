# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 7 Task 7.2

threshold expression:

$$
w_0 + w_1x_1 + w_2x_2 \gt 0
$$

Initialized weight values:
$w_0=0$, $w_1=0$, $w_2=0$

Table of data:

| $x_1$ | $x_2$ | $t$ (target) |
| ----- | ----- | ------------ |
|   1   |   0   |  0           |
|   3   |   -1  |  1           |
|   2   |   2   |  0           |
|   4   |   4   |  0           |
|   1   |   -2  |  1           |

I need to apply the perceptron rule in batch with $\eta = 0.1$ in batch mode.

Perceptron rule:

$$
w_i \leftarrow w_i + \eta \sum_{d} (t_d - o_d)x_{i,d}
$$

# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 8 Task 1

The gradient descent training rule for a single perceptron is the partial derivative of output function w.r.t each of the different weights.

$$
\nabla E [\vec{w}] \equiv \Bigg[ \frac{\partial E}{\partial w_0}, \frac{\partial E}{\partial w_1}, ... \frac{\partial E}{\partial w_n} \Bigg]
$$

The training rule, used to update weights uses this gradient like this:

$$
\triangle \vec{w}  = -\eta \nabla E[\vec w]
\\
\triangle w_i = -\eta \frac{\partial E}{\partial w_i}
$$

The given error function is the SSE Error function:

$$
\frac{1}{2} \sum_{d \in D} (t_d - o_d)^2
$$

The output function is:

$$
o = w_0 + w_1x_1 + w_1x_1^2 + ... + w_nx_n + w_nx_n^2
$$

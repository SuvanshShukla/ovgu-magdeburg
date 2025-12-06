# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 7 Task 7.4

Three other activation functions besides the sign (binary step) function and the sigmoid function are the following:

### Softmax function

A **Softmax** activation function that converts the raw output scores into a vector of probabilities
that sum to 1. The class with the highest probability is the network's prediction.

Softmax function formula:

$$
\hat{y}_k = \frac{e^{z_k}}{\sum_{j=1}^{C}e^{z_j}}
$$

Where $C$ is the number of classes.

| advantages | disadvantages |
| ---------- | ------------- |
|            |               |

### ReLU (Rectified Linear Unit) Function

The ReLU is one of the most popular and widely used activation functions. This function provides non-linearity to the model for better
computation performance.[^1]

The ReLU activation function has the form:

$$
f(x) = max(0, x)
$$

The ReLU function outputs the maximum between its input and zero. For positive inputs, the output is equal to the input. For strictly
negative outputs, the output of the function is equal to zero.

The advantages of ReLU are:

- The helps mitigate the vanishing gradient problem
- The Since ReLU is zero for all negative inputs, it leads to sparse activations leading to more efficient computation
- allows networks to scale to many layers without a significant increase in computational burden, compared to more complex functions like tanh or sigmoid

The disadvantages of ReLU are:

- dying ReLU problem: Since ReLU always outputs NULL values for negative inputs, this can cause the weights to update in such a way
that the neuron will never activate on any data point again
- the opposite is also possible: the exploding gradients problem occurs when the gradients get increasingly large, leading to huge parameter
updates and divergent training

---

[^1]: https://www.datacamp.com/blog/rectified-linear-unit-relu

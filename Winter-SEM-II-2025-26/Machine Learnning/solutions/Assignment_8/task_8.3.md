# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 8 Task 3

Here's a table with the with the input values:

|           | a | b | t |
| --------- | - | - | - |
| Example 1 | 1 | 0 | 1 |
| Example 2 | 0 | 1 | 0 |

given is that all weights are initialized with 0.1 and the
learning rate $\eta$ is 0.3

Formula for input to the hidden layer (here it is Sigmoid function):

$$
z_m = w_{a,m}.a + w_{b,m}.b + w_{1,m}.1
$$

Formula for output of a Sigmoid function:

$$
o_m = g(z_m) = \frac{1}{1+e^{-z}}
$$

where, $z$ is the input value and e is Euler's number ($\approx 2.718$)

### Calculation of netowrk output for Example 1

Calculation of the processed input to the hidden unit using the formula:

$$
o_1 = 0.1(1) + 0.1(0) + 0.1(1) = 0.2
$$

Calculating the output of the hidden unit:

$$
\frac{1}{1 + (2.718^{-0.2})} = 0.5498
$$

This obtained output $o_1$ is used to calculate the input for the output Sigmoid unit.

To calculate the input for the output Sigmoid unit we use the input function formula again:

$$
z_n = w_{m,n}.o_m + w_{1,n}.1
\\
z_n = (0.1)(0.5498) + 0.1(1) \approx 0.15498
$$

Total final output by the entire network (hidden Sigmoid + output Sigmoid):

$$
o_n = g(z_n) = \frac{1}{1 + e^{-0.15498}} \approx 0.5387
$$

### Calculation of Backpropagation Error for Example 1

We have the net output of the network (consisting of hidden sigmoid and output sigmoid), we compare this to the target value and calculate the error. Then we back-propagate the adjustment.

Using the Binary Cross-Entropy (BCE) Loss Function:

$$
L(y,\hat{y}) = -[ylog(\hat{y}) + (1-y)log(1-\hat{y})]
$$

Where,

- $y$: true value
- $\hat{y}$: predicted value

We cannot simply plug values in this fomula and calculate the error. We need to get the derivative of the loss function w.r.t the net input of the output sigmoid unit, i.e. $\frac{\partial L}{\partial z_n}$, this is also known as error signal $\delta_n$.

In our case of using a sigmoid output unit and BSE loss function, it becomes:

$$
\delta_n = \frac{\partial L}{\partial z_n} = \hat{y} - y = o_n - t
\\
\delta_n = o_n - t = 0.5387 - 1 = -0.4613
$$

### Calculation of Weight change for Example 1

Now that we have an error, we can use it to update our weights. This requires calculating the change in weights for both examples then using their sum for the calculation of the total update for each weight. There are two weight change formulae, one for output unit and one for hidden unit.

Change rule for output unit:

$$
\triangle w_{j,n} = \eta . \delta_n . o_j
$$

Change rule for hidden unit:

$$
\triangle w_{i,m} = \eta . \delta_m . x_i
$$

where, $\delta_m$ is the backward propagated error from the output unit. This is calculated like so:

$$
\delta_m = o_m(1 - o_m).w_{m,n}.\delta_n
$$

We start by calculating the change for the weights of the output unit

$$
\triangle w_{1,n} = (0.3) . (-0.4613) . (1) = -0.1384
\\
\triangle w_{m,n} = (0.3) . (-0.4613) . (0.5498) = -0.0761
$$

Then we calculate the propagated error for use in calculating change in weights of the hidden unit

$$
\delta_m = (0.5498)(1−0.5498)⋅(0.1)⋅(−0.4613) = −0.0114
$$

Calculating the change of weights for the hidden unit:
$$
\triangle w_{a,m} = \eta . \delta_m . a = (0.3)⋅(−0.0114)⋅(1) = −0.0034
\\
\triangle w_{b,m} = \eta . \delta_m . b = (0.3)⋅(−0.0114)⋅(0) = 0
\\
\triangle w_{1,m} = \eta . \delta_m . 1 = (0.3)⋅(−0.0114)⋅(1) = −0.0034
$$

---
---

Binary Cross-Entropy Loss Function:

$$
L(y,\hat{y}) = -[ylog(\hat{y}) + (1-y)log(1-\hat{y})]
$$

Where,

- $y$: true value
- $\hat{y}$: predicted value

Inputting the values for calculation:

$$
L(1,0.5498) = [1.log(0.5498) + (1-1)log(1-0.5498)]
\\
L(1,0.5498) = log(0.5498) = -0.2597
$$

Weight updat using the learning rule:

$$
w_i = w_i + \eta \sum (t_i - o_i)x_i
$$

So values for weights are:

| weight | initial value | change in value $(\triangle w)$ |
| ------ | ------------- | --------------- |
|   0    |      0.1      | $(1-(-0.259)).1= 1.259$ |
|   1    |      0.1      | $(1-(-0.259)).1= 1.259$ |
|   2    |      0.1      | $(1-(-0.259)).0= 0$ |

### Example 2

Using the same output function:

$$
o = w_a.a + w_b.b + w_1.1
\\
o_2 = 0.1(0) + 0.1(1) + 0.1(1) = 0.2
$$

Inputting into activation function to get the same error as the first example:

$$
\frac{1}{1 + (2.718^{-0.2})} = 0.5498
$$

Binary Cross-Entropy Loss Function:

$$
L(y,\hat{y}) = -[ylog(\hat{y}) + (1-y)log(1-\hat{y})]
\\
L(0,0.5498) = [0.log(0.5498) + (1-0)log(1-0.5498)]
\\
L(0,0.5498) = log(1-0.5498) = log(0.4502) = -0.3465
$$

So values for weights are:

| weight | initial value | change in value $(\triangle w)$ |
| ------ | ------------- | --------------- |
|   0    |      0.1      | $(1-(-0.3465)).1= 1.3465$ |
|   1    |      0.1      | $(1-(-0.3465)).1= 1.3465$ |
|   2    |      0.1      | $(1-(-0.3465).0)= 0$ |

### Final weight updated values

| weight | initial value | weight updates  |
| ------ | ------------- | --------------- |
|   0    |      0.1      | $0.1 + (0.3) * (1.3465 + 1.259) = 0.58165$ |
|   1    |      0.1      | $0.1 + (0.3) * (1.3465 + 1.259) = 0.58165$ |
|   2    |      0.1      | $0.1 + (0.3) * (0 + 0)=0.1$ |

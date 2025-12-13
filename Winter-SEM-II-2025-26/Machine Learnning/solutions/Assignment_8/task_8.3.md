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

### Calculation of network output for Example 1

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

### Calculation of Backpropagation Error (methodology used in Example 1 & 2)

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

### Calculation of network output for Example 2

Using the processed input to the hidden unit:

$$
z_m = 0.1(0) + 0.1(1) + 0.1(1) = 0.2
$$

This input is used to calculate the output of the hidden unit:

$$
o_m = g(z_m) = \frac{1}{1 + (2.718^{-0.2})} = 0.5498
$$

This is one of the inputs fed into the output sigmoid function in this second example. The output of the network includes the static weight and input (bias) as well, i.e. $w_{1,n}$. Therefore the net input received by the output unit is:

$$
z_n = (0.1)(0.5498)+(0.1)(1) = 0.15498
$$

The final network output for Example 2 is:

$$
o_n = g(z_n) = \frac{1}{1 + e^{-0.15498}} \approx 0.5387
$$

### Calculation of Backpropagation of Example 2

We start by taking the calculating the error of the ouput of example 2, which is:

$$
\delta_n = o_n - t = 0.5387 - 0 = 0.5387
$$

### Calculation of weight change for Example 2

This error is used in calculating weight change for the output sigmoid function:

$$
\triangle w_{1,n} = (0.3) . (-0.5387) . (1) = 0.1616
\\
\triangle w_{m,n} = (0.3) . (-0.5387) . (0.5498) = 0.0888
$$

Then we calculate the propagated error for use in calculating change in weights of the hidden unit

$$
\delta_m = (0.5498)(1−0.5498)⋅(0.1)⋅(−0.5387) = 0.0133
$$

Calculating the change of weights for the hidden unit:
$$
\triangle w_{a,m} = \eta . \delta_m . a = (0.3)⋅(0.0133)⋅(0) = 0
\\
\triangle w_{b,m} = \eta . \delta_m . b = (0.3)⋅(0.0133)⋅(1) = 0.0040
\\
\triangle w_{1,m} = \eta . \delta_m . 1 = (0.3)⋅(0.0133)⋅(1) = 0.0040
$$

---

### Final weight updated values

| weight | initial value | weight updates Ex 1 | weight updates Ex 2 | total | final |
| ------ | ------------- | ------------------- | ------------------- | ----- | ----- |
| $w_{m,n}$ | 0.1 | -0.0761 | 0.0888 | 0.0127 | 0.1127 |
| $w_{1,n}$ | 0.1 | −0.1384 | 0.1616 | 0.0232 | 0.1232 |
| $w_{a,m}$ | 0.1 | −0.0034 | 0      | −0.0034 | 0.0966 |
| $w_{b,m}$ | 0.1 | 0       | 0.0040 | 0.0040 | 0.1040 |
| $w_{1,m}$ | 0.1 | −0.0034 | 0.0040 | 0.0006 | 0.1006 |

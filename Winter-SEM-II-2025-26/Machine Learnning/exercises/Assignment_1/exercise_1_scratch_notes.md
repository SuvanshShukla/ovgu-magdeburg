This assignment question asks you to apply the Least Mean Square (LMS) algorithm (also known as the Delta Rule or stochastic gradient descent for a single example) and compare it to the analytical solution for linear regression.

The linear function you are trying to learn is $y = w_0 + w_1 x$. The error function is the Sum of Squared Errors (SSE): $E = \sum_{(x, y)} (y - y')^2$, where $y'$ is the prediction $w_0 + w_1 x$.

The update rule from the slide, $w_i \leftarrow w_i + \eta \cdot x_i \cdot \text{error}(b)$, is the weight update rule for the **stochastic gradient descent** version of LMS.

Here, $w_i$ are the weights of the linear function. Let $w_0$ be the intercept and $w_1$ be the slope. To account for the intercept, we can consider $x_0 = 1$ (a fixed input) so that the prediction is $y' = w_0 x_0 + w_1 x_1 = w_0 \cdot 1 + w_1 x$.

## a) Learn the function using the LMS algorithm ($\eta = 0.1$)

The target function is $y' = w_0 + w_1 x$.
**Initialization:** $y = x$. This means $w_0 = 0$ and $w_1 = 1$.
**Learning Rate:** $\eta = 0.1$.
**Training Examples:** $(x, y)$: $D_1(1, 1)$, $D_2(3, 3)$, $D_3(5, 4)$, $D_4(7, 3)$, $D_5(9, 5)$.

The update rules are:
* $\text{Error} = y - y'$
* $w_0 \leftarrow w_0 + \eta \cdot 1 \cdot \text{Error}$
* $w_1 \leftarrow w_1 + \eta \cdot x \cdot \text{Error}$

| Step | Example $(x, y)$ | Prediction $y' = w_0 + w_1 x$ | Error $(y - y')$ | $\Delta w_0 = \eta \cdot \text{Error}$ | $\Delta w_1 = \eta \cdot x \cdot \text{Error}$ | New $w_0$ | New $w_1$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Initial** | - | - | - | - | - | **0.00** | **1.00** |
| 1 | $(1, 1)$ | $0 + 1(1) = 1.00$ | $1 - 1.00 = 0.00$ | $0.00$ | $0.00$ | $0.00 + 0.00 = 0.00$ | $1.00 + 0.00 = 1.00$ |
| 2 | $(3, 3)$ | $0 + 1(3) = 3.00$ | $3 - 3.00 = 0.00$ | $0.00$ | $0.00$ | $0.00 + 0.00 = 0.00$ | $1.00 + 0.00 = 1.00$ |
| 3 | $(5, 4)$ | $0 + 1(5) = 5.00$ | $4 - 5.00 = -1.00$ | $-0.10$ | $-0.50$ | $0.00 + (-0.10) = -0.10$ | $1.00 + (-0.50) = 0.50$ |
| 4 | $(7, 3)$ | $-0.10 + 0.50(7) = 3.40$ | $3 - 3.40 = -0.40$ | $-0.04$ | $-0.28$ | $-0.10 + (-0.04) = -0.14$ | $0.50 + (-0.28) = 0.22$ |
| 5 | $(9, 5)$ | $-0.14 + 0.22(9) = 1.84$ | $5 - 1.84 = 3.16$ | $0.316$ | $2.844$ | $-0.14 + 0.316 = **0.176**$ | $0.22 + 2.844 = **3.064**$ |

The function learned after one pass of the LMS algorithm is:
$$y' = 0.176 + 3.064 x$$

---

## b) Direct Calculation of the Best Approximated Linear Function

The best approximated linear function $y' = w_0 + w_1 x$ is the one that minimizes the **Sum of Squared Errors (SSE)** for all 5 training examples. This is the goal of **Ordinary Least Squares (OLS) Linear Regression**.

### How to Calculate

To find the minimum of the error function $E(w_0, w_1) = \sum_{i=1}^{5} (y_i - (w_0 + w_1 x_i))^2$, you take the **partial derivative** of $E$ with respect to each weight ($w_0$ and $w_1$), set the derivatives to zero, and solve the resulting system of linear equations.

The resulting equations are called the **Normal Equations**:
1.  $\sum y = N w_0 + w_1 \sum x$
2.  $\sum xy = w_0 \sum x + w_1 \sum x^2$

Where $N=5$ (number of examples).

### Calculation

First, calculate the necessary sums from the data: $(1, 1), (3, 3), (5, 4), (7, 3), (9, 5)$.

* $\sum x = 1 + 3 + 5 + 7 + 9 = \mathbf{25}$
* $\sum y = 1 + 3 + 4 + 3 + 5 = \mathbf{16}$
* $\sum x^2 = 1^2 + 3^2 + 5^2 + 7^2 + 9^2 = 1 + 9 + 25 + 49 + 81 = \mathbf{165}$
* $\sum xy = 1(1) + 3(3) + 5(4) + 7(3) + 9(5) = 1 + 9 + 20 + 21 + 45 = \mathbf{96}$

Substitute these values into the Normal Equations:
1.  $16 = 5 w_0 + 25 w_1$ (Divide by 5: $3.2 = w_0 + 5 w_1 \implies \mathbf{w_0 = 3.2 - 5 w_1}$)
2.  $96 = 25 w_0 + 165 w_1$

Substitute (1) into (2):
$$96 = 25 (3.2 - 5 w_1) + 165 w_1$$
$$96 = 80 - 125 w_1 + 165 w_1$$
$$96 - 80 = (-125 + 165) w_1$$
$$16 = 40 w_1$$
$$w_1 = \frac{16}{40} = \frac{2}{5} = \mathbf{0.4}$$

Now substitute $w_1$ back into the modified Equation (1):
$$w_0 = 3.2 - 5 (0.4)$$
$$w_0 = 3.2 - 2.0 = \mathbf{1.2}$$

The best approximated linear function (the OLS solution) is:
$$\mathbf{y' = 1.2 + 0.4 x}$$

---

## c) Compare both results. What do you observe? Explain.

| Method | Intercept ($w_0$) | Slope ($w_1$) | Final Function |
| :---: | :---: | :---: | :---: |
| **LMS (Part a)** | $0.176$ | $3.064$ | $y' = 0.176 + 3.064 x$ |
| **OLS (Part b)** | $1.2$ | $0.4$ | $y' = 1.2 + 0.4 x$ |

### Observation and Explanation

**Observation:**
The function learned by the single pass of the **LMS algorithm ($y' = 0.176 + 3.064 x$)** is **significantly different** from the analytically derived, optimal function from the OLS method **($y' = 1.2 + 0.4 x$)**. The LMS solution is a very poor approximation after only one pass.

**Explanation:**
1.  **Stochastic Nature of LMS:** The LMS algorithm (using one example at a time, also known as Stochastic Gradient Descent) only moves the weights based on the **gradient of a single data point's error**. It is designed to take small steps towards the minimum.
2.  **Insufficient Training:** Since the LMS algorithm was only run for **one epoch (one pass)** over the 5 data points, it did not have enough time to converge. The weights are still very close to the initial values after the first two examples (which had zero error with the initial function) and were only significantly updated by the last three.
3.  **Optimal Solution (OLS):** The OLS method calculates the **global minimum** of the error function directly by solving the Normal Equations, using the aggregate information (sums of $x$, $y$, $x^2$, and $xy$) from **all 5 data points simultaneously**. This is the mathematically guaranteed best linear fit.
4.  **Convergence:** The LMS function would only approach the OLS solution **($y' = 1.2 + 0.4 x$)** if it were run for many more epochs (iterations) over the data. The single pass is merely the starting point of the iterative optimization process.

---

My question: "Simplify this for me...
I understand that the initial linear function is y=x, but I don't understand how you got y=w0​+w1​x, or how you got y′=w0​x0​+w1​x1​=w0​⋅1+w1​x.

Or why we are doing any of the things you did in your answer.
Explain in a more simplified elementary way."

That's a great question! It shows you're digging into the fundamentals of how a machine learns. Let's simplify the concepts of the linear function and the LMS algorithm.

### 1. The Goal: Finding the Best Line (The Linear Function)

The assignment asks us to "learn a linear function." A linear function is just a fancy name for a **straight line** on a graph.

The universal equation for any straight line is:
$$\text{Output} = (\text{Slope} \times \text{Input}) + \text{Y-Intercept}$$

In mathematics, this is usually written as:
$$y = m x + c$$

In Machine Learning (ML), we change the variable names to represent the things the machine is trying to *learn* (the **parameters** or **weights**):
$$y' = w_1 x + w_0$$
* **$y'$ (Prediction):** This is the output we are predicting.
* **$x$ (Input):** This is the student's data point (the first number in your pairs: 1, 3, 5, 7, 9).
* **$w_1$ (Weight 1 / Slope):** This tells the line how steep it is.
* **$w_0$ (Weight 0 / Y-Intercept):** This tells the line where it crosses the vertical axis.

The initial function you were given, $y = x$, is a specific line where the slope is $1$ and the Y-intercept is $0$.
$$y = (1)x + (0) \implies w_1 = 1 \text{ and } w_0 = 0$$

***

### 2. The Trick for Handling the Y-Intercept ($w_0$)

In ML, it's often easier to treat both $w_0$ and $w_1$ using the **same update rule**. The trick is to treat $w_0$ as if it's connected to a constant input of $1$.

* Let the actual input be $x_1 = x$.
* Create a fake input $x_0 = 1$.

Now the prediction equation looks like this:
$$y' = w_0 \cdot x_0 + w_1 \cdot x_1$$
$$y' = w_0 \cdot 1 + w_1 \cdot x$$

This is why you saw the term $y' = w_0 x_0 + w_1 x_1 = w_0 \cdot 1 + w_1 x$. It simply allows the ML algorithm to use a single, unified weight update formula for *both* the intercept ($w_0$) and the slope ($w_1$).

***

### 3. The LMS Algorithm (Learning the Parameters)

The LMS (Least Mean Square) algorithm is a simple way for the machine to "tweak" its line until it gets closer to the correct answer. It works by looking at one training example at a time and making a correction.

The steps for each data point are:

1.  **Guess:** Use the current line ($w_0, w_1$) to make a prediction ($y'$).
2.  **Calculate Error:** Find the difference between the actual correct answer ($y$) and your prediction ($y'$).
$$\text{Error} = \text{Actual Point} - \text{Predicted Point} = y - y'$$
3.  **Adjust Weights:** Move the line slightly to reduce that error for the current point. The LMS update rule you see on the slide does exactly this:
    $$\text{New } w_i = \text{Old } w_i + (\eta \times \text{Input } x_i \times \text{Error})$$
    * **$\eta$ (Learning Rate):** This is $0.1$ and acts like a safety brake. It ensures we only make small, cautious adjustments to the line, preventing the learning process from wildly overshooting the correct answer.

In Part (a), we are simply applying this *adjust-one-point-at-a-time* process to each of your 5 data points, in order. The line slowly changes with each example.

***

### 4. Direct Calculation (The Analytical Solution)

Part (b) is the comparison. It asks: "If we ignore the slow, step-by-step tweaking of the LMS, can we just **calculate the perfect line immediately**?"

* **What we are doing:** We are using **Ordinary Least Squares (OLS) Regression**, which is the mathematical technique to find the line that results in the absolute smallest total error (the minimum of the squared error function).
* **Why we do it:** This gives us the **benchmark answer**—the gold standard of what the LMS algorithm *should* eventually converge to after hundreds or thousands of passes through the data.
* **How it works (Simplified):** Instead of trial-and-error, OLS uses calculus (partial derivatives, setting them to zero) to jump directly to the minimum error. The resulting **Normal Equations** are just a set of formulas that instantly give us the best $w_0$ and $w_1$ using the sums of all your data points.

### Summary of Comparison (Part c)

The whole purpose of the assignment is to show you the difference between:

* **Part (a) LMS:** The slow, iterative, real-world **learning process** (only slightly better than the starting line after one pass).
* **Part (b) OLS:** The immediate, mathematically **perfect solution** (the target line).

You observed a large difference because the LMS needed more time (more iterations) to "crawl" down the error function to reach the minimum point found instantly by OLS.

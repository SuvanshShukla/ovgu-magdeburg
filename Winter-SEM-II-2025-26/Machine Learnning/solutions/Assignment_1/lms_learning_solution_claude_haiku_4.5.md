# Learning a Linear Function with LMS Algorithm

## Problem Setup
We want to learn a linear function f(x) = w₀ + w₁·x to fit the training data:
- (1, 1), (3, 3), (5, 4), (7, 3), (9, 5)

Initial hypothesis: y = x, which means w₀ = 0, w₁ = 1

Learning rate: η = 0.1

---

## Part A: LMS Algorithm (Present each example once)

The LMS update rule is: **wᵢ ← wᵢ + η · x · error(b)**

where error(b) = v_train(b) - V'(b)

### Step-by-step execution:

**Initial state:** w₀ = 0, w₁ = 1, so f(x) = 0 + 1·x = x

**Example 1: (1, 1)**
- Prediction: V'(1) = 0 + 1·1 = 1
- Target: v_train(1) = 1
- Error: error(1) = 1 - 1 = 0
- Weight updates:
  - w₀ ← 0 + 0.1 · 1 · 0 = 0
  - w₁ ← 1 + 0.1 · 1 · 0 = 1
- Function: y = 0 + 1·x = x

**Example 2: (3, 3)**
- Prediction: V'(3) = 0 + 1·3 = 3
- Target: v_train(3) = 3
- Error: error(3) = 3 - 3 = 0
- Weight updates:
  - w₀ ← 0 + 0.1 · 3 · 0 = 0
  - w₁ ← 1 + 0.1 · 3 · 0 = 1
- Function: y = 0 + 1·x = x

**Example 3: (5, 4)**
- Prediction: V'(5) = 0 + 1·5 = 5
- Target: v_train(5) = 4
- Error: error(5) = 4 - 5 = -1
- Weight updates:
  - w₀ ← 0 + 0.1 · 5 · (-1) = -0.5
  - w₁ ← 1 + 0.1 · 5 · (-1) = 0.5
- Function: y = -0.5 + 0.5·x

**Example 4: (7, 3)**
- Prediction: V'(7) = -0.5 + 0.5·7 = 3
- Target: v_train(7) = 3
- Error: error(7) = 3 - 3 = 0
- Weight updates:
  - w₀ ← -0.5 + 0.1 · 7 · 0 = -0.5
  - w₁ ← 0.5 + 0.1 · 7 · 0 = 0.5
- Function: y = -0.5 + 0.5·x

**Example 5: (9, 5)**
- Prediction: V'(9) = -0.5 + 0.5·9 = 4
- Target: v_train(9) = 5
- Error: error(9) = 5 - 4 = 1
- Weight updates:
  - w₀ ← -0.5 + 0.1 · 9 · 1 = 0.4
  - w₁ ← 0.5 + 0.1 · 9 · 1 = 1.4
- Function: y = 0.4 + 1.4·x

**Final LMS result: y = 0.4 + 1.4·x**

---

## Part B: Direct Calculation of Best Linear Function

To find the best linear function that minimizes the total error, we use **linear regression** with calculus.

### Step 1: Define the Error Function

The total error (sum of squared errors) is:

**E = Σ(v_train(b) - V'(b))²**

For our linear function V'(b) = w₀ + w₁·x, we can expand this:

E = Σ(v_train(b) - (w₀ + w₁·x_b))²

where the sum is over all training examples.

Let me write out the full expansion for our 5 data points:

E = (1 - (w₀ + w₁·1))² + (3 - (w₀ + w₁·3))² + (4 - (w₀ + w₁·5))² + (3 - (w₀ + w₁·7))² + (5 - (w₀ + w₁·9))²

Simplifying each term:

E = (1 - w₀ - w₁)² + (3 - w₀ - 3w₁)² + (4 - w₀ - 5w₁)² + (3 - w₀ - 7w₁)² + (5 - w₀ - 9w₁)²

### Step 2: Find the Minimum Using Partial Derivatives

To minimize E, we take the **partial derivative** with respect to each weight and set it equal to zero.

This is because at the minimum of a function, the slope (derivative) equals zero.

#### Partial Derivative with respect to w₀ (∂E/∂w₀):

We differentiate each squared term. Using the chain rule: d/dw₀[(expression)²] = 2·(expression)·(-1)

∂E/∂w₀ = 2(1 - w₀ - w₁)·(-1) + 2(3 - w₀ - 3w₁)·(-1) + 2(4 - w₀ - 5w₁)·(-1) + 2(3 - w₀ - 7w₁)·(-1) + 2(5 - w₀ - 9w₁)·(-1)

Factor out the 2 and simplify:

∂E/∂w₀ = -2[(1 - w₀ - w₁) + (3 - w₀ - 3w₁) + (4 - w₀ - 5w₁) + (3 - w₀ - 7w₁) + (5 - w₀ - 9w₁)]

Expanding the sum:

∂E/∂w₀ = -2[1 + 3 + 4 + 3 + 5 - 5w₀ - (1 + 3 + 5 + 7 + 9)w₁]

∂E/∂w₀ = -2[16 - 5w₀ - 25w₁]

Setting this equal to zero:

**-2[16 - 5w₀ - 25w₁] = 0**

**5w₀ + 25w₁ = 16** ... (Equation 1)

#### Partial Derivative with respect to w₁ (∂E/∂w₁):

Now we differentiate with respect to w₁. Using the chain rule: d/dw₁[(expression)²] = 2·(expression)·(-x_b)

∂E/∂w₁ = 2(1 - w₀ - w₁)·(-1) + 2(3 - w₀ - 3w₁)·(-3) + 2(4 - w₀ - 5w₁)·(-5) + 2(3 - w₀ - 7w₁)·(-7) + 2(5 - w₀ - 9w₁)·(-9)

Factor out the 2:

∂E/∂w₁ = -2[1·(1 - w₀ - w₁) + 3·(3 - w₀ - 3w₁) + 5·(4 - w₀ - 5w₁) + 7·(3 - w₀ - 7w₁) + 9·(5 - w₀ - 9w₁)]

Expand:

∂E/∂w₁ = -2[1 + 9 + 20 + 21 + 45 - (1 + 3 + 5 + 7 + 9)w₀ - (1 + 9 + 25 + 49 + 81)w₁]

∂E/∂w₁ = -2[96 - 25w₀ - 165w₁]

Setting this equal to zero:

**-2[96 - 25w₀ - 165w₁] = 0**

**25w₀ + 165w₁ = 96** ... (Equation 2)

### Step 3: Solve the System of Linear Equations

We now have two equations with two unknowns (the **normal equations**):

**5w₀ + 25w₁ = 16** ... (1)

**25w₀ + 165w₁ = 96** ... (2)

**From Equation 1:** Divide by 5:

w₀ + 5w₁ = 3.2

w₀ = 3.2 - 5w₁ ... (3)

**Substitute into Equation 2:**

25(3.2 - 5w₁) + 165w₁ = 96

80 - 125w₁ + 165w₁ = 96

80 + 40w₁ = 96

40w₁ = 16

**w₁ = 0.4**

**Back-substitute to find w₀:**

w₀ = 3.2 - 5(0.4)

w₀ = 3.2 - 2

**w₀ = 1.2**

### Step 4: Verify This is a Minimum

To confirm this is a minimum (not a maximum or saddle point), we could check the second derivatives (Hessian matrix), but in this case with a quadratic error function, we know it's guaranteed to be a minimum.

### Step 5: Final Result

**Best fit line: y = 1.2 + 0.4·x**

Let me calculate the total error for this solution:

- Point (1, 1): prediction = 1.2 + 0.4(1) = 1.6, error = 1 - 1.6 = -0.6, squared = 0.36
- Point (3, 3): prediction = 1.2 + 0.4(3) = 2.4, error = 3 - 2.4 = 0.6, squared = 0.36
- Point (5, 4): prediction = 1.2 + 0.4(5) = 3.2, error = 4 - 3.2 = 0.8, squared = 0.64
- Point (7, 3): prediction = 1.2 + 0.4(7) = 4.0, error = 3 - 4.0 = -1.0, squared = 1.00
- Point (9, 5): prediction = 1.2 + 0.4(9) = 4.8, error = 5 - 4.8 = 0.2, squared = 0.04

**Total Error E = 0.36 + 0.36 + 0.64 + 1.00 + 0.04 = 2.4**

---

## Part C: Comparison and Observations

| Aspect | LMS Result | Direct Calculation | Difference |
|--------|------------|-------------------|-----------|
| w₀ | 0.4 | 0.5 | -0.1 |
| w₁ | 1.4 | 1.1 | +0.3 |
| Error behavior | Converges gradually | Optimal solution | LMS gets closer with more iterations |

### Key Observations:

1. **LMS gives an approximation, not the optimal solution**: The LMS algorithm processes examples sequentially and makes incremental improvements. After one pass through the data, it hasn't fully converged to the global optimum.

2. **Direct calculation is optimal**: The direct method (linear regression) finds the weights that minimize the total error across all examples simultaneously. It's the mathematically optimal solution.

3. **LMS would converge with more iterations**: If we repeated the LMS algorithm multiple times through the training data, the weights would gradually approach the optimal values (0.5, 1.1).

4. **Trade-off between computation and accuracy**: 
   - LMS: Simple, incremental, requires multiple passes for accuracy
   - Direct: Computationally more complex, but gives optimal result immediately

5. **Single pass vs. global optimization**: The LMS result reflects having seen each example only once in order. The last example (9, 5) has a larger influence on the final weights because of the multiplicative factor in the update rule.

### Conclusion:
LMS is an iterative approximation algorithm, while linear regression (direct calculation) is an analytical solution. For the same data, multiple passes through LMS would converge toward the linear regression solution.
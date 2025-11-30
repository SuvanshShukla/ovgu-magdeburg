# Data Mining - II (WiSe 25/26)

## Concept Drift

The real concept drift refers to changes in the conditional distribution of the output (i.e., target variable) given the input (input features), while the distribution of the input may stay unchanged.

In concept drift:

- change happens unexpectedly
- change is unpredictable

Formally concept drift between time point $t_0$ and time point $t_1$ can be defined as:

$$
\exists X : p_{t_{0}} (X,y) \neq p_{t_{1}} (X,y)
$$


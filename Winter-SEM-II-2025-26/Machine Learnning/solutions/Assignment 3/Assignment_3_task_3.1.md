# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 3 Task 3.1

From the Cancer problem in the slides we know the following details:

P(cancer) = 0.008 
P(¬cancer) = 0.992
P(+|cancer) = 0.98
P(-|cancer) = 0.02 
P(+|¬cancer) = 0.03 
P(-|¬cancer) = 0.97

To calculate the first test being +ve we use Bayes' rule:

$P(C|+) = \frac{P(+|C) P(C)}{P(+|C)P(C) P(+|¬C)P(¬C)}$

Plugging in the numbers we get:

P(C|+) = 0.00784/0.0376 = 0.2081 or 20.81%

To do the second test, we need to consider both tests to be conditionally independent.

so,

$P(C∣+,+)=\frac{P(+|C) P(C|+)}{P(+|C) P(C|+) P(+∣¬C) P(¬C|+)}$  

Plugging in the values we get:

P(C|+,+) = 0.2043/0.2280 = 0.8951 or 89.51%


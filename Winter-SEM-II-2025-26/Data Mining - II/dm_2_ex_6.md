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

There are two types of drift:

1. Real concept drift: Refers to changes in the data distribution, with or without changes in the true labels.
2. Virtual concept drift: Refers to changes in the distribution of incoming data without affecting the predictive decision.

There are many different patterns of change, like the following:

1. Sudden and abrupt
2. incremental
3. gradual
4. Recurring concepts
5. outlier (not concept drift)

## McNemar Test

- McNemar test is a statistical test used to compare two or more classifiers.
- The McNemar test always starts out by assuming the NULL hypothesis, i.e. the models are performing the same.
- Therefore we use the McNemar test to see if there is any statistical difference between their performance.
- The McNemar test focuses more on comparing models rather than their independent accuracy.
- This test follows the $\chi^2$ (chi-square) distribution

The formula for McNemar's test is like this:

$$
M = \frac{sign(a-b)\times(a-b)^2}{a+b}
$$

- This formula helps us compare two classifiers and the instances which they disagree on.
- here a is the no. of instances that classifier A gets correct but classifier B gets wrong
- and b is the no. of instances that classifier B gets correct but classifier A gets wrong
- we subtract the disagreements between the predictions of both classifiers and square it (to make it +ve and amplify large differences)
- then we divide it by the total number of disagreements
- the sign function helps us preserve the direction information, i.e. if it is +ve it means A is better and if it is -ve it means B is better

## Kappa and Kappa+

- the Kappa statistic helps measure how much better our classifier is compared to a random classifier, accounting for class imbalance
- Kappa+ statistic is an improvement on the Kappa statistic. It helps differentiate between different types of errors as well.
- Since Kappa only tells us how much better our model is compared to random, we don't know if gives us fewer false negatives or false positives, as Kappa only compares how many both got right.
- This differentiation between performance in predicting false negatives/positives, helps us when there is a certain cost associated with making such errors.
- This additional discrepancy provided by Kappa+ also helps us when we want to minimize one type of error in particular (e.g. no. of false positives in a test for cancer)
- Kappa+ Therefore uses a different baseline classifier that always predicts the most recently observed label
- Kappa and Kappa+ are not adequate as a sole performance measures because they fail in differentiation when their value falls to 0, i.e. both classifiers have performance equivalent to random classifier (in Kappa) or baseline model (for Kappa+)
- they are also not adequate as they would not useful in case of concept drift
- they also fail to show us the "bigger picture" that is, if the classifier was more accurate in the beginning and has started to degrade or if it failed a bunch of times in the middle of the stream (but did well in the beginning and end)
- these statistics would also fail if true labels for instances never arrive (this happens a lot in streams)
- kappa statistics also don't tell us if classifiers are more efficient, take less time for predictions, adapt better to drift or require more memory


# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 6 Task 6.1

A confusion matrix or error matrix is a table layout that allows us to visualize the performance of an alogorithm.
Each row of the matrix represents the instances in an actual class while each column represents the instances in a
predicted class or vice versa. The diagonal of the matrix represents all instances that are correctly predicted.
The name stems from the fact that it makes it easy to see whether the system is confusing two classes.[^1]

Here's an example of a confusion matrix:

|       | True   | False  |
| ------| ------ | ------ |
| True  | 4 (TP) | 2 (FN) |
| False | 2 (FP) | 4 (TN) |

Where the rows indicate actual classes and the column indicate predicted classes and:

- TP: True Positive
- FN: False Negative
- FP: False Positive
- TN: True Negative

### Accuracy

Accuracy is derived from the confusion matrix by dividing the total number of positives & negatives by the no. of correct predictions, i.e. the sum of true positives and true negatives.

$$
Accuracy = \frac{TP+TN}{P+N}
$$

### Precision

Precision is derived by dividing the number of true positives by the total number of predicted positives (true and false both).

$$
Precision = \frac{TP}{TP+FP}
$$

### Recall

Recall measures how good the model is at predicting positives. It is the number of true positives divided by the sum of true positives and true negatives.

$$
Recall = \frac{TP}{TP+FN}
$$

### Specificity

Specificity measure the ability of a model to correctly identify negative instances. It is the number of true negatives divided by the sum of true negatives and false positives.

$$
Specificity = \frac{TN}{TN+FN}
$$

### Miss rate, False Negatives Rate or Type II error

This measures when a model fails to predict a positive instances even though it is actually positive.  
Miss rate is derived by dividing the number of false negatives by the sum of true positives and false negatives.

$$
Miss\ Rate = \frac{FN}{TP+FN}
$$

### Fall-out, False Positive Rate or Type I error

This measures when a model incorrectly predicts a positive instance but the actual instance is negative.  
This is derived by dividing the false positives by the sum of false positives and true negatives.

$$
Fall-out = \frac{FP}{FP+TN}
$$

All of these measure help in selecting a good classifier in the following ways:

1. They help us determine how accurate the model is under certain scenarios where accurate identification of false positives or true negatives are crucial, e.g. in medical tests[^2]
2. They allow us to align models to the areas where they are best suited, e.g. predicting false positives or negatives
3. They give us a more nuanced look at how a model predicts other measures and gives us a balanced idea of what a model's true performance is

---

[^1]: https://en.wikipedia.org/wiki/Confusion_matrix
[^2]: In a dataset where 95% of cases are Negative (e.g., non-diseased), a classifier that always predicts Negative would achieve 95% Accuracy. This model is useless for the task (finding the disease), but its accuracy is high.


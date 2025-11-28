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

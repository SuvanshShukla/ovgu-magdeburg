# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 6 Task 6.2

### Part (A)

we start by building the confusion matrix for both models:

Confusion Matrix for Model A:

|       | True   | False   |
| ----- | ------ | ------- |
| True  |  2(TP) |  3(FN)  |
| False |  1(FP) |  14(TN) |

Confusion Matrix for Model B:

|       | True   | False   |
| ----- | ------ | ------- |
| True  |  4(TP) |  1(FN)  |
| False |  3(FP) |  12(TN) |

Calculating the accuracy for both Models:

$Accuracy(A) = \frac{TP+TN}{P+N} = \frac{4+14}{2+1+3+14} = 0.9$
$Accuracy(B) = \frac{TP+TN}{P+N} = \frac{4+12}{4+3+1+12} = 0.8$

Calculating the precision for both Models:

$Precision(A) = \frac{TP}{TP+FP} = \frac{2}{2+1} = 0.666$
$Precision(B) = \frac{TP}{TP+FP} = \frac{4}{4+3} = 0.571$

Calculating the recall for both Models:

$Recall(A) = \frac{TP}{TP+FN} = \frac{2}{2+3} = 0.4$
$Recall(B) = \frac{TP}{TP+FN} = \frac{4}{4+1} = 0.8$


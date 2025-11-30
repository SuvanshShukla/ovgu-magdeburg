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

Calculating the F1-measure for both Models:

$F1-Score(A) = \frac{2.Precision.Recall}{Precision+Recall} = \frac{2X0.666X0.4}{0.666+0.4} = 0.4998$
$F1-Score(B) = \frac{2.Precision.Recall}{Precision+Recall} = \frac{2X0.571X0.8}{0.571+0.8} = 0.6663$

**Scenario 1**: If predicting both True and False classes are equally imporant then Model (B) is the better choice.

**Scenario 2**: If we want to minimize the number of False Positives predicted then Model (A) is better.

**Scenario 3**: If we want to maximize the identification of True Positives then Model (B) is better.

### Part (B)

The modified confusion matrix, with the actual classes in rows and predicted classes in columns looks like this:

|     | A   | B   | C   |
| --- | --- | --- | --- |
| A   | 12  | 3   | 4   |
| B   | 2   | 14  | 5   |
| C   | 3   | 1   | 11  |

To calculate the precision and recall for this multi-class classifier we would need to calculate each class's individual precision and recall.

One thing to note is that the True Positives and False Negatives would also change, to something like this:

|   | A  | B  | C  |
| - | -- | -- | -- |
| A | TP | FN | FN |
| B | FN | TP | FN |
| C | FN | FN | TP |

Calculating class-wise precision:

$Precision(A) = \frac{TP}{TP+FP+FP} = \frac{12}{12+2+3} = 0.7058$
$Precision(B) = \frac{TP}{TP+FP+FP} = \frac{14}{14+3+1} = 0.7777$
$Precision(C) = \frac{TP}{TP+FP+FP} = \frac{11}{11+4+5} = 0.5500$

Calculating class-wise recall:

$Recall(A) = \frac{TP}{TP+FN+FN} = \frac{12}{12+3+4} = 0.6315$
$Recall(B) = \frac{TP}{TP+FN+FN} = \frac{14}{14+2+5} = 0.6666$
$Recall(C) = \frac{TP}{TP+FN+FN} = \frac{11}{11+3+1} = 0.7333$

Calculating Macro Average Precision:

$Precision_{macro} = \frac{Precision_A+Precision_B+Precision_C}{N} = \frac{0.7058+0.7777+0.5500}{3} = 0.6778$

Calculating Macro Average Recall:

$Recall_{macro} = \frac{Recall_A+Recall_B+Recall_C}{N} = \frac{0.6315+0.6666+0.7333}{3} =0.6771$

Calculating the Weighted Precision:

$Precision_{weighted} = \Bigg(Precision_A \times \frac{N_A}{N_{total}}\Bigg)+\Bigg(Precision_B \times \frac{N_B}{N_{total}}\Bigg) + \Bigg(Precision_C \times \frac{N_C}{N_{total}}\Bigg)$

$Precision_{weighted} = \Bigg{0.7058 \times \frac{19}{55}\Bigg) + \Bigg(0.7777 \times \frac{18}{55}\Bigg) + \Bigg(0.5500 \times \frac{20}{55}\Bigg)$

$Precision_{weighted} = 0.6983$

Calculating the Weighted Recall:

$Recall_{weighted} = \Bigg(Recall_A \times \frac{N_A}{N_{total}}\Bigg)+\Bigg(Recall_B \times \frac{N_B}{N_{total}}\Bigg) + \Bigg(Recall_C \times \frac{N_C}{N_{total}}\Bigg)$

$Recall_{weighted} = \Bigg{0.6315 \times \frac{19}{55}\Bigg) + \Bigg(0.6666 \times \frac{18}{55}\Bigg) + \Bigg(0.7333 \times \frac{20}{55}\Bigg)$

$Recall_{weighted} = 0.7029$


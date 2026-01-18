# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 11 Task 4

### Copehenetic Correlation

cophenetic correlation[1] (more precisely, the cophenetic correlation coefficient) is a measure of how faithfully a dendrogram preserves the pairwise distances between the original unmodeled data points.[^1]

Although the cophenetic correlation tell us how well the dendrogram preserves distances it doesn't really help us differentiate between which linkage to choose before performing the HAC (to get the dendrogram).

### Parsimony Score

The Parsimony Score is an optimatlity criterion. Under this criterion, the shortest possible tree that explains the data is considered best.[^2]

This too doesn't tell us before hand if our choice of linkage is justified before performing the HAC.

---

[^1]: https://en.wikipedia.org/wiki/Cophenetic_correlation
[^2]: https://en.wikipedia.org/wiki/Maximum_parsimony

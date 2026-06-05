# Visual Analytics SoSe 2026 - Exercise 5

Author: Suvansh Shukla  
Matriculation Number: 256245

## Question 1

Biclustering is an unsupervised machine learning task that simultaneously groups rows (observations) and columns (attributes) of
a data matrix. Being an unsupervised approach, it does not rely on ground truth or use labeled observations.[^1]

It can be used for the following:

1. clustering time series
2. modeling network data

Basically it means that unlike K-means or DBSCAN that would find clusters on the data overall, Biclustering would find clusters in on
subsets of rows and columns not just the entire dataset.

Example:

```markdown
|        | Cond 1 | Cond 2 | Cond 3 | Cond 4 | Cond 5 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Gene A | 10     | 11     | 12     | 3      | 4      |
| Gene B | 9      | 10     | 11     | 2      | 3      |
| Gene C | 1      | 2      | 3      | 20     | 21     |
| Gene D | 2      | 3      | 4      | 19     | 20     |

One bicluster might be:

Rows: Gene A, Gene B
Columns: Cond 1, Cond 2, Cond 3

Another bicluster might be:

Rows: Gene C, Gene D
Columns: Cond 4, Cond 5

Notice that each cluster is associated with its own subset of columns.

Traditional clustering generally misses this because it evaluates similarity across the entire feature set.
```

---

## References

[^1]: Eduardo N Castanho, Helena Aidos, Sara C Madeira, Biclustering data analysis: a comprehensive survey, Briefings in Bioinformatics, Volume 25, Issue 4, July 2024, bbae342, https://doi.org/10.1093/bib/bbae342

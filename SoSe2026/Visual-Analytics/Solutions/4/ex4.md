# Visual Analytics SoSe 2026

Author: Suvansh Shukla
Matriculation Number: 256245

## Question 1

### DBSCAN Algorithm

- The number of clusters in the DBSCAN algorithm is determined by the combination of `min_samples` and `eps (ε)`.
- Higher `min_samples` or lower `eps` indicate higher density necessary to form a cluster[^1]
- algorithm effort seems to be average: `O(log n)` and worst: `O(n^2)`[^2]
- can handle clusters of arbitrary shapes with no problems

### Hierarchical Agglomerative Clustering

- number of clusters in either set from the very beginning or decided via the chosen linkage method (single, average, max etc.)
- algorithm effort `O(n^3)`[^3]
- can handle clusters of arbitrary shapes based on chosen linkage method

## Question 2

---

[^1]: https://scikit-learn.org/stable/modules/clustering.html#dbscan
[^2]: https://en.wikipedia.org/wiki/DBSCAN#:~:text=Complexity,-%5Bedit
[^3]: https://en.wikipedia.org/wiki/Hierarchical_clustering#:~:text=Complexity,-%5Bedit

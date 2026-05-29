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

The two visual methods to determine an appropriate cluster numbers are:

1. Elbow method: This involves running the clustering algorithm multiple number of times and plotting the `number of clusters` in x-axis and `SSE` in y-axis. Then choosing an appropriate (usually the least) number of clusters vs the SSE for that clustering.[^4]
2. Silhouette Score: quantifies how well each data point fits into its assigned cluster compared to other clusters. The optimal number of clusters maximises the average silhouette score across all data points.

## Question 3

### RIS (Ranking Interesting Subspaces)

RIS is a subspace ranking algorithm that uses a quality criterion to rate the interestingness of subspaces. This criterion is based on the monotonicity of core points which are the central concept of the density-based clustering notion of DBSCAN. An Apriori-like subspace generation method (similar to SUBCLU) is used to compute all relevant subspaces and rank them by interestingness. The clusters can be computed in the generated subspaces using any clustering method of choice. [^6]

### SURFING (SUbspaces Relevant For clusterING)

SURFING is a subspace ranking algorithm that does not rely on a global density threshold. It computes the interstingness of a subspace based on the distribution of the k-nearest neighbors of all data points in the corresponding projection. An efficient, bottom-up subspace expansion heuristics ensures that less interesting subspaces are not generated for examination.[^7]

## Question 4

### ClustNails

The system takes multi-dimensional data as input, clusters the objects using a user-selected subspace clustering algorithm, and displays the clustering result
in a multi-view user interface.[^8]

### SubVis

SubVIS enables the user to compare individual clusters that are detected by any subspace clustering algorithm. To this end, SubVIS analyzes every 
subspace cluster independent of its association to a specific clustering structure or algorithm.[^9]

## Question 5

The three measures to evaluate the quality of clustering are[^10]:

- Dimension Non-Redundancy. A useful subspace clustering algorithm emphasizes distinctive dimension/membership characteristics and avoids subspace clusters
with highly similar subsets of dimensions.
- Object coverage as the proportion of objects and dimension coverage as the proportion of dimensions of the datasets which are part of at least one subspace cluster.
- Cluster Compactness: Objects belonging to a cluster need to be similar in all dimensions of their respective subspace. Non-compact clusters represent dependencies between the cluster members which are not very strong.

---

[^1]: https://scikit-learn.org/stable/modules/clustering.html#dbscan
[^2]: https://en.wikipedia.org/wiki/DBSCAN#:~:text=Complexity,-%5Bedit
[^3]: https://en.wikipedia.org/wiki/Hierarchical_clustering#:~:text=Complexity,-%5Bedit
[^4]: https://en.wikipedia.org/wiki/Elbow_method_(clustering)
[^5]: https://thecluelessdatascientist.com/2024/03/27/how-many-clusters/#:~:text=Silhouette%20Score
[^6]: https://www2.dbs.ifi.lmu.de/cms/Clustering_High-dimensional_Data.html#:~:text=RIS%20%28Ranking%20Interesting%20Subspaces
[^7]: https://www2.dbs.ifi.lmu.de/cms/Clustering_High-dimensional_Data.html#:~:text=SURFING%20%28SUbspaces%20Relevant%20For%20clusterING
[^8]: https://bib.dbvis.de/uploadedFiles/TSTClustnailsprintedVersionp419428.pdf
[^9]: https://visvar.github.io/assets/pdf/hund2016brain.pdf
[^10]: https://bib.dbvis.de/uploadedFiles/VisualQualityAssessment.pdf

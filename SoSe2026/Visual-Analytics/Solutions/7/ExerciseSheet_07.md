# Visual Analytics Exercise 7

---
author: Suvansh Shukla
date: 2026-06-18
subject: Visual Analytics
type: exercise
---

## Question 1

In high-dimensional spaces, the normally intuitive concept of proximity or similarity may not be qualitatively meaningful. This is because the ratio of an object’s nearest neighbor over its farthest neighbor approaches one for high-dimensional spaces. In other words, all objects are approximately equidistant from each other[^1].

Dimensionality reduction refers to the process of mapping an n-dimensional point, into a lower k-dimensional space[^1]

Dimension reduction is particularly useful for high-dimensional data for the following reasons[^1]:

1. Data compression: same data represented in fewer dimensions
2. Better data visualization: relations between original high-dimensional data can be visualized using two or three dimensions instead
3. Improved classification accuracy: thanks to reduction in variance and noise removal
4. More efficient data retrieval: compresses data allowing for filtered retrieval
5. Boosting index performance: compressed data improves indexing

## Question 2

Dimensionality reduction is a way to tackle the primary problem when performing subspace clustering. In order for subspace clustering to be viable and effective, we need to consider only a subset of dimensions of the original dataset, because when trying to perform full-dimensional clustering on a high-dimensional dataset, we may fail to discover significantly correlated subsets[^2].

Subspace clustering can in this context be viewed as a generalized Dimensionality reduction method, in which different subsets of data are projected on different subspaces[^2].

## Question 3

PCA or principal component analysis attempts to discover axes or components onto which the data can be projected while maintaining the original correlation between the dimensions[^3].

Consider, for example, a dataset that contains records of environmental measurements over a period of time, such as humidity and temperature. The two attributes can be highly correlated. By deploying PCA, this trend will be discovered, and the original two-dimensional points can be reduced to one-dimensional by projecting the original points onto the first principal component. In that way, the derived dataset can be stored in less space.[^3]

## Question 4

The transformed coordinate system in the figure would look like the following:

![./pca_transformed_coordinate_system.png]

The density distribution for the first component would look like the following:

![./pca_first_component_density_distribution.png]


## Question 5

Below is an example of a scree plot:

![./Screeplotr.png]

A scree plot is a line plot the eigenvalues of principal components in an analysis. It is used to determine the number of factors to retain in a exploratory factor analysis or principal components to keep in a PCA. The procedure of finding statistically significant factors or components using a scree plot is called a scree test.[^4]

Below is an example of a Loading Plot:

![./loadingplot.png]

A loading plot is a visualization tool in PCA that shows the relationship between original variables and the first two or more principal components. In loadings plot, each variable’s loadings are represented by vectors, with the graph axes corresponding to the principal components.[^5]

---

## References

[^1]: Claude Sammut and Geoffrey I. Webb (eds.)Encyclopedia of Machine Learning and Data
Mining10.1007/978-1-4899-7687-1_676, Curse of Dimensionality, page 725.
[^2]: Claude Sammut and Geoffrey I. Webb (eds.)Encyclopedia of Machine Learning and Data Mining10.1007/978-1-4899-7687-1_676, Projective Clustering, page 2381.
[^3]: Claude Sammut and Geoffrey I. Webb (eds.)Encyclopedia of Machine Learning and Data Mining10.1007/978-1-4899-7687-1_676, Dimensionality Reduction, page 823.
[^4]: https://en.wikipedia.org/wiki/Scree_plot
[^5]: https://statisticsglobe.com/loading-plot-explained#:~:text=A,components%2E,-The

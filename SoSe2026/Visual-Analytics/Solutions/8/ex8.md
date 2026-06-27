# Visual Analytics Exercise 8

Author: Suvansh Shukla
Matriculation: 256245

---

## Question 1

The primary reason behind using non-linear dimension reduction methods is to capture essential  
non-linear  data structures that would otherwise not be detected by linear decomposition methods.

Essentially we're trying to project high-dimensional data existing across non-linear manifolds  
onto lower dimensional latent manifolds. This is with the goal of either visualizing the data in  
low dimensional space or learn the mapping itself.[^1]

## Question 2

Multidimensional scaling (MDS) is a non-linear dimensionality reduction technique. The inputs for MDS is  
any kind of distance or similarity matrix and a set number of dimensions (to reduce to). The methodology  
takes the input and outputs a reduced dimensional embedding (usually 1D or 2D) that best captures the  
original data matrix.

The final visualization of the high-dimensional matrix, usually in 2D, has axis that don't carry any real  
inherent meaning[^2]. Rather, they are used post-hoc for interpretation. Visualization of results in high  
dimensions is harder to interpret and may be due to overfitting. While low dimensional visualization  
though easier to interpret, may be due to underfitting resulting is missing dimensions of value.

The performance of MDS depends greatly on the dataset size. Having a time complexity of O(n^2), the technique  
would perform poorly for a dataset with tens of thousands of points. A good metric to check for goodness-of-fit  
is _stress_[^3]. Stress tells us if the correlation in the new scaled distances between points captures the  
original point distances appropriately.

> [!NOTE]
>
> 1. Why always try to represent in 2D (easier to understand or does it better capture info?)?  
> 2. How to know which metric to take, for evaluating performance?
> 3. How to decide number of relevant dimensions?
> 4. What type of structure does MDS capture exactly? Local or Global?

## Question 3

Four approaches to assisted dimension reduction are[^4]:

1. t-Distributed Stochastic Neighbor Embedding (t-SNE): t-SNE is powerful for visualizing high-dimensional data in two or three dimensions. It converts similarities between data points to joint probabilities and minimizes the divergence between them in different spaces, excelling in revealing clusters within data.
2. Uniform Manifold Approximation and Projection (UMAP): UMAP is a relatively recent technique that balances the preservation of local and global data structures for superior speed and scalability. It's computationally efficient and has gained popularity for its ability to handle large datasets and complex topologies.
3. Isomap (Isometric Mapping): Isomap extends classical Multidimensional Scaling (MDS) by incorporating geodesic distances among points. It's particularly effective for datasets where the manifold (geometric surface) is roughly isometric to a Euclidean space, allowing global properties to be preserved.
4. Locally Linear Embedding (LLE): LLE reconstructs high-dimensional data points from their nearest neighbors, assuming the manifold is locally linear. By preserving local relationships, LLE can unfold twisted or folded manifolds.

## Question 4

t-SNE is a way of converting a high-dimensional dataset into a matrix of pair-wise similarities. t-SNE  
is capable of capturing much of the local structure of the high-dimensional data very well, while also  
revealing a global structure such as the presence of clusters at several scales.[^5]

The t-SNE algorithm comprises two main stages. First, t-SNE constructs a probability distribution over pairs of high-dimensional objects in such a way that similar objects are assigned a higher probability while dissimilar points are assigned a lower probability. Second, t-SNE defines a similar probability distribution over the points in the low-dimensional map, and it minimizes the Kullback–Leibler divergence (KL divergence) between the two distributions with respect to the locations of the points in the map. While the original algorithm uses the Euclidean distance between objects as the base of its similarity metric, this can be changed as appropriate. A Riemannian variant is UMAP.[^6]

t-SNE is particularly effective for visualizing high-dimensional datasets, such as the Swiss Roll. It can help "unroll" the Swiss Roll data, revealing its underlying structure in a lower-dimensional space.

---

## References

[^1]: https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#:~:text=toolkit%2E-,Nonlinear,analysis%2E
[^2]: https://sites.math.washington.edu/~conroy/m381-general/lectureSlides/lecMDS01.pdf
[^3]: https://en.wikipedia.org/wiki/Multidimensional_scaling#Procedure
[^4]: https://encord.com/blog/dimentionality-reduction-techniques-machine-learning/
[^5]: Visualizing data using t-SNE, L.v.d. Maaten, G. Hinton. Journal of Machine Learning Research, Vol 9(Nov), pp. 2579—2605. 2008.
[^6]: https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding#:~:text=The%20t%2DSNE,UMAP%2E

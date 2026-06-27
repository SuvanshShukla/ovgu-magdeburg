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

---

## References

[^1]: https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#:~:text=toolkit%2E-,Nonlinear,analysis%2E
[^2]: https://sites.math.washington.edu/~conroy/m381-general/lectureSlides/lecMDS01.pdf
[^3]: https://en.wikipedia.org/wiki/Multidimensional_scaling#Procedure

# Recommender Systems Exercise 2

## Question 1

Euclidean Distance as a measure

$$
Euclidean\ distance\ formula = \sqrt{(x_1 - y_1)^2 + (x_2-y_2)^2}
$$

Calculated values:

for alpha & u1:  2.0
for alpha & u2:  2.0
for alpha & u3:  2.6457513110645907
for alpha & u4:  0.0

for beta & u1:  3.0
for beta & u2:  2.0
for beta & u3:  1.0
for beta & u4:  0.0

Cosine as a measure

$$
cosine(\theta) = \frac{A\cdot{B}}{||A||\cdot||B||}
$$

where,

- A.B is the dot product of vectors
- ||A|| & ||B|| are magnitudes

for alpha & u1:  0.9635883018483242
for alpha & u2:  0.9705817768262736
for alpha & u3:  0.7334770490389201
for alpha & u4:  0.7122123116119197

for beta & u1:  0.6454972243679028
for beta & u2:  0.49613893835683387
for beta & u3:  0.5222329678670935
for beta & u4:  0.0

Pearson Correlation Coefficient as a measure

$$
r = \frac{n(\sum{xy})- (\sum{x})(\sum{y})}{\sqrt{[n\sum{x^2}-(\sum{x})^2][n\sum{y^2}-(\sum{y})^2]}}
$$

where,

- n is no. of elements in one vector (both vectors should have same length)

for alpha & u1:  0.9045340337332909
for alpha & u2:  0.8017837257372732
for alpha & u3:  0.42640143271122083
for alpha & u4:  1.0

for beta & u1:  0
for beta & u2:  0
for beta & u3:  0
for beta & u4:  0

## Question 2

### 2 (a)

Calculated cosine similarity values are:

for u1 & u2:  1.0
for u1 & u3:  0.7559289460184544

The main drawback of this feature seems to be: it does not account for differences in rating scales.

### 2(b)

Calculated Pearson correlation similarity values are:

for u1 & u2:  1.0
for u1 & u3:  0.5773502691896258

The main drawback of this feature seems to be: that Pearson correlation only measures the linear relationship and penalizes a non-linear yet monotonic relationship.

### 2(c)

Calculated Euclidean distance values are:

for u1 & u2:  3.605551275463989
for u1 & u3:  2.23606797749979

Observations are:

The common drawback among all these similarity measures are: scaling issues

## Question 3

### 3(a)

Cosine similarity values for all pairs:

- for u4 & u1:  0.16035674514745463
- for u4 & u2:  0.3614031611621005
- for u4 & u3:  0.14907119849998599
- Min of all:  0.14907119849998599 (meaning u3 is least similar)

Now we would calculate the ratings for movies not yet rated by u4 (so 12 Monkeys, Fight Club, The Notebook)

$$
\hat{r_{iu}} = \frac{\sum_{z \in NN(u,k),r_{iz} \neq NULL}{r_{iz}.sim(u,z)}}{\sum_{z \in NN(u,k),r_{iz} \neq NULL}{sim(u,z)}}
$$

Now we estimate ratings for the previously unrated movies.

Movie: 12 Monkeys

$$
\begin{align}
\hat{r_{12\ Monkeys, u_4}} = \frac{(5*0.16)+(4*0.36)}{0.16+0.36} \\
\hat{r_{12\ Monkeys, u_4}} = \frac{2.24}{0.52} \\
\hat{r_{12\ Monkeys, u_4}} = 4.307
\end{align}
$$

Movie: Fight Club

$$
\begin{align}
\hat{r_{Fight\ Club, u_4}} = \frac{(3*0.16)+(4*0.36)}{0.16+0.36} \\
\hat{r_{Fight\ Club, u_4}} = \frac{1.92}{0.52} \\
\hat{r_{Fight\ Club, u_4}} = 3.692
\end{align}
$$

Movie: The Notebook

$$
\begin{align}
\hat{r_{The\ Notebook, u_4}} = \frac{(3*0.36)}{0.36} \\
\hat{r_{The\ Notebook, u_4}} = 3.0
\end{align}
$$

The top two recommendations are: **12 Monkeys & Fight Club**

### 3(b)

To take into account the users' biases/idiosyncrasies during the estimation we would use this formula:

$$
sim(u,z) = \frac{\sum_{y\in Y_u \cap Y_z}{(r_{yu}-\bar{r_u})(r_{yz}-\bar{r_z})}}
{\sqrt{\sum_{y \in Y_u \cap Y_z}{(r_{yu}-\bar{r_u})^2}}
\sqrt{\sum_{y \in Y_u \cap Y_z}{(r_{yz}-\bar{r_z})^2}}}
$$

where,

$$
\bar{r_u} = \frac{\sum_{Y_u \cap Y_z}{r_{yu}}}{|Y_u \cap Y_z|}
$$

I would say that top 2 recommendations stay the same, even when we account for user idiosyncrasies.
This is because 12 Monkeys is highly rated by all users (other than u4) and the runner up would still be Fight Club.

>[!QUESTION]
> What would be a logical/formal way to answer this? Like if it was asked in the exam what would I write as the answer?

## Question 4

Size of neighbourhood = 2

Pair-wise cosine similarity values are:

- for u4 & u1:  0.6205427141408237
- for u4 & u2:  0.7418318309487705
- for u4 & u3:  0.22522130823072542

This means the 2 nearest neighbours of are: u1 and u2.

Using them for calculating the recommended ratings:

Movie: 12 Monkeys

$$
\begin{align}
\hat{r_{12\ Monkeys, u_4}} = \frac{(5*0.62)+(2*0.74)}{0.62+0.74} \\
\hat{r_{12\ Monkeys, u_4}} = \frac{4.58}{1.36} \\
\hat{r_{12\ Monkeys, u_4}} = 3.36
\end{align}
$$

Movie: The Notebook

$$
\begin{align}
\hat{r_{The\ Notebook, u_4}} = \frac{(1*0.62)+(4*0.74)}{0.62+0.74} \\
\hat{r_{The\ Notebook, u_4}} = \frac{3.58}{1.36} \\
\hat{r_{The\ Notebook, u_4}} = 2.63
\end{align}
$$

The top-two recommendations are 12 Monkeys & The Notebook

## Question 5

Size of the neighbourhood: 2

Pair-wise cosine similarity values for item-based collaborative filtering are:

- for 12 Monkeys & Braveheart:  0.6599663291074443
- for 12 Monkeys & Titanic:  0.4913538149119954
- for 12 Monkeys & Fight Club:  0.7120653320005385
- for 12 Monkeys & The Notebook:  0.9561828874675149

- for The Notebook & 12 Monkeys:  0.9561828874675149
- for The Notebook & Braveheart:  0.4507489358552088
- for The Notebook & Titanic:  0.4969293465978882
- for The Notebook & Fight Club:  0.6670633740309423

This means the 2 nearest neighbours for 12 Monkeys is The Notebook & Fight Club, but since u4 hasn't rated The Notebook the two nearest neighbours are Fight Club and Braveheart

Similarly, the 2 nearest neighbours for The Notebook is Fight Club & Titanic.

Using these neighbours for calculating recommended ratings for u4, 12 Monkeys:

Rating for movie based on Fight Club

$$
\begin{align}
\hat{r_{12\ Monkeys, u_4}} = \frac{(5*0.71)+(1*0.65)}{0.71+0.65} \\
\hat{r_{12\ Monkeys, u_4}} = \frac{4.20}{1.36} \\
\hat{r_{12\ Monkeys, u_4}} = 3.08
\end{align}
$$

Using these neighbours for calculating recommended ratings for u4, The Notebook:

$$
\begin{align}
\hat{r_{The\ Notebook, u_4}} = \frac{(5*0.66)+(3*0.49)}{0.66+0.49} \\
\hat{r_{The\ Notebook, u_4}} = \frac{4.77}{1.15} \\
\hat{r_{The\ Notebook, u_4}} = 4.14
\end{align}
$$

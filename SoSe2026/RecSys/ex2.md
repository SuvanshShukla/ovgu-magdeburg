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

The main drawback of this feature seems to be: 

### 2(b) 

Calculated Pearson correlation similarity values are:

for u1 & u2:  1.0
for u1 & u3:  0.5773502691896258

The main drawback of this feature seems to be:

### 2(c)

Calculated Euclidean distance values are:

for u1 & u2:  3.605551275463989
for u1 & u3:  2.23606797749979

Observations are: 

The common drawback among all these similarity measures are:

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

So for 
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
\hat{r_{Fight\ Club, u_4}} = \frac{1.92}{0.52}
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

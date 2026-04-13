# Recommender Systems Exercise 1

## Question 1

### part (a)

A Recommender System is an engine that recommends the best item to each one/to me.

### part (b)

An *item* is the thing being recommended, while the *user* is the person operating the recommender or receiving the recommendation.

### part (c)

Common challenges in a recommender System are the following:

- constraint on products (e.g. what items are in stock)
- constraint on users (e.g. not allowed to recommend alcohol to kids)
- no. of items that can be recommended (e.g. requiring ranking to fit items in a webpage)

## Question 2

### 2 part (a)

$$
\hat{r}_{u3, 12\ Monkeys} = \frac{(5+4+3)}{3} = 12
$$

$$
\hat{r}_{u3, Braveheart} = \frac{(5+5+4)}{3} = 4.667
$$

$$
\hat{r}_{u3, Titanic} = \frac{(2+2)}{2} = 2
$$

The drawback of this approach is if a movie has fewer ratings, the guess would be affected.

### 2 part (b)

$$
\hat{r} = \frac{4 + 2}{2} = 3
$$

The main drawback of this approach is that each movie would receive the same rating.

### 2 part (c)

For '12 Monkeys', we need items rated by u3= 'Fight Club' & 'The Notebook'.
Users that have rated '12 Monkeys' and either 'Fight Club' or 'The Notebook' are: u2 & u4, so we only use their ratings

$$
\hat{r}_{u_3, 12\ Monkeys} = \frac{4 + 3}{2} = 3.5
$$

For 'Braveheart', we need items rated by u3= 'Fight Club' & 'The Notebook'.
Users that have rated 'Braveheart' and either 'Fight Club' or 'The Notebook' are: u2 & u4, so we only use their ratings

$$
\hat{r}_{u_3, Braveheart} = \frac{5 + 4}{2} = 4.5
$$

For 'Titanic', we need items rated by u3= 'Fight Club' & 'The Notebook'.
Users that have rated 'Titanic' and either 'Fight Club' or 'The Notebook' are: u2 & u4, so we only use their ratings

$$
\hat{r}_{u_3, Titanic} = \frac{2 + 2}{2} = 2
$$

The drawback of this approach is that this method doesn't account for similarity of the movies or users.

## Question 3

### 3 part (a)

$$
Total\ number\ of\ ratings = (15 \times 4) + (9 \times 3) = 87
$$

### 3 part (b)

$$
\begin{align}
\hat{r}_{u_3, 12\ Monkeys} = 2.6428 \\
\hat{r}_{Braveheart} = 3.25 \\
\hat{r}_{Titanic} = 2.727 \\
\hat{r}_{Fight\ Club} = 3.6 \\
\hat{r}_{The\ Notebook} = 4.142 \\
\hat{r}_{The\ Sixth\ Sense} = 2.375 \\
\hat{r}_{The\ Vow} = 2.666\\
\end{align}
$$

### 3 part (c)

Since the ratings for 'The Notebook', 'The Sixth Sense' and 'The Vow' have been moved to the test set. This means the system would have to recommend one of those three movies.

The movie that the system would recommend would be: "The Notebook".

### part (d)

$$
\begin{align}
Rating\ for\ u_{10}:  2.5 \\
Rating\ for\ u_{11}:  2.0 \\
Rating\ for\ u_{12}:  3.0 \\
Rating\ for\ u_{13}:  3.0 \\
Rating\ for\ u_{14}:  2.5 \\
Rating\ for\ u_{15}:  3.5 \\
\end{align}
$$

### part (e)

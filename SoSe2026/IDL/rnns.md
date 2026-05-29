# Notes regarding Recurrent Neural Networks

1. `h(t)=acth(Wh⋅[x(t),o(t−1)]+bh)h(t)=acth(Wh⋅[x(t),o(t−1)]+bh)`, in this equation does the bias not keep accumulating over time and cause issues? Because we added the bias once at t=0, then again at t=1 and so on, wouldn't it skew the results?

2. In the concatenation of output to the next time step's input, are we adding the values of the features, or are duplicate features being appended like copies of a column in a 1xN matrix? so vector -> [a, b, c] becomes [a, b, c, a, b, c] or [2a, 2b, 2c]?

3. 

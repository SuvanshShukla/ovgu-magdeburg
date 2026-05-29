# Notes regarding Recurrent Neural Networks

1. `h(t)=acth(Wh⋅[x(t),o(t−1)]+bh)h(t)=acth(Wh⋅[x(t),o(t−1)]+bh)`, in this equation does the bias not keep accumulating over time and cause issues? Because we added the bias once at t=0, then again at t=1 and so on, wouldn't it skew the results?

2. In the concatenation of output to the next time step's input, are we adding the values of the features, or are duplicate features being appended like copies of a column in a 1xN matrix? so vector -> [a, b, c] becomes [a, b, c, a, b, c] or [2a, 2b, 2c]?

3. In `Teacher Forcing`, since we're giving the desired output values directly to the next step does it mean that there would be no gradient? Since there is no error here, I would assume the network wouldn't learn anything until we stopped giving it the computed outputs. Would the gradient even be derived/calculated at all?

~~4. In the `hidden-to-hidden` connections architecture, what would happen if I add output-to-hidden connections too?~~

5. In bi-RNNs, for I understand that position x0 would be useful in calculating the next position o0 (this is being done in h1 forward part), but how does the future position x2 become useful in calculating o0 (as it is being propagated in h2 backward part)? It seems to me like we're using the future position of the car to calculate its past position?

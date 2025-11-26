# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 6 Task 6.3

### Part A

**Bias**: The bias of a model is its inherent error present when trying to fit an aribtrarily large training dataset. For example, if we use
a linear function to predict a quadratic relation then no matter how much data we put into training the model it will not get more accurate. Underfitting
and never getting things things right.

**Variance**: The variance of a model is its tendency to fit patterns in training data that may not actually be present in real life. For example,
a noisy U-shaped curve may be covered by a model that can make a U-shaped curve but it's wideness may vary (being narrow to being nearly flat). This
model too would fail to capture the ground truth, overfitting  to noise.

**Bias-Variance-Tradeoff**: Ideally we want our model to be able to easily recognize regularities in training data but still generalize on unseen data.
Bias and variance have a unique relationship. When the complexity of a model increases it is able to fit the training data better and thus see a reduction
in error. However, if the model complexity increases its variance also increases. Thus if we try to reduce the bias of a model we may inadvertantly increase
its variance and when we try to increase a model's variance we may inadvertantly decrease its bias.

### Part B

To estimate the bias a model has, we start out by taking different subsets of our original dataset. Then we train the model multiple times once on each subset
and calculate an average of our predicting function. This average is then compared with the average of the true function by calculating their Mean Square Error.
The final result of the MSE will be the bias present in out model.

It is mathematically represented like this:

$Bias(x) = E\Big[\hat{y}(x)\Big] - y(x)$

To estimate the variance a model may have, we again split out dataset into subsets and train our model on each of them. Then we take the average of all of these
individual predictions. Finally we subtract this average from each individual prediction made by the model to find out how far the average is from any one prediction
made by the model. This tells us that a prediction at a certain moment was this far from the average prediction, hence highlighting how much it "varied".

Variance is mathematically represented like this:

$Variance(x) = E\Big[(\hat{y}(x)-E\Big[\hat{y}(x)\Big])^2\Big]$

### Part C

Example 1: Comparison of football player statistics

- a model with a low degree of bias may misjudge certain days when the player plays well or worse than usual
- however the same model with a high degree of variance would be more accurate in capturing a player's overall performance over a period of time
- thus making it a better model for historical data trends

Example 2: Prediction of stock price.

- model with a high degree of bias may not always predict the price appreciation of a commodity to a high precision but it can accurately show a trend
- the same model with a low degree of variance may not have the enhanced precision but it would also have less deviation from unexpected market conditions
- thus making this model better for forecasting long-term prices


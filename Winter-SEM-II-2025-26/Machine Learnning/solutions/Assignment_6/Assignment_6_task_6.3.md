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

**Bias-Variance-Tradeoff**: Bias and variance have a unique relationship. When the complexity of a model increases it is able to fit the training data
better and thus see a reduction in error. However, if the model complexity increases its variance also increases. Thus if we try to reduce the bias of
a model we may inadvertantly increase its variance and when we try to increase a model's variance we may inadvertantly decrease its bias.


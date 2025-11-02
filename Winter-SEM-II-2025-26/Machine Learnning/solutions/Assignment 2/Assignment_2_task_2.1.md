# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

## Assignment 2 Task 2.1

**(a)**:

**Logistic Regression**: Supervised Learning (classification)
**Perception**: Supervised Learning (classification)
**ID3 Decision Tre**e: Supervised Learning (classification)
**K-Means**: Unsupervised Learning (clustering)

**(b)**:

According to [datacamp loss functions in machine learning](https://www.datacamp.com/tutorial/loss-function-in-machine-learning)  
Loss functions help us the approximate the accuracy of models. 
The way these work is basically by calculating the loss, i.e. error between the prediction and actual values.   
The official term for this numerical quantification is the prediction error.    
Then we compute the gradient of the loss function. (i.e. we graph it)   
This graph when compared to the graph of actual values would show us what the divergence is like.   
Using this divergence we can update the parameters of the model to minimize the loss.    

For classification we may apply 0-1 Loss Function because it is uniquely useful in figuring out exactly how many true positives, true negative, false positives and false negative we have classified.

For regression we apply the Sum-of-squared errors function because we have a set of input values that we can directly compare to a set of output values. This is
different from using 0-1 Loss as it doesn't tell us positives or negatives, rather how far our predicted values were from the actual values.

Other resources used:

[The clever machine: Cutting Your Losses: Loss Functions & the Sum of Squared Errors Loss](https://dustinstansbury.github.io/theclevermachine/cutting-your-losses)

[stack exchange: 0-1 Loss Function Explanation](https://stats.stackexchange.com/questions/284028/0-1-loss-function-explanation)


# Exercise 1 14/04/2025

## 1. What is meant by classification? Explain the two phases of classification.

Classification reflects what makes the instances in each class different from the instances in the other classes.   
There are two phases of classification learning and query phase.

## 2. Please provide a real-world example of a classification problem

A classification problem in the real world would be finding if a user is a bot or a human.

## 3. What is the learning set? Why is this set split into training and test sets?

A learining set is a collection of data used to fit the parameters of a model. The split is there to ensure unbiased evaluation so we don't train the model on the tests it self. This is also done to prevent "underfitting" and "overfitting". Random sampling of data may also lead to skewed results, with some data points having an unfairly large occurrence.

## 4. What is a target attribute? What properties must it have to be used for classification?

A target attribute respresents the desired outcome or target in a supervised learning algorithm. It must contain historical values used to train the model, they must have a simple data type and the target attribute should be categorical.

## 5. Please describe the variable type of each variables in Table 1. [numerical, categorical, ordinal] 

1. Home Owner - binary
2. Marital Status - categorical
3. Annual Income - numerical
4. Default Borrower - binary


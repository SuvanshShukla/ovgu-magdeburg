# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 2 Task 2.2

### Instance Space

An instance space is the space where our data is represented. (Not where the all possible values of it's dimension can be placed, i.e. they have to be actual values)

### Feature Space

A feature space is a multi-dimensional space in which all possible values of the features of a dataset are represented.

### Hypothesis Space

A hypothesis space is the space where our model instance are represented, i.e. the instances that our model has predicted and not the real instances.

### Version Space

Version space contains all the hypothesis that are consistent with the training data.

### Target Variable

A target variable is a variable that we are trying to predict using our machine learning model.

### Target Function

A function that helps derive variables to be as close to actual values is called the target function.

### Ambiguous models

In the given example of trying to separate two classes using a straight line, we may encounter ambiguity due to the following:

- some instances that are unhealthy may be misclassified as healthy
- some instances that are healthy may be misclassified as healthy
- multiple models (lines) may be able to perform this class division/separation, thus making it harder to identify which model is actually correct


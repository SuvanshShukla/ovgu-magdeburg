# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 8 Task 2

The function of an activation function of an output node is to give the final
result of the processed input. The purpose of the loss function is to determine
the difference between the predicted output processed by the node and the actual
value of the output. The output of the activation function is what is used as
the output term in the loss function. An example of this would be a Mean Square
Error function.

Mean Square Error:

$$
MSE = \frac{1}{n} \sum_{d} (t_d - o_d)^2
$$

Here you can see that the $o_d$ that is the output from the node is used as
in the calculation of MSE.

### Linear Activation Function

The linear activation function is a simple straight line function which is
directly proportional to the input, i.e. the weighted sum of neurons. It can
be used for regression. Where we try to draw a line over scattered points in
a 2D space. Here the error function would be euclidean distance, i.e. the
distance between a point on the line and the actual point in space.

Euclidean distance:

$$
Err = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$


# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 7 Task 7.1

A perceptron looks very much like a neuron from the human brain. It was originally designed to replicate  
the look of one as well. A perceptron basically works by taking multiple inputs from different input nodes,  
each input given a weight. The total values of all these inputs are calculated, this is known as the "weighted sum".  
There is also an element of bias that is added or subtracted to the weighted sum. This is done to position or offset  
of the decision boundary. This "weighted sum" is then checked against a threshold, if the value is greater than or  
equal to the threshold  the output of the perceptron is 1 (ON), if it is less than 0 the output is zero (OFF), this  
part of the perceptron is also called the activation function. Using these ON & OFF signals the perceptron classifies  
incoming input data. This output is then compared with the actual value and an error value is calculated. This error  
value is then used to correct or modify the weights of all the input nodes. Once the weights have been adjusted,  
the output is re-calculated and the error value is obtained. This process continues until all the training data has   
been used up. The goal here is to reduce training error down to zero for all training data.   


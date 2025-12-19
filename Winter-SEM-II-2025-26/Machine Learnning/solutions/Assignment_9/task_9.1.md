# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 9 Task 1

### Part A

One of the reasons why such algorithms like Naive Bayes might fail is because it assumes that there is no correlation between any of the instances in the dataset. We know this to not be true in real life, especially in the case of time-series where one instance is dependent on its predecessor.

Another case where a non-sequential data classification algorithm like K Nearest Neighbors may fail is that the proximity or similarity of data may not have any actual relevance. This would be especially obvious when trying to use KNN for text prediction, just because two words are closer to each other in proximity doesn't mean that one will always come after another.

### Part B

Feed-Forward Neural Networks process data in two ways: batch-wise or stochastically. In batch-wise processing the Neural Network doesn't discriminate among the inputs, and treats them all as discrete inputs with no connection. This means that if we tried to process text "The fruit basket" the neural network would process all the words but loose all the information that is present in their order. Now in stochastic (or one-by-one processing) the moment the network started to process "fruit" it would have forgotten all about "the" thus loosing critical information again. It's like the network has no memory.

Recurrent Neural Networks are able to retain things in memory and use it when processing succeeding data. So when a Recurrent neural network tries to process "fruit" it remembers that "the" came before it. This allows the recurrent neural network to capture the information inside the order of occurrence of instances.

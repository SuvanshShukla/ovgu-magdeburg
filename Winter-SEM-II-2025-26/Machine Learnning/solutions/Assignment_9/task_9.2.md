# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 9 Task 2

### Part A

Though KNN uses may use majority vote for labeling, there may be scenarios where the majority class may be misleading. One such scenario is when there is class imbalance in the dataset, leading to one class to be more numerous than others. This means that when trying to label the data point in question, even though it may be surrounded by instances from the more numerous class, it may actually belong to one of the less numerous (minority) classes. This would ultimately cause the instance to be mislabelled.

### Part B

The following are some alternatives to majority voting for classification in KNN:

1. Using weighted nearest neighbour classification: here we assign each instance a weight depending on its proximity to the instance we are trying to classify. The weight assigned to each point is inversely proportional to its distance from the instance we are trying to classify, i.e. the nearer a point is the greater its weight.
2. Time based emphasis: here each neighbour is given weights depending on how recently it was added to the dataset, so we give more recent instances greater weights than older instances when trying to classify an instance.

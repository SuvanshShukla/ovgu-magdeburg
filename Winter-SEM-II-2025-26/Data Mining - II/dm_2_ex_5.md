# Data Mining - II (WiSe 25/26)

## Notes

### VDFT

Referencing: [VFDT paper](./exercises/5/VFDT.pdf)

**anytime algorithm**: algo can be stopped anytime and return a valid result.[^1]

**constant memory**: doesn't store the entire data set only stores sufficient statistics.

- we have a lot of data to model complex phenomena but use inappropriately simple models, this is why we need efficient algos

Shortcomings of some online learning methods:

- sub-optimal early decisions, like splitting a node based on limited currently available data
- missing out on the "big picture" or globally optimum structure
- no backtracking to correct early mistakes
- efficient but structurally different from optimum model a batch learner would produce

- stream of data coming
- take initial data points and use them to choose root test
- once root attribute is chosen the succeeding examples will be passed down to the corresponding leaves
- these will then be used to choose the appropriate attributes at that level
- this will go on and on recursively

Choosing how many samples are required at every node uses statistical result known as Hoeffding bound[^2].
This is basically what it does:

- If we had infinite samples we'd use them all to figure out which attribute would give us the highest heuristic measure (e.g. informationgain or Gini index)
- But we don't so we use a subset of examples that we have encountered so far to calculate the heuristic measure
- This means we basically have to maximize the value of the heuristic measure by finding the best attribute to use as input, i.e. which attribute would give us the highest information gain or Gini index or whatever
- Now we can't be sure which attributes to choose so we take two that give us the highest heuristic measure scores
- This is where Hoeffding bound (ε) comes in, it says that if the difference between the heuristic measures between best attribute and second best attribute is greater than the Hoeffding bound, then it says it is likely that the best attribute is indeed the best.

Here's how you can think about it:

> ε is not compared directly to IG or any other heuristic measure.
> ε is a bound on uncertainty, not a “score.”
> 
> The comparison is:
> 
> “Is the gap between the best and second-best large enough that uncertainty cannot change the ranking?”

---

### Incremental Support Vector Machine Construction

- SVMs use hyper planes to separate data points
- data points closer to the decision boundary between two classes receive non-zero weights
- data points far away from the hyper plane don't participate in its specification and therefore receive zero weight
- support vectors are the data points closest to the hyper plane that define class boundaries

#### Incremental learning in SVMs

- partition data set in batches that fit into meory
- at each incremental step we already have a decision boundary (& weights) given by the support vectors we have encountered so far
- we keep only these support vectors and discard the non-participating data points
- now we only need to re-train on these new data points + the useful old ones
- since the number of support vectors are few compared to the total number of data points, this provides us with a compact representation of the data set
- This also means that the SVM generated using this incremental approach won't be too different from the one build with the complete data set

There are four different techniques for updating the model once new data is introduced:

1. **Error-driven technique**: The Error-driven technique, instead, keeps only the misclassified data. Given the model
$SVMt$ at time t, new data are loaded into memory and classified using $SVM_t$. If the data is misclassified, it is
kept, otherwise it is discarded. Once a given number $n_e$ of misclassified data is collected, the update of $SVM_t$ takes
place: the support vectors of $SVM_t$, together with the $n_e$ misclassified points, are used as training data to obtain the
new model $SVM_{t+1}$

Ques: does that mean the support vectors from $SVM_t$ are kept until $SVM_t$ is updated?

2. **Fixed-partition technique**: Partition training data into batches of fixed size. When a new batch of data is loaded into memeory
it is added to the current set of support vectors. This set is then used to train the new model. Support vectors from this are representation
of the data seen so far and they are kept in memory.

Ques: How long are they kept in memory? indefinately? or until they have no more weightage on the decision boundary?

3. **Exceeding-margin technique**: We already have an SVM at time t, we encounter new data points. These new data points are loaded into memory
Then we check if this new data point is closer to the already established decision boundary, on the wrong side of the pre-established decision
boundary or it is as far away as the established margin. If any of these conditions are fullfilled, we keep the point otherwise discard it. This is done until we reach a set number of points, at which time the SVM is updated using the initial Support vectors and the newly collected points.

Ques: How do we decide what $n_e$ to use?
---

[^2]: via [wikipedia](https://en.wikipedia.org/wiki/Hoeffding's_inequality), it basically says that there's an upper limit to how much
the sum of independent bound variables can deviate from an expected value of their sum.


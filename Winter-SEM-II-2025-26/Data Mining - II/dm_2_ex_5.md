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


---

[^2]: via [wikipedia](https://en.wikipedia.org/wiki/Hoeffding's_inequality), it basically says that there's an upper limit to how much
the sum of independent bound variables can deviate from an expected value of their sum.


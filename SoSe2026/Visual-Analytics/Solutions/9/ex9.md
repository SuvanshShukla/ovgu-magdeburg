# Visual Analytics Exercise 9

Author: Suvansh Shukla  
Matriculation: 256245

---

## Question 1

These are three techniques for visualizing decision trees[^1]:

1. Node-Link Diagrams: The traditional node-link diagram is enhanced through the use of varying node sizes to represent frequency or importance, and color-coding to distinguish between different types of decisions or outcomes. For example, a larger, red node could indicate a critical decision point in a financial decision tree, where a significant investment is at stake.

2. Enclosure Diagrams: These diagrams encapsulate nodes within geometric shapes, allowing for a hierarchical representation that is both space-efficient and visually intuitive. An enclosure diagram might be used to represent a company's organizational structure within a decision tree, with different departments enclosed in rectangles, nested within a larger rectangle representing the company.

3. Icicle Plots: Icicle plots display hierarchies in a more compact form, using contiguous rectangles to represent tree branches. This technique is particularly useful for visualizing pathways in a decision tree that has numerous levels, such as the steps involved in complex project management.. Node-Link Diagrams: The traditional node-link diagram is enhanced through the use of varying node sizes to represent frequency or importance, and color-coding to distinguish between different types of decisions or outcomes. For example, a larger, red node could indicate a critical decision point in a financial decision tree, where a significant investment is at stake.

4. Enclosure Diagrams: These diagrams encapsulate nodes within geometric shapes, allowing for a hierarchical representation that is both space-efficient and visually intuitive. An enclosure diagram might be used to represent a company's organizational structure within a decision tree, with different departments enclosed in rectangles, nested within a larger rectangle representing the company.

5. Icicle Plots: Icicle plots display hierarchies in a more compact form, using contiguous rectangles to represent tree branches. This technique is particularly useful for visualizing pathways in a decision tree that has numerous levels, such as the steps involved in complex project management.

## Question 2

There are a large number of approaches to decide which attribute to use for splitting in decision trees.
The choice has significant impact on the performance of the model.

According to the work done by [^2], this is a summary of different approaches:

- ID3 (information theory): uses information gain to evaluate the significance of attributes.
- C4.5 (information theory): this is an extension of the ID3 strategy and uses Gain Ratio to assess
  the importance of attributes and determine the optimal attributes for splitting.

- CART (distance-based splitting): uses Gini Index as an attribute evaluation metric to choose optimum splitting attributes
- PCC (statistical splitting): uses PCC as an impurity measure and selects the best attributes for splitting and the best splitting points

- Feature Weight based Decision Tree (Other):  FWDT decision tree approach based on the feature weight principle, where the weights of features are determined by employing the ReliefF algorithm

There are multiple stopping criteria for building trees, some of which are the following:

1. When the decision trees reaches 100% purity, meaning all examples now belong to the same class
2. When a pre-defined tree depth has been reached
3. When the size of the data in the node is below a threshold
4. When the error or information gain of objects in nodes have dropped below a threshold

## Question 4

The disadvantages of decision trees include[^3]:

1. Decision-tree learners can create over-complex trees that do not generalize the data well. This is called overfitting. Mechanisms such as pruning, setting the minimum number of samples required at a leaf node or setting the maximum depth of the tree are necessary to avoid this problem.
2. Decision trees can be unstable because small variations in the data might result in a completely different tree being generated. This problem is mitigated by using decision trees within an ensemble.
3. Predictions of decision trees are neither smooth nor continuous, but piecewise constant approximations as seen in the above figure. Therefore, they are not good at extrapolation.
4. The problem of learning an optimal decision tree is known to be NP-complete under several aspects of optimality and even for simple concepts. Consequently, practical decision-tree learning algorithms are based on heuristic algorithms such as the greedy algorithm where locally optimal decisions are made at each node. Such algorithms cannot guarantee to return the globally optimal decision tree. This can be mitigated by training multiple trees in an ensemble learner, where the features and samples are randomly sampled with replacement.
5. There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problems.
6. Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.

## Question 5

The following may be reasons for correlations in regression models:

- genuine relation between attributes, for example high humidity may indicate rain
- presence of a third attribute affecting two others, for example high demand of oil can increase its price as well as reduce its availability
- correlation may be the result of random chance, they may be increasing/decreasing by coincidence, an interesting example is Muenster cheese consumption correlating with the distance between Saturn and the sun.



---

## References

[^1]:<https://fastercapital.com/content/Visualization-Techniques--Decision-Trees--Visualizing-Pathways-to-Choices.html?__cf_chl_f_tk=ObkP7tkmKdInyhq02qavtj5LG7TMczm2108CwQWf_7I-1783144424-1.0.1.1-RBgnsVCwJf9dnUf66jG7BItp6KPGoaXTt.L81j36luk>
[^2]: https://journals.sagepub.com/doi/10.1177/17483026231198181
[^3]: https://scikit-learn.org/stable/modules/tree.html#:~:text=The%20disadvantages%20of%20decision%20trees%20include

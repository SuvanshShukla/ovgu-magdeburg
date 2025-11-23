# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 5 Task 5.1

By carefully looking at the 6 validation instances provided, we can see that all yes values for `Forgot Pruning` result in No. So there is no need to check for any additional attributes.

Next we see that for No values for `Forgot Pruning` we just need to check `Preciseness`.  

In `Preciseness` we see that for `medium` we get no, but for `low` & `high` we get yes.

So the final tree should look like the following:

![reduced-error pruning on decision tree](reduced_error_pruning_decision_tree_ML_assgn_5.1.png)


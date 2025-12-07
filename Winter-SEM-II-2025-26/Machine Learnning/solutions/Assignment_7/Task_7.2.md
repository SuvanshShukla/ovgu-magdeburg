# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 7 Task 7.2

threshold expression:

$$
w_0 + w_1x_1 + w_2x_2 \gt 0
$$

Initialized weight values:
$w_0=0$, $w_1=0$, $w_2=0$

Table of data:

| $x_1$ | $x_2$ | $t$ (target) |
| ----- | ----- | ------------ |
|   1   |   0   |  0           |
|   3   |   -1  |  1           |
|   2   |   2   |  0           |
|   4   |   4   |  0           |
|   1   |   -2  |  1           |

I need to apply the perceptron rule in batch with $\eta = 0.1$ in batch mode.

Perceptron rule:

$$
w_i \leftarrow w_i + \eta \sum_{d} (t_d - o_d)x_{i,d}
$$

|d|x1​|x2​|t|Net Input (w0​+w1​x1​+w2​x2​)|Output (o)|Error (E=t−o)|Δw0​ (E⋅1)|Δw1​ (E⋅x1​)|Δw2​ (E⋅x2​)|
|-|---|---|-|-----------------------------|----------|-------------|----------|-----------|------------|
|1|1|0|0|0(1)+0(0)+0(0)=0|0|0−0=0|0⋅1=0|0⋅1=0|0⋅0=0|
|2|3|-1|1|0(1)+0(3)+0(−1)=0|0|1−0=1|1⋅1=1|1⋅3=3|1⋅(−1)=−1|
|3|2|2|0|0(1)+0(2)+0(2)=0|0|0−0=0|0⋅1=0|0⋅2=0|0⋅2=0|
|4|4|4|0|0(1)+0(4)+0(4)=0|0|0−0=0|0⋅1=0|0⋅4=0|0⋅4=0|
|5|1|-2|1|0(1)+0(1)+0(−2)=0|0|1−0=1|1⋅1=1|1⋅1=1|1⋅(−2)=−2|
|SUM|||||||∑Δw0​=2|∑Δw1​=4|∑Δw2​=−3|

Update Weights (End of Iteration 1):

Apply the update rule wi​←wi​+η∑Δwi​ with η=0.1:

```
w0​=0+0.1⋅(2)=0.2
w1​=0+0.1⋅(4)=0.4
w2​=0+0.1⋅(−3)=−0.3
```

Weights from Iteration 1: $w0​=0.2,w1​=0.4,w2​=−0.3$

We repeat the process using these new weights

|d|x1​|x2​|t|Net Input (0.2+0.4x1​−0.3x2​)|Output (o)|Error (E=t−o)|Δw0​ (E⋅1)|Δw1​ (E⋅x1​)|Δw2​ (E⋅x2​)|
|-|---|---|-|-----------------------------|----------|-------------|----------|-----------|------------|
|1|1|0|0|0.2+0.4(1)−0.3(0)=0.6|1|0−1=−1|−1⋅1=−1|−1⋅1=−1|−1⋅0=0|
|2|3|-1|1|0.2+0.4(3)−0.3(−1)=0.2+1.2+0.3=1.7|1|1−1=0|0⋅1=0|0⋅3=0|0⋅(−1)=0|
|3|2|2|0|0.2+0.4(2)−0.3(2)=0.2+0.8−0.6=0.4|1|0−1=−1|−1⋅1=−1|−1⋅2=−2|−1⋅2=−2|
|4|4|4|0|0.2+0.4(4)−0.3(4)=0.2+1.6−1.2=0.6|1|0−1=−1|−1⋅1=−1|−1⋅4=−4|−1⋅4=−4|
|5|1|-2|1|0.2+0.4(1)−0.3(−2)=0.2+0.4+0.6=1.2|1|1−1=0|0⋅1=0|0⋅1=0|0⋅(−2)=0|
|SUM|||||||∑Δw0​=−3|∑Δw1​=−7|∑Δw2​=−6|

Final Weight Update (End of Iteration 2)

Apply the update rule to the weights from Iteration 1:

```
w0​=0.2+0.1⋅(−3)=0.2−0.3=−0.1
w1​=0.4+0.1⋅(−7)=0.4−0.7=−0.3
w2​=−0.3+0.1⋅(−6)=−0.3−0.6=−0.9
```

Final Perceptron

The final perceptron weights after two updates (two iterations) are:
$w_0=−0.1,w_1​=−0.3,w_2​=−0.9$

The final perceptron uses the decision boundary (threshold expression):
$$
−0.1−0.3x_1−0.9x_2​>0
$$

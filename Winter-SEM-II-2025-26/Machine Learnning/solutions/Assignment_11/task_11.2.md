# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 11 Task 2

Given:

- 5 Points: A(1, 2), B(3, 2), C(5, 2), D(1, 1) and E(5, 1)
- 2 Centroids: C1(1,0) and C2(5,6)

### Part A ($\eta = 0.2$) & 2 iterations

This is the equation for learning vector quantization:

$$
\vec{r}^{(new)} = \vec{r}^{(old)} + \eta \sum_{winner(\vec{p})=\vec{r}^{(old)}} (\vec{p} - \vec{r}^{(old)})
$$

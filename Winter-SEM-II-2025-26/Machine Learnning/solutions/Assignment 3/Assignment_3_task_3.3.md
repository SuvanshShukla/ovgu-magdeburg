# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 3 Task 3.3

The given training data is:

| day | outlook | temperature | humidity | wind | play tennis |
| --- | ------- | ----------- | -------- | ---- | ----------- |
| 1 | rain | mild | high | strong | no |
| 2 | overcast | hot | normal | weak | yes |
| 3 | overcast | mild | high | strong | yes |
| 4 | sunny | mild | normal | strong | yes |
| 5 | rain | mild | normal | weak | yes |
| 6 | sunny | cool | normal | weak | yes |
| 7 | sunny | mild | high | weak | no |
| 8 | overcast | cool | normal | strong | yes |
| 9 | rain | cool | normal | strong | no |
| 10 | rain | cool | normal | weak | yes |

We'll need to calculate the possibility for every feature according to both classifications of YES and NO.

### For the first instance i1 = (sunny, cool, high, strong)

For Class = YES

P(yes)=7/10=0,7  
P(outlook=sunny|yes)=2/7≈0.2857  
P(temperature=cool|yes)=3/7≈0.4286  
P(humidity=high|yes)=1/7≈0.1429  
P(wind=strong|yes)=3/7≈0.4286  

For Class = NO

P(no)=3/10=0.3  
P(outlook=sunny|no)=1/3≈0.3333  
P(temperature=cool|no)=1/3≈0.3333  
P(humidity=high|no)=2/3≈0.6667  
P(wind=strong|no)=2/3≈0.6667  

For yes we have  

P(yes|i1) = 0.7×P(sunny|yes)×P(cool|yes)×P(high|yes)×P(strong|yes)  
P(yes|i1) = 0.7 X 0.2857 X 0.4286 X 0.1429 X 0.4286  
P(yes|i1) = 0.0052  

For no we have

P(no|i1) = 0.3×P(sunny|no)×P(cool|no)×P(high|no)×P(strong|no)
P(no|i1) = 0.3 X 0.333 X 0.333 X 0.666 X 0.666
P(no|i1) = 0.0148

Now we normalize for proper probabilities:

P(yes|i) = 0.0052/(0.0052+0.0248) = 0.2616  
P(no|i1) = 0.0148/(0.0052+0.0248) = 0.7384  

**This means that No has a higher chance of occurring**

### For the second instance i2 = (overcast, mild, normal, weak)

For yes,

P(yes|i2) = 0.7XP(overcast|yes)×P(mild|yes)×P(normal|yes)×P(weak|yes)
P(yes|i2) = 0.7 X 0.4286 X 0.4286 X 0.8571 X 0.5714
P(yes|i2) = 0.06297

For no,

P(no|i2) = 0.3XP(overcast|no)...

But since there is no example for P(overcast|no) it's probability is 0.  
Therefore the entire probability of P(no|i2) is 0.  
**This means that the probability for P(yes|i2) is 1, i.e. it is certain**


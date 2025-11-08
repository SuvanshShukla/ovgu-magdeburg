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

For Class = YES

P(outlook=overcast|yes)=3/7≈0.4286
P(outlook=sunny|yes)=2/7≈0.2857 --
P(outlook=rain|yes)=2/7≈0.2857
P(temperature=cool|yes)=3/7≈0.4286 --  
P(temperature=mild|yes)=3/7≈0.4286
P(temperature=hot|yes)=1/7≈0.1429
P(humidity=normal|yes)=6/7≈0.8571
P(humidity=high|yes)=1/7≈0.1429 --  
P(wind=weak|yes)=4/7≈0.5714
P(wind=strong|yes)=3/7≈0.4286 --  

For Class = NO

P(outlook=rain|no)=2/3≈0.6667
P(outlook=sunny|no)=1/3≈0.3333
(no overcast examples in class=no → probability 0)
P(temperature=mild|no)=2/3≈0.6667
P(temperature=cool|no)=1/3≈0.3333
P(temperature=hot|no)=0
P(humidity=high|no)=2/3≈0.6667
P(humidity=normal|no)=1/3≈0.3333
P(wind=strong|no)=2/3≈0.6667
P(wind=weak|no)=1/3≈0.3333


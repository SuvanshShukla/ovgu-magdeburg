# Exercise 2

## 1. A patient goes to see a doctor. Suppose the doctor performs a test with 90% reliability, i.e., 99% of people who are sick test positive and 99% of the healthy people test negative. The doctor knows that only 1% of the people in the country are sick. If a patient has tested positive, what is the probability he is sick?

These are all the variables
P(A) = person is sick = 0.01    
P(B) = person is not sick = 0.99    
P(C|A) = test is positive if the person is sick = 0.99  
P(C|B) = test is positive if the person is not sick = 1 - P(C|A) = 1 - 0.99 = 0.01  

what we are looking for: person tested positive and is sick.    
Which is `P(A|C)`

using Bayes Theorem:

```
P(A|C) = ( P(C|A) * P(A) ) / P(C)
```

So we need to calculate the total probability that the person has tested positive `P(C)`    
Which is as follows,

```
P(C) = P(C|A) * P(A) + P(C|B) * P(B)
```

Plugging in the values we get,

```
P(C) = (0.99) * (0.01) + (0.01) * (0.99) = 0.0198
```

Taking the value of `P(C)` and plugging it in Bayes Theorem, we get:

```
P(A|C) = ( (0.99) * (0.01) ) / (0.0198)

P(A|C) = 0.5
```

This means there is only a 50% chance that a person who has tested positive is sick.

> [!Note]
> Look at an additional question in the book. Section `5.3.1 Bayes Theorem`.
> It will help you understand how to apply Bayes Theorem.

## 2. How does a Naïve Bayes classifier work? Explain using the underlying formula. Why is it “naive”?



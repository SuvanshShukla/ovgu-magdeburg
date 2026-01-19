# Data Mining - II (WiSe 25/26)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Question 1

### Part A

Exponential smoothing is a forecasting technique used in time series analysis that assigns exponentially decreasing weights to past observations, giving more importance to recent data. It is effective for predicting future trends based on historical data and can be adjusted to account for trends and seasonality.

It is called "exponential" because weights for older instances drop exponentially.

### Part B

Advantages:

- Mathematically simple, flexible solution
- Can be computed incrementally

Disadvantages:

- Makes only one future prediction, not appropriate for the far future.
- The parameter α is difficult to estimate.
- If there is a (linear) trend, SES may under/overestimate the actual value

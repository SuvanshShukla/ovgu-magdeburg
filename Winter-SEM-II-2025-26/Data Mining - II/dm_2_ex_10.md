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

### Part C

α sets how much the weights of the instance should be. If α is close to 1 then our estimate becomes the value we have just seen. If α is 0 then we ignore all new data, the forecast becomes a constant and we are left with a completely straight line.

## Question 2

## Question 3

### Part A

Simple Exponential smoothing is not suitable for time series with a trend because it may under/overestimate the actual value.

### Part B

The two components modeled by Holt's Exponential Smoothing are: Trend and Level

### Part C

- Level: $$L_t = \alpha z_t + (1-\alpha)(L_{t-1} + T_{t-1})$$
- Trend: $$T_t = \beta (L_t - L_{t-1}) + (1-\beta) T_{t-1}$$
- Forecast: $$ \widehat{z_{t+h}} = L_t + hT_t$$

## Question 4

### Part A

Holt-Winters model has the additional component of $\gamma$ or seasonality.

### Part B/C

A situation where Holt-Winters model is preferred over Holt's method is when the time series in question has seasonality.

Holt-Winters model can incorporate seasonality in both multiplicative and additive ways.


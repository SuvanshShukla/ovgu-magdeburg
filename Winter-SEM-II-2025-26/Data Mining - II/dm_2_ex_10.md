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

## Question 5

### Part A

In ARIMA:

- p: captures autocorrelation
- q: captures the error
- d: captures the trend

### Part B

Seasonal ARIMA model uses differencing at a lag equal to the number of seasons to remove additive seasonal effecs.

The seasonal ARIMA model includes autoregressive and moving average terms at a lag s.

### Part C

The notation: `SARIMA(p,d,q)(P,D,Q)s`, has two different parts.

`(p,d,q)`: which represents the Non-seasonal part of the model.

`(P,D,Q)s`: which represents the seasonal part of the model.

Note: `s`: The number of periods per season (e.g., s=12 for monthly data, s=4 for quarterly data)

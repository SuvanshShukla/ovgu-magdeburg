# Data Mining - II (WiSe 25/26)

## Q1

### Part A

**Trend**: A time series has a trend if and only if there is a long-term increase or decrease in the observed values, following an arbitrary increase (or decrease) pattern

**Seasonality**: a time series has seasonality if and only if next to a trend, there are also patterns that repeat in relatively constant intervals (a.k.a cyclic patterns)

**Residue**: a time series has residue if a component that captures the short term fluctuations - which are not systematic and cannot be predicted.

**Autocorrelation**: refers to the correlation of a series with its own past (lagged) values. It helps identify the dynamics of the data (e.g., how strongly past values influence current ones).

Explanation with sample graph:

![Time series graph of trade](./TimeSeriesTrade.png)

In this graph we can see that the overall **trend** is upwards (increasing), while the **seasonality** is the recurring peaks or highs encountered every 12 months. The **residue** is the unpredictable move upward of points as time goes on. The **autocorrelation** is how much higher the trade value is than it was 1 month, 2 month or even 12 months ago.

### Part B

The decomposition of a time series may be additive or multiplicative.

The decomposition is additive if all components use the same quantity as the time series at a timepoint.

$$Z_t = T_t + S_t + R_t$$

Where,

- Z is the time series
- T is the trend
- S is the seasonality
- R is the residue

The decomposition is multiplicative if the trend of the time series uses the same quantity unit as the time series and the other two components (seasonality and residue) are modifiers over the trend component.

$$Z_t = T_t \times S_t \times R_t$$

Where,

- Z is the time series
- T is the trend
- S is the seasonality
- R is the residue

## Q2

### Part (A)

Stationarity is when the statistical characteristics of the data distribution doesn't change, like if the mean, variance etc. don't change then the data is stationary. If mean, variance & other statistical data do change then there is no Stationarity.

The Augmented Dicky Fuller test is a statistical test that can be used to determine if a time series is stationary. The null hypothesis for this test states that the time series is stationary by default. If the p-value < 0.05 then we reject the null hypothesis and infer that the time series is stationary.

### Part (B)



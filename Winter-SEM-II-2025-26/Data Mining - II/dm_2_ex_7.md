# Data Mining - II (WiSe 25/26)

## Temporal mapping function

A Temporal mapping function is a function that takes as input a $x_k$ or a $y_k$ and returns the time $t$ that it becomes available.

## Verification latency

The latency until Verification can be seen as a delay. If for some labels the delay is infinite, then the stream is only partially labeled.

There are four cases of Verification delay:

1. Immediate and fully labelled: where the label for the instances arrives alongside the next instance and no labels are missed

$$ \forall x \in X, \forall y \in Y : T(y) - T(x) = 1 $$ $$ \forall k : v(x_k, y_k) = 1 $$

2. Delayed and fully labelled: where the label for the instance doesn't arrive alongside the next instance but takes some finite amount of time. No labels are missed.

$$ \forall x \in X, \forall y \in Y : T(y) - T(x) = D $$ $$ \forall k  \exists D_k \in \mathbb{Z_+} \ \infty : v(x_k, y_k) = D_k $$

3. Immediate and partially labelled: where the label for the instance either arrives alongside the next instance or it never arrives.

$$ \forall k : V(x_k, y_k) \in {x, \infty} $$

4. Delayed and partially labelled: where the label can arrive at any time or never arrive at all

$$ \forall k : V(x_k, y_k) \in \mathbb{Z_+} \wedge (\exists m, n : V(x_m, y_m) = \infty, V(x_n, y_n) \neq \infty) $$


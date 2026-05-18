# Intro To Deep Learning Exercise 4 notes

## `reshape` function

W3C Link -> [numpy reshape](https://www.w3schools.com/python/numpy/numpy_array_reshape.asp#gsc.tab=0a)
```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
```

## `arange` function

Simply creates a new numpy array with given params.

LINK -> [numpy.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

```py
import numpy as np
np.arange(3)
np.arange(3.0)
np.arange(3,7)
np.arange(3,7,2)
```


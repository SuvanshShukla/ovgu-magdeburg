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

## What we want to do

1. Establish a baseline (what you already have)
2. Add Adam → measure
3. Add LR scheduler → measure
4. Add augmentation → measure
5. Add Dropout/BatchNorm → measure

## Questions

1. Which batch norm should be used here? 1d or 2d?
2. How could we parallelize this model to make it train faster? Considering that I don't have a GPU, is this even worth considering or would it take too much effort?
3. Is adding ColorJitter, negatively affecting the performance too much?
4. Does implementing early stopping first, adversely affect the training? Or is it done last, only so that other experiments' effects are more clearly visible (in plots etc...)?
5. Is there some heuristic/rule-of-thumb using which I can better estimate values for certain params (e.g. label_smoothing value, drop out p value, scheduler's factor & patience, etc...)? Maybe the fact that we're using images tell us something?
6. Is adding & accounting for so many new params worth it? Don't we now have to handle the added complexity and test by mixing and matching things? (Could be that I'm seriously misunderstanding something here)
7. Is there any concrete relation between increase in number of epochs and increase in accuracy? Like we increased number of epochs by 50% then it should equate to a 50% increase in accuracy? Would this ever even be possible?
8. Is there any indicator that tells us if we should train a model for longer? Or is is only deducible by seeing the rate of improvement in accuracy?

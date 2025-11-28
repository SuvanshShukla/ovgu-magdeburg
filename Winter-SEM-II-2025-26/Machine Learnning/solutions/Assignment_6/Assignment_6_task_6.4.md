# Machine Learning (WiSe 2025/2026)

Author: Suvansh Shukla  
Matriculation No. 256245

---

## Assignment 6 Task 6.4

Cross validation is a way of splitting your entire dataset into training and validation data. It helps us form
a better picture of which model has the least amount of error. Sometimes we may wish to re-train the model after
testing, this second cycle of training is would be done on the entire dataset. This step has the following advantages:

1. Maximizing data utilization: helps the model find even more potential patterns and nuances possibly leading to a better final model
2. Helps finalize hyperparameters: cross-validation helps finalize the best hyperparameters (e.g. regularization strength, number of layers, learning rate etc...) Once these are fixed we re-train the model on the entire dataset.
3. The models trained on cross-validation are intermediates and not quite ready for production. This is because keeping all things equal, a model trained on more data will have better performance.

Though this does mean that even if we train the model on all the data after fixing hyperparameters, this tuning would have been done for 70% of the data rather than all of it, and there is no guarantee that the hyperparameters selected for 70% of the data will be equally effective for 100% of the data, this is why we still have "data wastage".

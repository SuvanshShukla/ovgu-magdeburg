# Data Mining - II (WiSe 25/26)

## 1 Hypothesis tests

Hypothesis tests is a form of testing done to use statistics to make a conclusion on a population of data inorder to
refute or confirm specific assumptions made about the data.

A null hypothesis is a hypothesis that assumes there to be no significant difference, no significant effect, or no significant relationship
between two objects being tested.

A significance level helps us set a threshold to determine if we should accept or reject the null hypothesis. In other word, it helps us determine how strong the evidence is that the null hypothesis is true based on the evidence if the hypothesis also happens to be true in reality.

The Chi-square test is such a statistical test that helps us determine if there is a significant association between two categorical variables, i.e. if they are independent in influencing the test statistic.

## 2 Test Statistic

A test statistic is a number calculated from sample data that helps us determine if the null hypothesis that we have assumed is valid or not.
It is usually a single summarized numerical value that can be used to perform the hypothesis test.

Examples of test statistics are:

- Chi-square statistic (testing for independence b/w two categorical values)
- z-statistic/t-statistic (comparing the means of two populations)
- F-statistic (comparing variances of three or more groups)

## 4 Three categories of semi supervised learning

Self training: We have a set of labelled and unlabeled instances in our dataset. We try to label an unlabeled instance with a classifier
that is trained on a subset of labelled data. Then we see its confidence, if the confidence is higher than a threshold we put the sample into
the labelled dataset. This is done until we hit convergence.

Co-training: Here we have two independent classifiers, each delivers predicted labels for which they are most confident. But these classifiers don't work as an ensemble, rather they exchange data. If one classifier is very confident in the prediction it has made for an unlabeled instance, it takes over the label & tells the second one to train on it. One of the constraints here is that the views of both classifiers must see the same data & they shouldn't deviate a lot in behavior. For example, they shouldn't disagree too much.

Learn by disagreement: There is a possibility that we may have more than 2 learners, in which case we train them to learn by disagreement. We try to enforce diversity among learners by giving each learner a different view of the data or simulate multiple views. Then have them each make a prediction on unlabelled instances. Then we take the predicted labels they diagree on & propagate the label of the most confident classifier to the rest of the classifers and train them on it.

## 5 Compare test-then-train, prequential evaluation and periodic holdout

test-then-train: each labeled instance is first used for testing, then for training. Each prediction affects future predictions.

prequential evaluation: test-then-train on a sliding window or with a fading factor. The impact of past predictions is gradually forgotten.

periodic holdout evaluation: some labeled instances are reserved for testing only, e.g. by using one batch for training and the next for testing. The holdout instances are 'wasted', i.e. not used for training.

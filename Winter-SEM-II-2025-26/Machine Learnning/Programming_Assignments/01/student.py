import argparse
import numpy as np


def load_data(filepath):
    # using , (comma) as delimiter becasuse we are using .csv files
    raw_data = np.loadtxt(filepath, delimiter=',')
    x = raw_data[:, :-1]
    y = raw_data[:, -1]

    # we add a row of 1s to accomodate bias term
    x_with_bias = np.column_stack([np.ones(x.shape[0]), x])

    return x_with_bias, y


def calculate_predictions(x, w):
    return np.dot(x, w)


def calculate_SSE(x, y, w):
    pred = calculate_predictions(x, w)
    err = y - pred
    sse = np.sum(err ** 2)
    return sse


def grad_descent(x_train, y_train, x_test, y_test, eta, threshold):
    # initialize weights to 0
    n_feats = x_train.shape[1]
    w = np.zeros(n_feats)

    iter = 0
    prev_sse = float('inf')

    while True:
        current_sse = calculate_SSE(x_train, y_train, w)

        weights = ','.join(map(str, w))
        print(f"{iter},{weights},{current_sse}")

        if iter > 0:
            err_change = abs(prev_sse - current_sse)
            if err_change < threshold:
                break

        prev_sse = current_sse
        predictions = calculate_predictions(x_train, w)
        errs = y_train - predictions
        gradient = np.dot(x_train.T, errs)
        w = w + eta * gradient

        iter = iter + 1

    test_sse = calculate_SSE(x_test, y_test, w)
    print(test_sse)


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Linear Regression Gradient Descent')
    parser.add_argument('--data', type=str, required=True)
    parser.add_argument('--eta', type=float, required=True)
    parser.add_argument('--threshold', type=float, required=True)

    args = parser.parse_args()

    train_file = f"{args.data}_train.csv"
    test_file = f"{args.data}_test.csv"

    x_train, y_train = load_data(train_file)
    x_test, y_test = load_data(test_file)

    grad_descent(x_train, y_train, x_test, y_test, args.eta, args.threshold)

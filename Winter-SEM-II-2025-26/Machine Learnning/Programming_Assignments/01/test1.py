import argparse
import numpy as np

def load_data(filepath):
    """Load CSV data from file."""
    data = np.loadtxt(filepath, delimiter=',')
    X = data[:, :-1]  # All columns except last
    y = data[:, -1]   # Last column
    
    # Add bias term (x0 = 1) as first column
    X_with_bias = np.column_stack([np.ones(X.shape[0]), X])
    
    return X_with_bias, y

def compute_predictions(X, w):
    """Compute predictions f(x) = w^T * x."""
    return np.dot(X, w)

def compute_sse(X, y, w):
    """Compute sum of squared errors."""
    predictions = compute_predictions(X, w)
    errors = y - predictions
    sse = np.sum(errors ** 2)
    return sse

def gradient_descent(X_train, y_train, X_test, y_test, eta, threshold):
    """
    Perform batch gradient descent for linear regression.
    
    Parameters:
    - X_train: Training data with bias term (N x (d+1))
    - y_train: Training labels (N,)
    - X_test: Test data with bias term
    - y_test: Test labels
    - eta: Learning rate
    - threshold: Convergence threshold for error change
    """
    # Initialize weights to zero
    n_features = X_train.shape[1]
    w = np.zeros(n_features)
    
    iteration = 0
    prev_sse = float('inf')
    
    while True:
        # Compute current predictions
        predictions = compute_predictions(X_train, w)
        
        # Compute errors: (y_i - f(x_i))
        errors = y_train - predictions
        
        # Compute gradient: sum over all data points of x_i * (y_i - f(x_i))
        gradient = np.dot(X_train.T, errors)
        
        # Update weights: w <- w + eta * gradient
        w = w + eta * gradient
        
        # Compute sum of squared errors on training set
        current_sse = compute_sse(X_train, y_train, w)
        
        # Print current iteration results
        weights_str = ','.join(map(str, w))
        print(f"{iteration},{weights_str},{current_sse}")
        
        # Check convergence
        error_change = abs(prev_sse - current_sse)
        if error_change < threshold:
            break
        
        prev_sse = current_sse
        iteration += 1
    
    # Compute and print test set error
    test_sse = compute_sse(X_test, y_test, w)
    print(test_sse)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Batch Linear Regression with Gradient Descent')
    parser.add_argument('--data', type=str, required=True, 
                        help='Base name of data files (e.g., random1)')
    parser.add_argument('--eta', type=float, required=True, 
                        help='Learning rate')
    parser.add_argument('--threshold', type=float, required=True, 
                        help='Convergence threshold for error change')
    
    args = parser.parse_args()
    
    # Construct file paths
    train_file = f"{args.data}_train.csv"
    test_file = f"{args.data}_test.csv"
    
    # Load data
    X_train, y_train = load_data(train_file)
    X_test, y_test = load_data(test_file)
    
    # Run gradient descent
    gradient_descent(X_train, y_train, X_test, y_test, args.eta, args.threshold)

if __name__ == "__main__":
    main()
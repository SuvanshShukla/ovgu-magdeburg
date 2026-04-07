import argparse
import csv
import math
import sys

def load_data(filename):
    """
    Reads the CSV file.
    Returns a list of tuples: (class_label, [attr1, attr2])
    """
    dataset = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row: continue
                # First column is class (A or B)
                label = row[0].strip()
                # Remaining columns are attributes (floats)
                attributes = [float(x) for x in row[1:]]
                dataset.append((label, attributes))
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    return dataset

def calculate_parameters(values):
    """
    Calculates Mean and Sample Variance (1/(N-1)) for a list of values.
    """
    n = len(values)
    if n == 0:
        return 0.0, 0.0
    
    # Mean
    mu = sum(values) / n
    
    # Sample Variance (formula given: 1/(n-1) * sum((x - mu)^2))
    if n > 1:
        variance = sum([(x - mu)**2 for x in values]) / (n - 1)
    else:
        variance = 0.0 # Edge case for single sample
        
    return mu, variance

def gaussian_probability(x, mu, var):
    """
    Calculates P(x|c) using the Gaussian PDF formula provided.
    """
    if var == 0:
        return 0 # Avoid division by zero
    
    exponent = math.exp(-((x - mu)**2) / (2 * var))
    denominator = math.sqrt(2 * math.pi * var)
    return (1 / denominator) * exponent

def predict(attributes, model_params, priors, classes):
    """
    Predicts the class for a given instance.
    Returns the class label with the highest posterior probability.
    """
    best_class = None
    max_posterior = -1.0
    
    for c in classes:
        # P(C)
        posterior = priors[c]
        
        # Multiply by P(x|C) for each attribute
        # P(C|X) = P(C) * P(x1|C) * P(x2|C) ...
        params = model_params[c]
        for i, x in enumerate(attributes):
            mu = params[i]['mu']
            var = params[i]['var']
            likelihood = gaussian_probability(x, mu, var)
            posterior *= likelihood
            
        if best_class is None or posterior > max_posterior:
            max_posterior = posterior
            best_class = c
            
    return best_class

def main():
    # 1. Parse Arguments
    parser = argparse.ArgumentParser(description='Naive Bayes Classifier')
    parser.add_argument('--data', required=True, help='Data file prefix')
    args = parser.parse_args()
    
    file_prefix = args.data
    train_file = f"{file_prefix}_train.csv"
    test_file = f"{file_prefix}_test.csv"
    
    # 2. Load Training Data
    train_data = load_data(train_file)
    
    # 3. Train Model (Estimate Parameters)
    # Separate data by class
    separated = {}
    for label, attrs in train_data:
        if label not in separated:
            separated[label] = []
        separated[label].append(attrs)
        
    classes = sorted(list(separated.keys())) # Sort to ensure A comes before B usually
    
    model_params = {}
    priors = {}
    total_samples = len(train_data)
    
    # Calculate stats for each class
    for c in classes:
        instances = separated[c]
        n_ci = len(instances)
        
        # Calculate Prior P(c)
        priors[c] = n_ci / total_samples
        
        # Calculate Gaussian params for each attribute
        # Assuming 2 attributes based on assignment description
        num_attrs = len(instances[0])
        model_params[c] = []
        
        for i in range(num_attrs):
            # Extract column i
            col_values = [row[i] for row in instances]
            mu, var = calculate_parameters(col_values)
            model_params[c].append({'mu': mu, 'var': var})

    # 4. Print Parameters (Line 1 and 2)
    # Output format: mu1, var1, mu2, var2, prior
    for c in ['A', 'B']: # Explicitly ordering A then B as implied by the problem
        if c in model_params:
            params = model_params[c]
            # Format: mu1, var1, mu2, var2, p
            output = f"{params[0]['mu']},{params[0]['var']},{params[1]['mu']},{params[1]['var']},{priors[c]}"
            print(output)
        else:
            # Handle case if a class is missing in training data
            print("0,0,0,0,0")

    # 5. Check Training Misclassifications (Line 3)
    train_errors = 0
    for label, attrs in train_data:
        prediction = predict(attrs, model_params, priors, classes)
        if prediction != label:
            train_errors += 1
    print(train_errors)

    # 6. Check Test Misclassifications (Line 4)
    test_data = load_data(test_file)
    test_errors = 0
    for label, attrs in test_data:
        prediction = predict(attrs, model_params, priors, classes)
        if prediction != label:
            test_errors += 1
    print(test_errors)

if __name__ == "__main__":
    main()
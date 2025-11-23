import argparse
import csv
import math
import sys


def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # class is the first column
                label = row[0]
                # attributes are the rest, convert to float
                attributes = [float(x) for x in row[1:]]
                data.append([label] + attributes)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    return data


def calculate_mean(values):
    return sum(values) / len(values)


def calculate_variance(values, mean):
    if len(values) <= 1:
        return 0.0
    return sum([(x - mean)**2 for x in values]) / (len(values) - 1)


def gaussian_probability(x, mean, variance):
    # Avoid division by zero
    if variance == 0:
        return 0
    exponent = math.exp(-((x - mean)**2 / (2 * variance)))
    return (1 / (math.sqrt(2 * math.pi * variance))) * exponent


def train(dataset):
    separated = {}
    total_count = len(dataset)

    # Separate by class
    for row in dataset:
        label = row[0]
        if label not in separated:
            separated[label] = []
        separated[label].append(row[1:])

    model = {}
    # Sort to ensure consistent output order (A, B)
    class_labels = sorted(separated.keys())

    for label in class_labels:
        instances = separated[label]
        n_ci = len(instances)

        # Calculate Prior p_c
        prior = n_ci / total_count

        # Calculate Mean and Variance for each attribute
        # Transpose instances to get lists of values per attribute
        # zip(*instances) converts [[1,2], [3,4]] to [(1,3), (2,4)]
        attributes_cols = list(zip(*instances))

        stats = []
        for col in attributes_cols:
            mu = calculate_mean(col)
            var = calculate_variance(col, mu)
            stats.append({'mean': mu, 'var': var})

        model[label] = {
            'stats': stats,
            'prior': prior
        }

    return model


def predict(model, attributes):
    best_label = None
    best_prob = -1

    # P(C|X) proportional to P(X|C) * P(C)
    # We calculate P(X|C) * P(C)

    for label, info in model.items():
        prior = info['prior']
        stats = info['stats']

        # Start with the prior probability
        posterior = prior

        # Multiply by the probability of each attribute value given the class
        # (Naive assumption: attributes are independent)
        for i in range(len(attributes)):
            mean = stats[i]['mean']
            var = stats[i]['var']
            x = attributes[i]
            prob = gaussian_probability(x, mean, var)
            posterior *= prob

        if best_label is None or posterior > best_prob:
            best_prob = posterior
            best_label = label

    return best_label


def main():
    parser = argparse.ArgumentParser(description='Naive Bayes Classifier')
    parser.add_argument('--data', type=str, required=True,
                        help='Name of the data set (e.g., Example)')
    args = parser.parse_args()

    base_name = args.data
    train_file = f"{base_name}_train.csv"
    test_file = f"{base_name}_test.csv"

    # 1. Load Data
    train_data = load_data(train_file)
    test_data = load_data(test_file)

    # 2. Train Model
    model = train(train_data)

    # 3. Print Model Statistics (Rows 1 and 2)
    # Format: mu_1, var_1, mu_2, var_2, ..., prior
    sorted_classes = sorted(model.keys())
    for label in sorted_classes:
        stats = model[label]['stats']
        prior = model[label]['prior']

        output_parts = []
        for stat in stats:
            output_parts.append(str(stat['mean']))
            output_parts.append(str(stat['var']))
        output_parts.append(str(prior))

        print(",".join(output_parts))

    # 4. Calculate Misclassifications

    # On Training Data
    train_errors = 0
    for row in train_data:
        actual = row[0]
        features = row[1:]
        prediction = predict(model, features)
        if prediction != actual:
            train_errors += 1

    # On Test Data
    test_errors = 0
    for row in test_data:
        actual = row[0]
        features = row[1:]
        prediction = predict(model, features)
        if prediction != actual:
            test_errors += 1

    # 5. Print Error Counts (Rows 3 and 4)
    print(train_errors)
    print(test_errors)


if __name__ == "__main__":
    main()

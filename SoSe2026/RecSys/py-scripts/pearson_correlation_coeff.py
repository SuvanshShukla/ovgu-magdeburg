def pearson(x, y):
    if len(x) != len(y):
        raise Exception('Vector lengths are different.')

    # Filter out pairs where either is None
    valid_pairs = [(x[i], y[i]) for i in range(len(x)) if x[i] is not None and y[i] is not None]
    n = len(valid_pairs)

    if n == 0:
        return 0

    sum_x = sum(p[0] for p in valid_pairs)
    sum_y = sum(p[1] for p in valid_pairs)
    ss_x = sum(p[0]**2 for p in valid_pairs)
    ss_y = sum(p[1]**2 for p in valid_pairs)
    prod_sum = sum(p[0] * p[1] for p in valid_pairs)

    nom = (n * prod_sum - sum_x * sum_y)

    # Calculate variance parts for denominator
    var_x = n * ss_x - sum_x**2
    var_y = n * ss_y - sum_y**2

    denom = (var_x * var_y)**0.5

    if denom == 0:
        return 0  # Handles cases with zero variance

    return nom / denom


alpha = [5, 5, 1, 3, 3]
beta = [2, None, None, None, None]

u1 = [5, 5, None, 1, 3]
u2 = [4, 5, 2, 2, 4]
u3 = [3, None, 2, 4, 2]
u4 = [None, 5, 1, 3, None]

print('for alpha & u1: ', pearson(alpha, u1))
print('for alpha & u2: ', pearson(alpha, u2))
print('for alpha & u3: ', pearson(alpha, u3))
print('for alpha & u4: ', pearson(alpha, u4))

print('for beta & u1: ', pearson(beta, u1))
print('for beta & u2: ', pearson(beta, u2))
print('for beta & u3: ', pearson(beta, u3))
print('for beta & u4: ', pearson(beta, u4))

def pearson(x, y):
    if len(x) != len(y):
        raise Exception('Vector lengths are different.')

    sum_x = 0
    sum_y = 0
    ss_x = 0
    ss_y = 0

    prod_sum = 0

    for i in range(len(x)):
        val_x = x[i] if x[i] is not None else 0
        val_y = y[i] if y[i] is not None else 0

        sum_x += val_x
        sum_y += val_y

        ss_x += val_x**2
        ss_y += val_y**2

        prod_sum += val_x * val_y

    nom = (len(x)*prod_sum - sum_x*sum_y)
    denom = ((len(x)*ss_x-sum_x**2)*(len(x)*ss_y-sum_y**2))**0.5

    return nom/denom


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

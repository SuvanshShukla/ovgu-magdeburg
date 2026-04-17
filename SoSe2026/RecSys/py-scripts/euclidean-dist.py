def euclidean_dist(arr1, arr2):
    output = 0
    for i in range(len(arr1)):
        if arr2[i] is not None and arr1[i] is not None:
            output += (arr1[i] - arr2[i])**2
    return output**0.5


alpha = [5, 5, 1, 3, 3]
beta = [2, None, None, None, None]

u1 = [5, 5, None, 1, 3]
u2 = [4, 5, 2, 2, 4]
u3 = [3, None, 2, 4, 2]
u4 = [None, 5, 1, 3, None]

print('for alpha & u1: ', euclidean_dist(alpha, u1))
print('for alpha & u2: ', euclidean_dist(alpha, u2))
print('for alpha & u3: ', euclidean_dist(alpha, u3))
print('for alpha & u4: ', euclidean_dist(alpha, u4))

print('for beta & u1: ', euclidean_dist(beta, u1))
print('for beta & u2: ', euclidean_dist(beta, u2))
print('for beta & u3: ', euclidean_dist(beta, u3))
print('for beta & u4: ', euclidean_dist(beta, u4))

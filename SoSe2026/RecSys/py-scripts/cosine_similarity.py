# Cosine similarity function Link: https://www.geeksforgeeks.org/dbms/cosine-similarity/

def cosine(x, y):
    mag_x = 0
    mag_y = 0
    dot = 0

    if len(x) != len(y):
        raise Exception('Vector lengths are different!')

    for i in x:
        if i is not None:
            mag_x += (i**2)
        mag_x = mag_x**0.5

    for i in y:
        if i is not None:
            mag_y += (i**2)
        mag_y = mag_y**0.5

    for i in range(len(x)):
        if x[i] is not None and y[i] is not None:
            dot += x[i]*y[i]

    return dot/(mag_x + mag_y)


alpha = [5, 5, 1, 3, 3]
beta = [2, None, None, None, None]

u1 = [5, 5, None, 1, 3]
u2 = [4, 5, 2, 2, 4]
u3 = [3, None, 2, 4, 2]
u4 = [None, 5, 1, 3, None]

print('for alpha & u1: ', cosine(alpha, u1))
print('for alpha & u2: ', cosine(alpha, u2))
print('for alpha & u3: ', cosine(alpha, u3))
print('for alpha & u4: ', cosine(alpha, u4))

print('for beta & u1: ', cosine(beta, u1))
print('for beta & u2: ', cosine(beta, u2))
print('for beta & u3: ', cosine(beta, u3))
print('for beta & u4: ', cosine(beta, u4))

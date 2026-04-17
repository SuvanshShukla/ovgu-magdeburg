# Cosine similarity function Link: https://www.geeksforgeeks.org/dbms/cosine-similarity/

def cosine(x, y):
    if len(x) != len(y):
        raise Exception('Vector lengths are different!')

    dot = 0
    sum_sq_x = 0
    sum_sq_y = 0

    for i in range(len(x)):
        # Treat None as 0 for the calculation
        val_x = x[i] if x[i] is not None else 0
        val_y = y[i] if y[i] is not None else 0

        dot += val_x * val_y
        sum_sq_x += val_x**2
        sum_sq_y += val_y**2

    mag_x = sum_sq_x**0.5
    mag_y = sum_sq_y**0.5

    # Prevent division by zero if a vector is all None/Zeros
    if mag_x == 0 or mag_y == 0:
        return 0

    return dot / (mag_x * mag_y)


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

print('---------------Ques 2------------------')

u1 = [1, 1, None, 1, 1]
u2 = [5, 5, None, 5, 5]
u3 = [1, 1, None, 1, 5]

print('for u1 & u2: ', cosine(u1, u2))
print('for u1 & u3: ', cosine(u1, u3))

print('---------------Ques 3------------------')

u1 = [5, None, 1, 3, None]
u2 = [4, 2, 2, 4, 3]
u3 = [3, 2, None, 2, 1]
u4 = [None, 1, 3, None, None]

print('for u4 & u1: ', cosine(u4, u1))
print('for u4 & u2: ', cosine(u4, u2))
print('for u4 & u3: ', cosine(u4, u3))

print('Min of all: ', min(cosine(u4, u1), cosine(u4, u2), cosine(u4, u3)))

print('---------------Ques 4------------------')

u1 = [5, 5, None, 1, 1]
u2 = [2, 5, 2, 2, 4]
u3 = [3, None, 3, 1, 2]
u4 = [None, 5, 1, 4, None]

print('for u4 & u1: ', cosine(u4, u1))
print('for u4 & u2: ', cosine(u4, u2))
print('for u4 & u3: ', cosine(u4, u3))

print('---------------Ques 5------------------')

monkeys = [5, 4, 3, None]
braveheart = [None, 2, 2, 1]
titanic = [1, 2, None, 3]
fight_club = [3, 4, 2, 5]
the_notebook = [5, 3, 1, None]

print('for 12 Monkeys & braveheart: ', cosine(monkeys, braveheart))
print('for 12 Monkeys & titanic: ', cosine(monkeys, titanic))
print('for 12 Monkeys & fight_club: ', cosine(monkeys, fight_club))
print('for 12 Monkeys & The Notebook: ', cosine(monkeys, the_notebook))

print('for The Notebook & 12 Monkeys: ', cosine(the_notebook, monkeys))
print('for The Notebook & braveheart: ', cosine(the_notebook, braveheart))
print('for The Notebook & titanic: ', cosine(the_notebook, titanic))
print('for The Notebook & fight_club: ', cosine(the_notebook, fight_club))

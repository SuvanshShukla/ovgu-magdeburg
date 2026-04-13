def calc_mean(nums):
    return sum(nums)/len(nums)


monkeys = [5, 4, 3, 1, 3, 5, 3, 2, 1, 1, 3, 2, 1, 3]
print('12 monkeys: ', calc_mean(monkeys))

brave = [5, 5, 4, 3, 4, 2, 4, 1, 3, 2, 4, 2]
print('Braveheart: ', calc_mean(brave))

titanic = [2, 2, 5, 1, 3, 2, 2, 4, 5, 2, 2]
print('Titanic: ', calc_mean(titanic))

fight = [4, 4, 1, 3, 5, 5, 4, 2, 3, 5]
print('Fight Club: ', calc_mean(fight))

notebook = [4,   2,   5,   4,   5,   4,   5]
print('The Notebook: ', calc_mean(notebook))

sense = [3, 2, 4, 1, 3, 2, 1, 3]
print('The Sixth Sense: ', calc_mean(sense))

vow = [1, 5, 3, 1, 1, 4, 5, 1, 3]
print('The Vow: ', calc_mean(vow))

print('Informed guess 2\n')

u1 = [5, 5, 3, 1]
u2 = [4, 5, 2, 4, 2, 5]
u3 = [4, 2, 4, 3]
u4 = [3, 4, 2, 4, 1, 1]
u5 = [1, 3, 5, 1, 5, 1]
u6 = [3, 1, 3, 4, 3, 4]
u7 = [5, 4, 3, 5, 2, 5]
u8 = [3, 2, 4, 1, 1]
u9 = [2, 4, 2, 5, 5, 3, 3]
# u10 = [1, 1, 5]
# u11 = [1, 3, 2]
# u12 = [3, 4, 4]
# u13 = [2, 2, 5, 2]
# u14 = [1, 4, 2, 3]
# u15 = [3, 2, 2, 5]
u10 = [3, 2]
u11 = [1, 3]
u12 = [2, 4]
u13 = [3]
u14 = [3, 2]
u15 = [4, 3]


print('Rating for u1: ', calc_mean(u1))
print('Rating for u2: ', calc_mean(u2))
print('Rating for u3: ', calc_mean(u3))
print('Rating for u4: ', calc_mean(u4))
print('Rating for u5: ', calc_mean(u5))
print('Rating for u6: ', calc_mean(u6))
print('Rating for u7: ', calc_mean(u7))
print('Rating for u8: ', calc_mean(u8))
print('Rating for u9: ', calc_mean(u9))
print('Rating for u10: ', calc_mean(u10))
print('Rating for u11: ', calc_mean(u11))
print('Rating for u12: ', calc_mean(u12))
print('Rating for u13: ', calc_mean(u13))
print('Rating for u14: ', calc_mean(u14))
print('Rating for u15: ', calc_mean(u15))

a = [3, 2, 5]
b = [2, 1, 3, 2, 4]
c = [3, 4, 3]
# d = []
# e = []
# f = []

print('Rating for a: ', calc_mean(a))
print('Rating for b: ', calc_mean(b))
print('Rating for c: ', calc_mean(c))
# print('Rating for d: ', calc_mean(d))
# print('Rating for e: ', calc_mean(e))
# print('Rating for f: ', calc_mean(f))

test1 = [5, 4, 3]
test2 = [3, 5, 1]
test3 = [2, 2]
test4 = [1, 4, 4]
test5 = [4, 4, 2]

print('Informed Guess for 12 monkeys: ', calc_mean(test1))
print('Informed Guess for Braveheart: ', calc_mean(test2))
print('Informed Guess for Titanic: ', calc_mean(test3))
print('Informed Guess for Fight Club: ', calc_mean(test4))
print('Informed Guess for The Notebook: ', calc_mean(test5))

actuala = [5, 4, 3]
actualb = [2, 3, 4]
preda = [4, 5, 2]
predb = [3, 2, 5]

print('avg for actual A Rating: ', calc_mean(actuala))
print('avg for actual B Rating: ', calc_mean(actualb))
print('avg for predicted A Rating: ', calc_mean(preda))
print('avg for predicted B Rating: ', calc_mean(predb))

print('ans 5 (a): ', ((4 - 3.66) + abs(3 - 3.333))/2)

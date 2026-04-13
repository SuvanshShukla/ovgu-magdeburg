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

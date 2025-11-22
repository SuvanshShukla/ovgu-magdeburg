def peasant_mult_iter(x: int, y: int) -> int:
    sum = 0
    if x % 2 != 0:
        sum += y
    while x > 1:
        x = x // 2
        y = y * 2
        if x % 2 != 0:
            sum += y
    return sum


sum = 0


def peasant_mult_rec(x: int, y: int) -> int:
    global sum

    if x == 0:
        return sum

    if x % 2 != 0:
        sum += y

    return peasant_mult_rec(x // 2, y * 2)


if __name__ == "__main__":
    sum = 0
    assert peasant_mult_iter(55, 10) == 55 * 10
    sum = 0
    assert peasant_mult_iter(24, 52) == 1248
    sum = 0
    assert peasant_mult_iter(78, 43) == 78 * 43

    sum = 0
    assert peasant_mult_rec(55, 10) == 55 * 10
    sum = 0
    assert peasant_mult_rec(24, 52) == 1248
    sum = 0
    assert peasant_mult_rec(78, 43) == 78 * 43

    print("ALL TESTS PASSED")

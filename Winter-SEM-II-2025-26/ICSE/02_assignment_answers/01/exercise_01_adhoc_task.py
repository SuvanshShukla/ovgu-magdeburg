def sqdigitsum(n: int) -> int:
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**2
        n = n // 10
    return sum


def test_sqdigitsum():
    assert sqdigitsum(10) == 1
    assert sqdigitsum(19) == 82
    assert sqdigitsum(99) == 162
    assert sqdigitsum(2098) == 4 + 0 + 81 + 64


# def is_happy(n: int) -> bool:
#     while sqdigitsum(n) > 0:
#         n = sqdigitsum(n)
#     return True


def is_happy_number(n: int) -> bool:
    seen = set()
    while n not in seen:
        print(n)
        if n == 1:
            return True
        seen.add(n)
        n = sqdigitsum(n)


def test_is_happy():
    assert is_happy_number(10) is True
    assert is_happy_number(99) is not True


if __name__ == "__main__":
    # test_sqdigitsum()
    test_is_happy()
    print("ALL TESTS PASSED.")

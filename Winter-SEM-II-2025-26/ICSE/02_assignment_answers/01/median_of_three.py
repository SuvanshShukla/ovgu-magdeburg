def median(a: int, b: int, c: int) -> int:
    if (a <= b and b <= c) or (c <= b and b <= a):
        return b
    if (b <= a and a <= c) or (c <= a and a <= b):
        return a
    if (b <= c and c <= a) or (a <= c and c <= b):
        return c
    raise NotImplementedError()


def median2(a: int, b: int, c: int) -> int:
    nums = [a, b, c]
    nums.sort()
    return nums[1]
    raise NotImplementedError()


def test_median():
    assert median(99, 7, 4) == 7
    assert median2(101, 87, 44) == 87
    assert median(77, 99, 23) == 77
    assert median(99, 99, 99) == 99
    assert median2(109, 108, 110) == 109

   
if __name__ == "__main__":
    print(median(0, 0, 0))
    test_median()
    print("TESTS PASSED.")

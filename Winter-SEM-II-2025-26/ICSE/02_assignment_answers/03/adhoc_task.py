def binary_search_helper(a: list, item: int,
                         low: int, high: int) -> int | None:
    if high < low:
        return None
    m = (high + low) // 2
    if a[m] == item:
        return m
    elif a[m] < item:
        return binary_search_helper(a, item, m + 1, high)
    else:
        return binary_search_helper(a, item, low, m - 1)


def exp_search(arr: list[int], item) -> int | None:
    i = 1
    while i <= len(arr) and arr[i] <= item:
        i *= 2
    return binary_search_helper(arr, item, i // 2, min(i, len(arr) - 1))

if __name__ == "__main__":
    assert exp_search([1, 2, 4, 6, 7, 8, 9, 11, 13, 15, 17, 19,
                       21, 23, 25], 17) == 10
    assert exp_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8
    print("ALL TEST CASES PASSED!")

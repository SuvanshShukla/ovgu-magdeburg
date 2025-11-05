from typing import List
from random import randint
import time


def binary_search(a: List[int], item: int) -> int | None:
    return binary_search_helper(a, item, 0, len(a) - 1)


def binary_search_helper(a: List[int], item: int,
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


def ternary_search(a: List[int], item: int) -> int | None:
    left = 0
    right = len(a) - 1
    while left <= right:
        p = left + (right - left) // 3
        q = right - (right - left) // 3
        if item == a[p]:
            return p
        elif item == a[q]:
            return q
        elif item < a[p]:
            right = p - 1
        elif item > a[q]:
            left = q + 1
        else:
            left = p + 1
            right = q - 1
    return None


def time_binary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    binary_search(arr, item)
    return time.time() - start


def time_ternary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    ternary_search(arr, item)
    return time.time() - start


if __name__ == "__main__":
    # TODO: Test your binary and ternary search implementation here...
    a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert binary_search(a1, 5) == 5
    assert ternary_search(a2, 6) == 5
    print("ALL TESTS PASSED.")

    # These constantsshould be defined here, don't move them!
    MAX_VALUE = 50_000_000
    NUM_ITER = 100_000
    SEARCH_VALUES = [randint(0, MAX_VALUE - 1) for _ in range(NUM_ITER)]
    ARRAY = list(range(MAX_VALUE))
    print(f"Searching {NUM_ITER:_} random values in an array of size {MAX_VALUE:_}")

    time_binary = 0.
    for value in SEARCH_VALUES:
        time_binary += time_binary_search_in_s(ARRAY, value)

    time_ternary = 0.
    for value in SEARCH_VALUES:
        time_ternary += time_ternary_search_in_s(ARRAY, value)

    print(f"Total binary search time:    {time_binary:.9f} s")
    print(f"Total ternary search time:   {time_ternary:.9f} s")
    print(f"Average binary search time:  {time_binary / NUM_ITER:.9f} s")
    print(f"Average ternary search time: {time_ternary / NUM_ITER:.9f} s")

"""
TASK3: No ternary search would not be faster than binary search. Due
to constantly having to find new pointers and moving them.
"""

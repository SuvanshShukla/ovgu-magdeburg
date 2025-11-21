"""
2.  # TODO

3.  # TODO

"""


def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    j = 0

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def qsort(array, start, end):
    if start < end:
        mid = partition(array, start, end)
        qsort(array, start, mid - 1)
        qsort(array, mid + 1, end)


def quick_sort(array: list) -> None:
    """Sorts `array` with quick-sort in-place."""
    qsort(array, 0, len(array) - 1)


if __name__ == "__main__":
    # Please include more test cases
    array = [3, 2, 4, 1, 5]
    quick_sort(array)
    arr2 = [64, 34, 25, 5, 22, 11, 90, 12]
    quick_sort(arr2)
    assert array == [1, 2, 3, 4, 5]
    assert arr2 == [5, 11, 12, 22, 25, 34, 64, 90]

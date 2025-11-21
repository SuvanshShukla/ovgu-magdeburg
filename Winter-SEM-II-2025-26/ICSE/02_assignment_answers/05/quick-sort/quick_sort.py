"""
2.  # TODO

3.  # TODO

"""


def quick_sort(array: list) -> None:
    """Sorts `array` with quick-sort in-place."""
    size = len(array)
    if size < 2:
        return array

    mid = size // 2
    pivot = array[mid]
    less = []
    equal = []
    greater = []
    # i = 0
    # j = size - 1

    for i in array:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        elif i > pivot:
            greater.append(i)
            
    # while i < j:
    #     if array[i] < pivot:
    #         less.append(array[i])
    #     i += 1
    #     if array[j] >= pivot:
    #         greater.append(array[j])
    #     j -= 1

    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    # Please include more test cases
    array = [3, 2, 4, 1, 5]
    quick_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]

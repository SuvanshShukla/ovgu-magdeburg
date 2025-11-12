"""
3.  # TODO

"""


def bubble_sort(array: list) -> None:
    """Sorts `array` with bubblesort inplace."""
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    bubble_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]

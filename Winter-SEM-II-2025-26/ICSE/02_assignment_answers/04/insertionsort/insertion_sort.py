"""
2. Insertion sort doesn't swap the items in a list/array arround.
Instead it takes the item and moves it to the correct location in
the sorted part of the array. The reason why the 1st figure and
the animation don't do anything is because this algorithm moves
the items instead of swapping them. It also assumes that a part
of the list/array is already sorted.

"""


def insertion_sort(array: list) -> None:
    """Sorts `array` with insertionsort inplace."""
    for i in range(1, len(array)):
        insert_loc = i
        anchor = array.pop(i)
        for j in range(i - 1, -1, -1):
            if array[j] > anchor:
                insert_loc = j
        array.insert(insert_loc, anchor)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    insertion_sort(array)
    assert array == [1, 2, 3, 4, 5]

"""
3. The bubble sort algorithm iterates over the entire list
or array and swaps two adjacent elements if the left element
is greater than the right element. The first figure generated
by the animation script shows us that sorting starts from the
end of the list/array and works its way to the front (i.e. greater
index to lower index). The second animation shows us how the
algorithm swaps adjacent elements from left to right and does
it again and again until it has iterated over the list a
number of times equivalent to the length of the list/array.
This means an iteration of adjacent swaps happens for every
element in the array/list.

The improvement that was discussed was that the sorting
algorithm still runs on the entire list if the list is
already sorted. To prevent this we add a check to see if
the elements were swapped or not, breaking out of the inner
swap loop if the elements weren't swapped.

"""


def bubble_sort(array: list) -> None:
    """Sorts `array` with bubblesort inplace."""
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    bubble_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]

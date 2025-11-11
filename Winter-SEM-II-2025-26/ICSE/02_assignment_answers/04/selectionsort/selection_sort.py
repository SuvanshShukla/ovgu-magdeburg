"""
1.  An "in-place" sorting algorithm doesn't need any extra space,
it overwrites the input with the desired output. An "out-of-place" algorithm
uses extra memory to store intermediary results.

3. The two plots help us visualize what selection sort is doing in the
background. The first figure shows us snippets of how the items are arranged
at 0%, 20%, 40%, 60%, 80% and 100%. From observation we notice that selection
sort gradually puts the smallest elements to the left (i.e. the start of
the array) and then moves slowly to the right (larger elements). The second
figure/animation shows us how the algorithm actually scans every element to
find the smallest values and then does it again and again iteratively until
the input array is completely sorted.

"""


def selection_sort(array: list) -> None:
    """Sorts `array` with selectionsort inplace."""
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[j] <= array[i]:
                array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    selection_sort(array)
    assert array == [1, 2, 3, 4, 5]

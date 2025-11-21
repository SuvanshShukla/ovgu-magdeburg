"""
2. Quick sort particularly its in-place version, sorts a list using the
    divide and conquer approach. In this approach the main list is divided
    into smaller lists based on whether they are greater or lesser than an
    arbitrarily chosen pivot element. Two pointers are then chosen to iterate
    over the list. The first pointer finds any element larger than the pivot
    element on the left side of the list and the second pointer finds any
    element smaller than or equal the pivot element on the right side of the
    list. Once both such elements are found, they are swapped with each other.
    This is done multiple times until the entire list is covered by both
    pointers, then the pivot element is swapped to the front of the right side
    of the list. The pointer demarcating the end of smaller elements and the
    start of larger elements is then returned. This index is then used to
    further split the list and the same swapping of larger & smaller elements
    is done until either a single element or no elements remain in the list.
    This smallest unit of the list is then returned and concatenated with
    other such smaller elements until the entire list is recreated in a sorted
    order.

3. The best case scenario for quick-sort is if the entire list already sorted
    this would result in O(n) time-complexity as we would only iterate over the
    list one time to partition it but see that no partiioning is actually
    required. The worst case scenario for quick-sort is if the elements are
    sorted but in reversed order, though this would be just like its average
    case resulting in O(n**2) time-complexity.

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

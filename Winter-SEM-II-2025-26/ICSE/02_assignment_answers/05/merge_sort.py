"""
1(a). Divide and Conquer is an approach in algorithmic thinking
    where a larger problem is divided into its smallest solvable
    unit, solved, then combined all together to get the whole solution.

1(b). Stable sorting is a type of sorting where two duplicates of the
    same element remain in their original positions relative to each
    other after sorting. This ensures that even if we sort objects having
    multiple attributes on a single chosen attribute they would retain
    relative positioning of the other attributes even after being sorted.

2. this is what the merge sort looks like in-progress:

[5, 3, -2, 7, 6, 9, 1, -8, 4, 10, 2, 1, -1, 8]
[5, 3, -2, 7, 6, 9, 1]
[5, 3, -2]
[5]
[3, -2]
[3]
[-2]
[-2, 3]
[-2, 3, 5]
[7, 6, 9, 1]
[7, 6]
[7]
[6]
[6, 7]
[9, 1]
[9]
[1]
[1, 9]
[1, 6, 7, 9]
[-2, 1, 3, 5, 6, 7, 9]
[-8, 4, 10, 2, 1, -1, 8]
[-8, 4, 10]
[-8]
[4, 10]
[4]
[10]
[4, 10]
[-8, 4, 10]
[2, 1, -1, 8]
[2, 1]
[2]
[1]
[1, 2]
[-1, 8]
[-1]
[8]
[-1, 8]
[-1, 1, 2, 8]
[-8, -1, 1, 2, 4, 8, 10]
[-8, -2, -1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def merge(left: list[int], right: list[int]):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result = result + left[i:] + right[j:]
    # print(result)
    return result


def merge_sort(array: list[int]) -> list[int]:
    # print(array)
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    sorted = merge_sort(array)
    arr2 = [5, 3, -2, 7, 6, 9, 1, -8, 4, 10, 2, 1, -1, 8]
    sorted_2 = merge_sort(arr2)
    assert sorted == [1, 2, 3, 4, 5]
    assert sorted_2 == [-8, -2, -1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

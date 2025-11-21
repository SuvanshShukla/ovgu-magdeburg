"""
1. Divide and Conquer is an approach in algorithmic thinking
    where a larger problem is divided into its smallest solvable
    unit, solved, then combined all together to get the whole solution.

2. Stable sorting is a type of sorting where two duplicates of the
    same element remain in their original positions relative to each
    other after sorting. This ensures that even if we sort objects having
    multiple attributes on a single chosen attribute they would retain
    relative positioning of the other attributes even after being sorted.

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
    print(result)
    return result


def merge_sort(array: list[int]) -> list[int]:
    print(array)
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
    assert sorted == [1, 2, 3, 4, 5]

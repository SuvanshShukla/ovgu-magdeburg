"""
1. Given the sequence of numbers 8, 3, 7, 1, 5, 9, 6 and how it gets sorted when using **heapsort** based on a max heap.
Describe the program flow by giving all necessary steps.

2. Complete the class MaxHeap with the following functions:
    `public void swapMax()`
    which exchanges the last and the manual element of a heap and restores the heap property by suing `sink()`

Changed task: write heapify function to try to explain heapsort.
"""

from typing import TypeVar, List

T = TypeVar('T')


class MaxHeap:
    def __init__(self, arr: List[T]) -> None:
        self.contents = arr
        if self.contents is not None:
            self.heapify()

    def __len__(self) -> int:
        return len(self.contents)

    def get_heap(self) -> List[T]:
        return self.contents.copy()

    def is_empty(self) -> bool:
        return True if len(self) == 0 else False

    def insert(self, obj: T) -> None:
        self.contents.append(obj)
        self.float(len(self.contents) - 1)

    def float(self, n: int) -> None:
        to_shift: T = self.contents[n]
        parent = (n - 1) // 2
        while n > 0 and to_shift > self.contents[parent]:
            self.contents[n] = self.contents[parent]
            n = parent
            parent = (n - 1) // 2

    def remove(self) -> T:
        if len(self) == 0:
            raise IndexError("Trying to remove from empty heap")
        if len(self) == 1:
            return self.contents.pop()

        to_return: T = self.contents[0]
        self.contents[0] = self.contents.pop()
        self.sink(0)
        return to_return

    def sink(self, n: int) -> None:
        while 2 * n + 1 < len(self):
            child = 2 * n + 1
            if (child + 1 < len(self) and self.contents[child] < self.contents[child + 1]):
                child = child + 1
            if self.contents[n] >= self.contents[child]:
                break
            self.contents[n], self.contents[child] = self.contents[child], self.contents[n]
            n = child

    def heapify(self):
        last_internal_index = len(self) // 2
        for i in range(last_internal_index, -1, -1):
            self.sink(i)


if __name__ == "__main__":
    heap_test = ['X', 'T', 'O', 'G', 'S', 'M', 'N', 'A', 'E', 'R', 'A', 'I']
    max_heap = MaxHeap(heap_test)
    pass


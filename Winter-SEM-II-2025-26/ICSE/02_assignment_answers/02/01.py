from numpy import random


def create_random(n: int) -> list[int]:
    for i in range(0, n):
        list[i] = random.randint(9, 55)


def to_string(arr: list[int]) -> str:
    str = ""
    for i in arr:
        str = str + i
    return str


def pos_min(arr: list[int]) -> int:
    i = 0
    j = len(arr) - 1
    while i != j:
        if arr[i] <= arr[j]:
            j = j - 1
        elif arr[j] < arr[i]:
            i = i + 1
    return i


def swap(arr: list[int]) -> None:
    temp = arr[0]
    arr[0] = arr[len(arr-1)]
    arr[len(arr-1)] = temp
    return arr

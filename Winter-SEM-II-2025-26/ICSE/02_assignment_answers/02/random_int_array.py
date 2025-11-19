import random


def create_random(n: int) -> list[int]:
    arr = [0] * n
    for i in range(n):
        arr[i] = random.randint(5, 99)
    return arr


def to_string(arr: list[int]) -> str:
    new_str = ""
    for i in arr:
        new_str = new_str + str(i)
    return new_str


def pos_min(arr: list[int]) -> int:
    return arr.index(min(arr))


def swap(arr: list[int]) -> None:
    temp = arr[0]
    arr[0] = arr[len(arr) - 1]
    arr[len(arr) - 1] = temp


if __name__ == "__main__":
    print(create_random(5))
    pass

from random import seed

seed(0)


def h2(x: int) -> int:
    return x << 5


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashLinQuadDouble:
    def __init__(self, n: int) -> None:
        # Zero indicates an empty slot
        self.table = [0 for _ in range(n)]
        self.capacity = n
        self.size = 0

    def add_lin(self, obj: int) -> int:
        raise NotImplementedError()  # TODO

    def add_quad(self, obj: int) -> int:
        raise NotImplementedError()  # TODO

    def add_double_hashing(self, obj: int) -> int:
        raise NotImplementedError()  # TODO


if __name__ == "__main__":
    # Initialize list with capacity of 1249
    hash1 = HashLinQuadDouble(1249)
    hash2 = HashLinQuadDouble(1249)
    hash3 = HashLinQuadDouble(1249)

    # Generating array of 1000 +ve elements
    rlist = []
    for i in range(1000):
        random_int = random.randint(1, 1000)
        rlist.append(random_int)

    col_count_1 = 0
    for j in rlist:
        col_count_1 += hash1.add_lin(j)

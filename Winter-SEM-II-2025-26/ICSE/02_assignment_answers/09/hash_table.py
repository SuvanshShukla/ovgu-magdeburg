from random import seed

seed(0)


def h2(x: int) -> int:
    return x << 5


class HashLinQuadDouble:
    def __init__(self, n: int) -> None:
        # Zero indicates an empty slot
        self.table = [0 for _ in range(n)]

    def add_lin(self, obj: int) -> int:
        raise NotImplementedError()  # TODO

    def add_quad(self, obj: int) -> int:
        raise NotImplementedError()  # TODO

    def add_double_hashing(self, obj: int) -> int:
        raise NotImplementedError()  # TODO


if __name__ == "__main__":
    pass  # TODO: Compare the insertion functions
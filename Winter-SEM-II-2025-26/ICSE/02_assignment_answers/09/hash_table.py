import random
from random import seed

seed(0)


def h2(x: int) -> int:
    return x << 5


class HashLinQuadDouble:
    def __init__(self, n: int) -> None:
        # Zero indicates an empty slot
        self.table = [0 for _ in range(n)]

    def add_lin(self, obj: int) -> int:
        size = len(self.table)
        index = obj % size
        count = 0

        while count <= size:
            if self.table[index] == 0 and obj is not None:
                self.table[index] = obj
                break
            else:
                index = (index + 1) % size
                count += 1

        return count

    def add_quad(self, obj: int) -> int:
        size = len(self.table)
        base_index = obj % size
        count = 0

        while count <= size:
            index = (base_index + count**2) % size
            if self.table[index] == 0 and obj is not None:
                self.table[index] = obj
                break
            else:
                count += 1

        return count

    def add_double_hashing(self, obj: int) -> int:
        size = len(self.table)
        index = obj % size
        count = 0

        step = h2(obj) % size

        if step == 0:
            step = 1

        while count <= size:
            if self.table[index] == 0 and obj is not None:
                self.table[index] = obj
                break
            else:
                index = (index + step) % size
                count += 1

        return count


if __name__ == "__main__":
    # Initialize list with capacity of 1249
    print("Creating hash tables")
    hash1 = HashLinQuadDouble(1249)
    hash2 = HashLinQuadDouble(1249)
    hash3 = HashLinQuadDouble(1249)

    # Generating array of 1000 +ve elements
    print("creating random int list")
    rlist = []
    for i in range(1000):
        random_int = random.randint(1, 1000)
        rlist.append(random_int)

    print("adding random ints to hashtable")
    col_count_1 = 0
    col_count_2 = 0
    col_count_3 = 0
    for j in rlist:
        col_count_1 += hash1.add_lin(j)
        col_count_2 += hash2.add_quad(j)
        col_count_3 += hash3.add_double_hashing(j)

    print("Collision count using linear probe: ", col_count_1)
    print("Collision count using quadratic probe: ", col_count_2)
    print("Collision count using double hasing probe: ", col_count_3)

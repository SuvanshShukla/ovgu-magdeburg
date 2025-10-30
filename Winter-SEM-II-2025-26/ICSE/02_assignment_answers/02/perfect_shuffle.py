def interleave(a: list[int], b: list[int]) -> list[int]:
    shuffled_deck = []
    for i in range(len(a)):
        shuffled_deck.append(a[i])
        shuffled_deck.append(b[i])
    return shuffled_deck


def perfect_shuffle(a: list[int]) -> list[int]:
    mid_ptr = int(len(a) / 2)
    l_half = a[0:mid_ptr]
    r_half = a[mid_ptr:len(a)]
    return interleave(l_half, r_half)


def shuffle_number(a: int) -> int:
    count = 0
    original = list(range(a))
    copy = original.copy()
    while True:
        copy = perfect_shuffle(copy)
        count += 1
        if original == copy:
            break
    return count


if __name__ == "__main__":
    assert shuffle_number(4) == 2
    assert shuffle_number(52) == 8
    print("ALL TESTS PASSED!")
    pass

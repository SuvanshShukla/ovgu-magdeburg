def is_prime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0 and i < n:
            return False
    return True


def prime_twins(n: int) -> list[tuple[int, int]]:
    list_of_twins = []
    twins = (int, int)
    i = 0
    if n <= 0:
        return []
    else:
        while len(list_of_twins) < n:
            if is_prime(i) and is_prime(i + 2):
                twins = (i, i + 2)
                print(twins)
                list_of_twins.append(twins)
        i = 3
    return list_of_twins


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    list_of_triplets = []
    triplets = (int, int, int)
    i = 0
    if n <= 0: 
        return []
    else:
        while len(list_of_triplets) < n:
            if is_prime(i) and is_prime(i + 2) and is_prime(i + 6):
                triplets = (i, i + 2, i + 6)
                list_of_triplets.append(triplets)
        i = i + 7
    return list_of_triplets


if __name__ == "__main__":
    assert prime_twins(2) == [(3, 5), (5, 7)]
    assert prime_twins(3) == [(3, 5), (5, 7), (11, 13)]
    assert prime_twins(8) == [(3, 5), (11, 17), (29, 41),
                              (59, 71), (101, 107), (137, 149),
                              (179, 191), (197, 227)]
    assert prime_triplets(2) == [(3, 5, 7), (11, 13, 17)]
    assert prime_triplets(3) == [(5, 7, 11), (7, 11, 13), (11, 13, 17)]
    assert prime_triplets(6) == [(5, 7, 11), (7, 11, 13), (11, 13, 17),
                                 (13, 17, 19), (17, 19, 23), (37, 41, 43),
                                 (41, 43, 47),
                                 (67, 71, 73), (97, 101, 103), (101, 103, 107)]
    print("ALL TESTS PASSED.")

def is_prime(n: int) -> bool:
    """Returns `True`, if and only if `n` is prime."""
    for i in range (2, n+1):
        if (n%i !=0 and n==i):
            return True
    return False
    raise NotImplementedError()


def next_prime(n: int) -> int:
    """Returns the next prime number that is bigger or equal to `n`."""
    j = n+1
    while not is_prime(j):
        j += 1
    return j
    raise NotImplementedError()


if __name__ == "__main__":
    pass
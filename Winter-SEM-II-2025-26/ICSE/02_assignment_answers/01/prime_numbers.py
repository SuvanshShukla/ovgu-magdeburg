def is_prime(n: int) -> bool:
    """Returns `True`, if and only if `n` is prime."""
    if n == 0 or n == 1:
        return False
        
    for i in range (2, n):
        if n % i == 0 and i < n:
            return False
    return True
    raise NotImplementedError()


def next_prime(n: int) -> int:
    """Returns the next prime number that is bigger or equal to `n`."""
    while not is_prime(n):
        n += 1
    return n
    raise NotImplementedError()

if __name__ == "__main__":
    pass
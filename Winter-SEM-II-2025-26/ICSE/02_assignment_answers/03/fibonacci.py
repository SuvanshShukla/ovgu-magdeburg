# Solution for part 2.
#                                               fib1(5)
#                                      fib1(3)             fib1(4)
#               fib1(1)             fib1(2)             fib1(2)         fib1(3)
#                   1         fib1(0)     fib1(1)     fib1(0)   fib1(1)     fib1(1)     fib1(2)
#                               0           1           0           1           1     fib1(0)   fib1(1)
#                                                                                       0           1
# total number of fib1() calls = 15

number_recursive_calls = 0
iteration = 0


def fib1(n: int) -> int:
    global number_recursive_calls
    # For some reason number_recursive_calls += 1 doesn't work
    number_recursive_calls = number_recursive_calls + 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)


def fib2(n: int) -> int:
    """Calculates the `n`th fibonacci number iteratively."""
    global iteration
    iteration += 1
    if n <= 1:
        return 1
    a = 1
    b = 1
    for i in range(2, n + 1):
        accumulator = a + b
        a = b
        b = accumulator
    return b


def testfibs():
    assert fib1(2) == 2
    assert fib1(3) == 3
    assert fib1(4) == 5
    assert fib1(5) == 8
    assert fib1(6) == 13

    assert fib2(2) == 2
    assert fib2(3) == 3
    assert fib2(4) == 5
    assert fib2(5) == 8
    assert fib2(6) == 13


if __name__ == "__main__":
    testfibs()
    print("ALL TESTS PASSED!")
    print("First 15 fibonacci numbers")
    print("23rd Fibonacci number: " + str(fib1(23)))
    print("No. of calls using recursion: " + str(number_recursive_calls))
    print("No. of calls using iteration: " + str(iteration))

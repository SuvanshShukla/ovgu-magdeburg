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
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)


def fib2(n: int) -> int:
    """Calculates the `n`th fibonacci number iteratively."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 0
        accumulator = 0
        for i in range(n):
            accumulator = 
    return i


def print_fibs():
    for i in range(15):
        print(fib1(i))
    global iteration
    iteration = i


def testfibs():
    # assert fib1(2) == 1
    # assert fib1(3) == 2
    # assert fib1(4) == 3
    # assert fib1(5) == 5
    # assert fib1(6) == 8
    assert fib2(2) == 1
    assert fib2(3) == 2
    assert fib2(4) == 3
    assert fib2(5) == 5
    assert fib2(6) == 8


if __name__ == "__main__":
    testfibs()
    print("ALL TESTS PASSED!")
    print("First 15 fibonacci numbers")
    # print_fibs()
    # print("23rd Fibonacci number: " + str(fib1(23)))
    # print("No. of calls using recursion: " + str(number_recursive_calls))
    print("No. of calls using iteration: " + str(iteration))

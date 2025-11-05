def fizzbuzz(n: int) -> list[str]:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(str(i))


if __name__ == "__main__":
    print("Please enter a number larger than 0.")
    n = int(input())
    while n <= 0:
        print("Please try again.")
        n = int(input())
    fizzbuzz(n)

def fizzbuzz(n: int) -> list[str]:
    arr = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FIZZBUZZ")
        elif i % 3 == 0:
            arr.append("FIZZ")
        elif i % 5 == 0:
            arr.append("BUZZ")
        else:
            arr.append(str(i))
    return arr


if __name__ == "__main__":
    print("Please enter a number larger than 0.")
    n = int(input())
    while n <= 0:
        print("Please try again.")
        n = int(input())
    print(fizzbuzz(n))

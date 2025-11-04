def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    for i in (a):
        if a[i] == item:
            return i
        else:
            return None


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    if len(a) == 0:
        return None
    elif len(a) == 1:
        return a[0]
    else:
        median = int(len(a) / 2)
        if a[median] == item:
            return median
        elif item < a[median]:
            search_binary(a[0:median], item)
        elif item >= a[median]:
            search_binary(a[median+1:len(a) - 1], item)


def search_linear_cmp_count(a: list[str], item: str) -> int:
    cmp = 0
    for i in (a):
        cmp += 1
        if a[i] == item:
            return cmp
        else:
            return None


def search_binary_cmp_count(a: list[str], item: str) -> int:
    cmp = 0
    if len(a) == 0:
        cmp += 1
        return cmp
    elif len(a) == 1:
        cmp += 1
        return cmp
    else:
        median = int(len(a) / 2)
        if a[median] == item:
            cmp += 1
            return cmp
        elif item <= a[median]:
            cmp += 1
            search_binary(a[0:median], item)
        elif item > a[median]:
            cmp += 1
            search_binary(a[median+1, len(a) - 1])


def test_search():
    assert search_linear([1, 9, 3, 2, 1, 5], 9) == 1
    assert search_binary(range(20), 10) == 10


if __name__ == "__main__":
    test_search()
    print("ALL TEST CASED PASSED!")
    pass

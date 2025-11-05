def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    for i in a:
        if i == item:
            return a.index(i)
    return None


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    temp_arr = a
    offset = 0
    if len(temp_arr) == 0:
        return None
    elif len(temp_arr) == 1 and temp_arr[0] == item:
        return 0
    while temp_arr:
        median = len(temp_arr) // 2
        mid_item = temp_arr[median]
        if mid_item == item:
            return offset + median
        elif item < mid_item:
            temp_arr = temp_arr[:median]
        elif item >= mid_item:
            offset += median + 1
            temp_arr = temp_arr[median + 1:]
    return None


def search_linear_cmp_count(a: list[str], item: str) -> int:
    cmp = 0
    for i in a:
        if i == item:
            cmp += 1
            return cmp
    return cmp


def search_binary_cmp_count(a: list[str], item: str) -> int:
    cmp = 0
    temp_arr = a
    offset = 0
    if len(temp_arr) == 0:
        cmp += 1
        return cmp
    elif len(temp_arr) == 1 and temp_arr[0] == item:
        cmp += 2
        return cmp
    while len(temp_arr) > 1:
        median = len(temp_arr) // 2
        mid_item = temp_arr[median]
        if mid_item == item:
            cmp += 1
            return 0
        elif item < mid_item:
            cmp += 1
            temp_arr = temp_arr[:median]
        elif item >= mid_item:
            cmp += 1
            offset += median + 1
            temp_arr = temp_arr[median + 1:]
        else:
            return cmp
    return cmp


def test_search():
    assert search_linear(["1", "9", "3", "2", "1", "5"], "9") == 1
    assert search_binary(["1", "1", "2", "3", "5", "9"], "5") == 4


if __name__ == "__main__":
    test_search()
    print("ALL TEST CASED PASSED!")
    pass

def transform_to_dual(dec: int) -> str:
    """Transforms a given decimal number to it's dual representation."""
    rem = 0
    binary_str = ""
    while dec > 0:
        rem = dec % 2
        dec = dec // 2
        binary_str = str(rem) + binary_str
    return binary_str
    raise NotImplementedError()


def test_transform():
    """This function tests if dec -> bin was correct"""
    assert transform_to_dual(2) == "10"
    assert transform_to_dual(13) == "1101"
    assert transform_to_dual(79) == "1001111"
    assert transform_to_dual(10297) == "10100000111001"
    assert transform_to_dual(74655) == "10010001110011111"
    assert transform_to_dual(746) == "1011101010"
    assert transform_to_dual(9999999) == "100110001001011001111111"


if __name__ == "__main__":
    test_transform()
    print("ALL TESTS PASSED.")

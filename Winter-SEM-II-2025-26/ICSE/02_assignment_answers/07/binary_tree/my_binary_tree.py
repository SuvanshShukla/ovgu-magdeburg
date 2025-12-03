from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        raise NotImplementedError()  # TODO: Add implementation

    def max_sum(self) -> int:
        """Returns the maximum sum of the left and right sub-tree."""
        raise NotImplementedError()  # TODO: Add implementation

    def max_path(self) -> int:
        """Returns the value of the biggest path from self to a leaf."""
        raise NotImplementedError()  # TODO: Add implementation

    def max_width(self) -> int:
        """Returns the value of the biggest level."""
        raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    pass

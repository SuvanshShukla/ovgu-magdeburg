from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        count = 0
        end = False
        while end is not True:
            if self.get_left() is not None:
                self = self.get_left()
                count += 1
            elif self.get_right() is not None:
                self = self.get_right()
                count += 1
            else:
                end = True
        return count

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
    left_left_tree = MyBinaryTree(0)
    left_tree = MyBinaryTree(1, left_left_tree)
    right_tree = MyBinaryTree(3)
    tree = MyBinaryTree(2, left_tree, right_tree)
    print(tree.height())
    assert tree.height() == 2
    pass

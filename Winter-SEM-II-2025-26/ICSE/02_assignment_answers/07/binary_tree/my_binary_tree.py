from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        if self is None:
            return -1

        stack = []
        stack.append(self)
        height = -1

        while len(stack) > 0:
            size = len(stack)
            height += 1
            while size > 0:
                node = stack.pop()
                if node.get_left() is not None:
                    stack.append(node.get_left())
                if node.get_right() is not None:
                    stack.append(node.get_right())
                size -= 1
        return height

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

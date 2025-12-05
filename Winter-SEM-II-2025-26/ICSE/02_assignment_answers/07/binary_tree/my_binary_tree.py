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
        if self is None:
            return 0

        stack = []
        stack.append(self)
        left_sum = 0
        right_sum = 0

        while len(stack) > 0:
            size = len(stack)
            while size > 0:
                node = stack.pop()
                if node.get_left() is not None:
                    stack.append(node.get_left())
                    left_sum += node.get_left().get_item()
                if node.get_right() is not None:
                    stack.append(node.get_right())
                    right_sum += node.get_right().get_item()
                size -= 1
        return max(left_sum, right_sum)

    def max_path(self) -> int:
        """Returns the value of the biggest path from self to a leaf."""
        if self is None:
            return 0

        left_max = 0
        right_max = 0

        if self.get_left() is not None:
            left_max += max(0, self.get_left().max_path())

        if self.get_right() is not None:
            right_max += max(0, self.get_right().max_path())

        return self.get_item() + max(left_max, right_max)

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
    print(tree.max_sum())
    assert tree.max_sum() == 3
    print(tree.max_path())
    assert tree.max_path() == 5
    pass

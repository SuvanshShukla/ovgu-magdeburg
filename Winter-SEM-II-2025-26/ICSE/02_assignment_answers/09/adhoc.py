# Ad Hoc task for exercise 9 (07/01/2026)

# We already have a BinaryTree class and now we have to implement
# is_balanced(self) -> bool this checks whether the given
# (sub)tree is AVL balanced or not and returns the corresponding bool value
# and inorder_next(self) -> BinaryTree | None this returns the node that would
# come next inorder traversal We can assume that the BinaryTree is also
# a SearchTree If no such successor exists then return None

class BinaryTree:
    def __init__(self, data: int):
        pass

    def get_parent(self) -> BinaryTree | None:
        pass

    def get_left(self) -> BinaryTree | None:
        pass

    def get_right(self) -> BinaryTree | None:
        pass

    def get_data(self) -> int:
        pass

    def height(self) -> int:
        pass

    def is_balanced(self) -> bool:
        """This is the function we have to implement"""
        # if self.get_right() is not None and self.get_left() is not None:
        #     if (self.get_left().height() - self.get_right().height() > 2
        #             or self.get_left().height() - self.get_right().height() < -2):
        #         return False
        # else:
        #     return True
        left = self.get_left()
        right = self.get_right()

        left_height = None
        right_height = None

        if left is not None:
            left_height = left.height()
        else:
            left_height = 0

        if right is not None:
            right_height = right.height()
        else:
            right_height = 0

        if abs(left_height - right_height) <= 1:
            return True
        else:
            return False

        if left and not left.is_balanced():
            return False

        if right and not right.is_balanced():
            return False

    def inorder_next(self) -> BinaryTree | None:
        """This is the second function we have to implement"""
        # if self.get_right() is None and self.get_parent() is not None:
        #     return self.get_parent()
        # if self.get_right() is not None:
        #     return self.get_right()
        # if current node has right child then go to the right child's left-most node then return it
        # if the current node doesn't have a right child you to to its parent
        # first ancestor where current node is in the left subtree
        # that ancestor is the successor
        # no ancestor return None

from typing import TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, item: T):
        self.item = item
        self.next = None


class SortedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, item: T):
        node = Node(item)

        if self.head is None:
            self.head = node
            self.size += 1
        elif self.head.item > node.item:
            node.next = self.head
            self.head = node
            self.size += 1
            return True
        elif self.head.item < node.item:
            self.head.next = node
            self.size += 1
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        temp_list = self
        while temp_list is not None and temp_list.head is not None:
            print(temp_list.head.item)
            self.head = temp_list.head.next


if __name__ == "__main__":
    slist = SortedList()
    slist.insert(1)
    slist.insert(2)
    slist.insert(0)
    assert len(slist) == 3
    assert slist.insert(3)
    assert slist.insert(3) is False
    print('PASSED')

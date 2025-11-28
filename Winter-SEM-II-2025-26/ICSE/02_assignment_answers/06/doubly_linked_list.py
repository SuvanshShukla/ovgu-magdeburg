class DoublyLinkedNode:
    def __init__(self, item: int = None,
                 next: "DoublyLinkedNode | None" = None,
                 prev: "DoublyLinkedNode | None" = None) -> None:
        self._item = item
        self._next = next
        self._prev = prev

    def get_next(self) -> "DoublyLinkedNode | None":
        return self._next

    def get_item(self) -> int | None:
        return self._item

    def get_prev(self) -> "DoublyLinkedNode | None":
        return self._prev

    def set_next(self, next):
        self._next = next

    def set_prev(self, prev):
        self._prev = prev

    def set_item(self, item):
        self._item = item


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode(next=self)
        self._tail = DoublyLinkedNode(prev=self)
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def add_first(self, item) -> None:
        node = DoublyLinkedNode(item)
        old_head = self._head
        node.set_next(old_head)
        old_head.set_prev(node)
        self._head = node
        self._size += 1

    def get_first(self) -> int:
        if self.is_empty():
            return None
        else:
            return self._head.get_item()

    def remove_first(self) -> int | None:
        if self.is_empty():
            return None
        else:
            first_item = self._head.get_item()
            self._head = self._head.get_next()
            self._size -= 1
            return first_item

    def add_last(self, item) -> None:
        node = DoublyLinkedNode(item)
        old_tail = self._tail
        old_tail.set_next(node)
        node.set_prev(old_tail)
        self._tail = node
        self._size += 1

    def get_last(self) -> int | None:
        if self.is_empty():
            return None
        return self._tail.get_item()

    def remove_last(self) -> int | None:
        if self.is_empty():
            return None
        else:
            item = self._tail.get_item()
            self._tail = self._tail.get_prev()
            self._size -= 1
            return item

    def at(self, index: int) -> int:
        if index > self._size:
            raise IndexError
        elif self.is_empty():
            return None
        else:
            current = self.get_first()
            i = 0
            while i < index:
                current = self._head.get_next()
                i += 1
            return current.get_item()

    # def __repr__(self):
    #     return f"[{self._head.get_item()}]"


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.add_first(1)
    assert ll.get_first() == 1
    ll.add_first(2)
    assert ll.get_first() == 2
    assert len(ll) == 2
    ll.add_last(0)
    assert ll.get_last() == 0
    assert ll.remove_first() == 2
    assert ll.remove_last() == 0
    assert ll.is_empty() is False
    assert ll.at(0) == 1
    print("ALL TESTS PASSED.")
    pass

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = 0

    def add_first(self, data):
        new = Node(data)
        head = self.head
        old = self.head.next
        new.next = old
        new.prev = head
        old.prev = new
        head.next = new
        self.size += 1

    def add_last(self, data):
        new = Node(data)
        tail = self.tail
        old = self.tail.prev
        new.next = tail
        new.prev = old
        old.next = new
        tail.prev = new
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_first(self):
        if self.is_empty():
            return None
        return self.head.next.data

    def get_last(self):
        if self.is_empty():
            return None
        return self.tail.prev.data

    def __len__(self):
        return self.size

    def remove_first(self):
        first = self.head.next
        new_first = first.next
        new_first.prev = self.head
        self.head.next = new_first
        self.size -= 1
        return first.data

    def remove_last(self):
        last = self.tail.prev
        new_last = last.prev
        new_last.next = self.tail
        self.tail.prev = new_last
        self.size -= 1
        return last.data

    def at(self, index):
        start = self.head.next
        while start is not None and index > 0:
            start = start.next
            index -= 1
        if start is not None and start != self.tail and index == 0:
            return start.data
        raise IndexError


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.add_first(1)
    ll.add_last(2)
    assert ll.is_empty() is False
    assert ll.get_first() == 1
    assert ll.get_last() == 2
    assert len(ll) == 2
    assert ll.remove_first() == 1
    assert len(ll) == 1
    assert ll.remove_last() == 2
    assert len(ll) == 0
    ll.add_first(10)
    ll.add_first(11)
    assert ll.at(1) == 10
    assert DoublyLinkedList().is_empty()
    assert len(DoublyLinkedList()) == 0
    assert DoublyLinkedList().get_first() is None
    pass

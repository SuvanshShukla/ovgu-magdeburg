class RNode:
    def __init__(self, data: int):
        self.data: int = data
        self.prev: RNode = self
        self.next: RNode = self


class Ring:
    def __init__(self):
        self.head = RNode(-1)
        self.tail = RNode(-1)
        self.tail.prev = self.head
        self.tail.next = self.head
        self.head.next = self.tail
        self.head.prev = self.tail
        self.size = 0

    def find(self, x):
        start = self.head.next
        index = 0
        while start is not None and start != self.head and start != self.tail:
            start = start.next
            if start.data == x:
                return start
            index -= 1
        return None

    def insert_before(self, n, pos):
        if pos == 0:
            self.head.prev = n
            self.tail.next = n
            n.next = self.head
            n.prev = self.tail
        ptr = self.find(pos)
        if ptr is not None:
            n.next = ptr
            n.prev = ptr.prev
            ptr.prev = n
            self.size += 1


if __name__ == "__main__":
    ring = Ring()
    node = RNode(10)
    ring.insert_before(node, 0)
    assert ring.find(0) == 10

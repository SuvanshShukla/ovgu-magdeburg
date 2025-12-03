from typing import Any, Optional
import random
from icse_queue import Queue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, item):
        self.queue = [item] + self.queue
        self.size += 1

    def dequeue(self) -> Optional[Any]:
        if self.is_empty():
            return None
        else:
            r = random.randint(0, self.size - 1)
            item = self.queue[r]
            left = self.queue[0:r]
            right = self.queue[r + 1:]
            self.size -= 1
            self.queue = left + right
            return item

    def sample(self) -> Optional[Any]:
        if self.is_empty():
            return None
        else:
            r = random.randint(0, self.size - 1)
            item = self.queue[r]
            return item

    def is_empty(self):
        if self.size <= 0:
            return True
        else:
            return False


if __name__ == "__main__":
    r1 = RandomQueue()
    assert r1.is_empty()
    r1.enqueue(1)
    r1.enqueue(2)
    # assert r1.sample() == 1
    i = r1.dequeue()
    print(i)
    r1.enqueue(10)
    r1.enqueue(11)
    r1.sample() == 10
    print('ALL TEST CASES PASSED.')
    pass

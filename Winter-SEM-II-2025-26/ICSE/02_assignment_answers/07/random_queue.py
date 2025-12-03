from typing import Any, Optional

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
            item = self.queue[0]
            self.queue[1:]
            self.size -= 1
            return item

    def sample(self) -> Optional[Any]:
        if self.is_empty():
            return None
        else:
            item = self.queue[0]
            return item

    def is_empty(self):
        if self.size <= 0:
            return True
        else:
            return False


if __name__ == "__main__":
    pass

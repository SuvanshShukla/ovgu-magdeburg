from typing import Any, Optional

from icse_queue import Queue


class RandomQueue(Queue):
    # TODO: Implement the missing methods.

    def dequeue(self) -> Optional[Any]:
        """Remove and return one random item from the queue (or `None` if the queue is empty)."""
        if self.is_empty:
            return None
        raise NotImplementedError()

    def sample(self) -> Optional[Any]:
        """Returns a random element from the queue (or `None` if the queue is empty)."""
        if self.is_empty:
            return None
        raise NotImplementedError()  # TODO: Implement the method `sample`.


if __name__ == "__main__":
    pass

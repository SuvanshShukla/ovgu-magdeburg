from typing import Any, Optional

from icse_queue import Queue


class RandomQueue(Queue):
    # TODO: Implement the missing methods.

    def dequeue(self) -> Optional[Any]:
        """Remove and return one random item from the queue (or `None` if the queue is empty)."""
        raise NotImplementedError()

    def sample(self) -> Optional[Any]:
        """Returns a random element from the queue (or `None` if the queue is empty)."""
        raise NotImplementedError()  # TODO: Implement the method `sample`.


if __name__ == "__main__":
    pass

# TODO: Remove all lines, that contain "# TODO:"...


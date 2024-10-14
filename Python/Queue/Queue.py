class Queue:
    """This class has Queue implementation with list with size delimiter"""
    def __init__(self, size: int) -> None:
        """Initialize the empty queue"""
        self._queue = []
        self._size = size

    def enqueue(self, value) -> None:
        """Push value to queue"""
        if self._size < len(self._queue):
            raise Exception('queue limit overflow')
        self._queue.append(value)

    def dequeue(self):
        """dequeue element from queue and returns it"""
        if len(self._queue) == 0:
            raise Exception('Can not pop from empty queue')
        return self._queue.pop(0)

    def peak(self):
        """Return last element in stack """
        return self._queue[0]

    def size(self) -> int:
        """Returns size of the stack"""
        return len(self._queue)

    def is_empty(self) -> bool:
        """Return True if stack is empty else False"""
        return len(self._queue) == 0


    def get_queue(self):
        """Return protected stack for testing purpose """
        return self._queue



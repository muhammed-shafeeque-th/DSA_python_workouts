class Queue:
    """This class has Queue implementation with list with capacity delimiter"""
    def __init__(self, capacity: int) -> None:
        """Initialize the empty queue"""
        self._stack = []
        self._extra_stack = []
        self._capacity= capacity

    def enqueue(self, value) -> None:
        """Push value to queue"""
        if self._capacity< len(self._stack):
            raise OverflowError('queue limit overflow')
        self._stack.append(value)

    def dequeue(self) -> int:
        """dequeue element from queue and returns it"""
        if len(self._stack) == 0:
            raise IndexError('Can not pop from empty queue')
        while self._stack:
            self._extra_stack.append(self._stack.pop())
        elem = self._extra_stack.pop()
        while self._extra_stack:
            self._stack.append(self._extra_stack.pop())
        return elem

    def peak(self):
        """Return last element in stack """
        return self._stack[0]

    def capacity(self) -> int:
        """Returns capacity of the stack"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Return True if stack is empty else False"""
        return len(self._stack) == 0


    def get_queue(self):
        """Return protected stack for testing purpose """
        return self._stack



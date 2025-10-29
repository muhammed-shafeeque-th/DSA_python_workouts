class Stack:
    """This class has stack implementation with list with size delimiter"""
    def __init__(self, capacity: int) -> None:
        """Initialize the empty queues for implement stack using stack"""
        self._queue = []
        self._extra_queue = []
        self._capacity = capacity

    def push(self, value) -> None:
        """Push value to stack"""
        if self._capacity <= len(self._queue):
            raise OverflowError('stack overflow')
        self._extra_queue.append(value)
        while self._queue:
            self._extra_queue.append(self._queue.pop(0))
        while self._extra_queue:
            self._queue.append(self._extra_queue.pop(0))

    def pop(self):
        """Pop element from stack and returns it"""
        if len(self._queue) == 0:
            raise IndexError('Can not pop from empty stack')
        elm = self._queue.pop(0)
        return elm

    def peak(self):
        """Return last element in stack """
        return self._queue[0]

    def size(self) -> int:
        """Returns size of the stack"""
        return len(self._queue)

    def is_empty(self) -> bool:
        """Return True if stack is empty else False"""
        return len(self._queue) == 0

    def get_stack(self):
        """Return protected stack for testing purpose """
        return self._queue



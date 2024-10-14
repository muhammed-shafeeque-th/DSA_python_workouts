class Stack:
    """This class has stack implementation with list with size delimiter"""
    def __init__(self, size: int) -> None:
        """Initialize the empty stack"""
        self._stack = []
        self._size = size

    def push(self, value) -> None:
        """Push value to stack"""
        if self._size < len(self._stack):
            raise Exception('stack overflow')
        self._stack.append(value)

    def pop(self):
        """Pop element from stack and returns it"""
        if len(self._stack) == 0:
            raise Exception('Can not pop from empty stack')
        return self._stack.pop()

    def peak(self):
        """Return last element in stack """
        return self._stack[-1]

    def size(self) -> int:
        """Returns size of the stack"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Return True if stack is empty else False"""
        return len(self._stack) == 0


    def get_stack(self):
        """Return protected stack for testing purpose """
        return self._stack



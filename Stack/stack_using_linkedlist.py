class Stack:
    """Stack datastructure implemented using LinkedList with its methods"""

    class _Node:
        """Private class to create Node which represent linkedlist stack Node"""
        def __init__(self, val: int) -> None:
            """Instantiate Node"""
            self._val = val
            self._next = None

    def __init__(self) -> None:
        """Instantiate the stack object with credentials"""
        self._top = None
        self._size = 0

    def push(self, val: int) -> None:
        """Push value to the top of the stack"""
        node = self._Node(val)
        if self._top is None:
            self._top = node
            self._size += 1
            return
        node._next = self._top
        self._top = node
        self._size += 1

    def pop(self) -> int:
        """Pops the top element from stack and returns it"""
        # check weather stack is empty or not
        if self._top is None:
            raise Exception("can not pop from empty stack")
        elem = self._top
        self._top = self._top._next
        self._size -= 1
        return elem._val

    def is_empty(self) -> bool:
        """Returns True if stack is empty else False"""
        return self._size == 0

    def peak(self) -> int:
        """Returns the top value from stack"""
        return self._top._val

    def get_stack(self) -> list:
        """Return Stack values in list"""
        lst = []
        curr = self._top
        while curr:
            lst.append(curr._val)
            curr = curr._next
        return lst

    def size(self) -> int:
        """Returns size of the stack"""
        return self._size












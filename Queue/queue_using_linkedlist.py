class Queue:
    """Queue datastructure implemented using LinkedList with its methods"""

    class _Node:
        """Private class to create Node which represent linkedlist queue Node"""
        def __init__(self, val: int) -> None:
            """Instantiate Node"""
            self._val = val
            self._next = None


    def __init__(self) -> None:
        """Instantiate the queue object with credentials"""
        self._front = None
        self._back = None
        self._size = 0

    def enqueue(self, val: int) -> None:
        """Add value to end of the queue"""
        node = self._Node(val)
        if self._back is None:
            self._back = node
            self._front = node
            self._size += 1
            return
        self._back._next = node
        self._back = node
        self._size += 1

    def dequeue(self) -> int:
        """Pops the top element from queue and returns it"""
        # check weather queue is empty or not
        if self._back is None:
            raise Exception("can not pop from empty queue")
        elif self._front._next is None:
            elem = self._front
            self._back = self._front = None
            return elem._val
        elem = self._front
        self._front = self._front._next
        self._size -= 1
        return elem._val

    def is_empty(self) -> bool:
        """Returns True if queue is empty else False"""
        return self._size == 0

    def front(self) -> int:
        """Returns the top value from queue"""
        return self._front._val

    def get_queue(self) -> list:
        """Return queue values in list"""
        lst = []
        curr = self._front
        while curr:
            lst.append(curr._val)
            curr = curr._next
        return lst

    def size(self) -> int:
        """Returns size of the queue"""
        return self._size












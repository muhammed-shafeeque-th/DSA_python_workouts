class Linked_List:
    """class Containing Linked List methods"""
    class _Node:
        """Private class for storing doubly Linked nodes"""
        __slots__ = '_val', '_next', '_prev'

        def __init__(self, val: int) -> None:
            """Node constructor"""
            self._val = val
            self._next = None
            self._prev = None

    def __init__(self) -> None:
        """Linked List constructor"""
        self._head = self._Node(None)
        self._tail = self._Node(None)
        self._head._next = self._tail
        self._tail._prev = self._head

        self._size = 0  # Number of Values in the list

    def insert_at_end(self, value: int) -> None:
        """Add element at the last end of the list"""
        node = self._Node(value)
        last_value = self._tail._prev
        node._next = self._tail
        self._tail._prev = node
        node._prev = last_value
        last_value._next = node
        self._size += 1

    def insert_at(self, val: int, pos: int) -> None:
        """Insert an element or value at a specified Index, Index range(0 to n)"""
        if pos < 0:
            raise IndexError('Invalid Index, index must be valid ')
        node = self._Node(val)
        if pos > self._size-1:
            self._tail._prev._next = node
            node._prev = self._tail._prev
            node._next = self._tail
            self._tail._prev = node
            return
        curr = self._head
        for i in range(1, pos):
            curr = curr._next
        node._next = curr._next
        curr._next._prev = node
        curr._next = node
        node._prev = curr
        self._size += 1

    def get_element_at(self, pos) -> int:
        """Get an element with index"""
        if 0 > pos or pos >= self._size:
            raise IndexError('Index out of range')

        if self._size == 0:
            raise ValueError('value does not found')

        curr = self._head
        for i in range(0, pos+1):
            curr = curr._next
        return curr._val

    def delete_element(self, value) -> None:
        """Delete an element with a specific value"""

        # Ensure list is not Empty
        if self._size == 0:
            raise ValueError('Can not remove %d from empty list', value)
        curr = self._head._next
        while curr._val is not None:
            curr = curr._next
            if curr._val is value:
                curr._prev._next = curr._next
                curr._next._prev = curr._prev
                self._size -= 1
                return

        raise ValueError('Value does not exist in list')

    def remove_element_at(self, pos: int) -> None:
        """Delete an element with Index"""

        # Ensure list is not Empty
        if self._size == 0:
            raise IndexError('Can not remove from empty list')
        # Check the validity of index
        if 0 >= pos >= self._size:
            raise IndexError("Index %d out of range ", pos)
        curr = self._head._next
        for i in range(pos):
            curr = curr._next
        curr._prev._next = curr._next
        curr._next._prev = curr._prev
        self._size -= 1
        return

    def to_list(self):
        """Return values in the linked list as list"""
        lst = []
        curr = self._head._next
        while curr._val is not None:
            lst.append(curr._val)
            curr = curr._next
        return lst

    def __str__(self) -> str:
        """Return string representation of list"""
        # Empty list -> []
        # List with values -> [n, n+1, ..]

        if self._size == 0:
            return "[]"
        return_string = '['
        curr = self._head._next
        while curr._val is not None:
            return_string += str(curr._val) + ', '
            curr = curr._next
        return return_string[:-2] + ']'

    def __len__(self) -> int:
        """Returns the number of values in the list """
        return self._size

    def __iter__(self):
        """Creating an iter-index-counter for the for-loop"""
        # Initialize a new attribute for walking thorough list
        self._iter_index = 0
        return self

    def __next__(self):
        """Used to grab the next value in the list """
        # using the attribute that you initialised with __iter__()
        # Fetch next value and returns it
        # If no more value to fetch , Raise StopIteration exception

        if self._iter_index == self._size:
            raise StopIteration
        curr = self.get_element_at(self._iter_index)
        self._iter_index += 1
        return curr









#Circular Doubly LinkedList

class CircularDoublyLinkedList:
    """"
    Circular Doubly LinkedList workout
     --Covered almost all topics(*)
        -- Add not at end -> None
        -- Add not at beginning -> None
        -- Insert at specific position -> None
        -- Check if a value exist in the list or not -> bool
        -- Print forward -> None
        -- Print backward -> None
        -- Delete Node -> None
        -- Reverse list -> None
        -- Find middle value -> _Node

     """


    class _Node:
        def __init__(self, value):
            self._value = value
            self._prev = None
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None



    def insert_at_beggning(self, value: _Node) -> None:
        node = self._Node(value)
        node._next = self._head
        self._head._prev = node
        self._head = node
        self._tail._next = self._head
        self._head._prev = self._tail

    def insert_at_end(self, value: _Node) -> None:
        node = self._Node(value)
        if not self._head and not self._tail:
            self._head = node
            self._tail = node
            return
        self._tail._next = node
        node._prev = self._tail
        self._tail = node
        self._tail._next = self._head
        self._head._prev = self._tail


    def insert_at_position(self, value: _Node, pos: int) -> None:
        node = self._Node(value)
        if not self._head:
            self._tail = node
            self._head = node
            return
        curr = self._head
        i = 0
        while curr:
            i += 1
            if 1 == pos:
                self.insert_at_beggning(value)
                return
            if i == pos:
                node._prev = curr._prev
                curr._prev._next = node
                node._next = curr
                curr._prev = node
                return
            curr = curr._next
        if pos > i:
            curr._next = node
            node._prev = curr
            return

    def is_exist(self, value: _Node) -> bool:
        node = self._head
        while node:
            if node.value == value:
                return True
            node = node._next
        return False

    def find_middle(self) -> _Node or None:
        slow = self._head
        fast = self._head._next
        if not self._head:
            return print('empty LL')
        if not self._head._next:
            return self._head._value
        while (fast and fast != self._head) and (fast._next and fast._next != self._head) :
            slow = slow._next
            fast = fast._next._next

        return slow._value

    def reverse(self) -> None:
        # Handle the edge Case
        if self._head is None :
            return
        curr = self._head
        nextt = None
        while curr != self._tail:
            print(curr._next._value, curr._prev._value)
            nextt = curr._next
            curr._next, curr._prev = curr._prev, nextt
            curr = nextt
        curr._next, curr._prev = curr._prev, nextt


    def print_forward(self) -> None:
        if not self._head:
             return print('Empty LL')
        node = self._head
        while node != self._tail:
            print(node._value, end=' -> ')
            node = node._next
        print(node._value ," -> None")

    def is_circular(self) -> bool:
        slow = self._head
        fast = self._head._next
        while slow != fast:
            if not fast and not fast._next:
                return False
            slow = slow._next
            fast = fast._next._next
        return True

    def print_backward(self) -> None:
        if not self._tail:
             return print('Empty LL')
        node = self._tail
        while node != self._head:
            print(node._value, end=' -> ')
            node = node._prev
        print(node._value ," -> None")

    def delete_node(self, value: int) -> None:
        if not self._head:
            return print('LL is empty')
        if value == self._head._value:
            self._head = self._head._next
            self._head._prev = self._tail
            return
        if value == self._tail._value:
            self._tail._prev._next = self._head
            self._tail = self._tail._prev
            self._tail._next = self._head
            return
        node = self._head
        while node:
            if node._value == value:
                node._next._prev = node._prev
                node._prev._next = node._next
                return
            node = node._next
        # Return if the value is not exist with a print statement
        return print('value does not found the list')
    def __str__(self):
        str(self.print_forward())


ll = CircularDoublyLinkedList()
arr = [1, 34, 54, 56, 23, 50, 22, 52, 23, 53, 65, 22]
for x in arr:
    ll.insert_at_end(x)

# ll.print_forward()
# ll.print_backward()
# ll.insert_at_beggning(10)
# ll.print_forward()
# ll.insert_at_position(4, 6 )
ll.print_forward()
# ll.print_backward()
# print(ll.find_middle())
ll.reverse()
ll.print_forward()
# print(ll.is_circular())
# #
# ll.delete_node(54)
# ll.print_forward()







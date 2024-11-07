#Doubly LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None



    def insert_at_beggning(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node


    def insert_at_position(self, value, pos):
        node = Node(value)
        if not self.head:
            self.tail = node
            self.head = node
            return
        curr = self.head
        i = 0
        while curr:
            i += 1
            if 1 == pos:
                self.head.prev = node
                self.head = node
                node.next = curr
                return
            if i == pos:
                node.prev = curr.prev
                curr.prev.next = node
                node.next = curr
                curr.prev = node
                return
            curr = curr.next
        if pos > i:
            curr.next = node
            node.prev = curr
            return

    def is_exist(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def find_middle(self):
        slow = self.head
        fast = self.head
        if not self.head:
            return print('empty LL')
        if not self.head.next:
            return self.head.value
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

    def reverse(self):
        curr = self.head
        nextt = None
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        self.head = prev

    def print_forward(self):
        if not self.head:
             return print('Empty LL')
        node = self.head
        while node:
            print(node.value, end=' -> ')
            node = node.next
        print("None")

    def print_backward(self):
        if not self.tail:
             return print('Empty LL')
        node = self.tail
        while node:
            print(node.value, end=' -> ')
            node = node.prev
        print("None")

    def delete_node(self, value: int) -> None:
        if not self.head:
            return print('LL is empty')
        if value == self.head.value:
            self.head = self.head.next
            self.head.prev = None
            return
        node = self.head
        while node:
            if node.value == value:
                node.next.prev = node.prev
                node.prev.next = node.next
                return
            node = node.next
        # Return if the value is not exist with a print statement
        return print('value does not found the list')



ll = DoublyLinkedList()
arr = [1, 34, 54, 56, 23, 50, 22, 52, 23, 53, 65, 22]
for x in arr:
    ll.insert_at_end(x)

ll.print_forward()
# ll.print_backward()
ll.insert_at_beggning(10)
ll.print_forward()
print(ll.find_middle())
ll.insert_at_position(4, 6 )
ll.print_forward()
# ll.print_backward()

print(ll.find_middle())
# ll.reverse()
# ll.print_forward()
#
# ll.delete_node(54)
# ll.print_forward()







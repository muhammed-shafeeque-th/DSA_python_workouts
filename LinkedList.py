#Create node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



#LinkedList DS
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def insert_at_position(self, value, pos):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        curr = self.head
        i = 0
        prev = None
        while curr:
            i += 1
            if 1 == pos:
                self.head = node
                node.next = curr
                return
            if i == pos:
                prev.next = node
                node.next = curr
                return
            prev = curr
            curr = curr.next
        if pos > i:
            curr.next = node
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

    def print(self):
        if not self.head:
             return print('Empty LL')
        node = self.head
        while node:
            print(node.value, end=' -> ')
            node = node.next
        print("None")

    def delete_node(self, value: int) -> None:
        if not self.head:
            return print('LL is empty')
        if value == self.head.value:
            self.head = self.head.next
            return
        prev = None
        node = self.head
        while node:
            if node.value == value:
                prev.next = node.next
                return
            prev = node
            node = node.next
        # Return if the value is not exist with a print statement
        return print('value does not found the list')

    def to_list(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.value)
            node = node.next
        return lst




ll = LinkedList()
arr = [1, 34, 54, 56, 23, 50, 22, 52, 23, 53, 65, 22]
for x in arr:
    ll.insert_at_end(x)

ll.print()
# ll.insert_at_beggning(10)
# ll.print()
print(ll.find_middle())
ll.insert_at_position(4, 6 )
ll.print()
# print(ll.find_middle())
ll.reverse()
ll.print()

ll.delete_node(54)
ll.print()










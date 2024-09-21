import unittest
from  LinkedList import *

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.ll = LinkedList()
    def test_insert(self) -> None:
        self.ll.insert_at_end(24)
        self.ll.insert_at_end(54)
        self.assertEqual(self.ll.to_list(), [24, 54],'values should be [24, 54]')

    def test_delete(self):
        self.ll.insert_at_end(24)
        self.ll.insert_at_end(5)
        self.ll.insert_at_end(21)
        self.ll.insert_at_end(50)
        self.ll.delete_node(50)
        self.assertEqual(self.ll.to_list(),[24, 5, 21],'values should be [24, 5, 21]')
        self.ll.delete_node(24)
        self.assertEqual(self.ll.to_list(), [5, 21], 'values must be [5, 21]')

    def test_delete_noneExisting(self):
        self.ll.insert_at_end(54)
        self.ll.delete_node(77)
        self.assertEqual(self.ll.to_list(),[54])


if __name__ == '__main__':
    unittest.main()
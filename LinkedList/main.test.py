import unittest
from main import *

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.ll = Linked_List()
        self._arr = [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]
    def test_insert(self) -> None:
        for x in self._arr:
            self.ll.insert_at_end(x)
        self.assertEqual(self.ll.to_list(), [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23],'Mismatch values while insert and end')

    def test_delete(self):
        for x in self._arr:
            self.ll.insert_at_end(x)
        self.ll.delete_element(54)
        self.assertEqual(self.ll.to_list(),[1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23],'values should be [1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]')
        self.ll.delete_element(343)
        self.assertEqual(self.ll.to_list(),[1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 2, 23],'values should be [1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 2, 23]')

    def test_delete_at_index(self):
        for x in self._arr:
            self.ll.insert_at_end(x)
        self.ll.remove_element_at(4)
        self.ll.remove_element_at(3)
        self.assertEqual(self.ll.to_list(),[1, 54, 64, 21, 87, 98, 345, 67, 34, 343, 2, 23],'values should be [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]')


if __name__ == '__main__':
    unittest.main()



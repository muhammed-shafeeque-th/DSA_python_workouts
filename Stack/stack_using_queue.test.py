import unittest
from stack_using_queue import *


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack(20)
        self._arr = [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]

    def test_push(self) -> None:
        for x in self._arr:
            self.stack.push(x)
        self.assertEqual(self.stack.get_stack(), [23, 2, 343, 34, 67, 345, 98, 87, 21, 34, 55, 64, 54, 1],'Mismatch values while insert ')

    def test_pop(self):
        for x in self._arr:
            self.stack.push(x)
        self.stack.pop()
        self.assertEqual(self.stack.get_stack(),[2, 343, 34, 67, 345, 98, 87, 21, 34, 55, 64, 54, 1],'values should be [1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2')
        self.stack.push(343)
        self.assertEqual(self.stack.get_stack(),[343, 2, 343, 34, 67, 345, 98, 87, 21, 34, 55, 64, 54, 1],'values should be [1, 64, 55, 34, 21, 87, 98, 345, 67, 34, 2, 343 ]')

    def test_size(self):
        for x in self._arr:
            self.stack.push(x)
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(self.stack.size(),len(self._arr) + 2,'Incorrect size')

    def test_peak(self):
        for x in self._arr:
            self.stack.push(x)
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(self.stack.peak(),3,'Validate peak method')

    def test_is_empty(self):
        for x in self._arr:
            self.stack.push(x)
        self.stack.push(4)
        self.stack.push(3)
        self.assertEqual(self.stack.is_empty(), False, 'Validate is empty method')


if __name__ == '__main__':
    unittest.main()



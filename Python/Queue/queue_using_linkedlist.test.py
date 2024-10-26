import unittest
from queue_using_linkedlist import *

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self._queue = Queue()
        self._arr = [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]
    def test_enqueue(self) -> None:
        for x in self._arr:
            self._queue.enqueue(x)
        self.assertEqual(self._queue.get_queue(), [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23],'Mismatch values while insert ')

    def test_dequeue(self):
        for x in self._arr:
            self._queue.enqueue(x)
        self._queue.dequeue()
        self.assertEqual(self._queue.get_queue(),[54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23],'values should be [54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23])')
        self._queue.enqueue(343)
        self.assertEqual(self._queue.get_queue(),[54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23, 343],'values should be [54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23, 343]')

    def test_size(self):
        for x in self._arr:
            self._queue.enqueue(x)
        self._queue.enqueue(4)
        self._queue.enqueue(3)
        self.assertEqual(self._queue.size(),len(self._arr) + 2,'Incorrect size')

    def test_peak(self):
        for x in self._arr:
            self._queue.enqueue(x)
        self._queue.enqueue(4)
        self._queue.enqueue(3)
        self.assertEqual(self._queue.front(),1,'Validate peak method')

    def test_is_empty(self):
        for x in self._arr:
            self._queue.enqueue(x)
        self._queue.enqueue(4)
        self._queue.enqueue(3)
        self.assertEqual(self._queue.is_empty(), False, 'Validate is empty method')


if __name__ == '__main__':
    unittest.main()
    



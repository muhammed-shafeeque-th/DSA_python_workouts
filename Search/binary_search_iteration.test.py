import unittest
from binary_search_iteration import *

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self._arr = [1, 2, 3, 4, 6, 7, 9, 12, 14, 16, 22, 25, 35, 66, 77, 78, 80, 88, 90]

    def test_for_non_existed_value(self):
        self.assertEqual(binary_search(self._arr, 888), -1,
                         'Search for non existed value in arr')

    def test_for_value(self):
        self.assertEqual(binary_search(self._arr, 3), 2,
                         'Search for  value in arr')

    def test_for_fist_value(self):
        self.assertEqual(binary_search(self._arr, 1), 0,
                         'Search for the fist value in arr')

    def test_for_last_value(self):
        self.assertEqual(binary_search(self._arr, 90), len(self._arr)-1,
                         'Search for the last value in arr')

if __name__ == '__main__':
    unittest.main()
import unittest
from selection_sort import *


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.arr = [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]

    def test_selection_sort1(self) -> None:
        self.assertEqual(selection_sort1(self.arr), [1, 2, 21, 23, 34, 34, 54, 55, 64, 67, 87, 98, 343, 345],
                         "Values of arr sort in ascending order")

    def test_selection_sort2(self) -> None:
        self.assertEqual(selection_sort2(self.arr), [345, 343, 98, 87 , 67, 64, 55, 54, 34, 34, 23, 21, 2, 1],
                         "Values of arr sort in descending order")

    def test_selection_sort_with_reversed1(self) -> None:
        self.assertEqual(selection_sort_with_reverse(self.arr, reversed=True), [345, 343, 98, 87, 67, 64, 55, 54, 34, 34, 23, 21, 2, 1],
                         "Reversed flag true, values of arr sort in descending order")

    def test_selection_sort_with_reversed2(self) -> None:
        self.assertEqual(selection_sort_with_reverse(self.arr),
                         [1, 2, 21, 23, 34, 34, 54, 55, 64, 67, 87, 98, 343, 345],
                         "Reversed flag false, values of arr sort in descending order")


if __name__ == '__main__':
    unittest.main()

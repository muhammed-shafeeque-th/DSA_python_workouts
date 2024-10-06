import unittest
from bubble_sort import *
import time
import  datetime


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.arr = [1, 54, 64, 55, 34, 21, 87, 98, 345, 67, 34, 343, 2, 23]
        self.almost_sorted_arr = [6, 1, 34, 54, 66, 67, 68, 68, 69, 70, 71, 72, 77]

    def test_bubble_sort1(self) -> None:
        self.assertEqual(bubble_sort(self.arr), [1, 2, 21, 23, 34, 34, 54, 55, 64, 67, 87, 98, 343, 345],
                         "Values of arr sort in ascending order")

    def test_bubble_sort_optimized(self) -> None:
        self.assertEqual(optimized_bubble_sort(self.arr), [1, 2, 21, 23, 34, 34, 54, 55, 64, 67, 87, 98, 343, 345],
                         "Values of arr sort in ascending order with optimized method")

    def test_bubble_sort_with_reversed1(self) -> None:
        self.assertEqual(optimized_bubble_sort_with_reversed(self.arr, reversed=True), [345, 343, 98, 87, 67, 64, 55, 54, 34, 34, 23, 21, 2, 1],
                         "Reversed flag true, values of arr sort in descending order")

    def test_bubble_sort_with_reversed2(self) -> None:
        self.assertEqual(optimized_bubble_sort_with_reversed(self.arr),
                         [1, 2, 21, 23, 34, 34, 54, 55, 64, 67, 87, 98, 343, 345],
                         "Reversed flag false, values of arr sort in descending order")

    def test_verify_optimized_method(self) -> None:
        un_start_time = datetime.datetime.now()
        bubble_sort(self.almost_sorted_arr)
        un_end_time = datetime.datetime.now()
        unoptimized_tm = un_start_time - un_end_time
        op_start_time = datetime.datetime.now()
        bubble_sort(self.almost_sorted_arr)
        op_end_time = datetime.datetime.now()
        optimized_tm = op_start_time - op_end_time
        print(optimized_tm.microseconds, unoptimized_tm.microseconds)
        self.assertEqual(unoptimized_tm.microseconds > optimized_tm.microseconds, True,
                         "Checks whether optimized method is better that unoptimized")


if __name__ == '__main__':
    unittest.main()

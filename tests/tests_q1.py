import unittest
from Q1 import two_sum 
from ed_utils.decorators import number
from data_structures.linked_list import LinkedList
from tests.conversions import AR, SL
from typing import List


class Test_Q1(unittest.TestCase):
    def customAssertEqual(self, actual: List[int], expected: List[int]):
        if len(actual) != len(expected):
            self.fail(f"Actual length, {len(actual)}, doesn't match expected length, {len(expected)}")
        
        if not ((actual[0] == expected[0] and actual[1] == expected[1]) or (actual[1] == expected[0] and actual[0] == expected[1])):
            self.fail(f"Actual elements ({actual[0]}, {actual[1]}) does match expected elements ({expected[0]}, {expected[1]})")


    @number("1.1")
    def test_examples(self):
        self.customAssertEqual(two_sum(SL([2,7,11,15]), 13), AR([0,2]))
        self.customAssertEqual(two_sum(SL([2,3,4]), 6), AR([0,2]))
        self.customAssertEqual(two_sum(SL([3,3]), 6), AR([0,1]))
        

    @number("1.2")
    def test_extra(self):
        self.customAssertEqual(two_sum(SL([-3,3,4,90]), 0), AR([0,1]))
        self.customAssertEqual(two_sum(SL([-5, -4, -3, -2, -1]), -8), AR([0, 2]))

if __name__ == '__main__':
    unittest.main()
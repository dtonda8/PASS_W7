import unittest
from Q1 import two_sum 
from ed_utils.decorators import number
from data_structures.linked_list import LinkedList
from tests.conversions import LLtoList, LL, AL
from typing import List


class Test_Q1(unittest.TestCase):
    def customAssertEqual(self, actual: List[int], expected: List[int]):
        if len(actual) != len(expected):
            self.fail(f"Actual length, {len(actual)}, doesn't match expected length, {len(expected)}")
        
        if not ((actual[0] == expected[0] and actual[1] == expected[1]) or (actual[1] == expected[0] and actual[0] == expected[1])):
            self.fail(f"Actual elements ({actual[0]}, {actual[1]}) does match expected elements ({expected[0]}, {expected[1]})")


    @number("1.1")
    def test_examples(self):
        self.customAssertEqual(two_sum(AL([2,7,11,15]), 13), [0,2])
        self.customAssertEqual(two_sum(AL([3,2,4]), 6), [1,2])
        self.customAssertEqual(two_sum(AL([3,3]), 6), [0,1])
        

    @number("1.2")
    def test_extra(self):
        self.customAssertEqual(two_sum(AL([-3,4,3,90]), 0), [0,2])
        self.customAssertEqual(two_sum(AL([-1,-2,-3,-4,-5],), -8), [2,4])

if __name__ == '__main__':
    unittest.main()
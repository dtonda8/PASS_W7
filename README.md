# PASS_W7
Welcome to week 7's coding activity. No in-builts allowed :)


### Q1: Two Sum (adapted from [here](https://leetcode.com/problems/two-sum/))
Given an array of integers `nums` and an integer `target`, return indices of two numbers in `nums` such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:  
**Input**: `nums` = [2,7,11,15], `target` = 13  
**Output**: [0,2]  
Explanation: Because nums[0] + nums[2] == 13, we return [0, 2].

Example 2:  
**Input**: `nums` = [2,3,4], `target` = 6  
**Output**: [1,2]  


Example 3:  
**Input**: `nums` = [3,3], `target` = 6  
**Output**: [0,1]  


Challenge: Can you come up with an algorithm that is less than O($n^2$) time complexity? If you assume that all dictionary operations take O(1), could you come up with a solution that is O(n) time complexity? 


---
### Testing you algorithm
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For if issues persist on Mac,  see this: https://docs.python-guide.org/starting/install3/osx/

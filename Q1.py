from data_structures.abstract_list import List
from data_structures.hash_table import LinearProbeTable
from data_structures.referential_array import ArrayR

"""
For every index, i, check if you've previously seen a number equal to (`target - nums[i]`). 
If so, retrieve the index of the number (`target - nums[i]`). 
There is a data structure that allows you to check this relatively quick.
"""

def two_sum(nums: List[int], target: int) -> ArrayR[int]:
	# Prep answer
	ans = ArrayR(2)

	# Dictionary mapping (target - nums[idx]) to idx
	history_dictionary = LinearProbeTable()

	for idx in range(len(nums)):
		# Check if we've seen (target - nums[idx]), remember, hash function takes iterables so converting to string 
		key = str(target - nums[idx])

		if key in history_dictionary:
			# we found match, populate ans
			other_idx = history_dictionary[key]
			ans[0] = idx
			ans[1] = other_idx
			#...
			break

		else:
			# add to history dictionary (key to idx)
			history_dictionary[str(nums[idx])] = idx

	return ans


if __name__ == "__main__": 
	pass
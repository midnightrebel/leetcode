"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index_dict = {}  # Renamed from hashmap for clarification
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_dict:
            return [i, index_dict[complement]]
        index_dict[num] = i
    return []  # Explicitly return empty list if no solution found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
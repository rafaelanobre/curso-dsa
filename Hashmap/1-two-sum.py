from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(num) is not None:
                return [hashmap[num], i]
            hashmap[target - num] = i

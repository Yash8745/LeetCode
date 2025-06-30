from typing import List
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        groups = []
        num_to_group = {}
        
        # Form groups of elements that can be swapped with each other
        for num in sorted_nums:
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1  # Map each number to its group index
        
        # Build the result by taking the smallest element from the corresponding group
        result = []
        for num in nums:
            group_idx = num_to_group[num]
            result.append(groups[group_idx].popleft())
        
        return result
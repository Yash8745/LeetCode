from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        counter = Counter(nums)

        for key in counter:
            if key + 1 in counter:
                res = max(res, counter[key] + counter[key + 1])

        return res

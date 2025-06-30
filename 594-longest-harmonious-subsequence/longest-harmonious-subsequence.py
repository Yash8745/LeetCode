from collections import Counter
from itertools import pairwise 
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res=0
        counter=Counter(nums)
        items = sorted(list(counter.items()))  


        for (curr_key, curr_val), (next_key, next_val) in pairwise(items):
            if next_val and abs(curr_key-next_key)==1:

                res=max(curr_val+next_val,res)
        
        return res

        
        
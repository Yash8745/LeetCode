class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        cur_max = values[0]  # Initialize with the first value's score potential
        
        for i in range(1, len(values)):
            # Update result with the maximum score for the current pair
            res = max(res, cur_max + values[i] - i)
            
            # Update cur_max to reflect the best score contribution so far
            cur_max = max(cur_max, values[i] + i)
        
        return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_index={}

        for index,value in enumerate(nums):
            complement=target-value
            if complement in nums_index:
                return [nums_index[complement],index]
            nums_index[value] = index
        
        return []


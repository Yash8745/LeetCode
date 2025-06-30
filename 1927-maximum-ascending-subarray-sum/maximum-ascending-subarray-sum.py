class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Initialize both the current subarray sum and the maximum found so far with the first element.
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate from the second element onward.
        for i in range(1, len(nums)):
            # If the current element is greater than the previous one,
            # add it to the current ascending subarray sum.
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                # If not, reset the current sum to the current element.
                current_sum = nums[i]
            
            # Update the maximum sum encountered.
            max_sum = max(max_sum, current_sum)
        
        return max_sum

        
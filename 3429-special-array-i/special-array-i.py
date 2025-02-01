class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):  # Avoid index error
            if (nums[i] % 2) == (nums[i+1] % 2):  # Same parity → invalid
                return False
        return True  # All pairs checked and valid
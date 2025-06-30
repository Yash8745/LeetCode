class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        res = []
        for fix in range(len(nums) - 2):
            if fix > 0 and nums[fix] == nums[fix - 1]:  # Skip duplicates
                continue
            left, right = fix + 1, len(nums) - 1
            while left < right:
                check_sum = nums[fix] + nums[left] + nums[right]
                if check_sum == 0:
                    res.append([nums[fix], nums[left], nums[right]])
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif check_sum < 0:
                    left += 1  # Increase the sum by moving left pointer to the right
                else:
                    right -= 1  # Decrease the sum by moving right pointer to the left
        return res

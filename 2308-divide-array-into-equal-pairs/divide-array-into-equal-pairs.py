class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
    
    # Count frequency of each number
        count = Counter(nums)
    
    # Check if all numbers have an even count
        for freq in count.values():
            if freq % 2 != 0:
                return False

        return True
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False
        freq = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        return odd_count <= k

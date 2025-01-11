from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Create a max frequency map from words2
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char, count in freq.items():
                max_freq[char] = max(max_freq[char], count)
        
        # Step 2: Filter words1 based on the max frequency map
        result = []
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= count for char, count in max_freq.items()):
                result.append(word)
        
        return result

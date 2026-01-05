from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)
            groups[key].append(word)

        return list(groups.values())

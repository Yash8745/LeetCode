from bisect import bisect_left, bisect_right

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hashmap = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Populate the hashmap
        for index, value in enumerate(words):
            if (value[0] in vowels) and (value[-1] in vowels):
                hashmap[index] = value
        
        # Preprocess keys
        sorted_keys = sorted(hashmap.keys())
        
        # Process queries
        result = []
        for query in queries:
            start, end = query
            # Find the range of keys using binary search
            left = bisect_left(sorted_keys, start)
            right = bisect_right(sorted_keys, end)
            result.append(right - left)
        
        return result

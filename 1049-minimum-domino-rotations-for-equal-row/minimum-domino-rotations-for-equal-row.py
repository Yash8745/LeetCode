from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missingT, missingB = 0, 0
            for i, (top, bottom) in enumerate(zip(tops, bottoms)):
                # ❌ BUG: Incorrect comparison
                if not (top == target or bottom == target): 
                    break
                if top != target:
                    missingT += 1
                if bottom != target:
                    missingB += 1
            else:
                # ✅ The `for-else` clause runs only if `break` is not hit
                return min(missingT, missingB)
        
        return -1  # If no target works

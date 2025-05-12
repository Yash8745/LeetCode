from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()  # Use a set to avoid duplicates

        # Generate all permutations of length 3
        for perm in permutations(digits, 3):
            # Skip if the first digit is 0, since it can't be a valid 3-digit number
            if perm[0] == 0:
                continue

            # Form the number from the 3 digits
            number = perm[0] * 100 + perm[1] * 10 + perm[2]

            # Check if the number is even
            if number % 2 == 0:
                result.add(number)

        # Return the result as a sorted list
        return sorted(result)

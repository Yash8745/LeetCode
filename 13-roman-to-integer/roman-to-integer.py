class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num_list = [roman_map[ch] for ch in s]

        total = 0
        n = len(num_list)

        for i in range(n-1):
            if num_list[i] < num_list[i+1]:
                total -= num_list[i]
            else:
                total += num_list[i]

        total += num_list[-1]

        return total
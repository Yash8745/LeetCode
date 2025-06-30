class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Convert to list of characters
        s_list = list(s)
        maxi = 0
        
        # Reverse shifts and apply cumulative sum
        shifts = list(reversed(shifts))
        
        for i in range(len(shifts)):
            shifts[i] += maxi
            maxi = shifts[i]

        # Reverse shifts back to apply from the start
        shifts = list(reversed(shifts))

        # Apply shifts to each character in the string
        for i in range(len(s_list)):
            # Apply the shift and wrap it around using % 26 (for 'a' to 'z')
            s_list[i] = chr((ord(s_list[i]) - 97 + shifts[i]) % 26 + 97)

        # Join the list of characters back into a string and return
        return ''.join(s_list)

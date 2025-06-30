class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""  # To store the longest palindrome
        max_length = 0  # Length of the longest palindrome
        
        for i in range(len(s)):
            # Odd-length palindromes (single center)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_length:  # Update result if we find a longer palindrome
                    res = s[l:r+1]
                    max_length = r - l + 1
                l -= 1
                r += 1

            # Even-length palindromes (center between two characters)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_length:  # Update result if we find a longer palindrome
                    res = s[l:r+1]
                    max_length = r - l + 1
                l -= 1
                r += 1

        return res

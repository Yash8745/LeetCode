class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            # If we've reached the end of both the string and the pattern
            if i >= len(s) and j >= len(p):
                return True
            
            # If we've reached the end of the pattern but the string is not exhausted
            if j >= len(p):
                return False
            
            # Check if current characters match
            match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))
            
            # If the next character in the pattern is a '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two possibilities: 
                # 1. Skip the '*' and the preceding character (match 0 times)
                # 2. Match the current character and continue to check if it's valid (match > 0 times)
                return (dfs(i, j + 2) or  # Skip '*' and the preceding character
                        (match and dfs(i + 1, j)))  # Match the current character and keep going
            # Otherwise, proceed normally, advancing both string and pattern
            elif match:
                return dfs(i + 1, j + 1)
            
            return False

        return dfs(0, 0)

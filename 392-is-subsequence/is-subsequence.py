class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0:
            return True  # empty string is subsequence of anything
        
        a = b = 0  # pointers for s and t
        
        while b < m:
            if s[a] == t[b]:
                a += 1
                b += 1
                # Only print if still in range
                if a < n and b < m:
                    print(f"value at s[a]= {s[a]} and value at t[b] = {t[b]}")
                # If we've matched all of s, we can return
                if a == n:
                    return True
            else:
                # Only print if still in range
                if a < n and b < m:
                    print(f"-----value at s[a]= {s[a]} and value at t[b] = {t[b]}----")
                b += 1
        
        # If we exit loop, we matched all of s only if a == n
        return a == n
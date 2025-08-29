class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # count odds and evens in 1..n
        odds_n = (n + 1) // 2
        evens_n = n // 2
        
        # count odds and evens in 1..m
        odds_m = (m + 1) // 2
        evens_m = m // 2
        
        # Alice wins if x+y is odd
        return odds_n * evens_m + evens_n * odds_m

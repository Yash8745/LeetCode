class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            if (r, c) in visit:
                return 0
            if grid[r][c] == 0:
                return 0
            visit.add((r, c))
            total = grid[r][c]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                total += dfs(r + dr, c + dc)
            return total
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visit:
                    current_sum = dfs(r, c)
                    res = max(res, current_sum)
        return res
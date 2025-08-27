from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid):
        n, m = len(grid), len(grid[0])

        # 4 diagonal directions
        dirs = {
            0: (1, 1),     # down-right
            1: (1, -1),    # down-left
            2: (-1, -1),   # up-left
            3: (-1, 1),    # up-right
        }
        # clockwise mapping
        clockwise = {0: 1, 1: 2, 2: 3, 3: 0}

        @lru_cache(None)
        def dfs(r, c, dir, expected, turn_used):
            # Out of bounds or mismatch
            if not (0 <= r < n and 0 <= c < m):
                return 0
            if grid[r][c] != expected:
                return 0

            # Flip expected for next step (2 <-> 0, after 1 → 2)
            if expected == 1:
                next_expected = 2
            elif expected == 2:
                next_expected = 0
            else:  # expected == 0
                next_expected = 2

            # Continue straight
            dr, dc = dirs[dir]
            straight = 1 + dfs(r + dr, c + dc, dir, next_expected, turn_used)

            # Try turn if not used
            turn = 0
            if turn_used == 0:
                ndir = clockwise[dir]
                dr2, dc2 = dirs[ndir]
                turn = 1 + dfs(r + dr2, c + dc2, ndir, next_expected, 1)

            return max(straight, turn)

        ans = 0
        # Start only from cells that are '1'
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    for dir in range(4):
                        ans = max(ans, dfs(r, c, dir, 1, 0))

        return ans



        
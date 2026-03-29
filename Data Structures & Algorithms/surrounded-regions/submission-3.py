class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        if not grid: return
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 'O':
                return
            grid[r][c] = 'T'  # Mark as safe
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark safe regions from the left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Step 2: Mark safe regions from the top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 3: Final pass to flip cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'  # Surrounded
                elif grid[r][c] == 'T':
                    grid[r][c] = 'O'  # Revert safe ones
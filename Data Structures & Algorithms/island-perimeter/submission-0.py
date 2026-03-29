class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check all 4 directions
                    # If neighbor is out of bounds OR water (0), it's a perimeter edge
                    
                    # Up
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    # Down
                    if r == rows - 1 or grid[r+1][c] == 0:
                        perimeter += 1
                    # Left
                    if c == 0 or grid[r][c-1] == 0:
                        perimeter += 1
                    # Right
                    if c == cols - 1 or grid[r][c+1] == 0:
                        perimeter += 1
                        
        return perimeter
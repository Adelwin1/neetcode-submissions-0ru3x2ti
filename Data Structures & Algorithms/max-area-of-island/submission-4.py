class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count =0
        n_count = 0

        if not grid:
            return 

        def h(r,c):
            nonlocal count 

            if c<0 or c>=cols or r<0 or r>=rows or grid[r][c]== 0:
                return
            count+=1
            grid[r][c]= 0
            h(r+1,c)
            h(r-1, c)
            h(r, c+1)
            h(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1:
                    count= 0
                    h(r,c)
                    n_count = max(count, n_count)
        return n_count



        
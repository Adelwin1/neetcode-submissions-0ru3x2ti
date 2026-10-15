class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0
        visited = set()

        def h(r, c):
            nonlocal count
            visited.add((r,c))
            d = [(0,1), (1,0), (-1,0), (0,-1)]

            for a, b in d:
                nr, nc =a+r, b+c

                if nr< 0 or nr>= row or nc<0 or nc>= col or grid[nr][nc]==0:
                    count+=1
                elif (nr, nc) not in visited:
                    h(nr, nc)



        for i in range(row):
            for j in range(col):
                st = grid[i][j]
                if st ==1:
                    h(i, j)
                    return count 


      
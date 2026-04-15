class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        ans = []
        p = set()
        a = set()
        if not heights:
            return []
        d = [(-1,0),(1,0), (0,-1), (0,1)]

        def h(r, c ,visited):
            visited.add((r,c))
            for cr, cc in d:
                nr, nc = r+cr, c+cc

                if (0<=nr<rows and 
                   0<=nc<cols and 
                   heights[nr][nc]>= heights[r][c] and 
                   (nr, nc) not in visited):
                   h(nr, nc, visited)

        for c in range(cols):
            h(0, c, p)
        for r in range(rows):
            h(r, 0, p)
        
        for c in range(cols):
            h(rows-1, c, a)
        for r in range(rows):
            h(r, cols-1, a)
        return [[r,c ] for (r,c ) in p & a ]
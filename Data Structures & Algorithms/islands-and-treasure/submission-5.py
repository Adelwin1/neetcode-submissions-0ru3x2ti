class Solution:
    def islandsAndTreasure(self, g: List[List[int]]) -> None:
        q= deque()
        rows, cols = len(g), len(g[0])

        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 0:
                    q.append((i,j))

        di= [(1,0), (0,1),(-1,0),(0,-1)]

        while q:
            r, c = q.popleft()

            for a,b in di:
                nr = r +a
                nc = c+b

                if nr<0 or nr>= rows  or nc<0 or nc>=cols:
                    continue 
                
                if g[nr][nc]!= 2147483647:
                    continue
                

                g[nr][nc] = g[r][c]+1

                q.append((nr, nc))

        
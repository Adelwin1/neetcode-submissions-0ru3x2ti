from collections import deque

class Solution:
    def islandsAndTreasure(self, g: List[List[int]]) -> None:
        INF = 2147483647
        some = deque()

        if not g:
            return None


        rows, cols = len(g), len(g[0])

        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 0:
                    some.append((i, j))

        while some:
            r, c = some.popleft()
            stuff = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for a, b in stuff:
                nr, nc = a + r, b + c

                if nr < 0 or nr>= rows or nc <0 or nc>= cols:
                    continue
                if g[nr][nc] == INF:
                    g[nr][nc] =g[r][c]+1
                    some.append((nr, nc))

                else:
                    continue  
                    

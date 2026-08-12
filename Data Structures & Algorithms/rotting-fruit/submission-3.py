from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, g: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(g), len(g[0])
        fresh = 0
        count = 0

        for i in range(rows):
            for j in range(cols):
                if g[i][j] == 2:
                    q.append((i, j))
                elif g[i][j] == 1:
                    fresh += 1

        di = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q and fresh > 0:

            for _ in range(len(q)):
                r, c = q.popleft()

                for a, b in di:
                    nr, nc = r + a, c + b

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if g[nr][nc] != 1:
                        continue

                    g[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            count += 1

        if fresh > 0:
            return -1

        return count
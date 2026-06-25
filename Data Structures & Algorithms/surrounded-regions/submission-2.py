from collections import deque

class Solution:
    def solve(self, b: List[List[str]]) -> None:
        if not b:
            return

        rows, cols = len(b), len(b[0])
        q = deque()

    
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and b[r][c] == "O":
                    q.append((r, c))
                    b[r][c] = "T"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

      
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if b[nr][nc] != "O":
                    continue

                b[nr][nc] = "T"
                q.append((nr, nc))

     
        for r in range(rows):
            for c in range(cols):
                if b[r][c] == "O":
                    b[r][c] = "X"
                elif b[r][c] == "T":
                    b[r][c] = "O"
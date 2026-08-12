from collections import deque

class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        if not h:
            return []

        rows, cols = len(h), len(h[0])

        pa = deque()
        at = deque()

        l1 = set()
        l2 = set()

        # Pacific: top row
        for c in range(cols):
            pa.append((0, c))
            l1.add((0, c))

        # Atlantic: bottom row
        for c in range(cols):
            at.append((rows - 1, c))
            l2.add((rows - 1, c))

        # Pacific: left column
        for r in range(rows):
            pa.append((r, 0))
            l1.add((r, 0))

        # Atlantic: right column
        for r in range(rows):
            at.append((r, cols - 1))
            l2.add((r, cols - 1))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Pacific BFS
        while pa:
            r, c = pa.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in l1
                ):
                    continue

                if h[nr][nc] < h[r][c]:
                    continue

                l1.add((nr, nc))
                pa.append((nr, nc))

        # Atlantic BFS
        while at:
            r, c = at.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in l2
                ):
                    continue

                if h[nr][nc] < h[r][c]:
                    continue

                l2.add((nr, nc))
                at.append((nr, nc))

        result = l1 & l2

        return [list(cell) for cell in result]
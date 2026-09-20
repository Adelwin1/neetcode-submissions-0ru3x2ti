from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, nc: int, e: List[List[int]]) -> int:

        g = defaultdict(list)
        visited = set()
        count = 0

        for i in range(len(e)):
            a, b = e[i]

            g[a].append(b)
            g[b].append(a)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in g[node]:
                dfs(nei)

        for stuff in range(nc):

            if stuff in visited:
                continue

            dfs(stuff)
            count += 1

        return count
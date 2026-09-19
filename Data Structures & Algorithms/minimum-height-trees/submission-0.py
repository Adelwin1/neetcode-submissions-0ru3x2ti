from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        # Edge case: only one node
        if n == 1:
            return [0]

        # 1. Build adjacency list
        graph = [[] for _ in range(n)]

        # 2. Store degree of each node
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

            degree[a] += 1
            degree[b] += 1

        # 3. Start with all current leaves
        queue = deque()

        for node in range(n):
            if degree[node] == 1:
                queue.append(node)

        remaining = n

        # 4. Peel leaves layer by layer
        while remaining > 2:

            leaf_count = len(queue)

            # Remove this entire outer layer
            remaining -= leaf_count

            for _ in range(leaf_count):

                leaf = queue.popleft()

                # Look at the leaf's neighbors
                for neighbor in graph[leaf]:

                    # Leaf is being removed,
                    # so neighbor loses one connection
                    degree[neighbor] -= 1

                    # If neighbor now has one connection,
                    # it becomes a new leaf
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        # 5. Whatever remains is the center(s)
        return list(queue)
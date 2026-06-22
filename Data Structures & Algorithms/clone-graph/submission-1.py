"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        some = {}

        def dfs(node):

            if node in some:
                return some[node]
            
            copy = Node(node.val)
            some[node] = copy

            for a in node.neighbors:
                copy.neighbors.append(dfs(a))
            return copy
        
        return dfs(node) if node else None

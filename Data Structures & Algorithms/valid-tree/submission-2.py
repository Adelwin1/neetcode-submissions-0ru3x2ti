class Solution:
    def validTree(self, n: int, e: List[List[int]]) -> bool:
        visited = []
        g = {}

        if len(e)!= n-1:
            return False

        for i in range(n):
            g[i] = []

        for a, b in e:
            g[b].append(a)
            g[a].append(b)

        def h(node, parent ):

            if node in visited:
                return False

            visited.append(node)

            for nei in g[node]:
                if nei == parent:
                    continue
                
                if not h(nei, node):
                    return False
            
            return True


        return h(0,-1) and len(visited) ==n

       
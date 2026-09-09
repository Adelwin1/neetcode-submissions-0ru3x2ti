class Solution:
    def checkIfPrerequisite(self, nc: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        

        g= {}
        for i in range(nc):
            g[i] = []

        for a, b in p:
            g[a].append(b)


        def h(node, target, visited):

            if node in visited:
                return False
            visited.add(node)

            if node == target:
                return True 
            

            for nei in g[node]:
                if h(nei, target, visited):
                    return True
                
            return False

        ans = []

        for c, t in q:
            ans.append(h(c,t ,set()))

        return ans

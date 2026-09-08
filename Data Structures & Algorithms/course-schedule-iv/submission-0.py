class Solution:
    def checkIfPrerequisite(self, nc: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:

        g = {i: [] for i in range(nc)}
    
        for a,b in p:
            g[a].append(b)

        def h(node, pr, visited):
            if node == pr:
                return True 

            if node in visited:
                return False

            visited.add(node)
        
            for nei in g[node]:
                if h(nei, pr, visited):
                    return True

            return False
        ans = []

        for pre, course in q:
            if not h(pre, course, set()):
                ans.append(False)
            else:
                 ans.append(True)

        return ans
    





        
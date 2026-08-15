class Solution:
    def canFinish(self, nc: int, pr: List[List[int]]) -> bool:
        path = set()
        finished = set()
        g = {}
        
        for i in range(nc):
            g[i] = []

        for a, b in pr:
            g[b].append(a)

        def h(c):

            if c in path:
                return False
            if c in finished:
                return True

            path.add(c)

            for n in g[c]:
                if not h(n):
                    return False
                
            path.remove(c)
            finished.add(c)
            return True 
                

        
        for course in range(nc):
            if not h(course):
                return False
        return True 

    
        

        

        
class Solution:
    def findOrder(self, nc: int, pr: List[List[int]]) -> List[int]:
        path = set()
        result = []
        finished = set()
        graph  = {}

        for i in range(nc):
            graph[i] = []

        for a, b in pr:
            graph[b].append(a)

        def h(c):
            if c in finished:
                return True 
            if c in path:
                return False
            
            path.add(c)
            for n in graph[c]:
                if not h(n):
                    return False

            result.append(c)
            path.remove(c)
            finished.add(c)

            return True 

        for course in graph:
            if not h(course):
                return []

        return result[::-1]
        
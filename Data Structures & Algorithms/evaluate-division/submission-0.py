from collections import defaultdict
class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(list)


        for (a, b), va in zip(e, v ):
            g[a].append([b, va])
            g[b].append([a, 1/va])


        def h(start, target, product, visited):
            if start == target:
                return product 

            visited.add(start)

            for nei, weight  in g[start]:

                if nei not in visited:
                    result = h(nei, target, weight*product, visited )

                    if result != -1.0:
                        return result 

            return -1.0


        answer = []
        for c ,d in queries:

            if c not in g or d not in g:
                answer.append(-1.0)
                continue

            
            answer.append(h(c, d, 1.0, set()))

        
        return answer 

        
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def h(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return 

            if remaining <0:
                return 
        
            for i in range (start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                h(i+1, path, remaining- candidates[i])
                path.pop()
        h(0, [], target)
        return res
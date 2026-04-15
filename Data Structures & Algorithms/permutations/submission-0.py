class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def h (path, remaining):

            if not remaining:
                res.append(path[:])
                return 
            for i in range(len(remaining)):
                path.append(remaining[i])
                h(path, remaining[:i]+remaining[i+1:])
                path.pop()
        h([], nums)
        return res
            
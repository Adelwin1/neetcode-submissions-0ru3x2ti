
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def h(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining <0:
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                h(i, path, remaining-nums[i])
                path.pop()
            
        h(0, [], target)
        return res
        

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def h(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i >start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                h(i+1, path)
                path.pop()
        h(0, [])
        return res
        
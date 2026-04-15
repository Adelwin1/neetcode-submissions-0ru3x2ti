class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def some(start, pull):
            res.append(pull[:])
            for i in range(start, len(nums)):
                pull.append(nums[i])
                some(i+1, pull)
                pull.pop()
            
        some(0, [])
        return res
            

                
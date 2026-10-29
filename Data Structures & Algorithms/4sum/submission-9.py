class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-3):
            for j in range (i+1, n-2, 1):
                p1 = j+1
                p2 = n-1
                while p1<p2:
                    total = nums[i]+nums[j]+nums[p1]+nums[p2]
                    four = [nums[i], nums[j], nums[p1], nums[p2]]

                    if total == target and four not in res:
                        res.append(four)
                    elif total < target:
                        p1+=1
                    else:
                        p2-=1
                    
        return res 
        
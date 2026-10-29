class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        n = len(nums)

        for i in range(n):
            p1 = i+1
            p2 = n-1
            while p1<p2:
                total = nums[i]+nums[p1]+nums[p2]
                trip = [nums[i], nums[p1], nums[p2]]

                if total == 0 and trip not in res:
                    res.append(trip)
                elif total<0:
                    p1+=1
                else:
                    p2-=1
        return res

                




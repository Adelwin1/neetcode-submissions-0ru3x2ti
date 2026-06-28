class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)


        while l<r:
            mid = (l+r)//2
            b = 0
            s= 1
            for a in nums:
                if a+b<= mid:
                    b+=a
                else:
                    s+=1
                    b = a

            if s<=k:
                r =mid
            else:
                l = mid+1

        return l



        
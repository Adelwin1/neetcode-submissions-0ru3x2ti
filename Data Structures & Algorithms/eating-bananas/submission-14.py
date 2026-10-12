from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r  = 1, max(piles)
        
        

        while l<=r:
            mid  = (r+l)//2
            hours = 0

            for num in piles:
                hours+= ceil(num/mid)

            if hours >h:
                l = mid+1
            else:
                r = mid -1

        return l
    



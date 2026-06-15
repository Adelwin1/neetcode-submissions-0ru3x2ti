import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r  = 1, max(piles)

        while l<=r:
            mid =(l+r)//2
            k = mid
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <=h:
                r = mid -1
                best = k
            else:
                l = mid+1
            
        return best
            




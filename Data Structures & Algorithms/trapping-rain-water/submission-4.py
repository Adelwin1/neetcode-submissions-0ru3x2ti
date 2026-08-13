class Solution:
    def trap(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        lm = 0
        rm = 0
        water = 0

        while l<r:
            if h[l]>= h[r]:
                if h[r]>= rm:
                    rm = h[r]
                
                else:
                    water+= rm - h[r]
                r-=1
            else:
                if h[l]>= lm:
                    lm = h[l]
                
                else:
                    water += lm - h[l]
                l+=1
        return water 


            

        
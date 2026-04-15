class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        max_water = 0
        while l<r:
            diff= r-l
            ch = min(heights[l], heights[r])
            max_water = max(max_water, diff*ch)

            if ch ==heights[l]:
                l+=1
            elif ch == heights[r]:
                r-=1
        return max_water



        
            
                
                

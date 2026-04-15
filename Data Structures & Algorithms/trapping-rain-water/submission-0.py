class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        left = right = 0
        water = 0

        while l<r:
            if height[l]<= height[r]:
                left = max(left, height[l])
                water+= left- height[l]
                l+=1
            else:
                right = max(right, height[r])
                water+= right- height[r]
                r-=1
        return water
        
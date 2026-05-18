class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        p1 = 0
        volume = 0

        while p1 < n:
            p2 = p1+1
            while p2<n:
                n_volume = (p2-p1) * min(h[p1], h[p2])
                volume = max(n_volume, volume)
                p2+=1
            p1+=1
        return volume

        


        
            
                
                

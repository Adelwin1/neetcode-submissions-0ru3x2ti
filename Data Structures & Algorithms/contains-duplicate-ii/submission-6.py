class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        window = set()
        l = 0


        for r in range(n):
            if abs(l-r)>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True 
            
            window.add(nums[r])
        return False

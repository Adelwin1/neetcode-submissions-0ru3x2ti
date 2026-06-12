class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen =set()
        l = 0

        for i in range(n):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
            
            if len(seen)>k:
                seen.remove(nums[l])
                l+=1
            
        return False


        
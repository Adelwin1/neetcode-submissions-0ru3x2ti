class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        n = len(nums)
        boats = []
        p1 = 0
        p2 = n - 1

        while p1 <= p2:
            total = nums[p1]+ nums[p2]
            if total <= limit:
                boats.append(1)
                p1+=1
                p2-=1

            if total> limit:
                boats.append(1)
                p2-=1
        return len(boats)
            
           
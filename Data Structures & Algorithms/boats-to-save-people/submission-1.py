class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        count= 0
        seen = []
        l, r = 0, len(nums)-1
        while l<=r:
            if l ==r:
                seen.append(nums[l])
                break
            so = nums[r]+nums[l]
            if so <= limit:
                count+=1
                l+=1
                r-=1
            elif so > limit:
                seen.append(nums[r])
                r-=1
            else:
                seen.append(nums[l])
                l+=1
            
        for num in seen:
                if num <=limit:
                    count+=1
        return count 

        
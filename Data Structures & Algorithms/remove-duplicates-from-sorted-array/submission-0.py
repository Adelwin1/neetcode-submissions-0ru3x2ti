class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = 0
        p2 = p1+1

        while p1 <n:
            p2 = p1+1
            while p2<n:
                if nums[p1]== nums[p2]:
                    nums.remove(nums[p2])
                    n-=1
                else:
                    p2+=1
            p1+=1
        return len(nums)
           
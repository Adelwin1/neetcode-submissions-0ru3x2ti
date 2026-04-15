class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m_c = 0
        n = len(nums)
        if n ==0:
            return 0
        for i in range(n):
            if nums[i]-1 in nums:
                continue
            else:
                s = set()
                start = nums[i]
                while start+1 in nums:
                    for j in range(0, n, 1):
                        if nums[j]== start+1:
                            s.add(nums[j])
                            start = nums[j]
                        c = len(s)
                        m_c = max(m_c, c)
        return m_c+1


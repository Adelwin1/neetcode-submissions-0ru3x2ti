
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = Counter(nums)
        n = len(nums)
        bucket = [[] for i in range(n+1)]


        for num, idx in fre.items():
            bucket[idx].append(num)
        
        result= []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) ==k:
                    return result

from typing import List

class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        l, r = max(w), sum(w)

        while l < r:
            m = (l + r) // 2

            d = 1
            a = 0

            for weight in w:
                if a + weight <= m:
                    a += weight
                else:
                    d += 1
                    a = weight

            if d <= days:
                r = m
            else:
                l = m + 1

        return l
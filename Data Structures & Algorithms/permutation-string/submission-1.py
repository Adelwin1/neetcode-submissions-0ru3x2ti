from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:k])

        if need == window:
            return True

        for r in range(k, len(s2)):
            window[s2[r]] += 1
            window[s2[r - k]] -= 1

            if window[s2[r - k]] == 0:
                del window[s2[r - k]]

            if window == need:
                return True

        return False
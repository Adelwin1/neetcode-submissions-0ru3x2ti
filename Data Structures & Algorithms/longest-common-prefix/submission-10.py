class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortest = min(strs, key = len)


        for i ,ch in enumerate(shortest):
            for word in strs:
                if word[i]!=ch:
                    return shortest[:i]
        return shortest
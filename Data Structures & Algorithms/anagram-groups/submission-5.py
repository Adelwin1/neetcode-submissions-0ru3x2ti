from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        ana = defaultdict(list)


        for word in strs:
            freq = [0]*26
            for ch in word:
                idx = ord(ch)- ord('a')

                freq[idx]+=1
            ana[tuple(freq)].append(word)

        return list(ana.values())
                

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        count =Counter()
        if n1> n2:
            return False
        s1c = Counter(s1)
        win = Counter(s2[:n1])
        if s1c ==win:
            return True
        for i in range(n1, n2):
            win[s2[i]]+=1
            leftc = s2[i-n1]
            win[leftc]-=1
            if win[leftc]==0:
                del leftc
            if win==s1c:
                return True
        return False

       
    
    
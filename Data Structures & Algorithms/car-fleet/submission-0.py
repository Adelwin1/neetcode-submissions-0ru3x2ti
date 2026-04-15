from typing import List
class Solution:
    def carFleet(self, target: int, p: List[int], sp: List[int]) -> int:
        cars = sorted(zip(p, sp), reverse=True)
        f = 0
        stack = []

        for po, spe in cars:
            time = (target-po)/spe

            if not stack or time>stack[-1]:
                f+=1
                stack.append(time)
            else:
                pass
        return f

            
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in bracket_map:
                stack.append(char)
            else:
                if not stack:
                    return False
                if bracket_map[stack.pop()]!=char:
                    return False
        return not stack

        
        
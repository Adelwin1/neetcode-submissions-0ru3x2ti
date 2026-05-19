class Solution:
    def calPoints(self, s: List[str]) -> int:
        stack = []
        n = len(s)
        suma = 0

        for i in range(n):
            if s[i] == "+":
                stack.append(int(stack[-1] + stack[-2]))

            elif s[i] == "C":
                stack.pop()

            elif s[i] == "D":
                stack.append(int(2 * stack[-1]))

            else:
                stack.append(int(s[i]))

        for num in stack:
            suma += num

        return suma
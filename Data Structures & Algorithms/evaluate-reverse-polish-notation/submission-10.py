class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(n):
            if tokens[i] == "+":
                a = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)
            
            elif tokens[i] == "*":
                b = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(b)
            
            elif tokens[i] == "-":
                c = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(c)
            
            elif tokens[i] == "/" and tokens[i-1] !=0:
                d = int(int(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(d)
            else:
                stack.append(int(tokens[i]))
        return sum(stack)

    
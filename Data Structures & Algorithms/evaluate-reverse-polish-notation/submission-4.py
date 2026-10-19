class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case "+":
                    res = stack[-2] + stack[-1]
                    stack = stack[:-2]
                    stack.append(res)

                case "-":
                    res = stack[-2] - stack[-1]
                    stack = stack[:-2]
                    stack.append(res)

                case "*":
                    res = stack[-2] * stack[-1]
                    stack = stack[:-2]
                    stack.append(res)

                case "/":
                    res = int(stack[-2] / stack[-1])
                    stack = stack[:-2]
                    stack.append(res)

                case _: # token is a number
                    stack.append(int(t))
        
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]

        stack = []

        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                print(a + t + b)
                stack.append(str(int(eval(a + t + b))))
            else:
                stack.append(t)
        
        return int(stack[0])




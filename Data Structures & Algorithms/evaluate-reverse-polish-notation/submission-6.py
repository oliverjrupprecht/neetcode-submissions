class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case "+":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.append(fst + snd)

                case "-":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.append(fst - snd)

                case "*":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.append(fst * snd)

                case "/":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.append(int(fst / snd))

                case _: # token is a number
                    stack.append(int(t))
        
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()

        for t in tokens:
            match t:
                case "+":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.push(fst + snd)

                case "-":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.push(fst - snd)

                case "*":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.push(fst * snd)

                case "/":
                    snd = stack.pop()
                    fst = stack.pop()

                    stack.push(int(fst / snd))

                case _: # token is a number
                    stack.push(int(t))
        
        return stack.top.val

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, v):
        if not self.top:
            self.top = Nd(v, None)
        
        self.top = Nd(v, self.top)
    
    def pop(self):
        value = self.top.val
        self.top = self.top.nxt
        return value

class Nd:
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt
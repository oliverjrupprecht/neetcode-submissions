class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
            return

        currMin = self.stack[-1][0]

        if currMin > val:
            self.stack.append((val, val))
        else:
            self.stack.append((currMin, val))

   
    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
        

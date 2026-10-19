class Solution:
    def isValid(self, s: str) -> bool:
        def matches(l,r):
            if l == "[" and r == "]": return True
            if l == "{" and r == "}": return True
            if l == "(" and r == ")": return True
            return False
            
        stack = []

        for p in s:
            if stack and matches(stack[-1], p): 
                stack.pop()
                continue
            
            stack.append(p)
        
        return not bool(stack)
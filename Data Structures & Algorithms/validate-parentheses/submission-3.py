class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        
        stack = []

        for c in s:
            if c == "(":
                stack.append("(")
            if c == "{":
                stack.append("{")
            if c == "[":
                stack.append("[")
            if c == ")":
                if not stack: return False
                head = stack.pop()
                if head != "(": return False
            if c == "}":
                if not stack: return False
                head = stack.pop()
                if head != "{": return False
            if c == "]":
                if not stack: return False
                head = stack.pop()
                if head != "[": return False
        
        if not stack: 
            return True
        else:
            return False 
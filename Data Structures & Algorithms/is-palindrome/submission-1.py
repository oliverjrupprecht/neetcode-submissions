class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i = 0
        j = len(clean) - 1 

        while i < len(clean):
            if i == j: break
            if clean[i] == clean[j]:
                print(clean[i])
                print(clean[j])
                i += 1
                j -= 1
            else: 
                return False
        
        return True
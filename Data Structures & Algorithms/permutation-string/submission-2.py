class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker = {}
        for char in s1:
            if char in checker:
                checker[char] += 1
            else:
                checker[char] = 1

        for i in range(len(s2)):
            slicee = s2[i: i + len(s1)]
            window = {}
            for char in slicee:
                if char in window: 
                    window[char] += 1
                else:
                    window[char] = 1

            if checker == window:
                return True
            
        return False
                
        
        
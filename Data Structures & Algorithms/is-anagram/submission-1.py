class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        for char in s_dict:
            if t_dict.get(char, 0) == 0:
                return False
            elif t_dict[char] != s_dict[char]:
                return False 
        
        return True
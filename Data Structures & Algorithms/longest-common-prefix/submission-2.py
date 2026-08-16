class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        ret = []

        for i in range(min_len):
            base = strs[0][i]

            for s in strs:
                if base == s[i]:
                    continue
                else:
                    return "".join(ret)
            
            ret.append(base)
        
        return "".join(ret)






        
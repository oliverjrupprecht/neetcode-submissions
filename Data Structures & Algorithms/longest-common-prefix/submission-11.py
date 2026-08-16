class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        ret = []

        for i in range(min_len):
            for s in range(1,len(strs)):
                if strs[s-1][i] == strs[s][i]:
                    continue
                else:
                    return "".join(ret)
            
            ret.append(strs[0][i])
        
        return "".join(ret)






        
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return the longest sequence where each element is 1 greater than the last

        # stacks? add if 1 greater, create a new one at each element? 


        if nums == []:
            return 0

        s = set(nums)

        longest = 0
        for n in nums:
            curr = 0
            while n + 1 in s:
                curr += 1
                n += 1
            
            if curr > longest:
                longest = curr
        
        return longest + 1
            



                

        print(sets)
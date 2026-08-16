class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

                # actual, count
        curr_max = ( 0 , float('-inf'))

        for n in nums:
            if hm.get(n):
                hm[n] = hm[n] + 1
            else:
                hm[n] = 1
            
            if hm[n] > curr_max[1]:
                curr_max = (n, hm[n])

        return curr_max[0]  


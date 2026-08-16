class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        without = sorted([x for x in nums if x != val])

        k = len(without)

        for i in range(len(without)):
            nums[i] = without[i]

        return k
        
            
            
        


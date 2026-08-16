class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        count = {}
        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1

        return False


        
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vtoi = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in vtoi:
                return [vtoi[diff], i]
            
            vtoi[n] = i
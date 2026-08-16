from collections import defaultdict 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dih = {} # values : indexes

        for n in range(len(nums)):
            difference = target - nums[n]

            if difference in dih:
                return [min(n, dih[difference]), max(n, dih[difference])]
            else:
                dih[nums[n]] = n

    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue 
                if nums[i] + nums[j] == target:
                    return [min(i,j), max(i,j)]


        
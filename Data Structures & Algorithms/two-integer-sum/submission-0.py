class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if x == y:
                    continue
                elif nums[x] + nums[y] == target:
                    return [min(x,y), max(x,y)]
                else:
                    continue
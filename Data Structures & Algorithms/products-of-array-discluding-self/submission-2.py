class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(0, len(nums)):
            prod = 1
            for y in range(0, len(nums)):
                if x == y: continue
                else:
                    prod *= nums[y]
                print(f"prod -> {prod}")
            output.append(prod)
        return output
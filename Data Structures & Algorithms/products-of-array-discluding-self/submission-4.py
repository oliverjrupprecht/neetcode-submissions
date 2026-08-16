class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the value at each index in the returned array is the product of all other indexes in the original array.

        out = []
        for i in range(len(nums)):
            elem_value = 1
            for j in range(len(nums)):
                if i == j:
                    continue 
                
                elem_value *= nums[j]
                print(elem_value)
            out.append(elem_value)
        
        return out


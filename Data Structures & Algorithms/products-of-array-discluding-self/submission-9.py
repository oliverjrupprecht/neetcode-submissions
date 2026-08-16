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

    def productExceptSelfFast(self, nums: List[int]) -> List[int]:
        
        product = 1
        one = (False, -1) 

        for i in range(len(nums)):
            if one[0] and nums[i] == 0:
                return [0] * len(nums)
            if nums[i] == 0:
                one = (True, i)
                continue
            
            product *= nums[i]
        
        if one[0]:
            out = [0] * len(nums) 
            out[one[1]] = product  
            return out
        
        return [product // elem for elem in nums]

        

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return an array of 2 integers, from the passed array, that sum to the target. The passed array will be sorted in ascending order.


        
    
        i = 0
        j = len(numbers) - 1
    
        while i < j:        
            sm = numbers[i] + numbers[j]  
            if sm == target:
                return [i+1,j+1]
            elif sm < target:
                i += 1
            else:
                j -= 1
        



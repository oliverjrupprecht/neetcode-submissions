class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elemToCount = {}

        for n in nums:
            if n in elemToCount:
                elemToCount[n] = elemToCount[n] + 1
            else:
                elemToCount[n] = 1
        
        majElem = (0,-math.inf)
        print(elemToCount) 

        for k,v in elemToCount.items():
            if v > majElem[1]:
                majElem = (k,v)

        return majElem[0]
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = {}

        for n in nums:
            if n != val:
                s[n] = s.get(n, 0) + 1
        

        i = 0
        for k, v in s.items():
            for _ in range(v):
                nums[i] = k  
                i += 1

        return i
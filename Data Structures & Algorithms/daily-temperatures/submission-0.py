class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        "return an array where an index i of the array is the amount of days it takes for the temp to be greater" 
        out = []

        for i in range(len(temperatures)):
            j = 1
            while i + j < len(temperatures) and temperatures[i + j] <= temperatures[i]: 
                j += 1
            
            if i + j == len(temperatures):
                out.append(0)
            else:
                out.append(j)
        
        return out

class Solution:
    def dailyTemperaturesBF(self, temperatures: List[int]) -> List[int]:
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


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            print(t)
            while stack and t > stack[-1][1]: # while the stack is not empty and the temp ontop of the stack is less that the current temp
                index, _ = stack.pop()
                out[index] = i - index
        

            stack.append((i,t)) # push to the top of the stack
            print(stack)
            print(out)
        
        
        return out

                

            
                











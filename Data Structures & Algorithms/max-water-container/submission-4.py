class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = self.calculate_area(heights, i, j)

                if area > max_area:
                    max_area = area
                
        return max_area
       
    def calculate_area(self, array, a, b):
        return min(array[a], array[b]) * (max(a,b) - min(a,b))
        # area increases when either, the difference increases, or the min height increases

    def maxAreaB(self, heights: List[int]) -> int:
        increasing = sorted(heights)

        i = 0 


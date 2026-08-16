class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows are sorted in ascending order, first integer of each row is greater than the last integer of the last row
        # i think i am overcomplicating this actually, just find a way to treat matrix as if it is a single array
        low = 0
        high = len(matrix) - 1

        while low <= high:
            m = (low + high) // 2

            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target and matrix[m][len(matrix[m]) - 1] >= target:
                break
            elif matrix[m][0] > target:
                high = m - 1
            else: # if value is not between the low and high of the current row and not less, then it must be in the high side
                low = m + 1 
            
        target_row = m
        print(target_row)
        print()

        low = 0
        high = len(matrix[target_row]) - 1

        while low <= high:
            m = (low + high) // 2
            if matrix[target_row][m] == target:
                return True
            elif matrix[target_row][m] < target:
                low = m + 1
            else:
                high = m - 1
            
        return False

        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.isValidRow(board):
            if self.isValidCol(board):
                if self.isValidSubGrid(board):
                    return True
        return False
    
    def isValidRow(self, board):
        for row in board:
            seen = set ()
            for elem in row:
                if elem == ".":
                    continue
                if elem in seen:
                    print(f"{row} is the problem")
                    return False

                seen.add(elem) 
        
        return True

    def isValidCol(self, board):
        for i in range(9):
            seen = set ()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in seen:
                    print(f"col {i} is the problem")
                    return False

                seen.add(row[i]) 
        
        return True

    def isValidSubGrid(self, board):

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                print(f"the start is {i},{j}")
                if not self.checkSub((i,j), board):

                    return False
        
        return True
                
    def checkSub(self, start, board):
        seen = set ()
        for i in range(start[0], start[0] + 3):
            for j in range(start[1], start[1] + 3):
                print(seen)
                print()
                print(f"i am at {i},{j}")

                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    print(f"element {board[i][j]} is the problem")
                    return False

                seen.add(board[i][j]) 
        return True
        
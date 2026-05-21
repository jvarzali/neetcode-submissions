class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[[] for i in range(3)] for i in range(3)]

        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board)):
                if board[i][j] != ".":
                    col.append(board[i][j])
                    boxes[math.floor(i/3)][math.floor(j/3)].append(board[i][j])
                if board[j][i] != ".":
                    row.append(board[j][i])
                if (len(set(col)) < len(col)):
                    print(col)
                    return False
                if (len(set(row)) < len(row)):
                    print(row)
                    return False
        
        

        for i in range(3):
            for j in range(3):
                if(len(set(boxes[i][j])) < len(boxes[i][j])):
                    return False


        return True
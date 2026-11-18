class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            array = [0] * 9
            for j in range(9):
                val = board[i][j]
                if(val != '.'):
                    index = int(val) - 1
                    array[index] += 1;
                    if(array[index] > 1):
                        return False
        
        for i in range(9):
            array = [0] * 9
            for j in range(9):
                val = board[j][i]
                if(val != '.'):
                    index = int(val) - 1
                    array[index] += 1;
                    if(array[index] > 1):
                        return False
        
 
        for box_row in range(3):
            for box_col in range(3):
                array = [0] * 9
                for i in range(3):
                    for j in range(3):
                        val = board[i + 3 * box_row][j + 3 * box_col]
                        if val != '.':
                            index = int(val) - 1
                            array[index] += 1
                            if array[index] > 1:
                                return False
                

        return True




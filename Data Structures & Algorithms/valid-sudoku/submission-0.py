class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep a hash of the row and col and i guess each box
        
        # for the row
        for row in board:
            elements_encountered = set() # make this a set so lookup is o(1)
            for element in row:
                if element != ".": # dot means its empty space 
                    if element in elements_encountered:
                        return False
                    else:
                        elements_encountered.add(element)

        for col in range(len(board)):
            elements_encountered = set()
            for col_val in range(len(board)):
                element = board[col_val][col]
                if element != ".":
                    if element in elements_encountered:
                        return False
                    else:
                        elements_encountered.add(element)
        # now weve checked the columns 
        def check_3x3(start_row: int, start_col: int):
            elements_encountered_c = set()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    element = board[row][col]
                    if element != ".":
                        if element in elements_encountered_c:
                            return False
                        else:
                            elements_encountered_c.add(element)
            return True
        
        for grid_row in range(0, 9, 3):
            for grid_col in range(0, 9, 3):
                if not check_3x3(grid_row, grid_col):
                    return False
        return True


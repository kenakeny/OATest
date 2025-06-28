class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows=defaultdict(set)
        squares=defaultdict(set)
        for r in range(9):
            for c in range (9):
                if board[r][c]=='.': #we're not adding dots LOL
                    continue
                if (board[r][c] in rows [r] or
                     board[r][c] in columns[c] or 
                    board[r][c] in squares[(r//3),(c//3)]) : return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True
        # essentially cols keeps track of all numbers in a certain coloumn, rows for rows, and squares for squares. we do //3 to floor the results 
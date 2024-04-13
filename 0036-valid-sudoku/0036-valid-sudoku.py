# Approach 1
class Solution(object):
    def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):

                # skip if empty
                if board[r][c] == '.':
                    continue

                # if repeating in rows, cols or squares
                elif (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])

        return True


# Approach 2
class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    res += [(i, element), (element, j), (i//3, j//3, element)]
                    
        return len(res)==len(set(res))

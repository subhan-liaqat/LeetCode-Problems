class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        myset = set()

        def issafe(i, j, value):
            if (i, value) in myset or (value, j) in myset or (i // 3, j // 3, value) in myset:
                return False
            else:
                return True

        def backtrack(board, row, column):
            if row == len(board):
                return True
            if board[row][column] == ".":
                for i in range(1, 10):
                    value = str(i)
                    if issafe(row, column, value):
                        myset.add((row, value))
                        myset.add((value, column))
                        myset.add((row // 3, column // 3, value))
                        board[row][column] = value

                        if column == len(board) - 1:
                            if backtrack(board, row + 1, 0):
                                return True
                        else:
                            if backtrack(board, row, column + 1):
                                return True

                        myset.remove((row, value))
                        myset.remove((value, column))
                        myset.remove((row // 3, column // 3, value))
                        board[row][column] = "."
            else:
                if column == len(board) - 1:
                    if backtrack(board, row + 1, 0):
                        return True
                else:
                    if backtrack(board, row, column + 1):
                        return True

            return False

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] != ".":
                    value = board[row][column]
                    myset.add((row, value))
                    myset.add((value, column))
                    myset.add((row // 3, column // 3, value))

        backtrack(board, 0, 0)
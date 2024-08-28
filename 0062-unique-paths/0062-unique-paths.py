class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prevRow = [1 for _ in range(n)]
        for row in range(1, m):
            currRow =  [1 for _ in range(n)]
            for col in range(1, n):
                currRow[col] = currRow[col - 1] + prevRow[col]
            prevRow = currRow

        return prevRow[-1]
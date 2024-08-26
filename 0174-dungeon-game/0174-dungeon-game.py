class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        @lru_cache(None)
        def dfs(i,j):
            if i == m-1 and j == n-1:
                if dungeon[i][j] >= 0:
                    return 1 
                else:
                    return 1-dungeon[i][j]

            if i == m or j == n:
                return float("inf")

            return max(1,min(dfs(i+1,j),dfs(i,j+1))-dungeon[i][j])

        return dfs(0,0)
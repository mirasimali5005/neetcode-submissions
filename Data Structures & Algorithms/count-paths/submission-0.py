class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for y in range(n):
            for x in range(m):
                if x == 0 and y == 0:
                    dp[x][y] = 1
                elif x == 0:
                    dp[x][y] = dp[x][y - 1]
                elif y == 0:
                    dp[x][y] = dp[x-1][y] 
                elif x != 0 and y != 0:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]

        return dp[-1][-1]

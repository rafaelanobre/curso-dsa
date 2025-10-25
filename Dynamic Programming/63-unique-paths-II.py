# LeetCode 63 - Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        # M (linhas) e N (colunas)
        dp = [[0] * N for _ in range(M)]

        dp[0][0] = 1

        for j in range(1, N):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]

        for i in range(1, M):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]

        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[M-1][N-1]
# LeetCode 70 - Climbing Stairs

class Solution:
    def climb_stairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

print(Solution().climb_stairs(5))
print(Solution().climb_stairs(10))



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # have to reach len(cost) + 1 height

        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost) + 1):
            if i == len(cost):
                return min(dp[i-1], dp[i-2])
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
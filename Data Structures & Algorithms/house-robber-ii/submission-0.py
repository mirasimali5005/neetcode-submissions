class Solution:
    def rob(self, nums: List[int]) -> int:
        # first part 0 to n-1
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        n = nums[:-1]
        dp = {}
        dp[0] = n[0]
        dp[1] = max(dp[0], n[1])
        for i in range(2, len(n)):
            dp[i] = max(dp[i-2] + n[i], dp[i-1])
        
        n = nums[1:]
        dp2 = {}
        dp2[0] = n[0]
        dp2[1] = max(dp2[0], n[1])
        for i in range(2, len(n)):
            dp2[i] = max(dp2[i-2] + n[i], dp2[i-1])
        return max(dp2[len(n)-1], dp[len(n) - 1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        # so our starting point would be 0th or 1st index 
        # since it doesnt make sense to start at 2nd index 
        # as you can always skip 2 steps and come from 0th index

        dp = {}
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[len(nums)-1]
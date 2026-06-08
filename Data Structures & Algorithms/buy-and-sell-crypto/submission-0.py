class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window 
        # when u find something smaller move left 
        # keep moving right until you find something smaller
        # then repeat the same thing 
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                # calculate the total max and shift the pointer
                profit = max(profit, prices[r] - prices[l])
                l = r
                r +=1
            else:
                profit = max(profit, prices[r] - prices[l])
                r +=1
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        tempProfit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                tempProfit += (prices[i+1] - prices[i])
            if prices[i+1] > prices[i] or len(prices)-2 == i:
                profit += tempProfit
                tempProfit = 0
        return profit
            
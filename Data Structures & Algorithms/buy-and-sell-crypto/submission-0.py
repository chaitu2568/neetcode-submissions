class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]
        maxi = 0

        for i in range(1,len(prices)):

            if prices[i] < mini:
                mini = prices[i]
            
            profit = prices[i] - mini
            maxi = max(profit, maxi)
        
        return maxi


        
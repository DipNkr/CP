class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp =  prices[0]
        
        maxProfit = 0
        for i in range(1,len(prices)):
            if maxProfit < prices[i] - temp:
                maxProfit = prices[i] - temp
            if temp > prices[i]:
                temp = prices[i]
                
            
        return maxProfit
            
            
        
                
        
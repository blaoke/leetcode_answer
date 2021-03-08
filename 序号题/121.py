class Solution:
    def maxProfit(self, prices: [int]) -> int:
        minprofit=float('inf')
        res=0
        for i in range(len(prices)):
            minprofit=min(prices[i],minprofit)
            if prices[i]>minprofit:
                res=max(prices[i]-minprofit,res)#如果这一天能获得利润,则求这一天得到的利润和之前利润的最大值
        return res




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 # 2 pointers that we can use to iterate :3
        maxPrice=0; #this is us keeping track of the max PROFIT
        while (r<len(prices)):
            buy,sell=prices[l],prices[r]
            if buy<sell:
                profit= sell-buy
                maxPrice=max(maxPrice, profit)
            else:
                l=r
            r+=1
        return maxPrice #my intro to sliding window, its just using two pointers ,nO? aint that complex ngl

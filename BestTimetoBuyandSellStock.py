class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min=prices[0]
        pft=0
        for i in range(1,len(prices)):
            pft=max(pft,prices[i]-curr_min)
            curr_min=min(prices[i],curr_min)
        return pft

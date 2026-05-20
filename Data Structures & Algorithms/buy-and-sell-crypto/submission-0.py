class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target = 0
        for i, cp in enumerate(prices):
            for sp in prices[i:]:
                difference = sp - cp
                target = max(sp-cp, target)

        return target
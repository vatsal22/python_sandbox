class Solution(object):
    # def maxProfit_helper(self, prices, )
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        largest_profit = 0
        cur_buy = prices[0]
        for price in prices:
            largest_profit = max(largest_profit, price-cur_buy)

            if(cur_buy > price): cur_buy=price
        return largest_profit
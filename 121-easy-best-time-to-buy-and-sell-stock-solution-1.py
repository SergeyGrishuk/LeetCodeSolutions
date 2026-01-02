

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price_seen = prices[0]
        max_profit = 0

        for price in prices:
            if price < lowest_price_seen:
                lowest_price_seen = price
            elif price - lowest_price_seen > max_profit:
                max_profit = price - lowest_price_seen

        return max_profit


if __name__ == '__main__':
    s = Solution()

    print(s.maxProfit([7,1,5,3,6,4]))

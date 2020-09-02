import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # [] 들어오는 것 대비
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

        # brute-force 타임아웃
        # output = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         output = max(output, prices[j] - prices[i])
        # return output


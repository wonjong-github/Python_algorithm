import sys


class Solution(object):
    def maxProfit(self, prices: list[int])->int:
        """
        :type prices: List[int]
        :rtype: int
        """
        min_v, max_v = sys.maxsize, 0
        answer = 0
        for i in range(len(prices)):
            min_v = min(min_v, prices[i])
            answer = max(answer, prices[i]-min_v)
        return answer
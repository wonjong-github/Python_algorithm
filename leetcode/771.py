import collections


class Solution(object):
    def numJewelsInStones(self, jewels:str, stones:str)->int:
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        stone = collections.Counter(stones)
        answer = 0
        for c in jewels:
            answer+=stone[c]
        return answer

a = Solution()
a.numJewelsInStones("aA", "aAAbbbb")
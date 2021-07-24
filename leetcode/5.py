class Solution(object):
    def longestPalindrome(self, s:str)->str:
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, len(s)
        for i in range(len(s)):
            ss, ee = i, len(s)
            
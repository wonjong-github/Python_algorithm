class Solution(object):
    def removeDuplicateLetters(self, s:str)->str:
        """
        :type s: str
        :rtype: str
        """
        m = {}
        for c in s:
            m.setdefault(c, 0)

        k = ''.join(sorted(list(m.keys())))
        return k

a = Solution()
a.removeDuplicateLetters("babbbsc")
class Solution(object):
    def isValid(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        m = {}
        for c in s:
            m.setdefault(c, 0)

        k = ''.join(list(m.keys()).sort())
        return k
a = Solution()
a.isValid("babbbsc")
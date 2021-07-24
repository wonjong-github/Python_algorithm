import re


class Solution(object):
    def isPalindrome(self, s : str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        s=s.lower()
        s = re.sub()
        ss = ""
        for c in s:
            if c.isalnum():
                ss = ss + c
        return ss==ss[::-1]

        import collections
        # slist = list()
        str_d = collections.deque()
        for c in s:
            if c.isalnum():
                str_d.append(c.lower())

        while len(str_d) > 1:
            if str_d.pop() != str_d.popleft():
                return False
        return True

        # length = len(slist)//2
        # for i in range(length):
        #     if slist[i] != slist[-i-1]:
        #         return False
        #
        # while len(slist) > 1:
        #     if slist.pop()!=slist.pop(0):
        #         return False
        return True

s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")
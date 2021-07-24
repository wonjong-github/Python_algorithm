class Solution(object):
    def reverseString(self, s: list)->None:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     temp = s[i]
        #     s[i] = s[-i-1]
        #     s[-i-1] = temp
        #
        s[:] = s[::-1]
        s.reverse()
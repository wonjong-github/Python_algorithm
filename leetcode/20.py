class Solution(object):
    def isValid(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        st = []
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for c in s:
            if c not in brackets:
                st.append(c)
            elif c in brackets and len(st)==0:
                return False
            elif c in brackets and st[len(st)-1] == brackets[c]:
                st.pop()
            else:
                return False

        if len(st)!=0:
            return False

        return True


a = Solution()
# a.isValid("{}[]()")
a.isValid("]")
a.isValid("{]")
a.isValid("([)]")
a.isValid("{[]}")
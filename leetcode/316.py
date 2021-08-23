class Solution(object):
    def removeDuplicateLetters(self, s:str)->str:
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c not in stack:
                stack.append(c)
            elif c in stack:
                isBehindMin = False
                index = stack.index(c)

                for i in range(index+1, len(stack)):
                    if stack[i] < c:
                        isBehindMin = True
                        break
                    elif stack[i] > c:
                        break

                if stack[len(stack)-1]==c:
                    pass
                elif isBehindMin:
                    stack.remove(c)
                    stack.append(c)
        answer = ''.join(stack)
        return answer


a = Solution()
a.removeDuplicateLetters("cbacdcbc")
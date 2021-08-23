class Solution(object):
    def dailyTemperatures(self, temperatures:list[int])->list[int]:
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            now = temperatures[i]
            while stack and now > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i-index
            stack.append(i)
        return answer

a = Solution()
a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
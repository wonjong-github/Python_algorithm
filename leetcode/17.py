class Solution(object):
    def letterCombinations(self, digits:str)->list[str]:
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {
                      '2': "abc", '3': "def",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        # digit_list = list(digits, lambda x: int(x))
        answer = []
        def dfs(index, path):
            if len(path) >= len(digits):
                answer.append(path)
                return
            for i in range(index, len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1, path+j)

        dfs(0, "")
        return answer

# a = Solution()
# a.letterCombinations("23")
results = ["1", "2", "3"]
results = list(map(int, results))
print(results)
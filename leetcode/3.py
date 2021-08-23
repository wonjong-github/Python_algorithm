class Solution(object):
    def lengthOfLongestSubstring(self, s:str)->int:
        """
        :type s: str
        :rtype: int
        """
        # answer = 1
        # for i in range(len(s)):
        #     temp = s[i]
        #     for j in range(i+1, len(s)):
        #         if s[j] in temp:
        #             break
        #         temp += s[j]
        #         answer = max(answer, len(temp))
        # return answer

        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index-start+1)
            used[char] = index
        return max_length

a = Solution()
a.lengthOfLongestSubstring("abcabcbb")
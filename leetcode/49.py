import collections


class Solution(object):
    def groupAnagrams(self, strs:list[str])->list[list[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #각각 정렬
        strdic = collections.defaultdict(list)
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            strdic[sorted_str].append(strs[i])

        return strdic.values()

a = Solution()
a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])




a = Solution()
a.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
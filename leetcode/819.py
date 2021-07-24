import collections
import re


class Solution(object):
    def mostCommonWord(self, paragraph:str, banned:list[str])->str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = re.sub('[!?\',;.]', ' ', paragraph)
        plist = paragraph.split()

        pcount = collections.Counter(plist)
        answer = ""
        for i in pcount.most_common():
            word, cnt = i
            if word in banned:
                continue
            else:
                answer = word
                break

        return answer


a = Solution()
a.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
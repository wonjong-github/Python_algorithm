import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums:list[int], k:int)->list[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num = collections.Counter(nums)
        answer = []
        heap = []
        for n, cnt in num.items():
            heapq.heappush(heap, (-cnt, n))
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer

a = Solution()
a.topKFrequent([1, 1, 1, 2, 2, 3], 2)
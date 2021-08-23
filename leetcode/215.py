import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        answer = 0
        # heapq.heapify(nums)
        # total_len = len(nums)
        # while total_len != k:
        #     answer = heapq.heappop(nums)
        #     k+=1
        # return heapq.heappop(nums)
        t = heapq.nlargest(k, nums)
        return t[-1]

a = Solution()
a.findKthLargest([3,2,1,5,6,4],2)
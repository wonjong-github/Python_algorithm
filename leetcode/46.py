import itertools


class Solution(object):
    def permute(self, nums:list[int])->list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # answer = []
        # # visit = []
        # def go(num, path):
        #     if len(path) == len(nums):
        #         answer.append(path[:])
        #         return
        #
        #     for n in nums:
        #         if not n in path:
        #             path.append(n)
        #             go(n, path)
        #             path.pop()
        #
        # for num in nums:
        #     # visit = []
        #     go(num, [num])
        #
        # return answer

        return list(map(list, itertools.permutations(nums)))

a = Solution()
# a.permute([1, 2, 3])
nums = [3, 651, 1]
t = list(map(list, itertools.permutations(nums)))
print(nums)